# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: AnsiLED.py
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


def led_bar(*colors):
    display = ''
    for c in colors:
      display += f"{C[c]}O{C['RESET']} "
    print(display,'\b' * len(display), end='')

def walker(lines, square, times, start='WHITE', top='BLUE', stop='RED'):
    if not square or not times:
       return ''
    display = []
    for ss in range(square):
        if ss < times:
           display.append(start)
        elif ss == times:
           display.append(top)
        else:
           display.append(stop)
    lines.append(display)
    times -= 1
    walker(lines, square, times, start, top, stop)
    return lines

if __name__ == '__main__':
    import time, sys
    times = 4
    even = times / 2
    count = 1
    lines = []
    while True:
        #print(count); count += 1
        for p in walker(lines, times, times):
            if not p:
                break
            if even:
                p.reverse()
            led_bar(*p)
            #print()
            sys.stdout.flush()
            time.sleep(0.05)
        even = False if even else True
        lines.clear()
    # led_bar('RED','YELLOW', 'BLUE')


