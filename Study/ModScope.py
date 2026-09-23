# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: ModScope.py
# AUTHOR: Randall Nagy
#
def __private_function(msg:str)->None:
    print(str)

def show(msg:str)->None:
    _private_function(msg)
