class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        fin = []
        i = j = 0
        while(i<len(nums1) and j<len(nums2)):
            
            if(nums1[i]<nums2[j]):
                fin.append(nums1[i])
                i+=1
            else:
                fin.append(nums2[j])
                j+=1
        if(i<len(nums1)):
            while(i<len(nums1)):
                fin.append(nums1[i])
                i+=1
        elif(j<len(nums2)):
            while(j<len(nums2)):
                fin.append(nums2[j])
                j+=1
        if(len(fin)%2):
            # print("returing mid")
            return fin[len(fin)//2]
        
        
        return (fin[len(fin)//2]+fin[len(fin)//2-1])/2