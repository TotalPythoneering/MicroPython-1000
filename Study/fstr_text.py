# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: fstr_text.py
# AUTHOR: Randall Nagy
# File: fstr_text.py
# Status: Unloved.
#

text = "uPy"
# Aligned left (default)
print(f"Left aligned:\t[{text:<10}]")
# Aligned center
print(f"Center aligned:\t[{text:^10}]")
# Aligned right
print(f"Right aligned:\t[{text:>10}]")
# Aligned center with surrounding character
print(f"Padded by ':':\t[{text::^10}]")
