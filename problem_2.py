def recur_fun(input_list, start, end, number):
    if input_list[start] == number:
        return start
    elif input_list[end] == number:
        return end
    elif end - start <= 1:
        return -1
    mid = (start + end) // 2
    left = recur_fun(input_list, start, mid, number)
    if left > -1:
        return left
    right = recur_fun(input_list, mid + 1, end, number)
    if right > -1:
        return right
    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) <= 0:
        return -1
    start = 0
    end = len(input_list) - 1
    return recur_fun(input_list, start, end, number)
    pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 1])
test_function([[2], 1])
test_function([[2], 2])