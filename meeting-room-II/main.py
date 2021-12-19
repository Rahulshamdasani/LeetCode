# 1 test case is failing
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if(len(intervals) == 0):
            return 0
        
        # Sort based on end times
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        

        end = []
        count = 1
        
        for interval in intervals:
            
            currStart = interval[0]
            currEnd = interval[1]
            
            used = False
            for i in range(len(end)-1,-1,-1):
                if(end[i]<=currStart):
                    used = True
                    if(currEnd>end[i]):
                        print("Replacing",end[i],"with",currEnd)
                        end[i] =currEnd 
                        
                    break
                    
            if(not used):
                print("Inserting",currEnd)
                end.append(currEnd)
        print(end)
                    
            
                
        return len(end)
