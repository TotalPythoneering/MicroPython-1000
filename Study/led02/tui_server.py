# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-27 12:35:42
# FILE: tui_server.py
# AUTHOR: Randall Nagy
# Mission: FOR PYTHON3, ONLY.
#          Create a 4 x 'BITWISE' LED emulator.
# File: tui_server.py
#

from ansi import *
from protocol import *
from tui_client import CsLED, LED_ARRAY

class ColorDisplayApp:
    def __init__(self):
        self.protocol = CsLED()
        self.lights = None
        self.led_colors = [
            COLORS['RED'],
            COLORS['WHITE'], # 'GOLD'
            COLORS['YELLOW'],
            COLORS['BLUE']]  # 'GREEN'

    def process_message(self, data:list):
        # NEW: Expects BIT list.
        display = '['
        try:
            self.protocol.check_params(data) # NEW
            for which, state in enumerate(data):
                if state: # NEW!
                    display += self.led_colors[which]
                else:
                    display += COLORS['BLACK'] # off
                display += '*' + COLORS['RESET']
            display += ']'
            if str(display) != str(self.lights):
                import sys
                self.lights = display
                row = 5; col = 2;
                sys.stdout.write(f"\033[{row};{col}H")
                sys.stdout.write(display)
                sys.stdout.write("\033[0m")
                sys.stdout.flush()
        except Exception as ex:           # Malformed message
            print('Error:', ex)

    def get_ipc(self)->str:
        try:
            import os.path
            if os.path.exists(self.protocol.ipc_file):
                data = self.protocol.recv()
                self.process_message(data)
        except Exception as ex:
            print('Failure:', ex)

    def ipc_server(self):
        try:
            import time
            while True:
                time.sleep(1)
                if (data := self.get_ipc()):
                    self.process_message(data)
        except Exception as ex:
            raise

if __name__ == "__main__":
    cls()
    ColorDisplayApp().ipc_server()

