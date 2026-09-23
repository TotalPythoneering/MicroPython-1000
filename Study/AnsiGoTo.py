# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: AnsiGoTo.py
# AUTHOR: Randall Nagy
#
C = {
'BLACK':'\033[30m',
'RED':'\033[31m',
'GREEN':'\033[32m',
'YELLOW':'\033[33m',
'BLUE':'\033[34m',
'MAGENTA':'\033[35m',
'CYAN':'\033[36m',
'WHITE':'\033[37m',
'RESET':'\033[0m'}

def hide_code():
    return f"\033[?25l"

def show_code():
    return f"\033[?25h"

def set_cursor(row=1, col=1):
    return f"\033[{row};{col}H"

def colorize(msg, cfore='BLACK'):
    return f"{C[cfore]}{msg}{C['RESET']}"

if __name__ == '__main__':
    import sys, time, random
    times = 4
    even = times / 2
    count = 1
    lines = []
    colors = list(C.keys())
    print(hide_code(),end='')
    try:
        while True:
            x = random.randrange(1,16)
            y = random.randrange(1,10)
            color = random.randrange(len(C))
            print(set_cursor(y,x),colorize('X', colors[color]))
            sys.stdout.flush()
            time.sleep(1)
    except:
        print(show_code(),emd='')
'''
Note: In Python, \x1b is the hexadecimal representation of the ESC character (ASCII code 27). 
2. Control Sequence Introducer (CSI)
The escape character is typically followed by the Control Sequence Introducer (CSI), which is represented by a left square bracket [. 
3. SGR (Select Graphic Rendition) codes
These codes are used to control the visual appearance of text, such as color and styling. 

    Colors:
        Foreground (text) colors: Start with 30-37 for standard colors, 90-97 for bright colors.
        Background colors: Start with 40-47 for standard colors, 100-107 for bright colors.
        Example:
            \x1b[31m for red text
            \x1b[42m for green background
        Reset to default color: \x1b[0m
    Styles:
        Bold: \x1b[1m
        Underline: \x1b[4m
        Negative (inverse, swap foreground and background): \x1b[7m
        Dim: \x1b[2m
        Blink: \x1b[5m 

4. Cursor control

    Move cursor to home position (0,0): \x1b[H
    Move cursor to specific position (line, column): \x1b[{line};{column}H
    Move cursor up N lines: \x1b[{N}A
    Move cursor down N lines: \x1b[{N}B
    Move cursor right N columns: \x1b[{N}C
    Move cursor left N columns: \x1b[{N}D
    Move cursor to beginning of next line, N lines down: \x1b[{N}E
    Move cursor to beginning of previous line, N lines up: \x1b[{N}F
    Move cursor to column N: \x1b[{N}G
    Request cursor position (reports as \x1b[#;#R): \x1b[6n
    Save cursor position (DEC): \x1b7
    Restore cursor position (DEC): \x1b8
    Save cursor position (SCO): \x1b[s
    Restore cursor position (SCO): \x1b[u
    Hide cursor: \x1b[?25l
    Show cursor: \x1b[?25h 

5. Screen manipulation

    Clear screen from cursor to end: \x1b[0J
    Clear screen from cursor to beginning: \x1b[1J
    Clear entire screen: \x1b[2J
    Clear entire screen (without scrollback): \x1b[3J
    Clear screen and move cursor to home position: \x1b[2J\x1b[H
    Clear line from cursor to end: \x1b[0K
    Clear line from cursor to beginning: \x1b[1K
    Clear entire line: \x1b[2K 
'''
        


