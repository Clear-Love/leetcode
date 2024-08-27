/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-29 09:23:56
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 322. 零钱兑换
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<int>> memo(n, vector<int>(amount+1, -1));
        function<int(int, int)> dfs = [&](int i, int c) -> int {
            if (i < 0) {
                return c == 0? 0:INT_MAX /2;
            }
            int &res = memo[i][c];
            if (res != -1) {
                return res;
            }
            if (c < coins[i]) {
                return res = dfs(i-1, c);
            }
            return res = min(dfs(i-1, c), dfs(i, c-coins[i])+1);
        };
        int res = dfs(n-1, amount);
        return res < INT_MAX /2 ? res: -1;
    }
};