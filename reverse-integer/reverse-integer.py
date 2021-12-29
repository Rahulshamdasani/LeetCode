class Solution:
    def reverse(self, x: int) -> int:
        l = []
        sig = (1 if x>0 else -1)
        
        x = abs(x)
        
        while(x>0):
            
            l.append(x%10)
            x = floor(x/10)
        print(l)
        n = 0
        mst = len(l)
        for c in l:
            
            p = 10**(mst-1) *int(c)
            mst -= 1
            n = n+p
        n = sig*n
        if(n>-2**31 and n<2**31 - 1):
            return n
        else:
            return 0