def non_divisible_subset_size(S, k):
    count = [0] * k
    for num in S:
        count[num % k] += 1

    res = min(count[0], 1)  # only one from remainder 0
    for i in range(1, k // 2 + 1):
        if i == k - i:  # when k is even and i = k/2
            res += min(count[i], 1)
        else:
            res += max(count[i], count[k - i])
    return res
