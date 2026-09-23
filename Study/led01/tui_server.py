# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 06:54:12
# FILE: tui_server.py
# AUTHOR: Randall Nagy
# Mission: FOR PYTHON3, ONLY.
#          Create a 4 x LED emulator.
# File: tui_server.py
#

from ansi import *
from protocol import *
from tui_client import CsLED, LED_ARRAY

class ColorDisplayApp:
    def __init__(self):
        self.protocol = CsLED()
        self.lights = None

    def process_message(self, data):
        # Expects LED_ARRAY dictionary.
        display = '['
        try:
            for key in data:
                if key not in LED_ARRAY:
                    # Ignore unknown colors
                    continue
                if data[key] == 0:
                    display += COLORS['BLACK']
                else:
                    key ='WHITE' if key == 'GOLD' else key
                    key ='BLUE' if key == 'GREEN' else key
                    display += COLORS[key] 
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
                
        except Exception as ex:
            # Malformed message
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

