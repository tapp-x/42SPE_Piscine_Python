def all_thing_is_obj(object: any) -> int:
    types_tab = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }
    type_obj = type(object)
    type_name = types_tab.get(type_obj, "Type not found")
    if type_obj == str:
        print(f"{object} is in the kitchen : {type_obj}")
    elif type_name != "Type not found":
        print(f"{type_name} : {type_obj}")
    else:
        print("Type not found")
    return (42)
