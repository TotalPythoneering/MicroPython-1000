# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-06-20 05:59:02
# FILE: Solution.py
# AUTHOR: Randall Nagy
#
print ("Enter 1 or 0: ")
isFun = int(input("isFun? "))
isTough = int(input("isTough? "))

if isFun and isTough:
    print("We get what we pay for?")

if isTough or isFun:
    print("One 'outta 2 ain't bad!")

if not isFun:
    print("Practice makes it fun!")
    
if not (isTough and isFun):
    print("Learn C/C++?")


