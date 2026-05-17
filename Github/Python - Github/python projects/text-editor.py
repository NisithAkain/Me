import tkinter as tk
from tkinter import filedialog, messagebox
import os

# ── Palette ──────────────────────────────────────────────
LIGHT = {
    "bg":        "#F7F6F3",
    "editor_bg": "#FFFFFF",
    "fg":        "#2C2C2C",
    "muted":     "#A0A0A0",
    "accent":    "#5B8CFA",
    "toolbar":   "#EFEFED",
    "border":    "#E0DED9",
    "btn_hover": "#E2E0DC",
}
DARK = {
    "bg":        "#1E1E1E",
    "editor_bg": "#252525",
    "fg":        "#E8E6E1",
    "muted":     "#6B6B6B",
    "accent":    "#7BA7FB",
    "toolbar":   "#2A2A2A",
    "border":    "#333333",
    "btn_hover": "#333333",
}

FONT_EDITOR = ("Georgia", 14)
FONT_UI     = ("Helvetica Neue", 11)
FONT_SMALL  = ("Helvetica Neue", 9)


class MinimalEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor")
        self.root.geometry("900x650")
        self.root.minsize(500, 400)

        self.filepath    = None
        self.is_dark     = False
        self.unsaved     = False
        self.theme       = LIGHT
        self._btn_refs   = []   # keep refs for hover binding

        self._build_ui()
        self._apply_theme()
        self._bind_keys()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ── Build ─────────────────────────────────────────────
    def _build_ui(self):
        # Toolbar
        self.toolbar = tk.Frame(self.root, height=46)
        self.toolbar.pack(fill="x", side="top")
        self.toolbar.pack_propagate(False)

        # Left buttons
        left = tk.Frame(self.toolbar)
        left.pack(side="left", padx=12, pady=6)

        self.btn_new   = self._toolbar_btn(left, "New",   self._new)
        self.btn_open  = self._toolbar_btn(left, "Open",  self._open)
        self.btn_save  = self._toolbar_btn(left, "Save",  self._save)
        self.btn_saveas= self._toolbar_btn(left, "Save As", self._save_as)

        for b in (self.btn_new, self.btn_open, self.btn_save, self.btn_saveas):
            b.pack(side="left", padx=3)

        # Right: theme toggle
        right = tk.Frame(self.toolbar)
        right.pack(side="right", padx=12, pady=6)
        self.btn_theme = self._toolbar_btn(right, "☽", self._toggle_theme, width=3)
        self.btn_theme.pack(side="right")

        # Thin separator
        self.sep = tk.Frame(self.root, height=1)
        self.sep.pack(fill="x")

        # Editor frame with padding
        editor_wrap = tk.Frame(self.root)
        editor_wrap.pack(fill="both", expand=True, padx=40, pady=30)

        self.text = tk.Text(
            editor_wrap,
            font=FONT_EDITOR,
            relief="flat",
            bd=0,
            wrap="word",
            insertwidth=2,
            spacing1=4,
            spacing3=4,
            undo=True,
            maxundo=-1,
            padx=8,
            pady=8,
        )
        self.text.pack(fill="both", expand=True)
        self.text.bind("<<Modified>>", self._on_modified)

        # Scrollbar (invisible unless needed)
        self.scrollbar = tk.Scrollbar(editor_wrap, command=self.text.yview)
        self.text.config(yscrollcommand=self._smart_scroll)

        # Status bar
        self.status_bar = tk.Frame(self.root, height=28)
        self.status_bar.pack(fill="x", side="bottom")
        self.status_bar.pack_propagate(False)

        self.lbl_file   = tk.Label(self.status_bar, text="Untitled", font=FONT_SMALL, anchor="w")
        self.lbl_file.pack(side="left", padx=16)

        self.lbl_stats  = tk.Label(self.status_bar, text="0 words · 0 chars", font=FONT_SMALL, anchor="e")
        self.lbl_stats.pack(side="right", padx=16)

    def _toolbar_btn(self, parent, text, cmd, width=7):
        btn = tk.Button(
            parent, text=text, command=cmd,
            font=FONT_UI, relief="flat", bd=0,
            cursor="hand2", width=width,
            padx=6, pady=2,
        )
        btn.bind("<Enter>", lambda e, b=btn: self._btn_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: self._btn_leave(b))
        self._btn_refs.append(btn)
        return btn

    # ── Theme ─────────────────────────────────────────────
    def _apply_theme(self):
        t = self.theme
        self.root.configure(bg=t["bg"])
        self.toolbar.configure(bg=t["toolbar"])
        self.sep.configure(bg=t["border"])
        self.status_bar.configure(bg=t["toolbar"])

        self.text.configure(
            bg=t["editor_bg"], fg=t["fg"],
            insertbackground=t["accent"],
            selectbackground=t["accent"] + "55",
            selectforeground=t["fg"],
        )

        # Editor wrap
        for w in self.root.winfo_children():
            if isinstance(w, tk.Frame) and w not in (
                self.toolbar, self.sep, self.status_bar
            ):
                w.configure(bg=t["bg"])

        for btn in self._btn_refs:
            btn.configure(
                bg=t["toolbar"], fg=t["fg"],
                activebackground=t["btn_hover"],
                activeforeground=t["fg"],
            )

        self.lbl_file.configure(bg=t["toolbar"], fg=t["muted"])
        self.lbl_stats.configure(bg=t["toolbar"], fg=t["muted"])

    def _toggle_theme(self):
        self.is_dark = not self.is_dark
        self.theme   = DARK if self.is_dark else LIGHT
        self.btn_theme.config(text="☀" if self.is_dark else "☽")
        self._apply_theme()

    def _btn_enter(self, btn):
        btn.configure(bg=self.theme["btn_hover"])

    def _btn_leave(self, btn):
        btn.configure(bg=self.theme["toolbar"])

    # ── Scrollbar logic ───────────────────────────────────
    def _smart_scroll(self, first, last):
        if float(first) <= 0.0 and float(last) >= 1.0:
            self.scrollbar.pack_forget()
        else:
            self.scrollbar.pack(side="right", fill="y")
            self.scrollbar.set(first, last)

    # ── File ops ──────────────────────────────────────────
    def _new(self):
        if self.unsaved and not self._confirm_discard():
            return
        self.text.delete("1.0", "end")
        self.filepath = None
        self.unsaved  = False
        self._update_title()

    def _open(self):
        if self.unsaved and not self._confirm_discard():
            return
        path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Markdown", "*.md"),
                       ("All files", "*.*")]
        )
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.filepath = path
        self.unsaved  = False
        self._update_title()

    def _save(self):
        if self.filepath:
            self._write(self.filepath)
        else:
            self._save_as()

    def _save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Markdown", "*.md"),
                       ("All files", "*.*")]
        )
        if not path:
            return
        self.filepath = path
        self._write(path)

    def _write(self, path):
        content = self.text.get("1.0", "end-1c")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        self.unsaved = False
        self._update_title()

    def _confirm_discard(self):
        return messagebox.askyesno(
            "Unsaved changes",
            "You have unsaved changes. Discard them?",
            icon="warning"
        )

    def _on_close(self):
        if self.unsaved and not self._confirm_discard():
            return
        self.root.destroy()

    # ── Status / title updates ────────────────────────────
    def _on_modified(self, _=None):
        if self.text.edit_modified():
            self.unsaved = True
            self._update_title()
            self._update_stats()
            self.text.edit_modified(False)

    def _update_title(self):
        name = os.path.basename(self.filepath) if self.filepath else "Untitled"
        dot  = " •" if self.unsaved else ""
        self.root.title(f"{name}{dot}  —  Editor")
        self.lbl_file.configure(text=name + dot)

    def _update_stats(self):
        content = self.text.get("1.0", "end-1c")
        words   = len(content.split()) if content.strip() else 0
        chars   = len(content)
        self.lbl_stats.configure(text=f"{words} words · {chars} chars")

    # ── Keyboard shortcuts ────────────────────────────────
    def _bind_keys(self):
        self.root.bind("<Control-n>", lambda e: self._new())
        self.root.bind("<Control-o>", lambda e: self._open())
        self.root.bind("<Control-s>", lambda e: self._save())
        self.root.bind("<Control-S>", lambda e: self._save_as())  # Ctrl+Shift+S
        self.root.bind("<Control-z>", lambda e: self.text.edit_undo())
        self.root.bind("<Control-y>", lambda e: self.text.edit_redo())


