# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: fstr_floats.py
# AUTHOR: Randall Nagy
# File: fstr_floats.py
# Status: Unloved.
#

pi = 3.14159
price = 19.99999
percentage = 0.8525

# Placing decimals
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Price rounded to 2 decimals: {price:.2f}")

# Formatting percentages
print(f"Percentage with 1 decimal: {percentage:.1%}")

# Zero padding
num = 5
print(f"Padded number: {num:0>2}")
