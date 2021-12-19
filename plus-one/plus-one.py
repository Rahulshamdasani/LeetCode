class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        carry = 1
        while(i>=0 and carry>0):
            if(digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += carry
                carry -= 1
            i-=1
        if(carry == 1):
            digits.insert(0,carry)
        return digits