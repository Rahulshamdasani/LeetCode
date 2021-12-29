class Solution:
    def myAtoi(self, s: str) -> int:
        flag = 0
        n = 0
        sign = 1
        for c in s:
            print('c=',c)
            if(c == '-' and flag == 0):
                print("In if")
                sign = -1
                flag =1
            elif(c == '+'  and flag == 0):
                flag =1
                print(" inside +")
                pass
            elif(c == ' ' and flag == 0):
                pass
            elif (c == ' '  and flag == 1):
                break
            elif(c == '0' or c =='1' or c == '2' or c == '3' or c == '4' or c == '5' or c =='6' or c == '7' or c =='8' or c == '9'):
                print("incrementing")
                flag = 1
                n += int(c)
                n = n*10
            else:
                print("breaking")
                break
                
        n = sign * int(n/10)
        if(n<-2**31):
            return -2**31
        elif(n>2**31-1):
            return 2**31-1
        return n
                