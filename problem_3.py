def merge(input_list, start, end, mid):
    n1 = mid - start + 1
    n2 = end - mid
    l1 = n1 * [0]
    for i in range(n1):
        l1[i] = input_list[start + i]
    l2 = n2 * [0]
    for i in range(n2):
        l2[i] = input_list[mid + 1 + i]
    j = 0
    k = 0
    for i in range(start, end + 1):
        if j < n1 and k < n2:
            if l1[j] <= l2[k]:
                input_list[i] = l1[j]
                j += 1
            else:
                input_list[i] = l2[k]
                k += 1
        elif j >= n1:
            input_list[i] = l2[k]
            k += 1
        else:
            input_list[i] = l1[j]
            j += 1
#     print("input_list: ", input_list, " start: ", start, " end: ", end)     
    
    
def recur_fun(input_list, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    recur_fun(input_list, start, mid)
    recur_fun(input_list, mid + 1, end)
    merge(input_list, start, end, mid)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [0, 0]
    if len(input_list) == 1:
        return [input_list[0], 0]
    start = 0
    end = len(input_list) - 1
    recur_fun(input_list, start, end)
#     print("input_list final: ", input_list)
    left = 0
    right = 0
    for i in range(end, -1, -2):
        left *= 10
        left += input_list[i]
        if i > 0:
            right *= 10
            right += input_list[i - 1]
#     print("left: ", left, " right: ", right)
    return [left, right]
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_case = [[1,5,4,3,8,6,9,7,2], [97531, 8642]]
test_function(test_case)
test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[2], [2, 0]]
test_function(test_case)
test_case = [[], [0, 0]]
test_function(test_case)