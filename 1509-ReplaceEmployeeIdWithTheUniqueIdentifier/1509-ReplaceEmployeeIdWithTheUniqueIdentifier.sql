-- Last updated: 8/19/2026, 4:17:10 PM
# Write your MySQL query statement below
select unique_id,name from Employees left join EmployeeUNI on Employees.id=EmployeeUNI.id;
