#Binary Search
#Time Complexity: O(nlogn+mlogm)
#Space Complexity: O(logn+logm)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        low = 0
        li = []
        if len(nums2) > len(nums1):
            return self.intersect(nums2,nums1)
        high = len(nums1) - 1
        for i in range(len(nums2)):
            index = self.binary_Search(nums1,low,high,nums2[i])
            if index != -1:
                low = index + 1
                li.append(nums2[i])
            
        return li
    
    def binary_Search(self,nums1,low,high,target):
        while low <= high:
            mid = (low + high) // 2
            if nums1[mid] == target:
                if low == mid or nums1[mid-1] < nums1[mid]:
                    return mid
                else:
                    high = mid - 1
            elif nums1[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

#Two Pointers
#Time Complexity: O(nlogn+mlogm)
#Space Complexity: O(logn+logm)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        li = []
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                li.append(nums1[i])
                i +=1
                j +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                j += 1
                
        return li
                
        
            
    
        
            