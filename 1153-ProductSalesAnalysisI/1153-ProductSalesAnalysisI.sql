-- Last updated: 8/19/2026, 4:18:26 PM
# Write your MySQL query statement below
select product_name,year,price from Sales left join Product on Sales.product_id=Product.product_id;