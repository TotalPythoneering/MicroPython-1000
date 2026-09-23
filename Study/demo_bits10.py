# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits10.py
# AUTHOR: Randall Nagy
# File: demo_bits10.py
#
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11

# 10. Bit Flipping
# Flip a specific bit
i_to_f = 1 << 1  # Toggling the 2nd bit (0-indexed)
i_fd = a ^ i_to_f
print(f"Bit f: {bin(a)} ^ {bin(i_to_f)} = {bin(i_fd)}")

