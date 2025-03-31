# Get Value
def get_value(my_dict, key, default=None):
    return my_dict.get(key, default)

# Check Key
def check_key(my_dict, key):
    return key in my_dict

# Count Keys
def count_keys(my_dict):
    return len(my_dict)

# Get All Keys
def get_all_keys(my_dict):
    return list(my_dict.keys())

# Get All Values
def get_all_values(my_dict):
    return list(my_dict.values())

# Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

# Remove Key
def remove_key(my_dict, key):
    my_dict.pop(key, None)
    return my_dict

# Clear Dictionary
def clear_dictionary(my_dict):
    my_dict.clear()
    return my_dict

# Check if Dictionary is Empty
def is_empty_dictionary(my_dict):
    return not bool(my_dict)

# Get Key-Value Pair
def get_key_value_pair(my_dict, key):
    return (key, my_dict.get(key))

# Update Value
def update_value(my_dict, key, value):
    my_dict[key] = value
    return my_dict

# Count Value Occurrences
def count_value_occurrences(my_dict, value):
    return list(my_dict.values()).count(value)

# Invert Dictionary
def invert_dictionary(my_dict):
    return {v: k for k, v in my_dict.items()}

# Find Keys with Value
def find_keys_with_value(my_dict, value):
    return [k for k, v in my_dict.items() if v == value]

# Create a Dictionary from Lists
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

# Check for Nested Dictionaries
def check_nested_dictionaries(my_dict):
    return any(isinstance(v, dict) for v in my_dict.values())

# Get Nested Value
def get_nested_value(nested_dict, keys):
    for key in keys:
        nested_dict = nested_dict.get(key, {})
    return nested_dict

# Create Default Dictionary
from collections import defaultdict
def create_default_dict(default_value):
    return defaultdict(lambda: default_value)

# Count Unique Values
def count_unique_values(my_dict):
    return len(set(my_dict.values()))

# Sort Dictionary by Key
def sort_dict_by_key(my_dict):
    return dict(sorted(my_dict.items()))

# Sort Dictionary by Value
def sort_dict_by_value(my_dict):
    return dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Filter by Value
def filter_by_value(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(v)}

# Check for Common Keys
def check_common_keys(dict1, dict2):
    return any(key in dict2 for key in dict1)

# Create Dictionary from Tuple
def create_dict_from_tuple(tuple_var):
    return dict(tuple_var)

# Get the First Key-Value Pair
def get_first_key_value_pair(my_dict):
    key = next(iter(my_dict))
    return (key, my_dict[key])

# Test the functions
if __name__ == "__main__":
    test_dict1 = {'a': 1, 'b': 2, 'c': 3}
    test_dict2 = {'c': 10, 'd': 4, 'e': 5}
    test_list_keys = ['a', 'b', 'c']
    test_list_values = [1, 2, 3]

    print(get_value(test_dict1, 'a'))
    print(check_key(test_dict1, 'b'))
    print(count_keys(test_dict1))
    print(get_all_keys(test_dict1))
    print(get_all_values(test_dict1))
    print(merge_dictionaries(test_dict1, test_dict2))
    print(remove_key(test_dict1, 'a'))
    print(clear_dictionary(test_dict1))
    print(is_empty_dictionary(test_dict1))
    print(get_key_value_pair(test_dict2, 'c'))
    print(update_value(test_dict2, 'c', 15))
    print(count_value_occurrences(test_dict2, 15))
    print(invert_dictionary(test_dict2))
    print(find_keys_with_value(test_dict2, 15))
    print(create_dict_from_lists(test_list_keys, test_list_values))
    print(check_nested_dictionaries({'a': 1, 'b': {'c': 2}}))
    print(get_nested_value({'a': {'b': 2}}, ['a', 'b']))
    print(create_default_dict('default'))
    print(count_unique_values(test_dict2))
    print(sort_dict_by_key(test_dict1))
    print(sort_dict_by_value(test_dict1))
    print(filter_by_value(test_dict1, lambda x: x % 2 == 0))
    print(check_common_keys(test_dict1, test_dict2))
    print(create_dict_from_tuple([('a', 1), ('b', 2), ('c', 3)]))
    print(get_first_key_value_pair(test_dict2))