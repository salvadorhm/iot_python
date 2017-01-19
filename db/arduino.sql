CREATE DATABASE arduino;

USE arduino;

CREATE TABLE data (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    update_time timestamp,
    value float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE control(
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    update_time timestamp,
    value int(10) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO data(value) VALUES(0.0);
INSERT INTO control(value) VALUES(0);
