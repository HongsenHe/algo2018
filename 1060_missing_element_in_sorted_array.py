class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        写个func, 来求当前idx下，丢失了多少数字。
        比如[4, 5, 8, 10], idx = 3, 4和10之间相差6，即 nums[idx] - nums[0]
        但还有4, 5, 8, 所以丢了3个数字，即6, 7, 9. 
        即func: nums[idx] - nums[0] - idx
        
        用经典二分法模板，如果当前idx (mid) 丢失的数量小于k, 则还有更多丢失的在idx后面
        即缩小左半部分的范围，即 left = mid
        如果当前丢的数量还超过了k， 则答案在当前idx的左边，即right = mid
        
        * 最后从当前idx出发，数有多少个剩下的，本应该丢了k个，但目前已知丢了x个
        即找到k - self.missing_cnt(res)个，加上当前的数字则是答案。
        '''
        
        left = 0
        right = len(nums) - 1
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.missing_cnt(nums, mid) < k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return nums[res] + (k - self.missing_cnt(nums, res))
    
    def missing_cnt(self, nums, idx):
        return nums[idx] - nums[0] - idx