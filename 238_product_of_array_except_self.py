class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        idx     0   1   2   3
        num     1   2   3   4
        left    1   1   2   6
        right   24  12  4   1
        total   24  12  8   6
        '''
        
        '''
        length = len(nums)
        res, l_lst, r_lst = [0] * length, [0] * length, [0] * length
    
        # get product from this number left
        l_lst[0] = 1
        for i in range(1, length):
            l_lst[i] = l_lst[i-1] * nums[i-1]
        
        # get product from this number right
        r_lst[length-1] = 1
        for j in range(length-2, -1, -1):
            r_lst[j] = r_lst[j+1] * nums[j+1]
            
        # merge 
        for k in range(length):
            res[k] = l_lst[k] * r_lst[k]
            
        return res
            
        '''
        
        left = 1
        prd = []
        for num in nums:
            # append this number's left product
            prd.append(left)
            # update left product with current number as next number's left product
            left *= num
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            prd[i] = prd[i] * right
            right *= nums[i]
        return prd
    