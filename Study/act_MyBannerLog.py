# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: act_MyBannerLog.py
# AUTHOR: Randall Nagy
# File: MyBannerLog.py
# Console Message
#

prefix = {1:"DEBUG", 2:"WARNING", 3:"ERROR", 4:"INFO"}
           
def message(which, message):
    pass


if __name__ == "__main__":
    for which in prefix.keys():
        message(which, "This is zMessage")

