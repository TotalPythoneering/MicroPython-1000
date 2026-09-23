# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits01.py
# AUTHOR: Randall Nagy
# File: demo_bits01.py
#

# 1. AND Operator (`&`)
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11
i_and = a & b
print(f"AND: {bin(a)} & {bin(b)} = {bin(i_and)}")

