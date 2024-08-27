#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        bool prev = ~nums[0]&1;
        for (auto &num: nums) {
            bool cur = num&1;
            if (!(prev ^ cur)) {
                return false;
            }
            prev = cur;
        }
        return true;
    }
};