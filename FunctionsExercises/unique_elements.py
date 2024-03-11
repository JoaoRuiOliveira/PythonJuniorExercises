# Write a function that takes a list and returns a new list with unique elements of the first list.
def unique_elements(input_list):
    # Convert the list to a set to remove duplicates
    unique_elements = set(input_list)
    # Convert to list again to return the result
    return list(unique_elements)

# Test Cases
test_list = [1, 4, 2, 2, 3, 4, 4, 5, "a", "a", "b", "b", "c", "c"]
print(unique_elements(test_list))  # [1, 2, 3, 4, 5, 'b', 'c', 'a']