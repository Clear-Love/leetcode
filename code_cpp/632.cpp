#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>> &nums) {
        int l = 0, r = INT_MAX;
        int n = nums.size();
        vector<int> cur(n, 0);
        priority_queue<int, vector<int>,
                       function<bool(const int &, const int &)>>
            pq([&](const int &u, const int &v) {
                return nums[u][cur[u]] > nums[v][cur[v]];
            });
        int minVal = 0, maxVal = INT_MIN;
        for (int i = 0; i < n; ++i) {
            pq.emplace(i);
            maxVal = max(maxVal, nums[i][0]);
        }

        while (true) {
            int row = pq.top();
            pq.pop();
            minVal = nums[row][cur[row]];
            if (maxVal - minVal < r - l) {
                l = minVal;
                r = maxVal;
            }
            if (cur[row] == nums[row].size() - 1) {
                break;
            }
            ++cur[row]; // 从第row个中取出，就要加回去，保证每个组都有一个元素
            maxVal = max(maxVal, nums[row][cur[row]]); // 更新最大值
            pq.emplace(row);
        }

        return {l, r};
    }
};