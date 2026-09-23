# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 04:14:10
# FILE: tui_server.py
# AUTHOR: Randall Nagy
# Mission: Create a "Red Alert Device" for CsThree.
# File: tui_server.py
#

from ansi import *
from protocol import *
from tui_client import CsThree

class ColorDisplayApp:
    def __init__(self):
        self.driver = CsThree()
        self.color = 'GREEN'
        self.message = None

    def process_message(self, data):
        # Expects "color|message" format
        try:
            color, message = data.split("|", 1)
            if self.color == color \
               and self.message == message:
                return
            if color not in COLORS:
                # Ignore unknown colors
                color = self.color
        except:
            # Malformed message
            color = self.color
            message = data
        else:
            show(color, message)
            self.color = color
            self.message = message

    def get_ipc(self)->str:
        import os.path # Not presently uPy
        try:
            if os.path.exists(self.driver.ipc_file):
                self.process_message(
                    self.driver.recv()
                    )
        except Exception as ex:
            self.process_message(
                f'red|{ex.args}') # CAVEAT uPy!

    def ipc_server(self):
        try:
            import time
            while True:
                time.sleep(1)
                if (data := self.get_ipc()):
                    self.process_message(data)
        except Exception as ex:
            self.process_message(
                f'red|{ex}')
            raise

if __name__ == "__main__":
    cls()
    ColorDisplayApp().ipc_server()

