# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        
        stack = collections.deque()
        stack.append((root, 1))
        
        while stack :
            node , depth = stack.popleft()
            if (node.right is None) and (node.left is None):
                return depth 
            else:
                if node.left:
                    stack.append((node.left, depth +1))
                if node.right:
                    stack.append((node.right, depth + 1))