# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: cs01_solution.py
# AUTHOR: Randall Nagy
# File: cs01_solution.py
# from cs01 import CsOne
#
import cs01

class CsOneSolution(cs01.CsOne): # 'Qualified'
    def __init__(self):
        super().__init__(None)

if __name__ == '__main__':
    print(CsOneSolution().recv())

