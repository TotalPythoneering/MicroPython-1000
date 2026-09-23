# MISSION: Support for ''Python 1000 - MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-11 08:14:46
# FILE: protocol.py
# AUTHOR: Randall Nagy
# Mission: Common protocol support.
# File: protocol.py
#

class BadColor(Exception):
    def __init__(self, err):
        super().__init__(err)
