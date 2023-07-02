from typing import List


def mostBooked(n: int, meetings: List[List[int]]) -> int:
    cnt, t = [0] * n, [0] * n
    for [s, e] in sorted(meetings):
        t = list(map(lambda x : max(x, s), t))
        choice = t.index(min(t))
        t[choice], cnt[choice] = t[choice] + e - s, cnt[choice] + 1
        
    return cnt.index(max(cnt))
