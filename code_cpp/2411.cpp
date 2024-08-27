/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-31 18:30:40
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2411. 按位或最大的最小子数组长度
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> ors;
        vector<int> res(n);
        for (int i = n-1; i >= 0; i--) {
            int x = nums[i];
            ors.emplace_back(0, i);
            int ptr = 0; //写指针
            for (auto &&v : ors) {
                v.first |= x;
                // 去重
                if (ors[ptr].first == v.first) {
                    // 重复，使用更小的下标，保证最小子数组
                    ors[ptr].second = v.second;
                }else {
                    // 不重复，写入
                    ptr++;
                    ors[ptr] = v;
                }
            }
            ors.resize(ptr+1);
            res[i] = ors[0].second-i+1;
        }
        return res;
    }
};