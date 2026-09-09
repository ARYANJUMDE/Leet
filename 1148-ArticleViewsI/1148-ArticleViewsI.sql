-- Last updated: 9/9/2026, 10:14:51 PM
# Write your MySQL query statement below
select Distinct(author_id) as id from Views where author_id=viewer_id order by author_id asc ;