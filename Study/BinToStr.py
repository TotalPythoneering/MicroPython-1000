# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: BinToStr.py
# AUTHOR: Randall Nagy
#
def binary_to_unicode_string(binary_input):
    """
    Converts a string of 8-bit binary numbers into a Unicode character string.

    Args:
        binary_input (str): A string containing concatenated 8-bit binary numbers.
                            For example, "0100100001100101011011000110110001101111"
                            for "Hello".

    Returns:
        str: The resulting Unicode character string.
    """
    if len(binary_input) % 8 != 0:
        raise ValueError("Binary input length must be a multiple of 8.")

    unicode_characters = []
    for i in range(0, len(binary_input), 8):
        eight_bit_binary = binary_input[i:i+8]
        decimal_value = int(eight_bit_binary, 2)
        unicode_character = chr(decimal_value)
        unicode_characters.append(unicode_character)

    return "".join(unicode_characters)

# Example Usage:
binary_string_example = "0100100001100101011011000110110001101111"  # "Hello" in 8-bit binary
unicode_result = binary_to_unicode_string(binary_string_example)
print(f"The 8-bit binary string '{binary_string_example}' converts to: '{unicode_result}'")

binary_string_another_example = "001100010011001000110011" # "123" in 8-bit binary
unicode_result_another = binary_to_unicode_string(binary_string_another_example)
print(f"The 8-bit binary string '{binary_string_another_example}' converts to: '{unicode_result_another}'")
