#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto res = lower_bound(nums.begin(), nums.end(), target);
        return res - nums.begin();
    }
};