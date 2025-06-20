def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    """Sorts a list using bubble sort on a linked list with length x."""

    x = len(unsorted_list)

    for f in range(x): 
        swapped = False  #used to track if any swaps occur. if no swaps occur    this means the list has been sorted.

        for j in range(0, x-f-1): # range given ensure that we dont compare elements that we have already sorted.
            if unsorted_list[j] > unsorted_list[j+1]: 
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j] # the   unsorted_list[j] loop reiterates the through the unsorted portion of the list comparing it to the next element unsorted_list[j+1]
                swapped = True
        if not swapped:
            break
    return unsorted_list
   # pass
