# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: my_hi_test.py
# AUTHOR: Randall Nagy
#
def Show():
    print("\t***************")
    print("\t* Hello World *")
    print("\t***************")

if __name__ == '__main__':
    should = '''	***************
	* Hello World *
	***************
'''
    import sys
    import io
    sys_stdout = sys.stdout
    stdout_buffer = io.StringIO()
    sys.stdout = stdout_buffer
    Show()
    sys.stdout = sys_stdout # restored
    if stdout_buffer.getvalue() != should:
        print("Regression.")
    else:
        print("Testing Success!")
