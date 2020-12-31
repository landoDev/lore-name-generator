# pre project sandbox for functions to use in name generation endpoints

name_cache = {} 

altmer_a = ['Ad', 'Caem', 'Elsin', 'Gae', 'Gray', 'High', 'Jor', 'Lareth', 'Silin', 'Spell', 'Storm', 'Throm']
altmer_b = ['aire', 'al', 'binder', 'ian', 'ire', 'ius', 'lock', 'or', 'orin', 'thar', 'us', 'watch']

def create_surnames_elder_scrolls(front_half_list, back_half_list):
    ''' Takes two lists, combines each half into every possible name combination.'''
    list_index = 0
    for partial_name in front_half_list:
        generated_surname = partial_name + back_half_list[list_index]
        if generated_surname not in name_cache:
            name_cache[generated_surname] = 'exists'


