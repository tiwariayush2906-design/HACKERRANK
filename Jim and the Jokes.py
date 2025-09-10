from collections import Counter

def to_decimal(day: int, base: int) -> int:
    """Convert 'day' (digits in base-10) to decimal using the given base.
    Return -1 if invalid (any digit >= base)."""
    result = 0
    place = 1
    
    while day > 0:
        digit = day % 10
        if digit >= base or base <= 1:
            return -1
        result += digit * place
        place *= base
        day //= 10
        
    return result

def jim_and_the_jokes(events):
    # events is a list of (month, day) pairs
    values = []
    for month, day in events:
        dec = to_decimal(day, month)
        if dec != -1:
            values.append(dec)
    
    freq = Counter(values)
    return sum(count * (count - 1) // 2 for count in freq.values())
