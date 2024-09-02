#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getFinalState(vector<int> &nums, int k, int multiplier) {
        static const int MOD = 1e9 + 7;
        vector<pair<int, int>> v(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            v[i].first = nums[i];
            v[i].second = i;
        }
        auto cmp = [](const pair<int, int> &a, const pair<int, int> &b) {
            if (a.first == b.first) {
                return a.second > b.second;
            }
            return a.first > b.first;
        };

        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)>
            pq(cmp);
        for (auto &it : v) {
            pq.push(it);
        }
        for (int i = 0; i < k; i++) {
            auto [val, idx] = pq.top();
            pq.pop();
            v[idx].first = v[idx].first * multiplier % MOD;
            pq.push(v[idx]);
        }
        vector<int> res(nums.size());
        for (auto [val, idx] : v) {
            res[idx] = val;
        }
        return res;
    }
};