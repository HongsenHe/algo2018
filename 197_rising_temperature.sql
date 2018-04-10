# Write your MySQL query statement below
SELECT w2.Id
FROM weather w1
JOIN weather w2
ON DATEDIFF(w2.Date, w1.Date) = 1
WHERE w2.Temperature > w1.Temperature;