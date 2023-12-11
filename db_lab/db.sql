CREATE DATABASE IF NOT EXISTS fourth_lab_db;
USE fourth_lab_db;

DROP TABLE IF EXISTS fourth_lab_db.attraction_has_staff;
DROP TABLE IF EXISTS fourth_lab_db.park_has_show;
DROP TABLE IF EXISTS fourth_lab_db.order_ticket;
DROP TABLE IF EXISTS fourth_lab_db.attraction_staff;
DROP TABLE IF EXISTS fourth_lab_db.park_has_attraction;
DROP TABLE IF EXISTS fourth_lab_db.attraction;
DROP TABLE IF EXISTS fourth_lab_db.order;
DROP TABLE IF EXISTS fourth_lab_db.client;
DROP TABLE IF EXISTS fourth_lab_db.actor_in_show;
DROP TABLE IF EXISTS fourth_lab_db.show;
DROP TABLE IF EXISTS fourth_lab_db.actor;
DROP TABLE IF EXISTS fourth_lab_db.ticket;
DROP TABLE IF EXISTS fourth_lab_db.staff;
DROP TABLE IF EXISTS fourth_lab_db.park;
DROP TABLE IF EXISTS fourth_lab_db.city;
DROP TABLE IF EXISTS fourth_lab_db.region;

CREATE TABLE IF NOT EXISTS fourth_lab_db.show (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NULL,
    description VARCHAR(45) NULL,
    PRIMARY KEY(id),
    INDEX idx_show_name (name) VISIBLE,
    INDEX idx_show_name_description (name, description) VISIBLE
) engine = InnoDB;

CREATE TABLE IF NOT EXISTS fourth_lab_db.region (
    name VARCHAR(45) NOT NULL,
    PRIMARY KEY(name),
    INDEX idx_region_name (name) VISIBLE
) engine = InnoDB;

