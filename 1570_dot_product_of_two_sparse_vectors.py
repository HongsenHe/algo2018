class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_dic = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nums_dic[i] = num
                
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        
        for i, num in vec.nums_dic.items():
            if i not in self.nums_dic:
                continue
                
            res += num * self.nums_dic[i]
            
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)