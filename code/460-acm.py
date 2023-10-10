from collections import OrderedDict, defaultdict
from typing import Optional


f=open("user.out",'w')
while True:
    try:
        input1=input()[13:-2].split('","')
        input2=input()[2:-2].split('],[')
        key_to_node = {}
        min_freq = 1
        freq_to_dict = defaultdict(OrderedDict)
        cap=int(input2[0])
        i=1
        def get_node(key: int) -> Optional[bool]:
            global min_freq
            # 没找到
            if key not in key_to_node:
                return False
            node = key_to_node[key]
            del freq_to_dict[node[0]][key]
            if not freq_to_dict[node[0]]:
                del freq_to_dict[node[0]]
                if node[0] == min_freq:
                    min_freq += 1
            node[0] += 1
            freq_to_dict[node[0]][key] = node
            return node
        ans="[null,"
        for fun in input1:
            match fun:
                case "put":
                    key, value = input2[i].split(',')
                    node = get_node(key)
                    if node:
                        node[1] = value  # 更新 value
                        i += 1
                        ans+="null,"
                        continue
                    if len(key_to_node) == cap:
                        k, node = freq_to_dict[min_freq].popitem(last=False)
                        del key_to_node[k]
                        if not freq_to_dict[node[0]]:
                            del freq_to_dict[node[0]]
                    node = [1, value]
                    key_to_node[key] = node
                    freq_to_dict[1][key] = node
                    min_freq = 1
                    ans+="null,"
                case "get":
                    key = input2[i]
                    node = get_node(key)
                    s = str(node[1]) if node else "-1"
                    ans += s + ','
            i += 1
        ans=ans[:-1]+"]"
        print(ans,file=f)
    except Exception as e:
        f.close()
        exit(0)