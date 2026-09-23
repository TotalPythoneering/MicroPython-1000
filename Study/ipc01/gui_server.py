# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-11 09:50:26
# FILE: gui_server.py
# AUTHOR: Randall Nagy
# Mission: Create a "Red Alert Device" for CsThree.
# File: gui_server.py
#

import tkinter as tk
import threading
from protocol import *
from ansi import COLORS # ALL we'll need!
from tui_client import CsThree as proto # ALIAS

class ColorDisplayApp:
    def __init__(self, master):
        self.master = master
        self.protocol = proto()
        self.master.title("IPC RAD Server")
        self.master.geometry("800x300")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, width=300, height=300, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.text_id = self.canvas.create_text(
            150, 150, text="Waiting...", font=("Helvetica", 20), fill="black"
        )

        self.color = 'GREEN'
        self.update_background(self.color)

        # Activate server threading:
        self.server_thread = threading.Thread(target=self.ipc_server, daemon=True)
        self.server_thread.start()

    def update_background(self, color):
        self.canvas.configure(bg=color)

    def update_text(self, message):
        self.canvas.itemconfig(self.text_id, text=message)

    def process_message(self, data):
        # Accepts message in the format: "color|message"
        try:
            color, message = data.split("|", 1)
            if color not in COLORS:
                color = self.color  # Ignore unknown colors
        except ValueError:
            # Malformed message
            color = self.color
            message = data

        self.color = color
        # UI updates must use main thread:
        self.master.after(0, self.update_background, color)
        self.master.after(0, self.update_text, message)

    def get_ipc(self)->str:
        try:
            import os.path
            if os.path.exists(self.protocol.ipc_file):
                self.process_message(
                    self.protocol.recv()
                    )
        except Exception as ex:
            self.process_message(
                f'red|{ex.args}')

    def ipc_server(self):
        try:
            import time
            while True:
                time.sleep(1)
                if (data := self.get_ipc()):
                    self.process_message(data)
        except Exception as ex:
            self.process_message(
                f'red|{ex.args}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorDisplayApp(root)
    root.mainloop()
