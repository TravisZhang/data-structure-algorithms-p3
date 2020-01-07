### Design

Because in order to get the largest sum, we need to put larger digits at higher bits. So we need to first sort the list, then we can set the digits from large to small, to to numbers at the same time.

### Time Complexity

The time complexity is O(n*log(n)), because we are first dividing the list in half each time for m times, and in worst case scenario the length of list n has to be divided to get 1, so the equation to solve for m is  
&emsp;n/2^m = 1  
With some deduction we get  
&emsp;m = log(n)
&emsp;So we need log(n) times to make the sub-list length to 1, and we can actually consider it as a recursive tree with depth log(n). Then for each ith of the tree from top down, we need to merge 2^i sub-lists with length (n / 2^i) into one list,
so the time cost is always n. So to add it together, the total time complexity is O(n*log(n)). And finally we go through the sorted list to get the two numbers, so the final time complexity is O(n + n*log(n)) = O(n*log(n)).

### Space Complexity

Since we are using recursion for the same list with length n, the space complexity is O(n).