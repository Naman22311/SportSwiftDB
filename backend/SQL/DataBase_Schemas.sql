Create database IF NOT EXISTS SportSwiftDB;
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

CREATE TABLE IF NOT EXISTS check_blocked(
        Customer_ID INT NOT NULL,
        blocked BOOL NOT NULL DEFAULT FALSE,
        PRIMARY KEY (Customer_ID)
);

CREATE TABLE IF NOT EXISTS Product
(
    Product_ID  INT            NOT NULL AUTO_INCREMENT,
    Name        VARCHAR(255)   NOT NULL,
    Category    VARCHAR(255)   NOT NULL,
    Description TEXT           NOT NULL,
    Price       DECIMAL(10, 2) NOT NULL,
    Quantity    INT            NOT NULL,
    Image_Path  VARCHAR(255),
    PRIMARY KEY (Product_ID)
);

INSERT INTO Product (Name, Category, Description, Price, Quantity, Image_Path)
VALUES 
('Nike Basketball', 'Basketball', 'High-quality basketball made of durable material', 2500.00, 50, 'images/basketball.jpeg'),
('Adidas Soccer Ball', 'Football', 'Official size and weight soccer ball', 2000.00, 100, 'images/soccer_ball.jpeg'),
('Wilson Tennis Racket', 'Tennis', 'Lightweight tennis racket with comfortable grip', 6000.00, 30, 'images/tennis_racket.jpeg'),
('Rawlings Baseball Glove', 'Baseball', 'Leather baseball glove for infielders', 4000.00, 40, 'images/baseball_glove.jpeg'),
('Riddell Football Helmet', 'Football', 'Certified football helmet with advanced protection', 8000.00, 20, 'images/football_helmet.jpeg'),
('Callaway Golf Clubs Set', 'Golf', 'Complete set of golf clubs for beginners', 24000.00, 10, 'images/golf_clubs.jpeg'),
('Mikasa Volleyball', 'Volleyball', 'Official size volleyball with soft touch', 1600.00, 70, 'images/volleyball.jpeg'),
('Bauer Hockey Stick', 'Hockey', 'Carbon fiber hockey stick for professional use', 8000.00, 15, 'images/hockeystick.png'),
('Gray-Nicolls Cricket Bat', 'Cricket', 'Professional-grade cricket bat made of willow', 4800.00, 25, 'images/cricket_bat.png'),
('Butterfly Table Tennis Paddle', 'Table Tennis', 'High-performance table tennis paddle with rubber grip', 1280.00, 60, 'images/table_tennis_paddle.jpeg');


INSERT INTO Customer VALUES (1, 'Shrutya', "adsish", 'abcd1@gmail.com', 'abcd1', 0);
INSERT INTO Customer VALUES (2, 'Naman', "askdn", 'abcd2@gmail.com', 'abcd2', 0);
SELECT *
from Customer;
SELECT * FROM Product

