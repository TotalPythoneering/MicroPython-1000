# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2025-08-20 10:12:18
# FILE: running_total_calculator.py
# AUTHOR: Randall Nagy
#
'''
Requirement:
 Use python to create a calculator to input integers and floating
point numbers so as to calculate a running total in a forever loop.
An entry of zero will exit the program.

Google A.I Response:
 The following Python code creates a calculator that accepts integer
and floating-point numbers, calculating a running total in a continuous
loop. The program exits when a zero is entered.
'''

def running_total_calculator():
    """
    Calculates a running total from user-inputted numbers.
    The program continues until the user enters 0.
    """
    total = 0.0  # Initialize the running total as a float

    print("Running Total Calculator")
    print("Enter numbers to add to the total. Enter 0 to exit.")

    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)  # Attempt to convert input to a float

            if number == 0:
                print(f"Exiting program. Final total: {total}")
                break  # Exit the loop if 0 is entered
            else:
                total += number  # Add the number to the running total
                print(f"Current running total: {total}")

        except ValueError:
            print("Invalid input. Please enter a valid number (integer or float).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    running_total_calculator()
