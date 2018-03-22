class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            groups[self.hashStr(s)].append(s)

            '''
            group is {'': ['a', 'z'], '1:1': ['abc', 'bcd', 'xyz'], '2:2:1': ['acef'], '25': ['az', 'ba']})
            '''

        result = []
        for k, v in groups.items():
            result.append(sorted(v))

        return result

    def hashStr(self, s):
        hashcode = []
        '''
        key point: 
        input acef: calculate c -> a = 2, e -> c = 2, f -> e = 1, so key is 2:2:1
        group by with same key or say same pattern
        
        input az: ord['z'] - ord['a'] = 122 - 97 = 25 then 25 % 26 = 25
        input ba: ord['a'] - ord['b'] = 97 - 98 = -1 then -1 % 26 = 25
        so 'az' and 'ba' have the same key '25'
        '''
        for i in xrange(1, len(s)):
            hashcode.append(str((ord(s[i]) - ord(s[i-1])) % 26))
        return ':'.join(hashcode)