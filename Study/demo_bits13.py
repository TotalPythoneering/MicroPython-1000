# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 08:41:24
# FILE: demo_bits13.py
# AUTHOR: Randall Nagy
# File: demo_bits13.py
#

# 13. Swapping Values Using XOR
x = 5  # 0b0101
y = 9  # 0b1001
print(f"Before Swap: x={x}, y={y}")
x = x ^ y
y = x ^ y
x = x ^ y
print(f"After Swap: x={x}, y={y}")

