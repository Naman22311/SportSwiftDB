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

CREATE TABLE IF NOT EXISTS Cart (
    Customer_ID INT NOT NULL,
    Product_ID INT NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);
INSERT INTO Cart VALUE (1, 1);
INSERT INTO Cart VALUE (1, 2);

CREATE TABLE IF NOT EXISTS check_blocked(
        Customer_ID INT NOT NULL,
        blocked BOOL NOT NULL DEFAULT FALSE,
        PRIMARY KEY (Customer_ID)
);

CREATE TABLE IF NOT EXISTS Product
(
    Product_ID  INT            NOT NULL AUTO_INCREMENT,
    Name        VARCHAR(255)   NOT NULL,
    Price       INT NOT NULL,
    Description TEXT           NOT NULL,
    PRIMARY KEY (Product_ID)
);

INSERT INTO Product VALUES(1, 'Tennis Racquets', 30, 'tennis racquets');
INSERT INTO Product VALUES(2, 'Badminton', 500, 'Badminton racquets');

INSERT INTO Customer VALUES (1, 'Shrutya', "adsish", 'abcd1@gmail.com', 'abcd1', 0);
INSERT INTO Customer VALUES (2, 'Naman', "askdn", 'abcd2@gmail.com', 'abcd2', 0);
SELECT *
from Customer;
