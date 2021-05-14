import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_cnt = collections.Counter(words)
        heap = []
        
        for word, cnt in word_cnt.items():
            heapq.heappush(heap, (-cnt, word))
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
            
    
        