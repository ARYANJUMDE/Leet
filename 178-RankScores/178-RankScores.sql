-- Last updated: 8/19/2026, 4:23:21 PM
# Write your MySQL query statement below
select score, DENSE_RANK() OVER (order by score desc) as `rank` from Scores;