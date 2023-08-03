# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
def sort_dict_by_value(d, ascending=True):
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_d

# Example usage:
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sorting in ascending order by value
sorted_ascending = sort_dict_by_value(d, ascending=True)
print("Dictionary sorted in ascending order by value:")
print(sorted_ascending)

# Sorting in descending order by value
sorted_descending = sort_dict_by_value(d, ascending=False)
print("Dictionary sorted in descending order by value:")
print(sorted_descending)
