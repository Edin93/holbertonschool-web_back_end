-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers//
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE n INT DEFAULT 0;
    DECLARE i INT DEFAULT 0;
    SELECT COUNT(*) FROM users INT n;
    SET i = 0;
    WHILE i < n DO
        SET new_average_score = (
            SELECT sum((SELECT weight FROM projects WHERE corrections.project_id = id) * score) / (SELECT sum(weight) FROM projects)
            FROM corrections
        )
        UPDATE users SET average_score = new_average_score;
        SET i = i + 1;
    END WHILE;
END//
DELIMITER ;
