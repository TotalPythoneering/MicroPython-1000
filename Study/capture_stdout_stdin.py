# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: capture_stdout_stdin.py
# AUTHOR: Randall Nagy
#
import sys
import io

# ---- Capture stdout to a string ----
sys_stdout = sys.stdout
stdout_buffer = io.StringIO()
sys.stdout = stdout_buffer

print("This will go into the string, not the console.")

# Restore original stdout
sys.stdout = sys_stdout
captured_output = stdout_buffer.getvalue()
print("Captured stdout:", captured_output)

# ---- Read stdin from a string ----
sys_stdin = sys.stdin
stdin_buffer = io.StringIO("Pretend this is user input\nSecond line\n")
sys.stdin = stdin_buffer

# Now input() and sys.stdin.read() will read from the string
user_input = input("Prompt (will not be shown): ")
print("Read from stdin:", user_input)

sys.stdin = sys_stdin  # Restore original stdin
