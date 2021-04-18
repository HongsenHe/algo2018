class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
                
        if i < len(nums1):
            nums.extend(nums1[i:])
        elif j < len(nums2):
            nums.extend(nums2[j:])
            
        n = len(nums)
        if n % 2 == 0:
            return float((nums[n//2-1] + nums[n//2])) / 2
        else:
            return nums[n//2]
        
    '''
    04172021 O(log(m+n))
    总体来讲折半搜索，分四个部分，nums1的前后部分和 nums2的前后部分
    对比他们的中点，如果小于k, 而且nums1的中点小于nums2的中点
    舍弃nums1的前部分，，同理大于k, 舍弃nums2的后半部分。
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        # write your code here
        len_a, len_b = len(A), len(B)
        if (len_a + len_b) % 2 == 1:
            return self.finf_kth(A, B, (len_a + len_b) // 2 + 1)
        else:
            left = self.finf_kth(A, B, (len_a + len_b) // 2 )
            right = self.finf_kth(A, B, (len_a + len_b) // 2 + 1)
            return (left + right) / 2
            
    def finf_kth(self, A, B, k):
        if len(A) == 0:
            left, right = B[0], B[-1]
        elif len(B) == 0:
            left, right = A[0], A[-1]
        else:
            left, right = min(A[0], B[0]), max(A[-1], B[-1])
        while left + 1 < right:
            mid = (left + right) // 2
            count1 = self.helper(A, mid)
            count2 = self.helper(B, mid)
            if count1 + count2 < k:
                left = mid
            else:
                right = mid
        count1 = self.helper(A, left)
        count2 = self.helper(B, left)
        if count1 + count2 >= k:
            return left
        else:
            return right
    
    def helper(self, array, flag):
        if len(array) == 0:
            return 0
        left, right = 0 ,len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= flag:
                left = mid
            else:
                right = mid
        if array[right] <= flag:
            return right + 1
        if array[left] <= flag:
            return left + 1
        return 0