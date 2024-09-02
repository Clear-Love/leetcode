#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        for (int i = 0; i < intervals.size(); i++) {
            intervals[i].push_back(i);
        }
        sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
            return a[0] < b[0];
        });
        auto res = vector<int>(intervals.size(), -1);
        for (int i = 0; i < intervals.size(); i++) {
            // 查找第一个大于等于intervals[i][1]的元素
            auto it = lower_bound(intervals.begin(), intervals.end(), intervals[i][1], [](auto& a, auto& b) {
                return b > a[0];
            });
            if (it != intervals.end()) {
                res[intervals[i][2]] = (*it)[2];
            } else {
                res[intervals[i][2]] = -1;
            }
        }
        return res;
    }
};