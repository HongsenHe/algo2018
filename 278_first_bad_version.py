# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while start <= end:
            mid = start + (end-start) // 2
            # if current mid is bad, means [mid, end] are bad as well!
            if isBadVersion(mid):
                end = mid - 1
            else:
                # if current mid is good, means [start, mid] are good as well!
                start = mid + 1
        return start
            