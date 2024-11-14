# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: # Base Case at the end of the tree
            return False
        csum = targetSum - root.val

        if root.left == None and root.right == None:
            return csum == 0
        if self.hasPathSum(root.left,csum):
            return True 
        if self.hasPathSum(root.right,csum):
            return True
        
        csum += root.val # add back value
        return False
    def construct_test_case(self) -> TreeNode:
        # Leetcode test case
        tr = TreeNode()
        tr.val = 5

        # Left subtree
        tr.left = TreeNode()
        tr.left.val = 4
        tr.left.left = TreeNode()
        tr.left.left.val = 11
        tr.left.left.left = TreeNode()
        tr.left.left.left.val = 7
        tr.left.left.right = TreeNode()
        tr.left.left.right.val = 2

        # Right subtree
        tr.right = TreeNode()
        tr.right.val = 8
        tr.right.left = TreeNode()
        tr.right.left.val = 13
        tr.right.right = TreeNode()
        tr.right.right.val = 4
        tr.right.right.right = TreeNode()
        tr.right.right.right.val = 1



def main():
    sol = Solution()
    assert(sol.hasPathSum(sol.construct_test_case()) == True)

if '__name__'=='__main__':
    main()
        