#include "utils.h"
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isSubtree(TreeNode *root, TreeNode *subRoot) {
        // 都为空
        if (!root && !subRoot) {
            return true;
        }
        // 其中一个为空
        if (!root || !subRoot) {
            return false;
        }
        if (root->val == subRoot->val &&
            isSametree(root->left, subRoot->left) &&
            isSametree(root->right, subRoot->right)) {
            return true;
        }
        return isSubtree(root->left, subRoot) ||
               isSubtree(root->right, subRoot);
    }

    bool isSametree(TreeNode *r1, TreeNode *r2) {
        if (!r1 && !r2) {
            return true;
        }
        if (!r1 || !r2) {
            return false;
        }
        return r1->val == r2->val && isSametree(r1->left, r2->left) &&
               isSametree(r1->right, r2->right);
    }
};