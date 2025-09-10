def highestValuePalindrome(s, n, k):
    s = list(s)
    changes = [0] * n
    l, r = 0, n - 1
    
    # First pass: make it palindrome
    while l < r:
        if s[l] != s[r]:
            bigger = max(s[l], s[r])
            s[l] = s[r] = bigger
            changes[l] = changes[r] = 1
            k -= 1
        l += 1
        r -= 1

    if k < 0:
        return "-1"

    # Second pass: maximize palindrome
    l, r = 0, n - 1
    while l <= r and k > 0:
        if l == r:
            if k > 0:
                s[l] = '9'
        else:
            if s[l] != '9':
                if changes[l] == 1 and k >= 1:
                    s[l] = s[r] = '9'
                    k -= 1
                elif changes[l] == 0 and k >= 2:
                    s[l] = s[r] = '9'
                    k -= 2
        l += 1
        r -= 1

    return "".join(s)
