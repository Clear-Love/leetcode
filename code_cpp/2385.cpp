#include<bits/stdc++.h>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
    int amountOfTime(TreeNode* root, int start) {
        int res = 0;
        function<pair<int, bool>(TreeNode*)> dfs = [&](TreeNode* node) -> pair<int, bool> {
            if (node == nullptr) {
                return {0, false};
            }
            auto [l_len, l_found] = dfs(node->left);
            auto [r_len, r_found] = dfs(node->right);
            if (node->val == start) {
                // 计算子树 start 的最大深度
                res = max(l_len, r_len);
                return {1, true};
            }
            if (l_found || r_found) {
                res = max(res, l_len + r_len);
                return {(l_found ? l_len : r_len) + 1, true};
            }
            return {max(l_len, r_len) + 1, false};
        };
        dfs(root);
        return res;
    }
};