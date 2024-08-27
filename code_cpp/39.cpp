#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        vector<vector<int>> res;
        auto dfs = [&](auto dfs, int idx, int sum) -> void {
            if (sum == target) {
                res.push_back(path);
                return;
            }
            for (int i = idx; i < candidates.size(); i++) {
                if (sum + candidates[i] > target) break;
                path.push_back(candidates[i]);
                dfs(dfs, i, sum + candidates[i]);
                path.pop_back();
            }
        };
        dfs(dfs, 0, 0);
        return res;
    }
};