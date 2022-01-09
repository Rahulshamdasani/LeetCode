class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def help(nums,res):            
            if not nums:                
                ans.append(res)
                return
                
            for i in range(len(nums)):               
                temp = nums[:]
                tempres = res[:]               
                tempres.append(temp.pop(i))
                help(temp,tempres)
                
        help(nums,[])
        
        return ans
     