CREATE TABLE IF NOT EXISTS fourth_lab_db.city (
    name VARCHAR(45) NOT NULL,
    region_name VARCHAR(45) NOT NULL,
    PRIMARY KEY(name, region_name),
    INDEX fk_city_region1_idx (region_name ASC) VISIBLE,
    INDEX idx_city_name (name) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.city
    ADD CONSTRAINT fk_city_region1
    FOREIGN KEY (region_name)
    REFERENCES fourth_lab_db.region (name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

CREATE TABLE IF NOT EXISTS fourth_lab_db.park (
    id INT NOT NULL AUTO_INCREMENT,
    max_visitors_per_day INT NULL,
    open_time VARCHAR(11) NOT NULL,
    city_name VARCHAR(45) NOT NULL,
    PRIMARY KEY (id),
    INDEX park_max_visitors_per_day_idx (max_visitors_per_day ASC) VISIBLE,
    INDEX fk_park_city1_idx (city_name ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.park
    ADD CONSTRAINT fk_park_city1
    FOREIGN KEY (city_name)
    REFERENCES fourth_lab_db.city (name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
	
CREATE TABLE IF NOT EXISTS fourth_lab_db.actor (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NULL,
  surname VARCHAR(45) NULL,
  PRIMARY KEY (id),
  INDEX id_name_idx (id, name) VISIBLE,
  INDEX id_name_surname_idx (id, name, surname) VISIBLE
) engine = InnoDB;

CREATE TABLE IF NOT EXISTS fourth_lab_db.staff (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NULL,
  surname VARCHAR(45) NULL,
  phonenumber VARCHAR(13) NULL,
  park_id INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX phonenumber_UNIQUE (phonenumber ASC) VISIBLE,
  INDEX fk_staff_park1_idx (park_id ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.staff 
	ADD CONSTRAINT fk_staff_park1
    FOREIGN KEY (park_id)
    REFERENCES fourth_lab_db.park (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;


CREATE TABLE IF NOT EXISTS fourth_lab_db.attraction (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NULL,
  capacity INT NOT NULL,
  PRIMARY KEY (id),
  INDEX name_idx (name ASC) VISIBLE,
  INDEX name_capacity_idx (name, capacity) VISIBLE
) engine = InnoDB;

CREATE TABLE IF NOT EXISTS fourth_lab_db.actor_in_show (
  actor_id INT NOT NULL,
  show_id INT NOT NULL,
  PRIMARY KEY (actor_id, show_id),
  INDEX fk_actor_in_show_has_show_show1_idx (show_id ASC) VISIBLE,
  INDEX fk_actor_in_show_has_show_actor_in_show_idx (actor_id ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.actor_in_show 
	ADD CONSTRAINT fk_actor_in_show_has_show_actor_in_show
    FOREIGN KEY (actor_id)
    REFERENCES fourth_lab_db.actor (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	ADD CONSTRAINT fk_actor_in_show_has_show_show1
    FOREIGN KEY (show_id)
    REFERENCES fourth_lab_db.show (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
CREATE TABLE IF NOT EXISTS fourth_lab_db.ticket (
  id INT NOT NULL AUTO_INCREMENT,
  park_id INT NOT NULL,
  in_stock INT NULL,
  date VARCHAR(10) NULL,
  price INT NULL,
  special_ticket INT NULL,
  PRIMARY KEY (id, park_id),
  INDEX fk_ticket_park1_idx (park_id ASC) VISIBLE,
  INDEX special_ticket_price_idx (special_ticket, price) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.ticket 
	ADD CONSTRAINT fk_ticket_park1
    FOREIGN KEY (park_id)
    REFERENCES fourth_lab_db.park (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
CREATE TABLE IF NOT EXISTS fourth_lab_db.client (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NULL,
  surname VARCHAR(45) NULL,
  age INT NULL,
  phone VARCHAR(13) NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX phone_UNIQUE (phone ASC) VISIBLE,
  INDEX  name_age_idx (name, age) VISIBLE
) engine = InnoDB;

CREATE TABLE IF NOT EXISTS fourth_lab_db.order (
  id INT NOT NULL AUTO_INCREMENT,
  client_id INT NOT NULL,
  date VARCHAR(10) NOT NULL,
  total_price VARCHAR(45) NULL,
  PRIMARY KEY (id),
  INDEX fk_order_visitor1_idx (client_id ASC) VISIBLE,
  INDEX total_price_idx (total_price ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.order 
	ADD CONSTRAINT fk_order_visitor1
    FOREIGN KEY (client_id)
    REFERENCES fourth_lab_db.client (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
CREATE TABLE IF NOT EXISTS fourth_lab_db.park_has_show (
  show_id INT NOT NULL,
  park_id INT NOT NULL,
  INDEX fk_park_has_show_show1_idx (show_id ASC) VISIBLE,
  INDEX fk_park_has_show_park1_idx (park_id ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.park_has_show
	ADD CONSTRAINT fk_park_has_show_show1
    FOREIGN KEY (show_id)
    REFERENCES fourth_lab_db.show (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	ADD CONSTRAINT fk_park_has_show_park1
    FOREIGN KEY (park_id)
    REFERENCES fourth_lab_db.park (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
CREATE TABLE IF NOT EXISTS fourth_lab_db.order_ticket (
  ticket_id INT NOT NULL,
  order_id INT NOT NULL ,
  number_of_tickets INT NULL,
  PRIMARY KEY (ticket_id, order_id),
  INDEX fk_ticket_has_order_order1_idx (order_id ASC) VISIBLE,
  INDEX number_of_tickets_tickets_park_id_idx (number_of_tickets ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.order_ticket
	ADD CONSTRAINT fk_ticket_has_order_ticket1
    FOREIGN KEY (ticket_id)
    REFERENCES fourth_lab_db.ticket (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	ADD CONSTRAINT fk_ticket_has_order_order1
    FOREIGN KEY (order_id)
    REFERENCES fourth_lab_db.order (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
CREATE TABLE IF NOT EXISTS fourth_lab_db.park_has_attraction (
  park_id INT NOT NULL,
  attraction_id INT NOT NULL,
  number INT NULL,
  PRIMARY KEY (park_id, attraction_id),
  INDEX fk_park_has_attraction_attraction1_idx (attraction_id ASC) VISIBLE,
  INDEX fk_park_has_attraction_park1_idx (park_id ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.park_has_attraction 
	ADD CONSTRAINT fk_park_has_attraction_park1
    FOREIGN KEY (park_id)
    REFERENCES fourth_lab_db.park (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	ADD CONSTRAINT fk_park_has_attraction_attraction1
    FOREIGN KEY (attraction_id)
    REFERENCES fourth_lab_db.attraction (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
CREATE TABLE IF NOT EXISTS fourth_lab_db.attraction_staff (
  staff_id INT NOT NULL,
  attraction_id INT NOT NULL,
  PRIMARY KEY (staff_id, attraction_id),
  INDEX fk_staff_has_attraction_attraction1_idx (attraction_id ASC) VISIBLE,
  INDEX fk_staff_has_attraction_staff1_idx (staff_id ASC) VISIBLE
) engine = InnoDB;

ALTER TABLE fourth_lab_db.attraction_staff 
	ADD CONSTRAINT fk_staff_has_attraction_staff1
    FOREIGN KEY (staff_id)
    REFERENCES fourth_lab_db.staff (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	ADD CONSTRAINT fk_staff_has_attraction_attraction1
    FOREIGN KEY (attraction_id)
    REFERENCES fourth_lab_db.attraction (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    
INSERT INTO fourth_lab_db.show (name, description) VALUES
('Cook Show', 'Description 1');

INSERT INTO fourth_lab_db.region (name) VALUES
    ('Lviv');
    
INSERT INTO fourth_lab_db.city (name, region_name) VALUES
	('Lviv', 'Lviv');
    
INSERT INTO fourth_lab_db.park (max_visitors_per_day, open_time, city_name) VALUES
	(100, '08:00-21:00', 'Lviv');
    
INSERT INTO fourth_lab_db.actor (name, surname) VALUES
	('name1', 'surname1');
    
INSERT INTO fourth_lab_db.staff (name, surname, phonenumber, park_id) VALUES
	('Svitlana', 'ssurname1', '+380970000001', 1);
    
INSERT INTO fourth_lab_db.attraction (name, capacity) VALUES
	('aname1', 10);
    
INSERT INTO fourth_lab_db.actor_in_show (actor_id, show_id) VALUES
	(1, 1);

INSERT INTO fourth_lab_db.ticket (park_id, in_stock, date, price, special_ticket) VALUES
	(1, 100, '01.01.2023', 100, 0);
    
INSERT INTO fourth_lab_db.client (name, surname, age, phone) VALUES
	('name1', 'surname1', 21, '+380960000001');
    
INSERT INTO fourth_lab_db.order (client_id, date, total_price) VALUES
	(1, '01.01.2023', 100);
    
INSERT INTO fourth_lab_db.park_has_show (show_id, park_id) VALUES
	(1, 1);
    
INSERT INTO fourth_lab_db.order_ticket (ticket_id, order_id, number_of_tickets) VALUES
	(1, 1, 1);
    
INSERT INTO fourth_lab_db.park_has_attraction (park_id, attraction_id, number) VALUES
	(1, 1, 1);
    
INSERT INTO fourth_lab_db.attraction_staff (staff_id, attraction_id) VALUES
	(1, 1);