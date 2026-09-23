# MISSION: The complete set of examples and source code for ''Python 1000 -
# MicroPython for Everyone.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/MicroPython-1000
# DATE: 2024-12-25 10:30:46
# FILE: skitz03.py
# AUTHOR: Randall Nagy
#
class Skitz:

    def __init__(self, *args, **kwargs):
        print(*args)
        if not 'zName' in kwargs:
            self.name = None
        else:
            self.name=kwargs['zName']
        if not 'zAge' in kwargs:
            self._age = -1
        else:
            self._age=kwargs['zAge']
        if not 'zPhone' in kwargs:
            kwargs['zPhone'] = ''
        self.phone=kwargs['zPhone']
        print(vars(self))

    def set_age(self, age):
        if age < 0:
            raise ValueError("Error: Age is negative")
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, zAge):
        self.set_age(zAge)
    
var = Skitz(1,2,4,zName='Nagy', zAge=123, zPhone='123-456-7890')
var = Skitz(1,2,3)
var = Skitz()



