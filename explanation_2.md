### Design

Similar to problem 1, we are dividing the list to search for the number. Each time we divide the list in half, and see if the new list's head or tail is equal to the number.

### Time Complexity

The time complexity is O(log(n)), because we are dividing the list in half each time for m times, and in worst case scenario the length of list n has to be divided to get 1, so the equation to solve for m is  
&emsp;n/2^m = 1  
With some deduction we get  
&emsp;m = log(n)
So the time complexity is O(m) = O(log(n))

### Space Complexity

Since we are using recursion for the same list with length n, the space complexity is O(n).