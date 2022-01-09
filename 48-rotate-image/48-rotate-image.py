class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        row = 0
        while(row<len(m)):
            col = row
            while(col<len(m)):
                
                m[row][col],m[col][row] = m[col][row],m[row][col]
                
                col += 1
            row += 1
       
        for i in range(len(m)):
            m[i].reverse()
       