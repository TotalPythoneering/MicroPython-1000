# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: demo_isalpha.py
# AUTHOR: Randall Nagy
#


option = input('Enter a string then press enter: ')

if option.isalpha():
    print("Is not numeric.")
else:
    print("Is not alphabetic.")

