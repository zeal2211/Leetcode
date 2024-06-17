# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def maxSum(node):
            if not node:
                return 0

            # Compute the max path sum "through" the left child
            left_max = max(maxSum(node.left), 0)
            # Compute the max path sum "through" the right child
            right_max = max(maxSum(node.right), 0)

            # Update the overall maximum path sum if needed
            self.ans = max(self.ans, node.val + left_max + right_max)

            # Return the maximum sum of the path that can be extended to the parent
            return node.val + max(left_max, right_max)

        maxSum(root)
        return self.ans
