# Count Occurrences
def count_occurrences(lst, element):
    return lst.count(element)

# Sum of Elements
def sum_elements(lst):
    return sum(lst)

# Max Element
def max_element(lst):
    return max(lst)

# Min Element
def min_element(lst):
    return min(lst)

# Check Element
def check_element(lst, element):
    return element in lst

# First Element
def first_element(lst, default=None):
    return lst[0] if lst else default

# Last Element
def last_element(lst, default=None):
    return lst[-1] if lst else default

# Slice List
def slice_list(lst):
    return lst[:3]

# Reverse List
def reverse_list(lst):
    return lst[::-1]

# Sort List
def sort_list(lst):
    return sorted(lst)

# Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))

# Insert Element
def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

# Index of Element
def index_of_element(lst, element):
    return lst.index(element)

# Check for Empty List
def is_empty(lst):
    return not bool(lst)

# Count Even Numbers
def count_even_numbers(lst):
    return sum(1 for num in lst if num % 2 == 0)

# Count Odd Numbers
def count_odd_numbers(lst):
    return sum(1 for num in lst if num % 2 != 0)

# Concatenate Lists
def concatenate_lists(lst1, lst2):
    return lst1 + lst2

# Find Sublist
def find_sublist(lst, sublist):
    return all(elem in lst for elem in sublist)

# Replace Element
def replace_element(lst, old_element, new_element):
    idx = lst.index(old_element)
    lst[idx] = new_element
    return lst

# Find Second Largest
def find_second_largest(lst):
    unique_nums = set(lst)
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)

# Find Second Smallest
def find_second_smallest(lst):
    unique_nums = set(lst)
    unique_nums.remove(min(unique_nums))
    return min(unique_nums)

# Filter Even Numbers
def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Filter Odd Numbers
def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

# List Length
def list_length(lst):
    return len(lst)

# Create a Copy
def create_copy(lst):
    return lst.copy()

# Get Middle Element
def get_middle_element(lst):
    length = len(lst)
    if length % 2 == 0:
        return lst[length // 2 - 1], lst[length // 2]
    else:
        return lst[length // 2]

# Find Maximum of Sublist
def find_max_of_sublist(lst, start, end):
    return max(lst[start:end+1])

# Find Minimum of Sublist
def find_min_of_sublist(lst, start, end):
    return min(lst[start:end+1])

# Remove Element by Index
def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst

# Check if List is Sorted
def is_sorted(lst):
    return lst == sorted(lst)

# Repeat Elements
def repeat_elements(lst, n):
    return [elem for elem in lst for _ in range(n)]

# Merge and Sort
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

# Find All Indices
def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

# Rotate List
def rotate_list(lst, n=1):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# Create Range List
def create_range_list(start, end):
    return list(range(start, end+1))

# Sum of Positive Numbers
def sum_positive_numbers(lst):
    return sum(num for num in lst if num > 0)

# Sum of Negative Numbers
def sum_negative_numbers(lst):
    return sum(num for num in lst if num < 0)

# Check Palindrome
def is_palindrome(lst):
    return lst == lst[::-1]

# Create Nested List
def create_nested_list(lst, sublist_size):
    return [lst[i:i+sublist_size] for i in range(0, len(lst), sublist_size)]

# Get Unique Elements in Order
def get_unique_elements_in_order(lst):
    return list(dict.fromkeys(lst))

# Test the functions
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 1, 3, 5]

    print(count_occurrences(test_list, 1))
    print(sum_elements(test_list))
    print(max_element(test_list))
    print(min_element(test_list))
    print(check_element(test_list, 6))
    print(first_element(test_list))
    print(last_element(test_list))
    print(slice_list(test_list))
    print(reverse_list(test_list))
    print(sort_list(test_list))
    print(remove_duplicates(test_list))
    print(insert_element(test_list, 10, 2))
    print(index_of_element(test_list, 3))
    print(is_empty([]))
    print(count_even_numbers(test_list))
    print(count_odd_numbers(test_list))
    print(concatenate_lists(test_list, [6, 7, 8]))
    print(find_sublist(test_list, [1, 3, 5]))
    print(replace_element(test_list, 3, 9))
    print(find_second_largest(test_list))
    print(find_second_smallest(test_list))
    print(filter_even_numbers(test_list))
    print(filter_odd_numbers(test_list))
    print(list_length(test_list))
    print(create_copy(test_list))
    print(get_middle_element(test_list))
    print(find_max_of_sublist(test_list, 2, 5))
    print(find_min_of_sublist(test_list, 1, 4))
    print(remove_element_by_index(test_list, 3))
    print(is_sorted(test_list))
    print(repeat_elements(test_list, 2))
    print(merge_and_sort(test_list, [6, 4, 2]))
    print(find_all_indices(test_list, 3))
    print(rotate_list(test_list, 2))
    print(create_range_list(1, 5))
    print(sum_positive_numbers(test_list))
    print(sum_negative_numbers(test_list))
    print(is_palindrome(test_list))
    print(create_nested_list(test_list, 2))
    print(get_unique_elements_in_order(test_list))