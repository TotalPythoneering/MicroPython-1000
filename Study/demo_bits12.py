# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits12.py
# AUTHOR: Randall Nagy
# File: demo_bits12.py
#
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11

# 12. Counting Set Bits
# Count the number of 1s in the binary representation
i_bits = bin(a).count('1')
print(f"Count Set Bits: {bin(a)} has {i_bits} set bits")

