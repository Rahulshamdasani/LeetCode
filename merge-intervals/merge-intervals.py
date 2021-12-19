class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        i = 0
        fin = []
        start = intervals[0][0]
        end = intervals[0][1]
        for elem in intervals:
            if(elem[0]<=end):
                end = max(end,elem[1])
            else:
                fin.append([start,end])
                start = elem[0]
                end = elem[1]
        fin.append([start,end])
            
        return fin