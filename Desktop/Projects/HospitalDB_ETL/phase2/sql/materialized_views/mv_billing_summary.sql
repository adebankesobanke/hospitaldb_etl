-- Materialized View: Billing Summary
CREATE MATERIALIZED VIEW mv_billing_summary AS
SELECT
    billing_id,
    patient_id,
    visit_id,
    billing_date,
    amount,
    status
FROM staging_billing;
