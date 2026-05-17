#!/usr/bin/env python3
"""
Kali Linux SSH Terminal - A Tkinter-based SSH client styled like Kali Linux.
Connects to a real local Kali VM via SSH and provides an interactive terminal.
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import threading
import queue
import time
import os
import sys

try:
    import paramiko
except ImportError:
    paramiko = None


# ─── Constants ────────────────────────────────────────────────────────────────

APP_TITLE    = "Kali Linux Terminal"
BG_COLOR     = "#1a1a1a"
FG_COLOR     = "#f0f0f0"
PROMPT_COLOR = "#5bc0de"
ERROR_COLOR  = "#e74c3c"
SUCCESS_COLOR= "#2ecc71"
ACCENT_COLOR = "#e84393"   # Kali's signature pink/magenta
BORDER_COLOR = "#333333"
INPUT_BG     = "#111111"
FONT_FAMILY  = "Courier"
FONT_SIZE    = 11
TITLE_FONT_SIZE = 13


# ─── SSH Connection Dialog ─────────────────────────────────────────────────────

class SSHConnectDialog(tk.Toplevel):
    """Modal dialog to collect SSH connection parameters."""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.result = None

        self.title("Connect to Kali VM")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)
        self.grab_set()

        self._build_ui()
        self._center()
        self.protocol("WM_DELETE_WINDOW", self._cancel)

    def _label(self, parent, text):
        return tk.Label(parent, text=text, bg=BG_COLOR, fg=FG_COLOR,
                        font=(FONT_FAMILY, FONT_SIZE), anchor="w")

    def _entry(self, parent, show=None, default=""):
        e = tk.Entry(parent, bg=INPUT_BG, fg=FG_COLOR,
                     insertbackground=FG_COLOR, relief="flat",
                     font=(FONT_FAMILY, FONT_SIZE),
                     highlightthickness=1,
                     highlightbackground=BORDER_COLOR,
                     highlightcolor=ACCENT_COLOR,
                     show=show)
        e.insert(0, default)
        return e

    def _build_ui(self):
        # ── Header ──
        header = tk.Frame(self, bg=ACCENT_COLOR)
        header.pack(fill="x")
        tk.Label(header, text="  ● KALI SSH CONNECTION",
                 bg=ACCENT_COLOR, fg="white",
                 font=(FONT_FAMILY, TITLE_FONT_SIZE, "bold"),
                 pady=8).pack(side="left")

        # ── Form ──
        form = tk.Frame(self, bg=BG_COLOR, padx=20, pady=16)
        form.pack(fill="both", expand=True)

        fields = [
            ("Host / IP Address", "host", False, "192.168.1.x"),
            ("Port",              "port", False, "22"),
            ("Username",         "user", False, "kali"),
            ("Password",         "pass", True,  ""),
        ]

        self._entries = {}
        for row, (label, key, secret, default) in enumerate(fields):
            self._label(form, label).grid(row=row*2,   column=0, sticky="w", pady=(6, 0))
            e = self._entry(form, show="●" if secret else None, default=default)
            e.grid(row=row*2+1, column=0, sticky="ew", ipady=4, pady=(2, 0))
            self._entries[key] = e

        # SSH key option
        self._use_key = tk.BooleanVar(value=False)
        tk.Checkbutton(form, text="Use SSH key instead of password",
                       variable=self._use_key,
                       bg=BG_COLOR, fg=FG_COLOR,
                       selectcolor=INPUT_BG,
                       activebackground=BG_COLOR, activeforeground=FG_COLOR,
                       font=(FONT_FAMILY, FONT_SIZE-1),
                       command=self._toggle_key).grid(
                           row=9, column=0, sticky="w", pady=(10, 0))

        self._key_frame = tk.Frame(form, bg=BG_COLOR)
        self._key_frame.grid(row=10, column=0, sticky="ew")
        self._label(self._key_frame, "Private Key Path").pack(anchor="w", pady=(4, 0))
        self._key_entry = self._entry(self._key_frame,
                                      default=os.path.expanduser("~/.ssh/id_rsa"))
        self._key_entry.pack(fill="x", ipady=4)
        self._key_frame.grid_remove()

        form.columnconfigure(0, weight=1)

        # ── Buttons ──
        btn_frame = tk.Frame(self, bg=BG_COLOR, padx=20, pady=12)
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Connect",
                  bg=ACCENT_COLOR, fg="white",
                  activebackground="#c73278", activeforeground="white",
                  relief="flat", font=(FONT_FAMILY, FONT_SIZE, "bold"),
                  padx=16, pady=6,
                  command=self._connect).pack(side="right", padx=(6, 0))

        tk.Button(btn_frame, text="Cancel",
                  bg=BORDER_COLOR, fg=FG_COLOR,
                  activebackground="#444", activeforeground=FG_COLOR,
                  relief="flat", font=(FONT_FAMILY, FONT_SIZE),
                  padx=16, pady=6,
                  command=self._cancel).pack(side="right")

    def _toggle_key(self):
        if self._use_key.get():
            self._key_frame.grid()
            self._entries["pass"].configure(state="disabled", fg=BORDER_COLOR)
        else:
            self._key_frame.grid_remove()
            self._entries["pass"].configure(state="normal", fg=FG_COLOR)

    def _center(self):
        self.update_idletasks()
        pw = self.parent.winfo_width()
        ph = self.parent.winfo_height()
        px = self.parent.winfo_x()
        py = self.parent.winfo_y()
        w  = self.winfo_width()
        h  = self.winfo_height()
        self.geometry(f"+{px + (pw-w)//2}+{py + (ph-h)//2}")

    def _connect(self):
        host = self._entries["host"].get().strip()
        port = self._entries["port"].get().strip()
        user = self._entries["user"].get().strip()
        pwd  = self._entries["pass"].get()
        key  = self._key_entry.get().strip() if self._use_key.get() else None

        if not host:
            messagebox.showerror("Missing Field", "Host/IP is required.", parent=self)
            return
        try:
            port = int(port)
        except ValueError:
            messagebox.showerror("Invalid Port", "Port must be a number.", parent=self)
            return

        self.result = {
            "host": host, "port": port,
            "user": user, "password": pwd,
            "key_path": key,
        }
        self.destroy()

    def _cancel(self):
        self.result = None
        self.destroy()


# ─── SSH Worker Thread ─────────────────────────────────────────────────────────

class SSHSession:
    """Manages the SSH connection and interactive shell in a background thread."""

    def __init__(self, params, output_queue):
        self.params = params
        self.q = output_queue
        self.client = None
        self.channel = None
        self._running = False
        self._thread = None

    def connect(self):
        """Open SSH connection and start reading thread."""
        if paramiko is None:
            self.q.put(("error", "paramiko is not installed.\n"
                                 "Run:  pip install paramiko\n"))
            return False
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            connect_kwargs = dict(
                hostname = self.params["host"],
                port     = self.params["port"],
                username = self.params["user"],
                timeout  = 10,
            )
            if self.params["key_path"]:
                connect_kwargs["key_filename"] = self.params["key_path"]
            else:
                connect_kwargs["password"] = self.params["password"]

            self.client.connect(**connect_kwargs)
            self.channel = self.client.invoke_shell(term="xterm", width=220, height=50)
            self.channel.settimeout(0.1)
            self._running = True
            self._thread = threading.Thread(target=self._read_loop, daemon=True)
            self._thread.start()
            self.q.put(("connected", self.params["host"]))
            return True
        except paramiko.AuthenticationException:
            self.q.put(("error", "Authentication failed. Check username/password.\n"))
        except paramiko.SSHException as e:
            self.q.put(("error", f"SSH error: {e}\n"))
        except OSError as e:
            self.q.put(("error", f"Connection error: {e}\n"))
        return False

    def send(self, data: str):
        if self.channel and self.channel.active:
            self.channel.send(data)

    def resize(self, cols: int, rows: int):
        if self.channel and self.channel.active:
            try:
                self.channel.resize_pty(width=cols, height=rows)
            except Exception:
                pass

    def _read_loop(self):
        while self._running:
            try:
                data = self.channel.recv(4096)
                if data:
                    self.q.put(("data", data.decode("utf-8", errors="replace")))
                else:
                    self._running = False
                    self.q.put(("disconnected", ""))
            except Exception:
                time.sleep(0.05)

    def disconnect(self):
        self._running = False
        try:
            if self.channel:
                self.channel.close()
            if self.client:
                self.client.close()
        except Exception:
            pass
        self.q.put(("disconnected", ""))


# ─── Main Application ──────────────────────────────────────────────────────────

class KaliTerminalApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.configure(bg=BG_COLOR)
        self.geometry("960x620")
        self.minsize(700, 400)

        self._session: SSHSession | None = None
        self._queue = queue.Queue()
        self._connected = False

        self._build_ui()
        self._poll_queue()
        self._print_banner()

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    # ── UI Construction ──────────────────────────────────────────────────────

    def _build_ui(self):
        # Top bar
        topbar = tk.Frame(self, bg=ACCENT_COLOR, height=36)
        topbar.pack(fill="x", side="top")
        topbar.pack_propagate(False)

        # Kali dragon-ish logo (Unicode approximation)
        tk.Label(topbar, text="⚙  KALI LINUX TERMINAL",
                 bg=ACCENT_COLOR, fg="white",
                 font=(FONT_FAMILY, TITLE_FONT_SIZE, "bold"),
                 padx=12).pack(side="left", fill="y")

        # Status label
        self._status_var = tk.StringVar(value="● DISCONNECTED")
        self._status_lbl = tk.Label(topbar, textvariable=self._status_var,
                                    bg=ACCENT_COLOR, fg="#ffccdd",
                                    font=(FONT_FAMILY, FONT_SIZE))
        self._status_lbl.pack(side="right", padx=12)

        # Toolbar
        toolbar = tk.Frame(self, bg="#222222", pady=3)
        toolbar.pack(fill="x", side="top")

        btn_cfg = dict(bg="#2a2a2a", fg=FG_COLOR,
                       activebackground="#444", activeforeground="white",
                       relief="flat", font=(FONT_FAMILY, FONT_SIZE-1),
                       padx=10, pady=2, cursor="hand2")

        self._conn_btn = tk.Button(toolbar, text="⚡ Connect",
                                   command=self._open_connect_dialog, **btn_cfg)
        self._conn_btn.pack(side="left", padx=3)

        self._disc_btn = tk.Button(toolbar, text="✖ Disconnect",
                                   command=self._disconnect,
                                   state="disabled", **btn_cfg)
        self._disc_btn.pack(side="left", padx=3)

        tk.Button(toolbar, text="⌫ Clear",
                  command=self._clear_terminal, **btn_cfg).pack(side="left", padx=3)

        tk.Button(toolbar, text="? Help",
                  command=self._show_help, **btn_cfg).pack(side="right", padx=3)

        # Terminal output area
        term_frame = tk.Frame(self, bg=BG_COLOR)
        term_frame.pack(fill="both", expand=True, padx=4, pady=(4, 0))

        self._terminal = tk.Text(
            term_frame,
            bg=BG_COLOR, fg=FG_COLOR,
            insertbackground=FG_COLOR,
            font=(FONT_FAMILY, FONT_SIZE),
            wrap="char",
            relief="flat",
            state="disabled",
            cursor="xterm",
            highlightthickness=1,
            highlightbackground=BORDER_COLOR,
            highlightcolor=ACCENT_COLOR,
            selectbackground="#444",
            selectforeground=FG_COLOR,
            spacing1=1, spacing3=1,
        )
        self._terminal.pack(side="left", fill="both", expand=True)

        # Tags for coloured output
        self._terminal.tag_configure("error",   foreground=ERROR_COLOR)
        self._terminal.tag_configure("success",  foreground=SUCCESS_COLOR)
        self._terminal.tag_configure("info",     foreground=PROMPT_COLOR)
        self._terminal.tag_configure("accent",   foreground=ACCENT_COLOR)

        scrollbar = tk.Scrollbar(term_frame, command=self._terminal.yview,
                                 bg=BORDER_COLOR, troughcolor=BG_COLOR,
                                 activebackground=ACCENT_COLOR, relief="flat")
        scrollbar.pack(side="right", fill="y")
        self._terminal.configure(yscrollcommand=scrollbar.set)

        # Bind terminal input when connected
        self._terminal.bind("<Key>", self._handle_key)
        self._terminal.bind("<Button-1>", self._on_terminal_click)

    # ── Banner ───────────────────────────────────────────────────────────────

    def _print_banner(self):
        banner = (
            "accent",
            r"""
  ██╗  ██╗ █████╗ ██╗     ██╗    ████████╗███████╗██████╗ ███╗   ███╗
  ██║ ██╔╝██╔══██╗██║     ██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
  █████╔╝ ███████║██║     ██║       ██║   █████╗  ██████╔╝██╔████╔██║
  ██╔═██╗ ██╔══██║██║     ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║
  ██║  ██╗██║  ██║███████╗██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
