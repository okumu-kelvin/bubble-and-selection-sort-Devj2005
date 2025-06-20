def selection_sort(unsorted_list):

    # TODO: Implement selection sort
    x = len(unsorted_list) # to fing the length of the unsorted list

    for j in range(x):
        min_index = j #this is done to find the minimum element in the unsorted part of the list is the first element
       
        for k in range(j+1, x):
            if unsorted_list[k] < unsorted_list[min_index]:
                min_index = k   


        # Swap the found minimum element with the first element of the unsorted part and put it in the sorted part
        unsorted_list[j], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[j]

    
    return unsorted_list  



