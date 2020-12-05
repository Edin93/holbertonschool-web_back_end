-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers//

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(proj.weight * corr.score) / SUM(proj.weight)
        FROM corrections AS corr
        RIGHT JOIN projects AS proj
        ON corr.project_id = proj.id
        WHERE corr.user_id = users.id
    );
END//

DELIMITER ;
