from functools import cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7
        def calc(s: str) -> int:
            @cache  # 记忆化搜索
            def f(i: int, pre: int, isLimit: bool, isNum: bool) -> int:
                if i == len(s):
                    return int(isNum)  # is_num 为 True 表示得到了一个合法数字
                res = 0
                if not isNum:  # 可以跳过当前数位
                    res = f(i + 1, pre, False, False)
                low = 0 if isNum else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                up = int(s[i]) if isLimit else 9  # 如果前面填的数字都和 s 的一样，那么这一位至多填 s[i]（否则就超过 s 啦）
                for d in range(low, up + 1):  # 枚举要填入的数字 d
                    if not isNum or abs(d - pre) == 1:  # 第一位数字随便填，其余必须相差 1
                        res += f(i + 1, d, isLimit and d == up, True)
                return res % MOD
            return f(0, 0, True, False)
        return (calc(high) - calc(str(int(low) - 1))) % MOD