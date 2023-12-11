USE fourth_lab_db;

DROP TRIGGER IF EXISTS before_staff_insert_trigger;
DROP TRIGGER IF EXISTS before_insert_staff;
DROP TRIGGER IF EXISTS before_delete_staff;

DELIMITER //
CREATE TRIGGER before_staff_insert_trigger
BEFORE INSERT ON fourth_lab_db.staff
FOR EACH ROW
BEGIN
  DECLARE allowed_names VARCHAR(100);
  SET allowed_names = 'Svitlana,Petro,Olha,Taras';
  
  IF NOT FIND_IN_SET(NEW.name, allowed_names) > 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Invalid name. Allowed names are: Svitlana, Petro, Olha, Taras';
  END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER before_insert_staff
BEFORE INSERT ON fourth_lab_db.staff
FOR EACH ROW
BEGIN
    IF NEW.phonenumber REGEXP '00$' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid phonenumber: should not end with two zeros';
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER before_delete_staff
BEFORE DELETE ON fourth_lab_db.staff
FOR EACH ROW
BEGIN
	IF OLD.name IS NOT NULL THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Deletion not allowed for records without a name';
    END IF;
END;
//
DELIMITER ;