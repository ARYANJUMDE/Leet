-- Last updated: 9/9/2026, 10:15:07 PM
# Write your MySQL query statement below
select player_id, min(event_date) as first_login from Activity group by player_id;