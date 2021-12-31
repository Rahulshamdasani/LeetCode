class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n= len(s)
        a=[None]*n
        i=0
        
        for x in s:
            print(x)
            if(x=='(' or x=='{' or x=='['):
                print("open paranthesis")
                a[i]=x
                i=i+1
                
            elif(x==')'):
                print("open paranthesis )")
                if(a[i-1]=='('):
                    a[i-1]=None
                    i=i-1
                    
                else:
                    print("returned from 1")
                    return 0
                
            elif(x=='}'):
                print("open paranthesis }")
                if(a[i-1]=='{'):
                    a[i-1]=None
                    i=i-1
                    
                else:
                    print("returned from 2")
                    return 0
                
                
            
            elif(x==']'):
                print("open paranthesis ]")
                if(a[i-1]=='['):
                    a[i-1]=None
                    i=i-1
                    
                else:
                    print("returned from 3")
                    return 0
                
            print("returned from 4")
        if(i==0):
            return 1
        else:
            return 0
            