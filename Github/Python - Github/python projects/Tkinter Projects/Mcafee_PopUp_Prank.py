import customtkinter as ctk
from tkinter import messagebox
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class McafeePrank:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("500x450")
        self.window.title("McAfee Security Alert")
        self.window.resizable(False, False)
        
        # Make window stay on top
        self.window.attributes('-topmost', True)
        
        self.current_theme = "mcafee"  # mcafee or modern
        
        self.setup_ui()
        
    def setup_ui(self):
        # Clear previous widgets
        for widget in self.window.winfo_children():
            widget.destroy()
        
        if self.current_theme == "mcafee":
            self.setup_mcafee_theme()
        else:
            self.setup_modern_theme()
    
    def setup_mcafee_theme(self):
        """Dark McAfee style theme"""
        # Header with McAfee branding
        header = ctk.CTkLabel(
            self.window,
            text="🔴 McAfee Total Protection",
            font=("Arial", 14, "bold"),
            text_color="white"
        )
        header.pack(fill="x", padx=0, pady=0)
        header.configure(bg_color="#ff0000", text_color="white")
        
        # Main content frame
        content_frame = ctk.CTkFrame(self.window, fg_color="#1a1a1a")
        content_frame.pack(padx=20, pady=15, fill="both", expand=True)
        
        # Alert title
        alert_title = ctk.CTkLabel(
            content_frame,
            text="⚠️ SECURITY THREAT DETECTED",
            font=("Arial", 12, "bold"),
            text_color="#ff6666"
        )
        alert_title.pack(pady=10)
        
        # Alert message
        alert_text = ctk.CTkLabel(
            content_frame,
            text=(
                "Unusual remote activity detected on your system!\n\n"
                "Threat Type: Potential Malware/Spyware\n"
                "Severity: CRITICAL\n"
                "Files Affected: 47\n\n"
                "Your system may be compromised.\n"
                "Immediate action is required to secure your device."
            ),
            font=("Arial", 10),
            text_color="white",
            justify="left"
        )
        alert_text.pack(pady=15)
        
        # Scanning progress
        progress_label = ctk.CTkLabel(
            content_frame,
            text="Scanning System...",
            font=("Arial", 9),
            text_color="#ffaa00"
        )
        progress_label.pack(pady=5)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            content_frame,
            width=300,
            height=15,
            fg_color="#333333"
        )
        self.progress_bar.pack(pady=5)
        self.progress_bar.set(0)
        
        # Animate progress
        self.animate_progress()
        
        # Buttons frame
        button_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        button_frame.pack(padx=20, pady=10, fill="x")
        
        clean_btn = ctk.CTkButton(
            button_frame,
            text="Clean Now",
            font=("Arial", 10, "bold"),
            fg_color="#ff0000",
            hover_color="#cc0000",
            command=self.show_popup_sequence
        )
        clean_btn.pack(side="left", padx=5)
        
        ignore_btn = ctk.CTkButton(
            button_frame,
            text="Ignore",
            font=("Arial", 10),
            fg_color="#333333",
            hover_color="#555555",
            command=self.on_ignore
        )
        ignore_btn.pack(side="left", padx=5)
        
        # Theme toggle button
        theme_btn = ctk.CTkButton(
            button_frame,
            text="Modern Theme",
            font=("Arial", 9),
            fg_color="#555555",
            hover_color="#777777",
            width=100,
            command=self.toggle_theme
        )
        theme_btn.pack(side="right", padx=5)
    
    def setup_modern_theme(self):
        """Modern light/blue theme"""
        # Header
        header = ctk.CTkLabel(
            self.window,
            text="🛡️ Security Guard Pro",
            font=("Arial", 14, "bold"),
            text_color="white"
        )
        header.pack(fill="x", padx=0, pady=0)
        header.configure(bg_color="#2E7D9A", text_color="white")
        
        # Main content frame
        content_frame = ctk.CTkFrame(self.window, fg_color="#f0f0f0")
        content_frame.pack(padx=20, pady=15, fill="both", expand=True)
        
        # Alert title
        alert_title = ctk.CTkLabel(
            content_frame,
            text="✓ System Status: Protected",
            font=("Arial", 12, "bold"),
            text_color="#2E7D9A"
        )
        alert_title.pack(pady=10)
        
        # Alert message
        alert_text = ctk.CTkLabel(
            content_frame,
            text=(
                "Your system is being monitored for threats.\n\n"
                "Last Scan: Just now\n"
                "Protection Status: Active\n"
                "Threats Blocked: 0\n\n"
                "Your computer is secure and up to date."
            ),
            font=("Arial", 10),
            text_color="#333333",
            justify="left"
        )
        alert_text.pack(pady=15)
        
        # Scanning progress
        progress_label = ctk.CTkLabel(
            content_frame,
            text="Real-time Protection Active",
            font=("Arial", 9),
            text_color="#2E7D9A"
        )
        progress_label.pack(pady=5)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            content_frame,
            width=300,
            height=15,
            fg_color="#d0d0d0"
        )
        self.progress_bar.pack(pady=5)
        self.progress_bar.set(1.0)
        
        # Buttons frame
        button_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        button_frame.pack(padx=20, pady=10, fill="x")
        
        scan_btn = ctk.CTkButton(
            button_frame,
            text="Run Full Scan",
            font=("Arial", 10, "bold"),
            fg_color="#2E7D9A",
            hover_color="#1d5a7a",
            command=self.show_popup_sequence
        )
        scan_btn.pack(side="left", padx=5)
        
        settings_btn = ctk.CTkButton(
            button_frame,
            text="Settings",
            font=("Arial", 10),
            fg_color="#cccccc",
            text_color="#333333",
            hover_color="#999999",
            command=self.on_ignore
        )
        settings_btn.pack(side="left", padx=5)
        
        # Theme toggle button
        theme_btn = ctk.CTkButton(
            button_frame,
            text="McAfee Theme",
            font=("Arial", 9),
            fg_color="#888888",
            hover_color="#666666",
            width=100,
            command=self.toggle_theme
        )
        theme_btn.pack(side="right", padx=5)
    
    def animate_progress(self):
        """Animate progress bar"""
        for i in range(101):
            self.progress_bar.set(i / 100)
            self.progress_bar.update()
            time.sleep(0.02)
    
    def toggle_theme(self):
        """Toggle between McAfee and Modern themes"""
        if self.current_theme == "mcafee":
            self.current_theme = "modern"
            ctk.set_appearance_mode("light")
        else:
            self.current_theme = "mcafee"
            ctk.set_appearance_mode("dark")
        
        self.setup_ui()
    
    def show_popup_sequence(self):
        """Show a sequence of messagebox popups to enhance the prank"""
        if self.current_theme == "mcafee":
            popups = [
                ("McAfee Security", "We've detected malware on your system.\n\nInitializing threat removal...", "info"),
                ("McAfee Security", "⚠️ WARNING: Your files are at risk!\n\nProceed with cleanup?", "warning"),
                ("McAfee Antivirus", "Critical System Threat Found!\n\nThreat: trojanbypasser.gen.2\nLocation: System32\n\nRemoving threat...", "error"),
                ("McAfee Security Alert", "🔒 Your system has been secured!\n\nThreats removed: 47\nQuarantined files: 12\n\nYour computer is now safe.", "info"),
            ]
        else:
            popups = [
                ("Security Guard Pro", "Starting full system scan...\n\nThis may take a few moments.", "info"),
                ("Scan Progress", "✓ Scan complete!\n\nFiles scanned: 2,847\nThreats found: 0\nSystem Status: Healthy", "info"),
                ("Scanner Status", "Your system is performing optimally.\n\nLast updated: Just now\nProtection: Active", "info"),
            ]
        
        for title, message, msg_type in popups:
            if msg_type == "info":
                messagebox.showinfo(title, message)
            elif msg_type == "warning":
                messagebox.showwarning(title, message)
            elif msg_type == "error":
                messagebox.showerror(title, message)
            time.sleep(0.5)
        
        # Final message
        final_msg = (
            "✓ SYSTEM SECURED\n\n"
            "Your system is protected.\n\n"
            "(Just kidding! You got pranked! 😄)"
        ) if self.current_theme == "mcafee" else (
            "✓ SCAN COMPLETE\n\n"
            "Your system is healthy.\n\n"
            "(Just kidding! You got pranked! 😄)"
        )
        
        messagebox.showinfo(
            "Security Status",
            final_msg
        )
    
    def on_ignore(self):
        """Handle ignore/settings button click"""
        title = "McAfee Security" if self.current_theme == "mcafee" else "Settings"
        msg = (
            "Ignoring threats may lead to system compromise!\n\n"
            "Are you absolutely sure?"
        ) if self.current_theme == "mcafee" else (
            "No settings available in this version.\n\n"
            "Continue to main screen?"
        )
        
        result = messagebox.askyesno(title, msg)
        if result and self.current_theme == "mcafee":
            messagebox.showerror(
                "CRITICAL ERROR",
                "⚠️ SYSTEM SHUTDOWN IMMINENT\n\n"
                "Your system has been encrypted.\n"
                "Pay 500 BTC to unlock...\n\n"
                "(PSYCH! You got pranked! 😆)"
            )
            self.window.quit()
        elif not result and self.current_theme == "mcafee":
            messagebox.showinfo(
                "McAfee Security",
                "Wise choice! Your system is now safe."
            )
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    prank = McafeePrank()
    prank.run()
