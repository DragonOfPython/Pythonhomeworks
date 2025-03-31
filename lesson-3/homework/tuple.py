# Count Occurrences
def count_occurrences(tuple_var, element):
    return tuple_var.count(element)

# Max Element
def max_element(tuple_var):
    return max(tuple_var)

# Min Element
def min_element(tuple_var):
    return min(tuple_var)

# Check Element
def check_element(tuple_var, element):
    return element in tuple_var

# First Element
def first_element(tuple_var, default=None):
    return tuple_var[0] if tuple_var else default

# Last Element
def last_element(tuple_var, default=None):
    return tuple_var[-1] if tuple_var else default

# Tuple Length
def tuple_length(tuple_var):
    return len(tuple_var)

# Slice Tuple
def slice_tuple(tuple_var):
    return tuple_var[:3]

# Concatenate Tuples
def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2

# Check if Tuple is Empty
def is_empty_tuple(tuple_var):
    return not bool(tuple_var)

# Get All Indices of Element
def get_all_indices_of_element(tuple_var, element):
    return tuple([i for i, x in enumerate(tuple_var) if x == element])

# Find Second Largest
def find_second_largest(tuple_var):
    unique_nums = set(tuple_var)
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)

# Find Second Smallest
def find_second_smallest(tuple_var):
    unique_nums = set(tuple_var)
    unique_nums.remove(min(unique_nums))
    return min(unique_nums)

# Create a Single Element Tuple
def create_single_element_tuple(element):
    return (element,)

# Convert List to Tuple
def convert_list_to_tuple(lst):
    return tuple(lst)

# Check if Tuple is Sorted
def is_sorted_tuple(tuple_var):
    return tuple_var == tuple(sorted(tuple_var))

# Find Maximum of Subtuple
def find_max_of_subtuple(tuple_var, start, end):
    return max(tuple_var[start:end+1])

# Find Minimum of Subtuple
def find_min_of_subtuple(tuple_var, start, end):
    return min(tuple_var[start:end+1])

# Remove Element by Value
def remove_element_by_value(tuple_var, element):
    index = tuple_var.index(element)
    return tuple_var[:index] + tuple_var[index+1:]

# Create Nested Tuple
def create_nested_tuple(tuple_var, sublist_size):
    return tuple(tuple_var[i:i+sublist_size] for i in range(0, len(tuple_var), sublist_size))

# Repeat Elements
def repeat_elements(tuple_var, n):
    return tuple(elem for elem in tuple_var for _ in range(n))

# Create Range Tuple
def create_range_tuple(start, end):
    return tuple(range(start, end+1))

# Reverse Tuple
def reverse_tuple(tuple_var):
    return tuple_var[::-1]

# Check Palindrome
def is_palindrome_tuple(tuple_var):
    return tuple_var == tuple_var[::-1]

# Get Unique Elements
def get_unique_elements(tuple_var):
    return tuple(dict.fromkeys(tuple_var))

# Test the functions
if __name__ == "__main__":
    test_tuple = (1, 2, 3, 4, 5, 1, 3, 5)

    print(count_occurrences(test_tuple, 1))
    print(max_element(test_tuple))
    print(min_element(test_tuple))
    print(check_element(test_tuple, 6))
    print(first_element(test_tuple))
    print(last_element(test_tuple))
    print(tuple_length(test_tuple))
    print(slice_tuple(test_tuple))
    print(concatenate_tuples(test_tuple, (6, 7, 8)))
    print(is_empty_tuple(()))
    print(get_all_indices_of_element(test_tuple, 3))
    print(find_second_largest(test_tuple))
    print(find_second_smallest(test_tuple))
    print(create_single_element_tuple(10))
    print(convert_list_to_tuple([1, 2, 3]))
    print(is_sorted_tuple(test_tuple))
    print(find_max_of_subtuple(test_tuple, 2, 5))
    print(find_min_of_subtuple(test_tuple, 1, 4))
    print(remove_element_by_value(test_tuple, 3))
    print(create_nested_tuple(test_tuple, 2))
    print(repeat_elements(test_tuple, 2))
    print(create_range_tuple(1, 5))
    print(reverse_tuple(test_tuple))
    print(is_palindrome_tuple(test_tuple))
    print(get_unique_elements(test_tuple))