/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-29 08:46:17
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2908. 元素和最小的山形三元组 I
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumSum(vector<int>& nums) {
        int lmin = INT_MAX;
        int rmin = INT_MAX;
        int n = nums.size();
        int l[n];
        int r[n];
        for (int i = 0; i < n; i++) {
            l[i] = lmin;
            r[n-1-i] = rmin;
            lmin = min(lmin, nums[i]);
            rmin = min(rmin, nums[n-i-1]);
        }
        int res = INT_MAX;
        for (int i = 1; i < n-1; i++) {
            if (nums[i] > l[i] && nums[i] > r[i])
                res = min(res, nums[i]+l[i]+r[i]);
        }
        return res == INT_MAX? -1:res;
    }
};