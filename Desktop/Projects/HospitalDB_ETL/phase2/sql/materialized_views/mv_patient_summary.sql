-- Materialized View: Patient Summary
CREATE MATERIALIZED VIEW mv_patient_summary AS
SELECT 
    patient_id,
    first_name,
    last_name,
    gender,
    DATE_PART('year', AGE(birth_date)) AS age,
    COUNT(visit_id) AS total_visits
FROM staging_visits
JOIN raw_patients USING (patient_id)
GROUP BY patient_id, first_name, last_name, gender, birth_date;
