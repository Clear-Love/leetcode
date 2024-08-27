/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-01 14:37:46
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 3097. 或值至少为 K 的最短子数组 II
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();
        int res = INT_MAX;
        vector<pair<int, int>> ors;
        for (int i = 0; i < n; i++) {
            ors.emplace_back(0, i);
            int x = nums[i];
            int ptr = 0;
            for (auto&& v: ors) {
                v.first |= x;
                if (ors[ptr].first == v.first) {
                    ors[ptr].second = v.second;
                }else {
                    ptr++;
                    ors[ptr] = v;
                }
                if (v.first >= k) {
                    res = min(res, i-v.second+1);
                }
            }
            ors.resize(ptr+1);
        }
        return res == INT_MAX? -1: res;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> arr = {0, 1, 2, 4,6, 7};
    s.minimumSubarrayLength(arr, 3);
    return 0;
}
