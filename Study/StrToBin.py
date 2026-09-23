# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: StrToBin.py
# AUTHOR: Randall Nagy
#
def char_to_binary(char):
  """
  Converts a single character to its 8-bit binary string representation.

  Args:
    char: The character to convert.

  Returns:
    A string representing the 8-bit binary form of the character.
    Returns an empty string if the input is not a single character.
  """
  if not isinstance(char, str) or len(char) != 1:
    print("Error: Input must be a single character string.")
    return ""

  # Get the ASCII/Unicode value of the character
  ascii_value = ord(char)

  # Convert the ASCII value to an 8-bit binary string, padded with leading zeros
  binary_string = format(ascii_value, '08b')

  return binary_string

# Example usage:
character1 = 'A'
binary_representation1 = char_to_binary(character1)
print(f"The character '{character1}' in binary is: {binary_representation1}")

character2 = 'z'
binary_representation2 = char_to_binary(character2)
print(f"The character '{character2}' in binary is: {binary_representation2}")

character3 = '5'
binary_representation3 = char_to_binary(character3)
print(f"The character '{character3}' in binary is: {binary_representation3}")

# Example with invalid input
invalid_input = "Hello"
binary_representation_invalid = char_to_binary(invalid_input)
print(f"Result for invalid input '{invalid_input}': {binary_representation_invalid}")
