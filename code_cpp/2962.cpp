#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int64_t countSubarrays(vector<int>& nums, int k) {
        int mx = ranges::max(nums);
        int64_t res = 0;
        int cnt_mx = 0, left = 0;
        for (int x : nums) {
            cnt_mx += (x == mx);
            while (cnt_mx == k) {
                cnt_mx -= (nums[left] == mx);
                left++;
            }
            res += left;
        }
        return res;
    }
};