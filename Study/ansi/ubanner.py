# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-12 11:32:38
# FILE: ubanner.py
# AUTHOR: Randall Nagy
# File: ubanner.py
# Super-Colorized Console Message (Uber!)
#

COLORS = {
    'BLACK'  :'\033[30m','BLUE'  :'\033[34m',
    'CYAN'   :'\033[36m','GREEN' :'\033[32m',
    'MAGENTA':'\033[35m','RED'   :'\033[31m',
    'WHITE'  :'\033[37m','YELLOW':'\033[33m',

    'LTBLACK'  :'\033[90m','LTBLUE'  :'\033[94m',
    'LTCYAN'   :'\033[96m','LTGREEN' :'\033[92m',
    'LTMAGENTA':'\033[95m','LTRED'   :'\033[91m',
    'LTWHITE'  :'\033[97m','LTYELLOW':'\033[93m',
    
    'BKBLACK'  :'\033[40m','BKBLUE'  :'\033[44m',
    'BKCYAN'   :'\033[46m','BKGREEN' :'\033[42m',
    'BKMAGENTA':'\033[45m','BKRED'   :'\033[41m',
    'BKWHITE'  :'\033[47m','BKYELLOW':'\033[43m',
    'RESET'    :'\033[0m'
    }

prefix = \
   {"DEBUG":  [COLORS['LTYELLOW'],   COLORS['BKBLACK']],
    "WARNING":[COLORS['LTGREEN'], COLORS['BKBLUE']],
    "ERROR":  [COLORS['RED'],    COLORS['BKBLACK']],
    "INFO":   [COLORS['WHITE'],  COLORS['BKBLUE']]}
           
def message(which:str, message:str):
    # "sanity checking"
    which = str(which).upper()
    if which not in prefix:
        which = 'DEBUG'
    print(prefix[which][0] +
          prefix[which][1] + which + ': ',
        message, COLORS['RESET'],sep='')

if __name__ == "__main__":
    for which in prefix:
        message(which,f"This is {which} ")

