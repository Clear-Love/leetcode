/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-03 22:50:35
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 1379. 找出克隆二叉树中的相同节点
 */
#include<bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        if (original == nullptr || original == target) {
            return cloned;
        }
        auto node = getTargetCopy(original->left, cloned->left, target);
        if (node) {
            return node;
        }
        return getTargetCopy(original->right, cloned->right, target);
    }
};