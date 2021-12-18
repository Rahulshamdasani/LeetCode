# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.visited = set()
        self.count = 0

    def helper(self,root,targetSum, currSum):
        
        # Base case
        if(not root):
            return 

        #print("Invoked for ",root.val,"With currSum=",currSum)

        if(currSum+root.val == targetSum):
            #print("Incremented for",root.val,"When prev sum was",currSum)
            self.count += 1
        


        # goto left child with the curr sum
        self.helper(root.left,targetSum,currSum+root.val)

        # goto right child with the curr sum
        self.helper(root.right,targetSum,currSum+root.val)

            
        


    def pathSum(self, root, targetSum) :
        if(not root):
            return 0
        if(root.left):
            self.pathSum(root.left,targetSum)
        self.helper(root,targetSum,0)
        if(root.right):
            self.pathSum(root.right,targetSum)
        return self.count
        
        


        

