from typing import Optional

from utils.node import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 找最大值
        def findMaximun(root: TreeNode) -> TreeNode:
            while root.right:
                root = root.right
            return root.val
        # 找最小值
        def findMinimun(root: TreeNode) -> TreeNode:
            while root.left:
                root = root.left
            return root.val
        # 1.找到删除的节点位置
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2.叶子节点直接删除
            if not root.left and not root.right:
                return None
            # 3.有左子树，把前驱节点替换，删掉前驱
            elif root.left:
                root.val = findMaximun(root.left)
                root.left = self.deleteNode(root.left, root.val)
            # 4.有右子树，把后继节点替换，删掉后继
            else:
                root.val = findMinimun(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root