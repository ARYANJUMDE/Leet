-- Last updated: 8/19/2026, 4:23:08 PM
# Write your MySQL query statement below
select name as Customers from customers left join Orders on Customers.id=Orders.customerId where Orders.id is Null; 
