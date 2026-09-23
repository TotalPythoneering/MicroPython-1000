# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: list_classes2.py
# AUTHOR: Randall Nagy
#
import os
import ast

def find_python_files(directory='.'):
    """Find all .py files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.py') and os.path.isfile(os.path.join(directory, f))]

def extract_classes_from_file(filename):
    """Extract all class names from a given Python file."""
    class_names = []
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(), filename=filename)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_names.append(node.name)
        except Exception as e:
            print(f"Could not parse {filename}: {e}")
    return class_names

def main():
    pwd = 'C:/Users/ranag/Desktop/TotalPythoneering-main/PyTrek0001000/PyTrek/'
    all_class_names = set()
    python_files = find_python_files(pwd)
    for py_file in python_files:
        class_names = extract_classes_from_file(pwd + py_file)
        all_class_names.update(class_names)
    for class_name in sorted(all_class_names):
        print(class_name)

if __name__ == '__main__':
    main()
