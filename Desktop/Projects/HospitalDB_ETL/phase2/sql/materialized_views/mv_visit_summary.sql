-- Materialized View: Visit Summary
CREATE MATERIALIZED VIEW mv_visit_summary AS
SELECT
    visit_id,
    patient_id,
    visit_date,
    department,
    doctor_id,
    total_amount
FROM staging_visits;
