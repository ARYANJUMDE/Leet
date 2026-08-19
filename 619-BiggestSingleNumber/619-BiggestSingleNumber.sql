-- Last updated: 8/19/2026, 4:20:15 PM
# Write your MySQL query statement below
select max(num) as num from (select num,count(*) from MyNumbers group by num having count(*)=1) as t;