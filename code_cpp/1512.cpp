#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        auto m = unordered_map<int, int>();
        for (auto& num: nums) {
            ++m[num];
        }
        int res = 0;
        for (auto& [k, v]: m) {
            res += v * (v - 1) / 2;
        }
        return res;
    }
};