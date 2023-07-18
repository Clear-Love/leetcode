class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        n1, n2 = len(num1)-1, len(num2)-1
        res = ""
        while n1 > 0 and n2 > 0:
            v1 = 0 if n1 < 0 else int(num1[n1])
            v2 = 0 if n2 < 0 else int(num2[n2])
            carry, i = divmod(v1+v2+carry, 10)
            res = str(i) + res
            n1 -= 1
            n2 -= 1
        return '1' + res if carry else res
