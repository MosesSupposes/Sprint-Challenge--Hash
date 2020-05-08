def intersection(arrays):
    tally = {}
    for sub_array in arrays: 
        for number in sub_array:
            if number not in tally:
                tally[number] = 1
            else:
                tally[number] += 1
    
    result = list(filter(lambda tally_tuple: tally_tuple[1] == len(arrays), tally.items()))
    result = list(map(lambda tally_tuple: tally_tuple[0], result))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
