# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def reverseNodes(node):
            if node is None:
                return
           
            reverseNodes(node.left)
            reverseNodes(node.right)
            
            node.left, node.right = node.right, node.left

        
        reverseNodes(root)
        return root


      
        