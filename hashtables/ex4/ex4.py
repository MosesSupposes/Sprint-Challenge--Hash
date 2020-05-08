# To speed up the second test, you can reduce the range of the loop from 5 million to 500. 
# If it works with 500 items, it should work with 5 million as well.
def has_negatives(a):
    postivie_nums = {}
    for num in a:
        if num > 0 and num not in postivie_nums:
            postivie_nums[num] = False
    result = list(filter(lambda num: num * -1 in a, postivie_nums.keys()))
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
