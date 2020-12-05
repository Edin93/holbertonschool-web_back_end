-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers//
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE n INT DEFAULT 0;
    DECLARE i INT DEFAULT 0;
    SELECT COUNT(*) FROM users INTO n;
    SET i = 0;
    WHILE (i < n) DO
        UPDATE users SET average_score = (
            SELECT sum((SELECT weight FROM projects WHERE corrections.project_id = id) * score) / (SELECT sum(weight) FROM projects)
            FROM corrections
            WHERE 1 = 1
        );
        SET i = i + 1;
    END WHILE;
END//
DELIMITER ;
