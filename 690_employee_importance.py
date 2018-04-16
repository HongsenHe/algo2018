"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {e.id:e for e in employees}
        return self.helper(emap, id)
    
    def helper(self, emap, id):
        e = emap[id]
        res = e.importance
        for sub in e.subordinates:
            res += self.helper(emap, sub)
        return res
            
            