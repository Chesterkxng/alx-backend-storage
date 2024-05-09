-- stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    	UPDATE users
	SET average_score = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) FROM corrections INNER JOIN projects
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = users.id);
END$$
DELIMITER ;
