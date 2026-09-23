#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: ListBlocks2.py
# AUTHOR: Randall Nagy
#
'''
Mission: Scan every file in the 'pwd' listing
class and function definitions found in any
Python file.

File: ListBlocks2.py

State: READY (R.S.C)
'''
import os, os.path

TC2 = False


def list_files(zDir, file_type='.py'):
    '''
    Return an unsorted list of typed file names in zDir.
    '''
    if not zDir.endswith(os.path.sep): # Fun - see TC2.
        zDir += os.path.sep
    results = list()
    for file in os.listdir(zDir):
        if file.lower().endswith(file_type):
            zFile = zDir + file
            results.append(zFile)
    return results


if __name__ == '__main__':
    import re
    
    ptrn_class = re.compile(
        r'^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\([^\)]*\))?\s*:',
        re.MULTILINE
    )

    ptrn_both = re.compile(r'^\s*(class|def)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(', re.MULTILINE)

    if TC2:
        pwd = r'C:\Users\ranag\Desktop\TotalPythoneering-main\PyTrek0001000\PyTrek'
    else:
        pwd = 'C:/Users/ranag/Desktop/TotalPythoneering-main/PyTrek0001000/PyTrek/'

    for fss, zFile in enumerate(sorted(list_files(pwd)), 1):
        if TC2:
            print(zFile) # "/\"
            
        with open(zFile) as fh:
            prev_class = False              # EDGE: Fix ZeroBased def problem.
            data = str(fh.read())
            zBlocks = ptrn_both.findall(data)
            print(zFile.split(os.path.sep)[-1])
        if not zBlocks:
            print("\tThere are no blocks.") # EDGE: Confirm there are no blocks.
            continue
        for ss, zBlock in enumerate(zBlocks,0):
            if zBlock[0].startswith('class'):
                prev_class = True           # NOTE: Why not ... not?  =)
            if zBlock[0].startswith('def'):
                print('..... ',end='')
                if not prev_class:
                    print(f'{fss:02}.{ss + 1:02} {zBlock[0]} {zBlock[1]}')
                    continue
            print(f'{fss:02}.{ss:02} {zBlock[0]} {zBlock[1]}')
            
    import sys
    m = sys.argv[0].split(os.path.sep)
    print("\nFile:",m[-1])
