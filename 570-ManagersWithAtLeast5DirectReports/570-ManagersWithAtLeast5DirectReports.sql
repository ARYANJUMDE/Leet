-- Last updated: 8/19/2026, 4:20:35 PM
# Write your MySQL query statement below
select name from Employee where id in (select managerId from Employee group by managerId having count(*)>=5); 