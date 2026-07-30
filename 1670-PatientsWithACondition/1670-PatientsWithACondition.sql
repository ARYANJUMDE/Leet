-- Last updated: 7/30/2026, 11:02:14 PM
# Write your MySQL query statement below
select patient_id, patient_name,conditions from Patients where conditions like 'DIAB1%' or conditions like "% DIAB1%";