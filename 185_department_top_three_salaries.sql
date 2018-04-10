# Write your MySQL query statement below
/*
把每个部门的前三名找出来，加上部门名字即可。如何找前三名？自交让DepartmentID 相等 确保自己部门
如果是第一名，要大于所有其他人n-1（除了自己），如果是第二名，要大于n-2个人，第三名，大于n-3个人即可
也就是当前这个人的薪水要大于其他人，但不能超过n-3个人，也就是选出来的数量最多是3个。
或者说，这个部门没有超过3个人大于当前这个人的薪水，如果超过3个人大于当前这人，这不就老四了嘛。。。
*/
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;