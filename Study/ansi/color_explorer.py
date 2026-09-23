# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-12 07:01:06
# FILE: color_explorer.py
# AUTHOR: Randall Nagy
# We're using W.S.L, a.k.a
# "Windows Subsystem for
# Linux" - Debian.
# Video: https://ko-fi.com/post/Colorizing-Your-App--T-U-I-Style-C0C31JKS47
#

ESC = '\33[' # Escape 
RESET = ESC + '0m' # Yup

r = range(1,100)
for s,x in enumerate(r,1):
    print(f'{ESC}{x}m',
          f'{x:02}{RESET}',
          end='')
    if s % 10 == 0: print()
print()

