# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-27 12:50:10
# FILE: tui_client.py
# AUTHOR: Randall Nagy
#
from ansi import *
from protocol import *

LED_ARRAY = {'RED':0, 'GOLD':1, 'YELLOW':2, 'GREEN':3}

class CsLED():
    def __init__(self):
        self.ipc_file = 'cs_led2.proto'

    def check_params(self, data:list)->Exception: # NEW
        if len(data) != 4:
            raise BadColor("Try something like [0,0,1,1]")
        for item in data:
            if item != 0 and item != 1:
                raise BadColor(f'Value {item} is not supported.')
        return None # Implied!

    def send(self, *args)->bool:
        with open(f'{self.ipc_file}', 'w') as fh:
            fh.write(str(args))
            return True
        return False
    
    def recv(self)->list:
        with open(f'{self.ipc_file}') as fh:
           return list(eval(fh.read()))

    def mainloop(self):
        while True:
            colors = input("bits:")
            colors.strip()
            if not colors:
                return
            try:
                ary = list(eval(colors))
                self.check_params(ary) # NEW
                self.send(*ary)
            except Exception as ex:
                print(ex)
                

if __name__ == '__main__':
    cls()
    cs = CsLED()
    if not cs.send(0,0,0,0): # UPDATED
       print('File creation error.')
    else:
       print(cs.recv())
       cs.mainloop()
    print('Testing Success.')

