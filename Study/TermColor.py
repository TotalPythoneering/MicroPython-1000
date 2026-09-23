# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: TermColor.py
# AUTHOR: Randall Nagy
# pip install termcolor
#
from termcolor import colored

print(colored("Hello, World!", "red"))
print(colored("This is bold and underlined", "green", attrs=["bold", "underline"]))
print(colored("Yellow background", "black", "on_yellow"))
