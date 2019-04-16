class Solution:
    def countAndSay(self, n: int) -> str:
        # 每次依照上次的结果继续计算
        result = "1"
        
        for i in range(n-1):
            next_result = ""
            count = 1
            
            for j in range(len(result)):
                if j == len(result) - 1 or result[j] != result[j+1]:
                    # add count with number into new result and reset count
                    next_result += str(count) + result[j]
                    count = 1
                else:
                    # if same with next number, keep adding the count
                    count += 1
            result = next_result
        return result
            
            
            
            