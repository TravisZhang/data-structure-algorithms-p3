def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 0:
        return ()
    min_value = ints[0]
    max_value = ints[0]
    for i in range(len(ints)):
        temp = ints[i]
        if temp <= min_value:
            min_value = temp
        if temp >= max_value:
            max_value = temp
    output = (min_value, max_value)
#     print("output: ", output)
    return output
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [1]
print(get_min_max(l))

l = []
print(get_min_max(l))
