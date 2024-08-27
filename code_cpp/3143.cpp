#include <bits/stdc++.h>

using namespace std;

// 可以二分优化
class Solution {
public:
    int maxPointsInsideSquare(vector<vector<int>>& points, string s) {
        auto g = map<int, vector<int>>();
        for (int i = 0; i < points.size(); i++) {
            auto key = max(abs(points[i][0]), abs(points[i][1]));
            g[key].push_back(s[i]);
        }
        unordered_set<int> m;
        int res = 0;
        for (auto& [_, q] : g) {
            int cnt = 0;
            for (auto& c : q) {
                if (m.contains(c)) {
                    return res;
                }
                m.insert(c);
                cnt++;
            }
            // 标签全部不冲突才增加正方形边长
            res += cnt;
        }
        return res;
    }
};