# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: MyHiKwargs.py
# AUTHOR: Randall Nagy
# File: MyHiKwargs.py
#

def create_message(msg, char)->str:
    line = len(msg) + 4
    result = f'{char*line}\n'
    result += f"{char} {msg} {char}\n"
    result += f'{char*line}\n'
    return result

def show(**kwargs)->str:
    print(kwargs)
    zmsg = create_message(kwargs['msg'], kwargs['char'])
    print(zmsg)
    return zmsg


if __name__ == '__main__':
    should = '''***************
* Hello World *
***************
'''
    result = show(msg='Hello World',char='*')
    if result != should:
        print("Regression.")
    else:
        print("Testing Success!")
