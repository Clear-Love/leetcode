#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph) {
        vector<vector<int>> res;
        vector<int> path{0};
        auto dfs = [&](auto &&dfs, int cur) -> void {
            if (cur == graph.size() - 1) {
                res.push_back(path);
                return;
            }

            for (auto &v : graph[cur]) {
                path.push_back(v);
                dfs(dfs, v);
                path.pop_back();
            }
        };
        dfs(dfs, 0);
        return res;
    }
};