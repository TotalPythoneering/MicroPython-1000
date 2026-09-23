# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-13 13:22:44
# FILE: demo_except.py
# AUTHOR: Randall Nagy
# Mission: Demonstrate exceptional possibilities
# File: demo_except.py
#

colors = {'red', 'green', 'yellow'}
for _ in range(3): # try three times, most.
    try:
        data = input("test:")
        if data not in colors:
            raise Exception(
                f'Color [{data}] unfound.')
    except Exception as ex:
        print('*'*10, ex)
        raise
    else:
        print(f'"{data}" is ok.')
        #break
        continue
    finally:
        print('finally...')

