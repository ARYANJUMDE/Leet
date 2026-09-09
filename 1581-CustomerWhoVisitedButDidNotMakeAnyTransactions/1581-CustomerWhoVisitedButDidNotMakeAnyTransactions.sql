-- Last updated: 9/9/2026, 10:12:58 PM
# Write your MySQL query statement below
select customer_id,count(*) as count_no_trans from Visits left join Transactions on Visits.visit_id=Transactions.visit_id  where Transactions.transaction_id is NULL group by customer_id;
