# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-12 04:41:20
# FILE: x.py
# AUTHOR: Randall Nagy
#
for s, x in enumerate(range(1,100),1):
    print(f' \33[{x}m{x:02}\33[0m', end='')
    if s % 10 == 0: print()
print()
