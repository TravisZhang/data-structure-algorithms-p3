### Design

We are dynamically dividing the number to get the correct answer. Each time we divide it into half and increase start or decrease end to half whether the square of half is smaller or bigger than the number.

### Time Complexity

The time complexity is O(log(n)), because we are dividing n by 2 each time for m times, and the equation to solve for m is  
&emsp;(n/2^m)^2 = n  
With some deduction we get  
&emsp;m = log(n) - 1  
So the time complexity is O(m) = O(log(n))

### Space Complexity

Since we are using while loop, there are only two varaibles to store, start and end, the space Complexity is O(1).