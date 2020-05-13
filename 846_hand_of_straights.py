class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        dic = Counter(hand)
        '''
        斗地主的顺子，先把手里的扑克数量关系搞定。然后每次取最小，依次查找。
        比如手里的牌是[1, 2, 2, 3, 3, 4]
        start就是1，W=3 即要找到 1, 2, 3 如果在dic里找不到 就直接返回false
        每次找到了就删减一个数量，牌不能重复用，不然出千了。
        '''
        
        while dic:
            start = min(dic)
            for cur in range(start, start + W):
                if not dic[cur]:
                    return False
                dic[cur] -= 1
                if dic[cur] == 0:
                    del dic[cur]
        return True
                    