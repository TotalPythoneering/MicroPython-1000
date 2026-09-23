# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:45:30
# FILE: demo_bits08.py
# AUTHOR: Randall Nagy
# File: demo_bits08.py
#

# 8. Bit Setting
# Set a specific bit
a = 0b1101
i_sh = 1 << 3  # Setting the 4th bit (0-indexed)
i_set = a | i_sh
print(f"Bit Set: {bin(a)} | {bin(i_sh)} = {bin(i_set)}")

