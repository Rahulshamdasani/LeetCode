
class Solution:
    def compress(self, chars) :

        pointer = 1  # This is the place where count or next char will go
        i = 1   # We are ignoring the char as zero bec it remains the same
        count = 1 # Initally count will be 1
        while(i<len(chars)):
            # print(i)
            if(chars[i] == chars[i-1]):
                count += 1
                # print("same",count)
            
            else:
                if(count == 1):
                    # Then we dont need to store the count
                    chars[pointer] = chars[i]
                    pointer +=1
                else:
                    cHat = str(count)
                    
                    for j in range(len(cHat)):
                    
                        chars[pointer] = cHat[j]
                        pointer +=1
                    
                    chars[pointer] = chars[i]
                    pointer += 1
                    count = 1
                   


            i += 1
        
        if(count >1):
            cHat = str(count)
            for j in range(len(cHat)):
                chars[pointer] = cHat[j]
                pointer +=1
            
        return pointer
        


        

