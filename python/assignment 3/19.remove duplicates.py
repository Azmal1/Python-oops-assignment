# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]





def remove_duplicates(input_list):
    # Convert each inner list to a tuple and use set to remove duplicates
    unique_tuples = set(tuple(sublist) for sublist in input_list)

    # Convert the unique tuples back to lists to create the new list
    new_list = [list(sublist) for sublist in unique_tuples]

    return new_list

# Sample list of lists
sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

new_list = remove_duplicates(sample_list)

print("Sample list:", sample_list)
print("New List:", new_list)
