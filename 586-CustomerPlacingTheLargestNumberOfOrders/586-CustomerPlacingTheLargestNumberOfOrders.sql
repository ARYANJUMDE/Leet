-- Last updated: 8/19/2026, 4:20:29 PM
# Write your MySQL query statement below
select customer_number from Orders group by customer_number order by count(*) desc limit 1;