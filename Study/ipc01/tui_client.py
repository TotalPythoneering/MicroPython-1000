# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 04:01:42
# FILE: tui_client.py
# AUTHOR: Randall Nagy
#
from ansi import *
from protocol import *

class CsThree():
    def __init__(self):
        self.ipc_file = 'csdemo.proto'

    def send(self, color, message)->bool:
        if not color in COLORS:
            raise BadColor(f'Color "{color}"?')
        with open(f'{self.ipc_file}', 'w') as fh:
            fh.write(f'{color}|{message}')
            return True
        return False
    
    def recv(self)->str:
        with open(f'{self.ipc_file}') as fh:
           return fh.read()

    def mainloop(self):
        while True:
            color = input("color: ")
            color.strip()
            if not color:
                return
            if not color in COLORS:
                continue
            self.send(color, input("message: "))

if __name__ == '__main__':
    cs = CsThree()
    if not cs.send('BLUE','This is a test!'):
       print('File creation error.')
    else:
       print(cs.recv())
       print('Colors:', *COLORS)
       cs.mainloop()
    print('Testing Success.')

