-- Last updated: 9/9/2026, 10:13:46 PM
# Write your MySQL query statement below
select unique_id,name from Employees left join EmployeeUNI on Employees.id=EmployeeUNI.id;
