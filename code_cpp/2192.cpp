/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-04 16:30:02
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2192. 有向无环图中一个节点的所有祖先
 */
#include<bits/stdc++.h>
#include<ranges>
using namespace std;

class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>> &edges) {
        vector<vector<int>> g(n);
        for (auto &edge : edges) {
            g[edge[1]].push_back(edge[0]); // 反向建图
        }
        vector<vector<int>> ans(n);
        vector<int> vis(n);
        function<void(int)> dfs = [&](int x) {
            vis[x] = true; // 避免重复访问
            for (int y : g[x]) {
                if (!vis[y]) {
                    dfs(y); // 只递归没有访问过的点
                }
            }
        };
        for (int i = 0; i < n; i++) {
            ranges::fill(vis, false);
            dfs(i); // 从 i 开始 DFS
            vis[i] = false; // ans[i] 不含 i
            for (int j = 0; j < n; j++) {
                if (vis[j]) {
                    ans[i].push_back(j);
                }
            }
        }
        return ans;
    }
};