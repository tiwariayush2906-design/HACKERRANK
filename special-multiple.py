from collections import deque
import sys

def find_special(n):
    if n == 1:
        return "1"
    parent = [-1] * n         # parent remainder for reconstructing path
    digit = [''] * n          # digit used to reach this remainder ('0' or '1')

    start = 1 % n
    q = deque()
    q.append(start)
    parent[start] = -2        # mark root
    digit[start] = '1'
    if start == 0:
        return "1"

    while q:
        cur = q.popleft()
        # append '0'
        r0 = (cur * 10) % n
        if parent[r0] == -1:
            parent[r0] = cur
            digit[r0] = '0'
            if r0 == 0:
                return reconstruct(r0, parent, digit)
            q.append(r0)

        # append '1'
        r1 = (cur * 10 + 1) % n
        if parent[r1] == -1:
            parent[r1] = cur
            digit[r1] = '1'
            if r1 == 0:
                return reconstruct(r1, parent, digit)
            q.append(r1)

    # should never get here for n >= 1
    return None

def reconstruct(rem, parent, digit):
    res = []
    x = rem
    while x != -2:
        res.append(digit[x])
        x = parent[x]
    res.reverse()
    return ''.join(res)

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out_lines = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        out_lines.append(find_special(n))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
