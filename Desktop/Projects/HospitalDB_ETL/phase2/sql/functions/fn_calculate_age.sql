-- Function: Calculate Age from Birth Date
CREATE OR REPLACE FUNCTION fn_calculate_age(birth_date DATE)
RETURNS INT AS $$
BEGIN
    RETURN DATE_PART('year', AGE(birth_date));
END;
$$ LANGUAGE plpgsql;
