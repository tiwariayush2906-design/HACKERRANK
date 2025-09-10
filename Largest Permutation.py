def largestPermutation(k, arr):
    n = len(arr)
    
    # map value -> index for O(1) swaps
    pos = {val: idx for idx, val in enumerate(arr)}
    
    for i in range(n):
        if k == 0:
            break
        
        # the value that should ideally be here
