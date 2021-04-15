# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        # 用倍增法找到最小的end index. 常规二分模板
        end = self.find_end(reader, target)
        start = 0
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
                
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        
        return -1
        
    def find_end(self, reader, target):
        end = 0
        
        while reader.get(end) < target:
            end = (end + 1) * 2
            
        return end
            
            