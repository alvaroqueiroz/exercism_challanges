def flatten_array(nested_array):
    """
    flattens nested list
    input: nested list
    output: flatten list
    """
    # new array to be populated
    flatted_array = []

    #looping over the nested array
    for element in nested_array:

        # test type, if element is a list, call the function again for this element
        if type(element) == list:
            flatted_array.extend(flatten_array(element))

        # if it is str, int, float, etc, append to list
        elif element != None and element != ():
            flatted_array.append(element)

    return flatted_array

print(flatten_array([1,[2,3,None,4],[None],5]))