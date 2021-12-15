
def get_element_from_dicts(list_dicts, key, value):

    elements = list(filter(lambda d: d[key] == value, list_dicts))
    return elements[0]
