/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-05 16:19:53
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2644. 找出可整除性得分最大的整数
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        int max_cnt = 0, res = INT_MAX;
        for (auto& d: divisors) {
            int c = 0;
            for (auto&num: nums) {
                if (num%d == 0) {
                    c += 1;
                }
            }
            if (c > max_cnt || c == max_cnt && d < res) {
                max_cnt = c;
                res = d;
            }
        }
        return res;
    }
};