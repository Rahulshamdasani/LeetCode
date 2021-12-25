class Solution:
    def intToRoman(self, num: int) -> str:
        
        d = {1: ["","I","II","III","IV","V","VI","VII","VIII","IX"],
        10: ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        100: ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"], 
        1000: ["","M","MM","MMM"]}
        s = ""
        power = 1
        while(num>0):
            
            dig = num%10  # Extracting the last digit
            # print("power =",power,"digit = ",dig)
            s = d[power][dig]+s
            power *= 10
            num//=10
        # print(s)
        return s
            