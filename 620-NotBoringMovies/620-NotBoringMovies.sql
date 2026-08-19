-- Last updated: 8/19/2026, 4:20:12 PM
# Write your MySQL query statement below
select *from Cinema where id%2!=0 and description not like "boring" order by rating desc;