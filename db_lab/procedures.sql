USE fourth_lab_db;

DROP PROCEDURE IF EXISTS insert_client;
DROP PROCEDURE IF EXISTS insert_attraction_has_staff;
DROP PROCEDURE IF EXISTS multi_insert;
DROP PROCEDURE IF EXISTS call_client_age_statistics;
DROP FUNCTION IF EXISTS client_age_statistics;
DELIMITER //
CREATE PROCEDURE insert_client(IN in_name VARCHAR(45), IN in_surname VARCHAR(45), IN in_age INT, IN in_phone VARCHAR(13))
BEGIN
    INSERT INTO fourth_lab_db.client (name, surname, age, phone)
    VALUES (in_name, in_surname, in_age, in_phone);
END;
//
DELIMITER ;

DELIMITER //

CREATE PROCEDURE insert_attraction_has_staff(IN staff_name VARCHAR(45), IN staff_surname VARCHAR(45), 
IN attraction_name VARCHAR(45))
BEGIN
    DECLARE staff_id INT;
    DECLARE attraction_id INT;

    SELECT id INTO staff_id
    FROM fourth_lab_db.staff
    WHERE name = staff_name AND surname = staff_surname
    LIMIT 1;

    SELECT id INTO attraction_id
    FROM fourth_lab_db.attraction
    WHERE name = attraction_name
    LIMIT 1;

    INSERT INTO fourth_lab_db.attraction_has_staff (attraction_id, staff_id)
    VALUES (attraction_id, staff_id);
END //
DELIMITER ;

DELIMITER //

CREATE PROCEDURE multi_insert()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        -- Генерація значень для вставки
        SET @name = CONCAT('unknown', counter);
        SET @surname = CONCAT('unknown', counter);
        SET @age = 0;
        SET @phone = CONCAT('unknown', counter);

        -- Вставка рядка у таблицю
        INSERT INTO fourth_lab_db.client (name, surname, age, phone)
        VALUES (@name, @surname, @age, @phone);

        SET counter = counter + 1;
    END WHILE;
END //

DELIMITER ;

DELIMITER //

CREATE FUNCTION client_age_statistics(stat_type VARCHAR(10))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE result INT;

    IF stat_type = 'Max' THEN
        SELECT MAX(age) INTO result FROM client;
    ELSEIF stat_type = 'Min' THEN
        SELECT MIN(age) INTO result FROM client;
    ELSEIF stat_type = 'Sum' THEN
        SELECT SUM(age) INTO result FROM client;
    ELSEIF stat_type = 'Avg' THEN
        SELECT AVG(age) INTO result FROM client;
    ELSE
        SET result = NULL;
    END IF;

    RETURN result;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE call_client_age_statistics()
BEGIN
    DECLARE max_age INT;
    DECLARE min_age INT;
    DECLARE sum_age INT;
    DECLARE avg_age INT;

    SET max_age = client_age_statistics('Max');
    SELECT CONCAT('Max Age: ', max_age) AS Result;

    SET min_age = client_age_statistics('Min');
    SELECT CONCAT('Min Age: ', min_age) AS Result;

    SET sum_age = client_age_statistics('Sum');
    SELECT CONCAT('Sum Age: ', sum_age) AS Result;

    SET avg_age = client_age_statistics('Avg');
    SELECT CONCAT('Avg Age: ', avg_age) AS Result;
END //

DELIMITER ;