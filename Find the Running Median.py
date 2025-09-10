import heapq

def runningMedian(stream):
    lower_half = []  # max-heap via negating values
    upper_half = []  # min-heap
    medians = []
    
    for num in stream:
        # Decide heap based on current median
        if not lower_half or num <= -lower_half[0]:
            heapq.heappush(lower_half, -num)
        else:
            heapq.heappush(upper_half, num)
        
        # Rebalance heaps to ensure size difference ≤ 1
        if len(lower_half) > len(upper_half) + 1:
            moved = -heapq.heappop(lower_half)
            heapq.heappush(upper_half, moved)
        elif len(upper_half) > len(lower_half):
            moved = heapq.heappop(upper_half)
            heapq.heappush(lower_half, -moved)
        
        # Compute median
        if len(lower_half) == len(upper_half):
            median = (-lower_half[0] + upper_half[0]) / 2.0
        else:
            median = -lower_half[0] * 1.0
        
        medians.append(f"{median:.
