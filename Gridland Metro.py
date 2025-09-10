def gridlandMetro(n, m, k, tracks):
    from collections import defaultdict
    
    rows = defaultdict(list)
    for r, c1, c2 in tracks:
        rows[r].append((c1, c2))
    
    occupied = 0
    for r in rows:
        intervals = sorted(rows[r])
        merged = []
        start, end = intervals[0]
        for c1, c2 in intervals[1:]:
            if c1 <= end:
                end = max(end, c2)
            else:
                merged.append((start, end))
                start, end = c1, c2
        merged.append((start, end))
        
        for s, e in merged:
            occupied += (e - s + 1)
    
    return n * m - occupied
