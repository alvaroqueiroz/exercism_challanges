def transform(word_dict):
    """
    Transforms data format, "flattens" dict values and change keys->values
    input : dict
    output : dict
    """
    # new dict to populate on the loop
    transformed_data = {}
    #loop over dict
    for number, words in word_dict.items():
        # loop over the list inside the keys values of the dict
        for word in words:
            # add them with the same key name
            transformed_data[word.lower()] = number

    return transformed_data

# test
data = {

    "1 point": ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    "3 points": ["B", "C", "M", "P"],
    "4 points": ["F", "H", "V", "W", "Y"],
    "5 points": ["K"],
    "8 points": ["J", "X"],
    "10 points": ["Q", "Z"]
    }

print(transform(data))