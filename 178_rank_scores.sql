# Write your MySQL query statement below
/*
搞两个表a and b, 外面的表b是大循环，算当前的分数排名多少，怎么算？当前的分数要和所有的分数对比
也就是小循环，看看有几个比这当前循环的大，有几个就是排名第几，也就是rank 那么一次大循环就返回当前分数和排名
比如大循环当前分数是3.85, 里面小循环中，a.Score >= b.Score (3.85)的就只是他自己和4.00. 即rank = 2
*/

SELECT
  b.Score,
  (SELECT count(distinct a.Score) FROM Scores a WHERE a.Score >= b.Score) Rank
FROM Scores b
ORDER BY b.Score desc