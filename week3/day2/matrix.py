import numpy as np

# create a function that can intake a shape, data type, x, y
def create_matrix(start,stop, shape, datatype):
    if datatype == 'int':
        return np.random.randint(start, stop, shape)

    else:
        return np.random.uniform(start, stop, shape)
    
print(create_matrix(start=0,stop =10, shape = (5,2), datatype= 'int'))
