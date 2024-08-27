#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int> &nums, int k) {
        auto sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) {
            return false;
        }
        auto target = sum / k;
        sort(nums.begin(), nums.end());
        if (nums[nums.size() - 1] > target) {
            return false;
        }
        int n = nums.size();
        vector<bool> dp(1 << n, true);
        auto end = (1 << n) - 1;
        auto dfs = [&](auto &&dfs, int s, int cur) -> bool {
            if (s == end) {
                return true;
            }
            if (!dp[s]) {
                return dp[s];
            }
            dp[s] = false;
            for (int i = 0; i < n; i++) {
                if (nums[i] + cur > target) {
                    break;
                }
                if (s & (1 << i)) {
                    continue;
                }
                if (dfs(dfs, s ^ (1 << i), (cur + nums[i]) % target)) {
                    return true;
                }
            }
            return false;
        };
        return dfs(dfs, 0, 0);
    }
};