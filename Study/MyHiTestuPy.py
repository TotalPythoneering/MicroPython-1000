# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: MyHiTestuPy.py
# AUTHOR: Randall Nagy
# File: MyHiTestuPy.py
#

def create_message(msg, char)->str:
    line = len(msg) + 4
    result = f'{char*line}\n'
    result += f"{char} {msg} {char}\n"
    result += f'{char*line}\n'
    return result

def show(msg='Hello World', char='*')->str:
    zmsg = create_message(msg, char)
    print(zmsg)
    return zmsg


if __name__ == '__main__':
    should = '''***************
* Hello World *
***************
'''
    result = show()
    print(result)
    if show() != should:
        print("Regression.")
    else:
        print("Testing Success!")
