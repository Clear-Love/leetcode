'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 15:34:57
LastEditors: lmio 2091319361@qq.com
Description: 内存空间
'''

tm = {'int': 4, 'long': 8, 'String': 1, 'long[]': 8, 'int[]': 4}

mem = {"GB": 1024 * 1024 * 1024, "MB": 1024 * 1024, "KB": 1024, "B": 1}

def size_to_string(size: int):
    res = []
    for unit in ["GB", "MB", "KB", "B"]:
        if size >= mem[unit]:
            res.append(str(size // mem[unit]) + unit)
            size %= mem[unit]
    return ''.join(res)

T = int(input())

size = 0

for _ in range(T):
    i = 0
    src = input()
    s = src.split()
    sz = 0
    isNums = False
    t = ""
    # 获取类型
    while i < len(s):
        if s[i] in tm:
            if s[i].find('[]') != -1:
                isNums = True
            sz = tm[s[i]]
            t = s[i]
            break
        i += 1
    i += 1
    if not isNums and s[i] == '[]':
        isNums = True
        i += 1

    if isNums:
        while i < len(s):
            for w in s[i].split(','):
                l = w.find('[')
                if l == -1:
                    continue
                r = w.find(']')
                size += sz * int(w[l+1:r])
            i += 1
    else:
        while i < len(s):
            for w in s[i].split(','):
                idx = w.find('=')
                if idx == -1:
                    continue
                if t != "String":
                    size += sz
                else:
                    if w[-1] == ';':
                        w = w[:-1]
                    size += sz * (len(w) - idx-3)
            i += 1

print(size_to_string(size))