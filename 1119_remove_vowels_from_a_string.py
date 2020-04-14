class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = []
        for s in S:
            if s not in vowels:
                res.append(s)
        return ''.join(res)
        