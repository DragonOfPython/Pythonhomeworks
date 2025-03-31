import random

# Union of Sets
def union_sets(set1, set2):
    return set1.union(set2)

# Intersection of Sets
def intersection_sets(set1, set2):
    return set1.intersection(set2)

# Difference of Sets
def difference_sets(set1, set2):
    return set1.difference(set2)

# Check Subset
def check_subset(set1, set2):
    return set1.issubset(set2)

# Check Element
def check_element_in_set(my_set, element):
    return element in my_set

# Set Length
def set_length(my_set):
    return len(my_set)

# Convert List to Set
def convert_list_to_set(my_list):
    return set(my_list)

# Remove Element
def remove_element_from_set(my_set, element):
    my_set.discard(element)
    return my_set

# Clear Set
def clear_set(my_set):
    my_set.clear()
    return my_set

# Check if Set is Empty
def is_empty_set(my_set):
    return not bool(my_set)

# Symmetric Difference
def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

# Add Element
def add_element_to_set(my_set, element):
    my_set.add(element)
    return my_set

# Pop Element
def pop_element_from_set(my_set):
    if my_set:
        return my_set.pop()
    else:
        return None

# Find Maximum
def find_maximum(set_of_nums):
    return max(set_of_nums)

# Find Minimum
def find_minimum(set_of_nums):
    return min(set_of_nums)

# Filter Even Numbers
def filter_even_numbers(set_of_nums):
    return {num for num in set_of_nums if num % 2 == 0}

# Filter Odd Numbers
def filter_odd_numbers(set_of_nums):
    return {num for num in set_of_nums if num % 2 != 0}

# Create a Set of a Range
def create_set_of_range(start, end):
    return set(range(start, end+1))

# Merge and Deduplicate
def merge_and_deduplicate(list1, list2):
    return set(list1).union(set(list2))

# Check Disjoint Sets
def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

# Remove Duplicates from a List
def remove_duplicates_from_list(my_list):
    return list(set(my_list))

# Count Unique Elements
def count_unique_elements(my_list):
    return len(set(my_list))

# Generate Random Set
def generate_random_set(size, start, end):
    return set(random.sample(range(start, end+1), size))

# Test the functions
if __name__ == "__main__":
    test_set1 = {1, 2, 3, 4, 5}
    test_set2 = {4, 5, 6, 7, 8}
    test_list1 = [1, 2, 3, 4, 5, 1, 3, 5]
    test_list2 = [4, 5, 6, 7, 8]

    print(union_sets(test_set1, test_set2))
    print(intersection_sets(test_set1, test_set2))
    print(difference_sets(test_set1, test_set2))
    print(check_subset(test_set1, test_set2))
    print(check_element_in_set(test_set1, 6))
    print(set_length(test_set1))
    print(convert_list_to_set(test_list1))
    print(remove_element_from_set(test_set1, 3))
    print(clear_set(test_set1))
    print(is_empty_set(test_set1))
    print(symmetric_difference_sets(test_set1, test_set2))
    print(add_element_to_set(test_set1, 6))
    print(pop_element_from_set(test_set1))
    print(find_maximum(test_set1))
    print(find_minimum(test_set1))
    print(filter_even_numbers(test_set1))
    print(filter_odd_numbers(test_set1))
    print(create_set_of_range(1, 10))
    print(merge_and_deduplicate(test_list1, test_list2))
    print(check_disjoint_sets(test_set1, test_set2))
    print(remove_duplicates_from_list(test_list1))
    print(count_unique_elements(test_list1))
    print(generate_random_set(5, 1, 10))