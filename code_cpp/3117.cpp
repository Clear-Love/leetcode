#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minimumValueSum(vector<int> &nums, vector<int> &andValues) {
        int n = nums.size(), m = andValues.size();
        vector<unordered_map<int, int>> memo;
        memo.resize(m * n);
        static const int INF = (1 << 20) - 1;
        auto dfs = [&](auto &&dfs, int i, int j, int cur) -> int {
            int n = nums.size(), m = andValues.size(), key = i * m + j;
            if (i == n && j == m) {
                return 0;
            }
            if (i == n || j == m) {
                return INF;
            }
            if (memo[key].count(cur)) {
                return memo[key][cur];
            }
            cur &= nums[i];
            // 越进行& 操作 addValues[j] 越小，剪枝
            if ((cur & andValues[j]) < andValues[j]) {
                return INF;
            }

            // 继续添加值到当前组，如果当前值已经等于andValues[j]，则可以跳过
            int res = dfs(dfs, i + 1, j, cur);
            if (cur == andValues[j]) {
                res = min(res, dfs(dfs, i + 1, j + 1, INF) + nums[i]);
            }
            memo[key][cur] = res;
            return res;
        };
        int res = dfs(dfs, 0, 0, INF);
        return res < INF ? res : -1;
    }
};