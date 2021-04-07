class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] = self.nums.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.nums:
            # 两种情况。rem在pool里是个前提，1. rem和num 是不同数字。2. num不仅有一个
            # 举例 add 2 find 4。rem = num = 2, 但只有一个在nums里 则false
            rem = value - num
            if rem in self.nums and (rem != num or self.nums[num] > 1):
                return True
                
        return False
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)