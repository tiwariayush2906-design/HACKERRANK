def toys(w):
    w.sort()
    containers = 0
    i = 0
    n = len(w)
    
    while i < n:
        threshold = w[i] + 4
        containers += 1
        i += 1
        # Skip all toys within the threshold
        while i < n and w[i] <= threshold:
            i += 1
    
    return containers
