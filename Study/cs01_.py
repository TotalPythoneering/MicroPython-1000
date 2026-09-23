# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-13 11:14:40
# FILE: cs01_.py
# AUTHOR: Randall Nagy
#
from csdemo_ import CsDemo

class CsOne(CsDemo):
    def __init__(self, msg):
        super().__init__(msg)
        
    def send(self)->bool:
        with open("csdemo.txt", 'w') as fh:
            fh.write(self._data)
            return True
        return False
    
    def recv(self)->str:
        with open('csdemo.txt') as fh:
           return fh.read()

if __name__ == '__main__':
    cs = CsOne('This is a test')
    if not cs.send():
       print('File creation error.')
    else:
       print(cs.recv())

