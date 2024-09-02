#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int64_t sumDigitDifferences(vector<int>& nums) {
        uint64_t n = nums.size(), m = to_string(nums[0]).size();
        auto cnts = vector<array<int, 10>>(m, array<int, 10>{0});
        int64_t res = m*(n*(n-1)/2);
        for (auto& num : nums) {
            int i = 0;
            while (num) {
                int d = num % 10;
                // 减去相同的数对
                res -= cnts[i][d];
                cnts[i][d]++;
                num /= 10;
                i++;
            }
        }
        return res;
    }
};