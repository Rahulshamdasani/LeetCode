class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)!=0):
            
            a=strs[0]
            print(a+"=a")
            
            for str in strs:

                # print("***************ITR1***************************")
                # print("str is" +str)
                max=len(a)

                currmax=len(str)   

                # print("curr max  is " , currmax)
                # print("max  is " , max)

                max=min(max, currmax)
                # print("min max  is " , max)
                
                a=a[:max]
                for i in range(max):
                    if(a[i]!=str[i]):
                        a=a[:i]
                        break;
                    
                
                
            return a


        
        else:
            return ""