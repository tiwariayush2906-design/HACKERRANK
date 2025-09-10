import math

def encryption(s: str) -> str:
    # Remove spaces
    s = s.replace(" ", "")
    L = len(s)
    
    # Determine grid dimensions
    root = math.sqrt(L)
    rows = int(math.floor(root))
    cols = int(math.ceil(root))
    
    if rows * cols < L:
        rows = cols
    
    # Build encrypted message by reading column-wise
    encrypted_words = []
    for col in range(cols):
        word = []
        for row in range(rows):
            idx = row * cols + col
            if idx < L:
                word.append(s[idx])
        encrypted_words.append("".join(word))
    
    return " ".join(encrypted_words)
