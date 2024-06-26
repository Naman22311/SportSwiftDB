USE SportSwiftDB;

CREATE TABLE IF NOT EXISTS Customer (
    Customer_ID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    email_ID VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    failed_attempts INT DEFAULT 0,
    PRIMARY KEY (Customer_ID)
);

CREATE TABLE IF NOT EXISTS check_blocked(
        Customer_ID INT NOT NULL,
        blocked BOOL NOT NULL DEFAULT FALSE,
        PRIMARY KEY (Customer_ID)
);

INSERT INTO Customer VALUES (1, 'Shrutya', "adsish", 'abcd1@gmail.com', 'abcd1', 0);
INSERT INTO Customer VALUES (2, 'Naman', "askdn", 'abcd2@gmail.com', 'abcd2', 0);
SELECT *
from Customer;
