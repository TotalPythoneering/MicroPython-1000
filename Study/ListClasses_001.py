#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: ListClasses_001.py
# AUTHOR: Randall Nagy
#
'''
Mission 0001001s: Scan every file in the 'pwd' listing
any class definitions found in the Python files.

State: READY (R.S.C)
'''
import os
import os.path

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


if __name__ == '__main__':
    pwd = r'C:\Users\ranag\Desktop\TotalPythoneering-main\PyTrek0001000\PyTrek'
    for fss, zFile in enumerate(list_files(pwd), 1):
        print(fss, ".)", zFile)
