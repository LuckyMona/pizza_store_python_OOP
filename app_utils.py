# from os import path
from enum import Enum

class NumberType(Enum):
    INT = "int"
    FLOAT = "float"

class LibraryAppUtils:
    def get_number_input(self, tint:str, type: NumberType) -> int|float:
        res = 0
        while True:
            try:
                if type == NumberType.INT:
                    res =int(input(f"Enter {tint}: "))
                elif type == NumberType.FLOAT:
                    res =float(input(f"Enter {tint}: "))
                break
            except Exception as e:
                print(f"Invalid {tint}")
        return res
    