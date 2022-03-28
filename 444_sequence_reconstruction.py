class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # maybe next time
        indegrees = [0] * len(org)
        graph = defaultdict(list)
        for sequence in seqs:
            for i, j in zip(sequence, sequence[1:]):
                graph[i].append(j)
                indegrees[j - 1] += 1
        stack = []
        for i, v in enumerate(indegrees):
            if v == 0:
                stack.append(i + 1)
        res = []
        while stack:
            if len(stack) > 1: return False
            cur = stack.pop()
            res.append(cur)
            for other in graph[cur]:
                indegrees[other - 1] -= 1
                if indegrees[other - 1] == 0:
                    stack.append(other)
        return res == org