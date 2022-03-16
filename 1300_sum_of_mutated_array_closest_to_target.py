class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        mean = target // n
        if abs(target - mean * n) > abs(target - (mean + 1) * n):
            mean = mean + 1
        if arr[0] > mean:
            return mean
        if arr[-1] <= mean:
            return arr[-1]
        i = 0
        while i < n and arr[i] <= mean:
            target -= arr[i]
            i += 1
        return self.findBestValue(arr[i:], target)
            
            
            