def get_value_or_null(dictionary: dict, key: str):
    if key in dictionary:
        return dictionary[key]
    return None


def get_value_or_throw_error(dictionary: dict, key: str):
    if key not in dictionary:
        raise Exception('The field "{}" can\'t be empty'.format(key))
    return dictionary[key]
