class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        二分法 + 双指针的思想。
        先二分找到分界点，最接近X的点。
        然后用相向双指针 + 打擂台来确定结果。
        '''
        
        index = self.find_index(arr, x)
        start = index - 1
        end = index
        
        res = self.find_elements(start, end, arr, k, x)
        return sorted(res)
        
        
    def find_index(self, arr, x):
        # 经典二分模板
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            
            if arr[mid] < x:
                left = mid
            else:
                right = mid
        
        # 此时的left部分已经比x大了，可以作为起点，找最后一个比x大的
        if arr[left] >= x:
            return left
        
        # 如果left部分没有，看right部分，找第一个比x大的就好
        if arr[right] >= x:
            return right
        
        # 如果没找到x 则返回arr长度
        return len(arr)
            
        
    def find_elements(self, start, end, arr, k, x):
        res = []
        '''
        一共填充k个数字到res就好 所以用for k
        如果start越界了（走完了）则加入end指针的数字并且end继续走
        同理，如果end指针走完了，需要加入start指针并且继续走
        如果都有，比较和x的差异，取小的
        start部分都比x小，所以用x - arr[start]
        相反end部分都比x大，用 arr[end] - x
        如果start部分小，就放start相对应的index 并且走一步。
        同理处理end, 最后排个序。
        
        '''
        for i in range(k):
            if start < 0:
                res.append(arr[end])
                end += 1
            elif end >= len(arr):
                res.append(arr[start])
                start -= 1
            else:
                if x - arr[start] <= arr[end] - x:
                    res.append(arr[start])
                    start -= 1
                else:
                    res.append(arr[end])
                    end += 1
                    
        return res
             