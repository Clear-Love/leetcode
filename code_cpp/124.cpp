#include "utils.h"
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxPathSum(TreeNode *root) {
        int res = INT_MIN;
        auto dfs = [&](auto &&dfs, TreeNode *root) -> int {
            if (!root) {
                return 0;
            }
            auto l = dfs(dfs, root->left);
            auto r = dfs(dfs, root->right);
            res = max({res, root->val + l + r});
            return max({0, root->val + l, root->val + r});
        };
        dfs(dfs, root);
        return res;
    }
};