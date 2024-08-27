/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-08-22 09:53:34
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 3133. 数组最后一个元素的最小值
 */

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    long long minEnd(int n, int x) {
        n--;
        uint64_t res = x;
        int j = 0;
        for (size_t t = ~x, lb; n >> j; t ^= lb) {
            lb = t & -t; //lowbit
            res |= (uint64_t)(n >> j & 1) * lb;
            j++;
        }
        return res;
    }
};