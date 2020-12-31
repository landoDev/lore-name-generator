
def bulk_create_names_from_halves(front_half_list, back_half_list):
    ''' Takes two lists, combines each half into every possible name combination.'''
    
    generated_names = []

    for partial_name in front_half_list:
        names = [partial_name + string for string in back_half_list]
        generated_names.append(names)
    
    # squash the list of lists
    generated_names = [name for sublist in generated_names for name in sublist]

    return generated_names


