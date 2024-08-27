/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-02 14:32:42
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 894. 所有可能的真二叉树
 */
#include<bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<TreeNode*> dp[11];
auto init = [] {
    dp[1] = {new TreeNode()};
    for (int i = 2; i < 11; i++) {
        for (int j = 1; j < i; j++) {
            for (auto left: dp[j]) {
                for (auto right: dp[i-j]) {
                    dp[i].push_back(new TreeNode(0, left, right));
                }
            }
        }
    }
    return 0;
}();

class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        return dp[n&1 == 0? 0: n/2+1];
    }
};