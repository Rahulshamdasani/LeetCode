"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Input: nums = [1], k = 1
Output: [1]


Initialize the sliding window to first k
then choose max
shift sliding window by 1
if(max goes out of window):
    update max


"""
nums = [1,3,-1,-3,5,3,6,7]
k = 3

def slidingWindow(nums,k):

    if(len(nums)<k):            # False
        return [max(nums)]
    
    firstMax = max(nums[:k])    # max(1,3,-1) = 3

    index = nums.index(firstMax) # 1
    res = [firstMax]        # res =[3]
    for i in range(1,len(nums)-(k-1)): # i=4

        if(i>index):     # True
            maxEle = max(nums[i:i+k])  # max(-1,-3,5) = 5
            index = nums.index(maxEle) # 4
            
        if(nums[i] > maxEle):  # True
            maxEle = nums[i] # 6
            index = i # 6
        res.append(maxEle)      #[3,3,5,5,6,7]
    
    return res