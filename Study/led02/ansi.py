# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-14 06:55:04
# FILE: ansi.py
# AUTHOR: Randall Nagy
# File: ansi.py
#
CLS = '\033[2J\033[H'

COLORS = {
    'BLACK':'\033[30m','BLUE':'\033[34m',
    'CYAN':'\033[36m','GREEN':'\033[32m',
    'MAGENTA':'\033[35m','RED':'\033[31m',
    'WHITE':'\033[37m','YELLOW':'\033[33m',
    'RESET':'\033[0m'
    }

def cls():
    print(CLS,end='')

def show(color,message):
    if color not in COLORS:
        color = 'WHITE'
    print(f'{COLORS[color]}{message}{COLORS["RESET"]}')

if __name__ == '__main__':
    cls()
    show(COLORS['BLUE'],'Welcome!')
    for color in COLORS:
        show(color, f'This is color #{color}...')
    show('GREEN','Testing Success!')
