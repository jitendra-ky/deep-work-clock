def read_state(filename):
    '''
    this function will real the text file filename which contain some key value pairs like:
    key1 : value1
    key2 : value2
    and then return a dictionary with these key value pairs
    '''
    with open(filename, 'r') as file:
        lines = file.readlines()
        state = {}
        for line in lines:
            key, value = line.split(":")
            state[key.strip()] = value.strip()
    return state