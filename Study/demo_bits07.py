# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits07.py
# AUTHOR: Randall Nagy
# File: demo_bits07.py
#
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11

# 7. Bit Masking
# Use a mask to isolate certain bits
mask = 0b111  # Mask with the last 3 bits set
m = a & mask
print(f"Masking: {bin(a)} & {bin(mask)} = {bin(m)}")

