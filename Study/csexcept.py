# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-13 12:55:00
# FILE: csexcept.py
# AUTHOR: Randall Nagy
# Mission: Demonstrate exception basics.
# File: csexcept.py
#

RED=0; GREEN=1; YELLOW=2
COLORS = ['RED','GREEN','YELLOW']

class BadColor(Exception):
    def __init__(self, err):
        super().__init__(err)

class CsExcept():
    def __init__(self):
        pass
    
    def __get(self,fh)->str:
        try:
            data = fh.read()
            fh.close()
            return data
        except Exception as ex:
            print(ex)
            return None
        
    def __put(self,fh,message)->bool:
        if message not in COLORS:
            raise BadColor(\
                f'Color {message} not found.')
        try:
            print(message,file=fh)
            fh.close()
            return True
        except:
            return False
        
    def __open(self,mode):
        try:
            return open('ipc.dat', mode)
        except:
            return False
        
    def send(self, data)->bool:
        if (fh := self.__open('w')):
            return self.__put(fh, data)
        return False
    
    def recv(self)->str:
        if (fh := self.__open('r')):
            return self.__get(fh)
        return ''

if __name__ == '__main__':
    cs = CsExcept()
    if not cs.send(COLORS[RED]):
       print('File creation error.')
    else:
       print(f'Status: [{cs.recv()}]')
