# Write your MySQL query statement below
# 这种找最小最大值的，都需要自交，然后自己比其他人小或者大作为条件
delete p1 from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id;