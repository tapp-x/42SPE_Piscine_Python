import math


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif type(object) is float and math.isnan(object):
        print("Cheese: nan <class 'float'>")
    elif object == 0 and type(object) is int:
        print("Zero: 0 <class 'int'>")
    elif object == '':
        print("Empty:  <class 'str'>")
    elif object is False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not found")
        return 1
    return 0
