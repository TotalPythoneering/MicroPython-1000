#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: ListClassesMega.py
# AUTHOR: Randall Nagy
#
'''
Mission: Scan every file in the 'pwd' listing
any class definitions found in any Python file.
'''
from typing import List, Text


def list_blocks2(py_file:Text, gate_keeper:Text)->List:
    return list_structure(py_file, [gate_keeper])


def list_structure(py_file:Text, gate_keepers:List)->List:
    results = []
    if not py_file:
        return results
    try:
        with open(py_file) as fh:
            # 80:20 Rule?
            for line in fh:
                for gate_keeper in gate_keepers:
                    pos = line.find(gate_keeper)
                    if pos != -1:
                        zStr = line[pos:]
                        pos = zStr.find(':')
                        if pos != -1:
                            zStr = zStr[0:pos]
                            results.append(zStr)
                            # break?
    except Exception as ex:
        print(ex)
    return results


def list_blocks(py_file:Text, gate_keeper:Text)->List:
    results = []
    if not py_file:
        return results
    try:
        with open(py_file) as fh:
            # 80:20 Rule?
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


def list_all_file(zDir:Text, file_type='.py')->List: 
    import os, os.path
    results = list() # could also use []
    for root, dirs, files in os.walk(zDir):
        for file in files:
            if file.lower().endswith(file_type):
                results.append(root + '/' + file)
    return results


def list_files(zDir, file_type='.py'): 
    import os
    results = list() # could also use []
    for file in os.listdir(zDir):
        if file.lower().endswith(file_type):
            zFile = zDir + '/' + file
            results.append(zFile)
    return results


if __name__ == '__main__':
    pwd = r'C:\Users\ranag\Desktop\TotalPythoneering-main\PyTrek0001000\PyTrek'
    for fss, zFile in enumerate(list_files(pwd), 1):
        #zBlocks = list_blocks(zFile, 'class ')
        zBlocks = list_structure(zFile, ['class ', 'def '])
        #zBlocks = list_blocks2(zFile, 'class ')
        for ss, zBlock in enumerate(sorted(zBlocks), 1):
            if zBlock.startswith('def'):
                print('..... ',end='')
            print(f'{fss:02}.{ss:02}.) {zBlock}')
                
