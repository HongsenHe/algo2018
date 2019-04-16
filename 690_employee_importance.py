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
            
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp = self.id_emp(employees, id)
        return self.helper(emp, employees)
    
    def helper(self, emp, employees):
        if len(emp.subordinates) == 0:
            return emp.importance
        
        sub_total = emp.importance
        for id in emp.subordinates:
            cur_emp = self.id_emp(employees, id)
            sub_total += self.helper(cur_emp, employees)
        return sub_total
            
    def id_emp(self, employees, id):
        for employee in employees:
            if employee.id == id:
                return employee
    