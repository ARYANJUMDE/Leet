-- Last updated: 8/19/2026, 4:18:00 PM
# Write your MySQL query statement below
select Distinct(author_id) as id from Views where author_id=viewer_id order by author_id asc ;