class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split by . and compare each slot
        v1 = version1.split(".")
        v2 = version2.split(".")
        n1 = len(v1)
        n2 = len(v2)
        
        for i in range(max(n1, n2)):
            # if current verson has no value, assign 0
            if i < n1:
                i1 = int(v1[i])
            else:
                i1 = 0
            
            if i < n2:
                i2 = int(v2[i])
            else:
                i2 = 0
            
            if i1 != i2:
                if i1 < i2:
                    return -1
                else:
                    return 1
        return 0
        