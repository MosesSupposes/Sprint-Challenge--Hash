def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {} 
    for i in range(length):
        weight_dict[weights[i]] = i
    
    for weight, index in weight_dict.items():
        if len(weights) == 2 and weights[0] == weights[1]:
            return (1,0)
        if limit - weight in weight_dict:
            indices = []
            indices.append(index)
            indices.append(weight_dict[limit - weight])
            indices.sort()
            indices.reverse()
            return tuple(indices)
    
    return None