"""
        )
        self._write(*banner)
        self._write("info", "  SSH Terminal  ·  Connect to your local Kali Linux VM\n")
        self._write("info", "  Click ⚡ Connect or use Ctrl+Shift+C to begin.\n\n")

    # ── Terminal Output ───────────────────────────────────────────────────────

    def _write(self, tag: str, text: str):
        self._terminal.configure(state="normal")
        self._terminal.insert("end", text, tag)
        self._terminal.mark_set("insert", "end")
        self._terminal.see("end")
        if not self._connected:
            self._terminal.configure(state="disabled")

    def _write_plain(self, text: str):
        self._write("", text)

    def _clear_terminal(self):
        self._terminal.configure(state="normal")
        self._terminal.delete("1.0", "end")
        self._terminal.mark_set("insert", "end")
        self._terminal.see("end")
        if not self._connected:
            self._terminal.configure(state="disabled")

    # ── Queue Polling ─────────────────────────────────────────────────────────

    def _poll_queue(self):
        try:
            while True:
                kind, payload = self._queue.get_nowait()
                if kind == "data":
                    self._write_plain(payload)
                elif kind == "connected":
                    self._on_connected(payload)
                elif kind == "disconnected":
                    self._on_disconnected()
                elif kind == "error":
                    self._write("error", payload)
        except queue.Empty:
            pass
        self.after(50, self._poll_queue)

    # ── Connection Lifecycle ──────────────────────────────────────────────────

    def _open_connect_dialog(self):
        if self._connected:
            if not messagebox.askyesno("Already Connected",
                                       "Disconnect current session and open a new one?"):
                return
            self._disconnect()

        dialog = SSHConnectDialog(self)
        self.wait_window(dialog)

        if dialog.result:
            self._write("info", f"\n  Connecting to {dialog.result['host']}:{dialog.result['port']} …\n")
            self._session = SSHSession(dialog.result, self._queue)
            threading.Thread(target=self._session.connect, daemon=True).start()

    def _on_connected(self, host: str):
        self._connected = True
        self._status_var.set(f"● CONNECTED  →  {host}")
        self._status_lbl.configure(fg="#aaffaa")
        self._conn_btn.configure(state="disabled")
        self._disc_btn.configure(state="normal")
        self._terminal.configure(state="normal")
        self._terminal.focus_set()
        self._terminal.mark_set("insert", "end")
        self._terminal.see("end")

    def _disconnect(self):
        if self._session:
            self._session.disconnect()
        self._on_disconnected()

    def _on_disconnected(self):
        self._connected = False
        self._status_var.set("● DISCONNECTED")
        self._status_lbl.configure(fg="#ffccdd")
        self._conn_btn.configure(state="normal")
        self._disc_btn.configure(state="disabled")
        self._terminal.configure(state="disabled")
        self._write("info", "\n  [Session closed]\n")

    # ── Input Handling ────────────────────────────────────────────────────────

    def _handle_key(self, event):
        if not self._connected or not self._session:
            return "break"
        
        # Handle special keys
        if event.keysym == 'Return':
            self._session.send('\n')
        elif event.keysym == 'BackSpace':
            self._session.send('\b')
        elif event.keysym == 'Tab':
            self._session.send('\t')
        elif event.keysym == 'Up':
            self._session.send('\x1b[A')
        elif event.keysym == 'Down':
            self._session.send('\x1b[B')
        elif event.keysym == 'Right':
            self._session.send('\x1b[C')
        elif event.keysym == 'Left':
            self._session.send('\x1b[D')
        elif event.keysym == 'Home':
            self._session.send('\x1b[H')
        elif event.keysym == 'End':
            self._session.send('\x1b[F')
        elif event.keysym == 'Delete':
            self._session.send('\x1b[3~')
        elif event.state & 4:  # Control key pressed
            if event.keysym == 'c':
                self._session.send('\x03')
            elif event.keysym == 'd':
                self._session.send('\x04')
            elif event.keysym == 'l':
                self._clear_terminal()
            else:
                return "break"
        elif event.char and event.char.isprintable():
            self._session.send(event.char)
        else:
            return "break"
        
        return "break"

    def _on_terminal_click(self, event):
        # Prevent editing previous text, keep cursor at end
        self._terminal.mark_set("insert", "end")
        self._terminal.see("end")
        return "break"

    # ── Help ─────────────────────────────────────────────────────────────────

    def _show_help(self):
        msg = (
            "Kali Terminal — Keyboard Shortcuts\n\n"
            "Type directly in the terminal area when connected.\n\n"
            "Enter        →  Send command\n"
            "↑ / ↓ / ← / → →  Arrow keys\n"
            "Tab          →  Remote tab-completion\n"
            "Backspace    →  Delete character\n"
            "Ctrl+C       →  Interrupt (SIGINT)\n"
            "Ctrl+D       →  EOF / exit shell\n"
            "Ctrl+L       →  Clear terminal\n\n"
            "Requirements:\n"
            "  pip install paramiko\n\n"
            "Your Kali VM must have SSH running:\n"
            "  sudo service ssh start"
        )
        messagebox.showinfo("Help", msg)

    # ── Close ─────────────────────────────────────────────────────────────────

    def _on_close(self):
        if self._session:
            self._session.disconnect()
        self.destroy()


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if paramiko is None:
        print("⚠  paramiko not found. Install it with:  pip install paramiko")
        print("   The app will launch but SSH will not work until paramiko is installed.\n")

    app = KaliTerminalApp()
    app.mainloop()