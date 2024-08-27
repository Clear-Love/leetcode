/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-05 13:28:50
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 1026. 节点与其祖先之间的最大差值
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
 
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int res = 0;
        function<pair<int, int>(TreeNode*)> dfs = [&](TreeNode* node) -> pair<int, int> {
            if (node == nullptr) {
                return pair<int, int>(INT_MAX, 0);
            }
            pair<int, int> ans(node->val, node->val);
            auto left = dfs(node->left);
            auto right = dfs(node->right);
            ans.first = min(ans.first, min(left.first, right.first));
            ans.second = max(ans.second, max(left.second, right.second));
            res = max(res, max(abs(node->val - ans.first), abs(node->val - ans.second)));
            return ans;
        };
        dfs(root);
        return res;
    }
};