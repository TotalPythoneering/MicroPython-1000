# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits11.py
# AUTHOR: Randall Nagy
# File: demo_bits11.py
#
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11

# 11. Checking if a Bit is Set
# Check if the 4th bit (0-indexed) is set
i_to_ck = 1 << 3
is_set = bool(a & i_to_ck)
print(f"Is Bit Set: {bin(a)} & {bin(i_to_ck)} = {is_set}")

