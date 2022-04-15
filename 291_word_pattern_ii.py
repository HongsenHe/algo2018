class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # from ch9
        return self.helper(pattern, s, {}, set())
    
    def helper(self, pattern, str, mapping, used):
        if len(pattern) == 0 and len(str) == 0:
            return True
        if len(pattern) == 0 or len(str) == 0:
            return False
        if pattern[0] in mapping:
            s = mapping[pattern[0]]
            return s == str[0:len(s)] and self.helper(pattern[1:], str[len(s):], mapping, used)
        else:
            for k in range(1, len(str) + 1):
                if str[:k] in used:
                    continue
                mapping[pattern[0]] = str[:k]
                used.add(str[:k])
                if self.helper(pattern[1:], str[k:], mapping, used):
                    return True
                del mapping[pattern[0]]
                used.remove(str[:k])
            return False