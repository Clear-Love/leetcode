/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-01 15:12:03
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 1521. 找到最接近目标值的函数值
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        vector<int> ands;
        int res = INT_MAX;
        for (auto&& num: arr) {
            int ptr = 0;
            ands.push_back(0xffff);
            for (auto&& v: ands) {
                v &= num;
                res = min(res, abs(v-target));
                if (ands[ptr] != v) {
                    ptr++;
                    ands[ptr] = v;
                }
            }
            ands.resize(ptr+1);
        }
        return res;
    }
};