# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: IntBytes.py
# AUTHOR: Randall Nagy
# Convert int to bytes
#
number = 259
# 2 bytes, big-endian
number.to_bytes(2, 'big')

# 2 bytes, little-endian
number.to_bytes(2, 'little') 

number = -259
# For signed signed=True
number.to_bytes(2, 'big', True)

n = number.to_bytes(2, 'little', False)
number.from_bytes(n, False)

'''
>>> number.from_bytes('0', False)
48
>>> ord('0')
48
'''
