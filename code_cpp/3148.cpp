#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxScore(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        auto preMin = vector<vector<int>>(n, vector<int>(m, 0));
        preMin[0][0] = grid[0][0];
        int res = INT_MIN;
        for (int i = 1; i < n; i++) {
            preMin[i][0] = min(preMin[i - 1][0], grid[i][0]);
            res = max(res, grid[i][0] - preMin[i - 1][0]);
        }
        for (int j = 1; j < m; j++) {
            preMin[0][j] = min(preMin[0][j - 1], grid[0][j]);
            res = max(res, grid[0][j] - preMin[0][j - 1]);
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                preMin[i][j] =
                    min({grid[i][j], preMin[i - 1][j], preMin[i][j - 1]});
                res = max(res, grid[i][j] - min(preMin[i - 1][j], preMin[i][j - 1]));
            }
        }
        return res;
    }
};