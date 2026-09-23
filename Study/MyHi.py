# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: MyHi.py
# AUTHOR: Randall Nagy
#
def show(msg='Hello World', char='*')->None:
    line = len(msg) + 4
    print(char * line)
    print(char, msg, char)
    print(char * line)

if __name__ == '__main__':
    show(__name__)

