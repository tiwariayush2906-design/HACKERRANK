from collections import Counter

def sherlockAndAnagrams(s: str) -> int:
    n = len(s)
    substr_count = Counter()
    
    # Step 1 & 2: Generate and normalize all substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = ''.join(sorted(s[i:j]))
            substr_count[substr] += 1
    
    # Step 3 & 4: Count the combinations of anagram pairs
    total_pairs = 0
    for freq in substr_count.values():
        if freq > 1:
            total_pairs += freq * (freq - 1) // 2
    
    return total_pairs
