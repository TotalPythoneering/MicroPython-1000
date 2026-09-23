# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits09.py
# AUTHOR: Randall Nagy
# File: demo_bits09.py
#
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11

# 9. Bit Clearing
# Clear a specific bit
i_to_x = ~(1 << 2)  # z 3rd bit (0-based)
i_xed = a & i_to_x
print(f"Clear: {bin(a)} & {bin(i_to_x)} = {bin(i_xed)}")

