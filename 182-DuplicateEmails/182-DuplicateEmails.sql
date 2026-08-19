-- Last updated: 8/19/2026, 4:23:10 PM
# Write your MySQL query statement below
select email from Person group by email having count(id)>1;