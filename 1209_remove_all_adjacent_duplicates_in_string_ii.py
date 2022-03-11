class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        sk = []
        
        '''
        遍历每一个元素，维护一个stack, 如果当前元素和stack的顶一样了。
        则看它在stack里的数字是多少，如果已经满足k了，则继续。
        如果不满足，更新数字。此题先弹出，再判断数字。
        如果和顶不一样，就默认数值是1，好比构建hashmap的方法。
        最后打印stack, 看每个 字母对应多少数字。
        
        '''
        
        for i in range(len(s)):
            cur = s[i]
            if sk and cur == sk[-1][0]:
                cnt = sk.pop()[1] + 1
                if cnt == k:
                    continue
                else:
                    sk.append([cur, cnt])
            else:
                sk.append([cur, 1])
                
        res = []
        for ele in sk:
            res.append(ele[0] * ele[1])

        return ''.join(res)
        
                
        
        
        