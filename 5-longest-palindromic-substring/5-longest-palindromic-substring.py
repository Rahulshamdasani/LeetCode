class Solution:
    
    
    def __init__(self):
        self.maxlen = 1
        self.start = 0
        self.end = 1
    
    
    def checkFromMidPalin(self,s,left,right):
        # print("called for",s[left],s[right],left,right)
        while(left>=0 and right<len(s) and s[left] == s[right]):
            left -= 1
            right +=1
        left +=1
        # print(left,right,s[left:right])
        # print("end,start",self.end,self.start)
        # print(s[left:right],s[self.start:self.end])
        if(len(s[left:right])>=len(s[self.start:self.end])):
            self.start = left 
            self.end = right
            # print("Updated",s[self.start:self.end])
        
        
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)-1):
            self.checkFromMidPalin(s,i,i)
            self.checkFromMidPalin(s,i,i+1)
            
        return s[self.start:self.end]

        
        
    
    class bruteForceSolution:
        def ispalindrome(self,ss):
            start = 0
            end = len(ss)-1

            while(start<=end):
                if(ss[start] == ss[end]):
                    start += 1
                    end -= 1
                else:
                    return False
            return True


        def longestPalindrome(self, s: str) -> str:

            maxlen = 1
            start = 0
            end = 0
            for i in range(len(s)): # this i will keep track of where to start the substring

                for j in range(maxlen,len(s)+1): # This j will keep track of end of the substring
                    # print("computing for",s[i:i+j])
                    if(i+j>len(s)):
                        break

                    if(self.ispalindrome(s[i:i+j])):
                        if(j>maxlen):
                            maxlen = j
                            # print("updated maxlen=",maxlen)
                            start = i
            return s[start:start+maxlen]
