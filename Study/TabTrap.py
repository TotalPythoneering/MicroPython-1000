# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-06-19 08:55:30
# FILE: TabTrap.py
# AUTHOR: Randall Nagy
#
option = input("Entry: ")
if option.isalpha():
    print(option)
    print(".isalpha()!")
else:
    print("Nope...")

