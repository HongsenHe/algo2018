# Write your MySQL query statement below
SELECT 
IFNULL(
    (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC
    limit 1 offset 1), NULL) 
AS SecondHighestSalary;
# return only 10 records, start on record 16 (OFFSET 15)":
# $sql = "SELECT * FROM Orders LIMIT 10 OFFSET 15";
# or $sql = "SELECT * FROM Orders LIMIT 15, 10";
