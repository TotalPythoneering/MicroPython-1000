# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 07:00:32
# FILE: tui_client.py
# AUTHOR: Randall Nagy
#
from ansi import *
from protocol import *

LED_ARRAY = {'RED':0, 'GOLD':1, 'YELLOW':2, 'GREEN':3}

class CsLED():
    def __init__(self):
        self.ipc_file = 'cs_led.proto'

    def send(self, *args)->bool: # UPDATED
        message = {}.fromkeys(LED_ARRAY, 0)
        for color in args:
            if not color in LED_ARRAY:
                raise BadColor(
                    f'No "{color}" L.E.D.')
            message[color] = 1               
        with open(f'{self.ipc_file}', 'w') as fh:
            fh.write(str(message))
            return True
        return False
    
    def recv(self)->dict:
        with open(f'{self.ipc_file}') as fh:
           return dict(eval(fh.read())) # NEW

    def mainloop(self):
        while True:
            colors = input("colors:")
            colors.strip()
            if not colors:
                return
            ary = list(eval(colors))
            self.send(*ary)

if __name__ == '__main__':
    cls()
    cs = CsLED()
    if not cs.send(*LED_ARRAY.keys()):
       print('File creation error.')
    else:
       print(cs.recv())
       cs.mainloop()
    print('Testing Success.')

