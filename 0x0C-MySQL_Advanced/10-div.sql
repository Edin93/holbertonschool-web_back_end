-- Creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
-- SOLUTION FOR MySQL 5.7 (old working solution):
/*
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN (a / b);
    END IF;
END$$
DELIMITER ;
*/
-- SOLUTION FOR MySQL 8.0 (new version - updated november 2026)
DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER;
