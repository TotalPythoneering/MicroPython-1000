# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: ColorizedSolution.py
# AUTHOR: Randall Nagy
# PLEASE RUN FROM THE COMMAND LINE, ONLY.
# The following codes work on POSIX / Linux
# command line interfaces ONLY. Tested on WSL.
#

COLORS = [
    '\033[30m','\033[34m','\033[36m',
    '\033[32m','\033[35m','\033[31m',
    '\033[37m','\033[33m','\033[0m'
    ]

# "Manifest Constants"
BLACK   = 0
BLUE    = 1
CYAN    = 2
GREEN   = 3
MAGENTA = 4
RED     = 5
WHITE   = 6
YELLOW  = 7
RESET   = 8

def show(message, color=WHITE):
    if color not in range(len(COLORS)):
        color = WHITE
    print(f'{COLORS[color]}\
{message}\
{COLORS[RESET]}')

if __name__ == '__main__':
    show('Welcome!')
    for color in range(len(COLORS)):
        show(f'This is color #{color}...', color)
    show('Testing Success!')
