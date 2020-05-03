class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = Counter(list(magazine))
        for note in ransomNote:
            if note in maga and maga[note] > 0:
                maga[note] -= 1
            else:
                return False
        return True
                