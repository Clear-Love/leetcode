#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        // 前缀和数组
        vector<int> preSum(nums.size(), 0);
        for (int i = 1; i < nums.size(); i++) {
            preSum[i] = preSum[i-1] + (nums[i-1]%2 == nums[i]%2);
        }
        vector<bool> res(queries.size(), false);
        for (int i = 0; i < queries.size(); i++) {
            auto &q = queries[i];
            res[i] = (preSum[q[1]] - preSum[q[0]] == 0);
        }
        return res;
    }
};