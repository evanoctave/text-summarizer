def merge_plus_sort(list_1, list_2):
    """This function takes two lists of numbers as input.
    It will merge the two lists together and then sort the merged list.
    The sorted list will then be returned.
    """
    
    # First, we merge the two lists together
    merged_list = list_1 + list_2
    
    # Then, we sort the merged list
    sorted_list = sorted(merged_list)
    
    # Finally, we return the sorted list
    return sorted_list

def main():
    # First, we will get the two lists of numbers from the user
    
    # Get the first list of numbers
    # The user will enter a string of numbers separated by spaces
    # We will split that string into a list of strings
    # Then, we will convert each of those strings into an integer
    list_1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
    
    # Get the second list of numbers
    # The user will enter a string of numbers separated by spaces
    # We will split that string into a list of strings
    # Then, we will convert each of those strings into an integer
    list_2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
    
    # Now, we will print the result of merging and sorting the two lists
    # The result is the merged list sorted in numerical order
    print("Merged and sorted list: ", merge_plus_sort(list_1, list_2))
    
    
if __name__ == "__main__":
        main()