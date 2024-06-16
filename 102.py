# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        arr = []
        def level(root, depth):
            nonlocal arr
            if not root:
                return
            if root:
                print(root.val, depth)
                if len(arr) == depth:
                    arr.append([root.val])
                else:
                    arr[depth].append(root.val)
            
            level(root.left, depth+ 1)
            level(root.right, depth+1)

        
        level(root, 0)
        return arr
