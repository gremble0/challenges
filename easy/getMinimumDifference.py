# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.lowest = float('inf')
        self.previous = float('inf')

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.getMinimumDifference(root.left)

        self.lowest = min(self.lowest, abs(root.val - self.previous))
        self.previous = root.val

        if root.right:
            self.getMinimumDifference(root.right)

        return self.lowest
