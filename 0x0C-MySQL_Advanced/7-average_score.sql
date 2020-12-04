-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	SET @avrg = (SELECT TRUNCATE(AVG(score)) FROM corrections WHERE user_id = user_id);
	UPDATE users
	SET
		average_score = @avrg
	WHERE
		id = user_id;
END//
DELIMITER ;
