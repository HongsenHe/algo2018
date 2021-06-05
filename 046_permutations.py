class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, each):
        # 退出条件就是当前子集长度是输入长度，深拷贝到最终解
        if len(each) == len(nums):
            res.append(list(each))
            return 
        
        
        # 可以是任何组合，不涉及start index, 所以直接for loop
        # 经典回溯：把当前数字加进去，跑下一层，弹出去。如果重复了则继续
        for num in nums:
            if num in each:
                continue
            each.append(num)
            self.helper(nums, res, each)
            each.pop()