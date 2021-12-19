# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preOrder(self,root,s):
        # if root is none then return
        if(root == None):
            return s
        
        # If its not none then append its value to string
        s+=str(root.val)

        # Append opening paranthesis
        s+="("

        # Do traversal
        s = self.preOrder(root.left,s)
        s+=")"
        sright = self.preOrder(root.right,"")

        if(len(sright)>0):
            s+="("+sright+")"
        else:
            if(s[-1] == ")" and s[-2] == "("):
                s = s[:-2]
        
        return s
        

    def clean(self,s):
        sHat = ""
        i = 0
        while(i<len(s)-1):
            if(s[i] == "(" and s[i+1] == ")"):
                i+=2
            else:
                sHat += s[i]
                i+=1
        return sHat+s[i:]

    def tree2str(self, root) :
        s = self.preOrder(root,"")
        #s = self.clean(s)
        return s
        