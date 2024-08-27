/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-08-19 15:04:54
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 3128. 直角三角形
 */
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    long long numberOfRightTriangles(vector<vector<int>> &grid) {
        auto cols = vector<int>(grid[0].size(), 0);
        auto rows = vector<int>(grid.size(), 0);
        auto ones = vector<pair<int, int>>();
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    cols[j]++;
                    rows[i]++;
                    ones.emplace_back(i, j);
                }
            }
        }
        long long res = 0;
        for (auto &[i, j] : ones) {
            res += (cols[j] - 1) * (rows[i] - 1);
        }
        return res;
    }
};

auto init = [](){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    return 0;
}();