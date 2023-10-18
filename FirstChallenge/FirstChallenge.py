def no_it_isnt(given_list):
    list_of_opposite_values = []
    for value in given_list:  
        if isinstance(value, bool):
            list_of_opposite_values.append(not value)
        elif isinstance(value, int) or isinstance(value, float):
            list_of_opposite_values.append(-value)
        elif isinstance(value, str):
            list_of_opposite_values.append(value[::-1])
    list_of_opposite_values.reverse()
    return list_of_opposite_values