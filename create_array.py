import numpy as np


def create_array(sum_value, samples, min_value, max_value):
    
    # The max_value will be the boundary, so it won't be included in the items of the array
    
    # Posible Values
    boundaries = range(min_value, max_value)
    
    # Random percentages for the samples with dirichlet distribution
    weights = np.random.dirichlet(np.ones(len(boundaries)),size=1)[0]
    
    # Getting random vector
    vector = np.random.choice(len(boundaries), p=weights, size=(samples))
    
    # Sum one to avoid zeros and include the max_value - 1
    vector = vector + 1
    
    sum_vector = sum(vector)

    
    batches = [10000,1000, 100, 10, 1]

    if sum_vector < sum_value:
        
        diference = sum_value - sum_vector

        #The difference will be distributed through all the values in the array, 
        # except those which are equals to the limit value
        
        while diference != 0:
            
            possible_idx = np.where(vector < max_value-1)[0]
            
            if possible_idx.size:
                
                for batch in batches:
                    if diference%batch != diference:
                        batch = batch
                        break
                
                choice_idxs = np.random.choice(possible_idx, batch)
                vector[choice_idxs] = vector[choice_idxs]+1

                sum_vector = sum(vector)
                diference = sum_value - sum_vector
                
            else:
                raise ValueError('MAYBE YOU SHOULD INCREASE MAX_VALUE, OTHERWISE ITS NOT POSSIBLE BUILD THE ARRAY DESIRED')
                break
            
    else:
        diference = sum_vector - sum_value
        
        # The difference will be subtracted from all the values in the array higher than 1 
        
        while diference != 0:
            
            possible_idx = np.where(vector > min_value)[0]
            
            if possible_idx.size:
                for batch in batches:
                    if diference%batch != diference:
                        batch = batch
                        break
                
                choice_idxs = np.random.choice(possible_idx, batch)
                vector[choice_idxs] = vector[choice_idxs]-1

                sum_vector = sum(vector)
                diference = sum_vector - sum_value
                
            else:
                raise ValueError('MAYBE YOU SHOULD INCREASE MAX_VALUE, OTHERWISE ITS NOT POSSIBLE BUILD THE ARRAY DESIRED')
                break
    
    np.random.shuffle(vector)
    
    return vector
