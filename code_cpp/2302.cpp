#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int64_t countSubarrays(vector<int>& nums, int64_t k) {
        int64_t res = 0, sum = 0;
        int left = 0, right = 0;
        while (right < nums.size()) {
            sum += nums[right];
            while (sum * (right - left + 1) >= k) {
                sum -= nums[left];
                left++;
            }
            res += right - left + 1;
            right++;
        }
        return res;
    }
};