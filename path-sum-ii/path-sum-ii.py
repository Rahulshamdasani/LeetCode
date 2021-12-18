# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        
        self.ans = []
        
    
    def helperSum(self,root,l,s,target):
        if(root == None):
            return
        
        s += root.val
        l.append(root.val)
        
        if(s == target and root.left == None and root.right == None):
            self.ans.append(l)
            return
            
        
        self.helperSum(root.left,copy.copy(l),s,target)
        self.helperSum(root.right,copy.copy(l),s,target)
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.helperSum(root,[],0,targetSum)
        
        return self.ans