import os
import threading
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# ============================================
# AUTO INSTALL DEPENDENCIES
# ============================================

REQUIRED_PACKAGES = ["yt-dlp"]

def install_package(package):
    try:
        __import__(package.replace("-", "_"))
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call(
            ["python3", "-m", "pip", "install", package]
        )

for pkg in REQUIRED_PACKAGES:
    install_package(pkg)

# ============================================
# IMPORT AFTER INSTALL
# ============================================

import yt_dlp

# ============================================
# GUI APP
# ============================================

class VideoDownloaderApp:

    def __init__(self, root):

        self.root = root
        self.root.title("YouTube Batch Downloader")
        self.root.geometry("700x500")

        self.source_file = ""
        self.destination_folder = ""

        # =========================
        # TITLE
        # =========================

        title = tk.Label(
            root,
            text="YouTube Batch Downloader",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=15)

        # =========================
        # SOURCE FILE
        # =========================

        self.source_label = tk.Label(
            root,
            text="No source file selected",
            wraplength=600
        )
        self.source_label.pack(pady=5)

        source_btn = tk.Button(
            root,
            text="Select TXT File",
            command=self.select_source_file,
            width=25,
            height=2
        )
        source_btn.pack(pady=10)

        # =========================
        # DESTINATION
        # =========================

        self.dest_label = tk.Label(
            root,
            text="No destination folder selected",
            wraplength=600
        )
        self.dest_label.pack(pady=5)

        dest_btn = tk.Button(
            root,
            text="Select Destination Folder",
            command=self.select_destination,
            width=25,
            height=2
        )
        dest_btn.pack(pady=10)

        # =========================
        # DOWNLOAD BUTTON
        # =========================

        self.download_btn = tk.Button(
            root,
            text="START DOWNLOAD",
            command=self.start_download_thread,
            bg="green",
            fg="white",
            font=("Arial", 14, "bold"),
            width=25,
            height=2
        )

        self.download_btn.pack(pady=20)

        # =========================
        # PROGRESS BAR
        # =========================

        self.progress = ttk.Progressbar(
            root,
            orient="horizontal",
            length=500,
            mode="determinate"
        )

        self.progress.pack(pady=15)

        # =========================
        # LOG BOX
        # =========================

        self.log_box = tk.Text(
            root,
            height=12,
            width=85
        )

        self.log_box.pack(pady=10)

    # ============================================
    # LOGGING
    # ============================================

    def log(self, message):

        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.root.update()

    # ============================================
    # SELECT FILE
    # ============================================

    def select_source_file(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )

        if file_path:
            self.source_file = file_path
            self.source_label.config(text=file_path)

    # ============================================
    # SELECT DESTINATION
    # ============================================

    def select_destination(self):

        folder = filedialog.askdirectory()

        if folder:
            self.destination_folder = folder
            self.dest_label.config(text=folder)

    # ============================================
    # THREADING
    # ============================================

    def start_download_thread(self):

        thread = threading.Thread(target=self.download_videos)
        thread.start()

    # ============================================
    # DOWNLOAD LOGIC
    # ============================================

    def download_videos(self):

        if not self.source_file:
            messagebox.showerror(
                "Error",
                "Please select a TXT file."
            )
            return

        if not self.destination_folder:
            messagebox.showerror(
                "Error",
                "Please select a destination folder."
            )
            return

        with open(self.source_file, "r", encoding="utf-8") as f:
            links = [line.strip() for line in f if line.strip()]

        total = len(links)

        self.progress["maximum"] = total

        for index, link in enumerate(links, start=1):

            try:

                self.log(f"[{index}/{total}] Downloading:")
                self.log(link)

                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'merge_output_format': 'mp4',
                    'outtmpl': os.path.join(
                        self.destination_folder,
                        '%(title)s.%(ext)s'
                    ),
                    'noplaylist': True,
                    'quiet': True,
                    'ignoreerrors': True,
                    'restrictfilenames': False,
                    'windowsfilenames': False,
                    'writesubtitles': False,
                    'writeautomaticsub': False,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])

                self.log("SUCCESS\n")

            except Exception as e:

                self.log("FAILED")
                self.log(str(e))
                self.log("\n")

            self.progress["value"] = index
            self.root.update()

        self.log("ALL DOWNLOADS COMPLETE!")

        messagebox.showinfo(
            "Done",
            "All downloads completed!"
        )

# ============================================
# RUN APP
# ============================================

root = tk.Tk()
app = VideoDownloaderApp(root)
root.mainloop()