# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
def main():
    user_list = []

    # Take inputs to create the list
    num_elements = int(input("Enter the number of elements in the list: "))
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    # Take input to search and delete
    element_to_delete = input("Enter the element to delete from the list: ")

    # Search and delete the element if found
    found = False
    for element in user_list:
        if element == element_to_delete:
            user_list.remove(element)
            found = True

    if found:
        print(f"{element_to_delete} was found and deleted from the list.")
    else:
        print(f"{element_to_delete} was not found in the list.")

    # Print the updated list
    print("Updated list:")
    for element in user_list:
        print(element)


if __name__ == "__main__":
    main()

    
