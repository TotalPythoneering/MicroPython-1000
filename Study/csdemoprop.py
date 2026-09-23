# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-09 15:15:28
# FILE: csdemoprop.py
# AUTHOR: Randall Nagy
#
class CsDemo():
    def __init__(self, data=None):
        self.__data = data
    def send(self): ...
    def recv(self): ...
    @property
    def data(self): return self.__data
    @data.setter
    def data(self,value): self.__data = value
    @data.deleter
    def data(self): self.__data = '(deleted)'


