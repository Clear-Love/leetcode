/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-28 23:31:32
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2580. 统计将重叠区间合并成组的方案数
 */
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int countWays(vector<vector<int>> &ranges) {
        const int MOD = 1000000007;
        sort(ranges.begin(), ranges.end());
        int left = 0, right = 0;
        int n = ranges.size();
        int c = 0;
        while (right < n)
        {
            int r = ranges[left][1];
            while (right < n && r >= ranges[right][0])
            {
                r = std::max(r, ranges[right][1]);
                right++;
            }
            left = right;
            c++;
        }
        int res = 1;
        for (int i = 0; i < c; i++) {
            res = (res * 2) % MOD;
        }
        return res;
    }
};