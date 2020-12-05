-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET
        average_score = (
            SELECT sum((SELECT weight FROM projects WHERE corrections.project_id = id) * score) / (SELECT sum(weight) FROM projects)
            FROM corrections
            WHERE 1 = 1)
    WHERE
        1 = 1;
END//
DELIMITER ;
