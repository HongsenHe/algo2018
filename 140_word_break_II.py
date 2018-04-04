class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        """
        基本上把当前字段劈成凉拌，如果左边的在字典里，就分析右边有多少种可能
        再加上左边的作为子集，返回去（当然中间要优化啦，加入memo 证明已经分析过此字段）
        返回去之后算是前一个右边字段的所有可能，再加上前一个左边字段作为子集，返回去
        你懂的。。。
        """
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        # print("===> s is %s, memo is %s" % (s, memo))
        # 一个优化，如果是重复字段 就直接用吧！
        if s in memo:
            return memo[s]

        res = []
        # 如果当前字段在字典里，就加入结果集吧！
        if s in wordDict:
            res.append(s)

        for i in range(1, len(s)):
            # 把当前字段左右劈开！
            left = s[:i]
            right = s[i:]

            # print("left is: %s, right is: %s" % (left, right))
            # 如果连左边都不在字典里，还有什么可讲？下一位。
            if left not in wordDict:
                continue

            '''
            重点来啦！如果左边在字典里，那右边字段怎么个情况？DFS 来一直调用
            也就是右边字段或许分为几个小字段都在字典里，
            比如左边是a, 右边是bcd，字典是有b和cd 这里就返回[b, cd]
            再加上左边放到res里，就是['a b cd']
            '''
            restRes = self.helper(right, wordDict, memo)
            # print("left word is: %s, rest result set is: %s" % (left, restRes))

            for each in restRes:
                res.append(left + " " + each)
                # print("adding res is: %s" % res)
        # memo, key是当前字段，value是他的所有组合bcd could be bc+d or b+cd or bcd
        memo[s] = res
        # print("<=== memo is: %s" % memo)
        # print("<=== current s is %s, current res is %s" % (s, res))
        return res
    
    '''
    output:
    ===> s is abcd, memo is {}
    left is: a, right is: bcd
    ===> s is bcd, memo is {}
    left is: b, right is: cd
    ===> s is cd, memo is {}
    left is: c, right is: d
    <=== memo is: {'cd': ['cd']}
    <=== current s is cd, current res is ['cd']
    left word is: b, rest result set is: ['cd']
    adding res is: ['bcd', 'b cd']
    left is: bc, right is: d
    ===> s is d, memo is {'cd': ['cd']}
    <=== memo is: {'d': ['d'], 'cd': ['cd']}
    <=== current s is d, current res is ['d']
    left word is: bc, rest result set is: ['d']
    adding res is: ['bcd', 'b cd', 'bc d']
    <=== memo is: {'bcd': ['bcd', 'b cd', 'bc d'], 'd': ['d'], 'cd': ['cd']}
    <=== current s is bcd, current res is ['bcd', 'b cd', 'bc d']
    left word is: a, rest result set is: ['bcd', 'b cd', 'bc d']
    adding res is: ['a bcd']
    adding res is: ['a bcd', 'a b cd']
    adding res is: ['a bcd', 'a b cd', 'a bc d']
    left is: ab, right is: cd
    left is: abc, right is: d
    ===> s is d, memo is {'bcd': ['bcd', 'b cd', 'bc d'], 'd': ['d'], 'cd': ['cd']}
    left word is: abc, rest result set is: ['d']
    adding res is: ['a bcd', 'a b cd', 'a bc d', 'abc d']
    <=== memo is: {'bcd': ['bcd', 'b cd', 'bc d'], 'abcd': ['a bcd', 'a b cd', 'a bc d', 'abc d'], 'd': ['d'], 'cd': ['cd']}
    <=== current s is abcd, current res is ['a bcd', 'a b cd', 'a bc d', 'abc d']
    ['a bcd', 'a b cd', 'a bc d', 'abc d']
    '''
    