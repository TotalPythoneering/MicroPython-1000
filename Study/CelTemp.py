# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: CelTemp.py
# AUTHOR: Randall Nagy
#
class CelTemp:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        print("Reading Celsius.")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  # absolute 0
            self._celsius = -273.15 # not below
        else:
            self._celsius = value
        print("Set to", self._celsius,"Celsius.")

    @celsius.deleter
    def celsius(self):
        print("Deleting temperature attribute.")
        del self._celsius

# Usage example
temp = Temperature(25)

# Accessing the property (calls the getter)
print(f"Current temperature: {temp.celsius}°C")

# Modifying the property (calls the setter)
temp.celsius = 30
print(f"New temperature: {temp.celsius}°C")

# Attempting to set an invalid value (triggers ValueError from setter)
try:
    temp.celsius = -300
except ValueError as e:
    print(e)

# Deleting the property (calls the deleter)
try:
    del temp.celsius
    # Attempting to access after deletion will raise an AttributeError
    print(temp.celsius)
except AttributeError as e:
    print(f"Error accessing deleted attribute: {e}")
