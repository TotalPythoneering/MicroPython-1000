# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits15.py
# AUTHOR: Randall Nagy
# File: demo_bits15.py
#
a = 0b1101  # Binary for 13
b = 0b1011  # Binary for 11

# 15. Parity Testing
# Tally 1s as either 'odd' or 'even'
parity = bin(a).count('1') % 2
print(f"Parity: {bin(a)} has \
{'odd' if parity else 'even'} \
parity")

