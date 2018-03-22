class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # 103ms
        tf = {}
        
        for c in s:
            if c in tf:
                tf[c] += 1
            else:
                tf[c] = 1
        
        # time O(nlgn)
        tf2 = sorted(tf.items(), key=lambda x:x[1], reverse=True)
        
        res = []
        for ele in tf2:
            k = ele[0]
            v = ele[1]
            for i in range(v):
                res.append(k)
        return ''.join(res)
    
        
        '''
        # one line solution 97ms
        return ''.join(c * t for c, t in collections.Counter(s).most_common())
        '''
        