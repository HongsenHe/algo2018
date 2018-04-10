# Write your MySQL query statement below
select 
    d.Name as Department,    
    e.Name as Employee, 
    e.Salary
from Employee e join Department d
on e.DepartmentId = d.Id
where 
    (e.DepartmentId, Salary) in 
    (   select 
            DepartmentId, max(Salary)
        from 
            employee
        group by DepartmentId 
    )
;