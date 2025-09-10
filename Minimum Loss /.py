def minimumLoss(prices):
    indexed = [(p, i) for i, p in enumerate(prices)]
    indexed.sort(reverse=True)  # sort by price descending
    
    min_loss = float('inf')
    for i in range(len(indexed) - 1):
        price1, year1 = indexed[i]
        price2, year2 = indexed[i + 1]
        if year1 < year2:  # must buy after sell
            min_loss = min(min_loss, price1 - price2)
    
    return min_loss
