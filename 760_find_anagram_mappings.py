class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for k, v in enumerate(B):
            dic[v] = k
        for a in A:
            res.append(dic[a])
        return res

        '''
        #too slow way
        res = []
        for i in range(len(A)):
            k = 0
            for j in range(len(B)):
                if A[i] == B[j]:
                    k = j
                    break
            res.append(k)    
        return res
        '''        
        
        '''
        # too fast way
        D = {x: i for i, x in enumerate(B)}
        return [D[x] for x in A]
        '''