def insertion_sort(unsorted_list):
    """
    Sorts a list in ascending order using the insertion sort alghoritm.

    Args: 
        data_list: A list of comparable elements

    Returns: 
        A sorted list of the same elements
    """

    # Check that input is a list
    if not isinstance(unsorted_list, list):
        raise TypeError("Input must be a list")

    for i in range(1, len(unsorted_list)):
        j = i
        # we should use j > 0 to exit loop when j becomes 0
        # while loop to move the element to its position in the sorted list
        while ((j > 0) and (unsorted_list[j] < unsorted_list[j-1])):      
            # Swap values
            unsorted_list[j], unsorted_list[j-1] = \
            unsorted_list[j-1], unsorted_list[j]
            # Go to the next pair
            j -= 1
    return unsorted_list

# Example usage
unsorted_list = list('insertionsort') 
sorted_list = insertion_sort(unsorted_list)
# ['e','i','i','n','n','o','o','r','r','s','s','t','t']
print(sorted_list)