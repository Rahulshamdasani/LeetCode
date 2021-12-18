class Solution:
    
    def helper(self,mem1Left, mem2Left,i):
        
        flag = False
        
        if(mem1Left == mem2Left and mem1Left >=i):
            #print(i," given to mem1 bec both are same")
            mem1Left -= i
            flag= True
        
        elif(mem1Left > mem2Left and mem1Left >= i):
            mem1Left -= i
            #print(i,"given to mem1 bec it is bigger")
            flag= True
        
        elif(mem2Left >= i):
            mem2Left -= i
            #print(i,"given to mem2 bec it is bigger")
            flag= True
        
        if(flag):
            # This means it is taken care of
            return self.helper (mem1Left, mem2Left,i+1)
        
        else:
            return [i,mem1Left,mem2Left]
        
    
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        return self.helper(memory1, memory2, 1)
        
        