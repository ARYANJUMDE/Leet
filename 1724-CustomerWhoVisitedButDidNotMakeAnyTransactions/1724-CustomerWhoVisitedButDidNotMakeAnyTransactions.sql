-- Last updated: 8/19/2026, 4:16:29 PM
# Write your MySQL query statement below
select customer_id,count(*) as count_no_trans from Visits left join Transactions on Visits.visit_id=Transactions.visit_id  where Transactions.transaction_id is NULL group by customer_id;