# ── Entry point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(True, True)
    try:
        root.tk.call("tk", "scaling", 1.3)   # crisp on HiDPI
    except Exception:
        pass
    app = MinimalEditor(root)
    root.mainloop()

        # Toolbar
        self.toolbar = tk.Frame(self.root, height=46)
        self.toolbar.pack(fill="x", side="top")
        self.toolbar.pack_propagate(False)

        # Left buttons
        left = tk.Frame(self.toolbar)
        left.pack(side="left", padx=12, pady=6)

        self.btn_new   = self._toolbar_btn(left, "New",   self._new)
        self.btn_open  = self._toolbar_btn(left, "Open",  self._open)
        self.btn_save  = self._toolbar_btn(left, "Save",  self._save)
        self.btn_saveas= self._toolbar_btn(left, "Save As", self._save_as)

        for b in (self.btn_new, self.btn_open, self.btn_save, self.btn_saveas):
            b.pack(side="left", padx=3)

        # Right: theme toggle
        right = tk.Frame(self.toolbar)
        right.pack(side="right", padx=12, pady=6)
        self.btn_theme = self._toolbar_btn(right, "☽", self._toggle_theme, width=3)
        self.btn_theme.pack(side="right")

        # Thin separator
        self.sep = tk.Frame(self.root, height=1)
        self.sep.pack(fill="x")

        # Editor frame with padding
        editor_wrap = tk.Frame(self.root)
        editor_wrap.pack(fill="both", expand=True, padx=40, pady=30)

        self.text = tk.Text(
            editor_wrap,
            font=FONT_EDITOR,
            relief="flat",
            bd=0,
            wrap="word",
            insertwidth=2,
            spacing1=4,
            spacing3=4,
            undo=True,
            maxundo=-1,
            padx=8,
            pady=8,
        )
        self.text.pack(fill="both", expand=True)
        self.text.bind("<<Modified>>", self._on_modified)

        # Scrollbar (invisible unless needed)
        self.scrollbar = tk.Scrollbar(editor_wrap, command=self.text.yview)
        self.text.config(yscrollcommand=self._smart_scroll)

        # Status bar
        self.status_bar = tk.Frame(self.root, height=28)
        self.status_bar.pack(fill="x", side="bottom")
        self.status_bar.pack_propagate(False)

        self.lbl_file   = tk.Label(self.status_bar, text="Untitled", font=FONT_SMALL, anchor="w")
        self.lbl_file.pack(side="left", padx=16)

        self.lbl_stats  = tk.Label(self.status_bar, text="0 words · 0 chars", font=FONT_SMALL, anchor="e")
        self.lbl_stats.pack(side="right", padx=16)

    def _toolbar_btn(self, parent, text, cmd, width=7):
        btn = tk.Button(
            parent, text=text, command=cmd,
            font=FONT_UI, relief="flat", bd=0,
            cursor="hand2", width=width,
            padx=6, pady=2,
        )
        btn.bind("<Enter>", lambda e, b=btn: self._btn_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: self._btn_leave(b))
        self._btn_refs.append(btn)
        return btn

    # ── Theme ─────────────────────────────────────────────
    def _apply_theme(self):
        t = self.theme
        self.root.configure(bg=t["bg"])
        self.toolbar.configure(bg=t["toolbar"])
        self.sep.configure(bg=t["border"])
        self.status_bar.configure(bg=t["toolbar"])

        self.text.configure(
            bg=t["editor_bg"], fg=t["fg"],
            insertbackground=t["accent"],
            selectbackground=t["accent"] + "55",
            selectforeground=t["fg"],
        )

        # Editor wrap
        for w in self.root.winfo_children():
            if isinstance(w, tk.Frame) and w not in (
                self.toolbar, self.sep, self.status_bar
            ):
                w.configure(bg=t["bg"])

        for btn in self._btn_refs:
            btn.configure(
                bg=t["toolbar"], fg=t["fg"],
                activebackground=t["btn_hover"],
                activeforeground=t["fg"],
            )

        self.lbl_file.configure(bg=t["toolbar"], fg=t["muted"])
        self.lbl_stats.configure(bg=t["toolbar"], fg=t["muted"])

    def _toggle_theme(self):
        self.is_dark = not self.is_dark
        self.theme   = DARK if self.is_dark else LIGHT
        self.btn_theme.config(text="☀" if self.is_dark else "☽")
        self._apply_theme()

    def _btn_enter(self, btn):
        btn.configure(bg=self.theme["btn_hover"])

    def _btn_leave(self, btn):
        btn.configure(bg=self.theme["toolbar"])

    # ── Scrollbar logic ───────────────────────────────────
    def _smart_scroll(self, first, last):
        if float(first) <= 0.0 and float(last) >= 1.0:
            self.scrollbar.pack_forget()
        else:
            self.scrollbar.pack(side="right", fill="y")
            self.scrollbar.set(first, last)

    # ── File ops ──────────────────────────────────────────
    def _new(self):
        if self.unsaved and not self._confirm_discard():
            return
        self.text.delete("1.0", "end")
        self.filepath = None
        self.unsaved  = False
        self._update_title()

    def _open(self):
        if self.unsaved and not self._confirm_discard():
            return
        path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Markdown", "*.md"),
                       ("All files", "*.*")]
        )
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.filepath = path
        self.unsaved  = False
        self._update_title()

    def _save(self):
        if self.filepath:
            self._write(self.filepath)
        else:
            self._save_as()

    def _save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Markdown", "*.md"),
                       ("All files", "*.*")]
        )
        if not path:
            return
        self.filepath = path
        self._write(path)

    def _write(self, path):
        content = self.text.get("1.0", "end-1c")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        self.unsaved = False
        self._update_title()

    def _confirm_discard(self):
        return messagebox.askyesno(
            "Unsaved changes",
            "You have unsaved changes. Discard them?",
            icon="warning"
        )

    def _on_close(self):
        if self.unsaved and not self._confirm_discard():
            return
        self.root.destroy()

    # ── Status / title updates ────────────────────────────
    def _on_modified(self, _=None):
        if self.text.edit_modified():
            self.unsaved = True
            self._update_title()
            self._update_stats()
            self.text.edit_modified(False)

    def _update_title(self):
        name = os.path.basename(self.filepath) if self.filepath else "Untitled"
        dot  = " •" if self.unsaved else ""
        self.root.title(f"{name}{dot}  —  Editor")
        self.lbl_file.configure(text=name + dot)

    def _update_stats(self):
        content = self.text.get("1.0", "end-1c")
        words   = len(content.split()) if content.strip() else 0
        chars   = len(content)
        self.lbl_stats.configure(text=f"{words} words · {chars} chars")

    # ── Keyboard shortcuts ────────────────────────────────
    def _bind_keys(self):
        self.root.bind("<Control-n>", lambda e: self._new())
        self.root.bind("<Control-o>", lambda e: self._open())
        self.root.bind("<Control-s>", lambda e: self._save())
        self.root.bind("<Control-S>", lambda e: self._save_as())  # Ctrl+Shift+S
        self.root.bind("<Control-z>", lambda e: self.text.edit_undo())
        self.root.bind("<Control-y>", lambda e: self.text.edit_redo())


# ── Entry point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(True, True)
    try:
        root.tk.call("tk", "scaling", 1.3)   # crisp on HiDPI
    except Exception:
        pass
    app = MinimalEditor(root)
    root.mainloop()