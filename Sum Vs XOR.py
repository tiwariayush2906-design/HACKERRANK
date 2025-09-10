def sumXor(n: int) -> int:
    if n == 0:
        return 1  # special case: only x=0 works
    
    # Count zero bits in n
    zero_bits = 0
    while n > 0:
        if n & 1 == 0:   # if last bit is zero
            zero_bits += 1
        n >>= 1
    return 1 << zero_bits  # 2^zero_bits
