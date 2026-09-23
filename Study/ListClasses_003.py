#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: ListClasses_003.py
# AUTHOR: Randall Nagy
#
'''
Mission 0001002s: Scan every file in the 'pwd' listing
any class and function definitions found in the Python
files.

State: READY (R.S.C)
'''
import os
import os.path
from typing import Text, List


def list_files(zDir, file_type='.py'):
    ''' Return a list of file_type ending
    files found in zDir.
    '''
    results = list() # could also use []
    for file in os.listdir(zDir):
        if file.lower().endswith(file_type):
            zFile = zDir + os.path.sep + file
            results.append(zFile)
    return results


def list_blocks(py_file:Text, gate_keeper:List)->List:
    results = [] # could also use list()
    try:
        with open(py_file) as fh:
            for line in fh:
                pos = line.find(gate_keeper)
                if pos != -1:
                    zStr = line[pos:]
                    pos = zStr.find(':')
                    if pos != -1:
                        zStr = zStr[0:pos]
                        results.append(zStr)
    except Exception as ex:
        print(ex)
    return results


if __name__ == '__main__':
    pwd = r'C:\Users\ranag\Desktop\TotalPythoneering-main\PyTrek0001000\PyTrek'
    report = []
    for fss, zFile in enumerate(list_files(pwd), 1):
        report.extend(list_blocks(zFile, 'class '))

    report.sort()    
    for ss, block in enumerate(report, 1):
        print(ss, block)
    
