from itertools import permutations

m = {0:'A', 1:'B', 2: 'C', 3: 'D'}
k = {'A': 1 << 3, 'B': 1 << 2, 'C': 1 << 1, 'D': 1}
res = set()
for arr in permutations(['1', '1', '0', '0']):
    key = int(''.join(arr), 2)
    a, b, c, d = k['A']&key, k['B']&key, k['C']&key, k['D']&key
    if a and ((not c) and (not d)):
        continue
    if b and c:
        continue
    if c and d:
        continue
    res.add(' '.join(m[i] for i in range(4) if arr[i] == '1'))

for r in list(res):
    print(r)