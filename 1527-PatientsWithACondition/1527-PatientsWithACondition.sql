-- Last updated: 9/9/2026, 10:13:04 PM
# Write your MySQL query statement below
select patient_id, patient_name,conditions from Patients where conditions like 'DIAB1%' or conditions like "% DIAB1%";