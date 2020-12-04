-- Create a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(
	user_id INT,
	project_name VARCHAR(255),
	score FLOAT
)
BEGIN
		INSERT INTO projects (name)
		SELECT * FROM (SELECT project_name) AS tmp
		WHERE NOT EXISTS (
			SELECT name FROM projects WHERE name = project_name
		) LIMIT 1;
		SET @project_id = (SELECT id FROM projects WHERE name = project_name);
		INSERT INTO corrections (user_id, project_id, score)
		VALUES (user_id, @project_id, score);
END//
DELIMITER ;
