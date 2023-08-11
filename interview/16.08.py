'''
Author: lmio 2091319361@qq.com
Date: 2023-08-11 17:00:59
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.08. 整数的英语表示
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = 'Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,Eleven,Twelve,Thirteen,Fourteen,Fifteen,Sixteen,Seventeen,Eighteen,Nineteen'.split(',')
        tens = 'Twenty,Thirty,Forty,Fifty,Sixty,Seventy,Eighty,Ninety'.split(',')
        hundreds = 'Thousand,Million,Billion'.split(',')
        if num == 0:
            return ones[0]
        num = str(num)
        def to_str(s: str) ->str:
            s = s.lstrip('0')
            if not s:
                return ''
            n = len(s)
            if n == 1:
                return ones[int(s[0])]
            res = ''
            if n == 3:
                if int(s[-2:]) == 0:
                    return ones[int(s[0])] + ' Hundred'
                res += ones[int(s[0])] + ' Hundred '
            if int(s[-2:]) <= 19:
                return res + ones[int(s[-2:])]
            else:
                if s[-1] == '0':
                    return res + tens[int(s[-2])-2]
                return res + tens[int(s[-2])-2] + ' ' + ones[int(s[-1])]
        l = max(len(num)-3, 0)
        res = to_str(num[l:])
        r = l
        cnt = 0
        while r > 0 and cnt < 2:
            l = max(r-3, 0)
            s = to_str(num[l:r])
            if s:
                res = s + ' ' + hundreds[cnt] + ' ' + res
            r = l
            cnt += 1
        if r > 0:
            return (self.numberToWords(int(num[:r])) + ' ' + hundreds[2] + ' ' + res).strip()
        return res.strip()