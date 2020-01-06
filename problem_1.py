import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 1 or number == 0 or number == None:
        return number
    start = 1
    end = number
    while start <= end:
        mid = (start + end) / 2
        if mid * mid == number:
#             print("result: ", math.floor(mid))
            return math.floor(mid)
        if mid * mid < number:
            start = mid
        else:
            end = mid
#     print("result: ", math.floor(end))
    return math.floor(end)
        
# Test Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(None)) else "Fail")
