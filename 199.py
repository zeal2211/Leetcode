# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        max_height = [0]

        def helper(node, curr_height):
            if not node:
                return
            
            if curr_height > max_height[0]:
                answer.append(node.val)
                max_height[0] = curr_height

            helper(node.right, curr_height+1)
            helper(node.left, curr_height+1)

        helper(root, 1)

        return answer
