import heapq
from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cache = defaultdict(list)  # {student_id: [top-5 scores]}

        '''
        用一个min heap来表示学生top 5的成绩，
        如果heap超过5了，则pop出去。 cache[student_id] 是一个list 也就是min heap
        留意defaultdict写法。
        
        '''
        for student_id, score in items:
            if len(cache[student_id]) < 5:  # make sure the size of heap for each student does not exceed 5.
                heapq.heappush(cache[student_id], score)
            else:
                heapq.heappushpop(cache[student_id], score)

        ans = []
        for student_id, scores in cache.items():
            average = sum(scores) // len(scores)
            ans.append((student_id, average))

        return sorted(ans, key=lambda x: x[0])