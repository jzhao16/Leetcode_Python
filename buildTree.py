# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def buildTree(self, inorder, postorder):
		if len(inorder) == 0 or len(postorder) == 0:
			return None

		root = TreeNode(postorder.pop())
		rootIndex = inorder.index(root.val)

		root.right = self.buildTree(inorder[rootIndex+1:],postorder)
		root.left = self.buildTree(inorder[:rootIndex],postorder)

		return root


