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
CREATE TABLE IF NOT EXISTS Cart (
    Customer_ID INT NOT NULL,
    Product_ID INT NOT NULL,
    Quantity INT NOT NULL DEFAULT 1,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);


CREATE TABLE IF NOT EXISTS check_blocked(
        Customer_ID INT NOT NULL,
        blocked BOOL NOT NULL DEFAULT FALSE,
        PRIMARY KEY (Customer_ID)
);



INSERT INTO Product (Name, Category, Description, Price, Quantity, Image_Path)
VALUES
('Nike Basketball', 'Basketball', 'High-quality basketball made of durable material', 2500.00, 50, 'images/basketball.jpeg'),
('Adidas Soccer Ball', 'Football', 'Official size and weight soccer ball', 2000.00, 100, 'images/soccer_ball.jpeg'),
('Wilson Tennis Racket', 'Tennis', 'Lightweight tennis racket with comfortable grip', 6000.00, 30, 'images/tennis_racket.jpeg'),
('Novak Tennis Racket', 'Tennis', 'Lightweight tennis racket with comfortable grip', 7000.00, 30, 'images/tennis_racket.jpeg'),
('Rawlings Baseball Glove', 'Baseball', 'Leather baseball glove for infielders', 4000.00, 40, 'images/baseball_glove.jpeg'),
('Riddell Football Helmet', 'Football', 'Certified football helmet with advanced protection', 8000.00, 20, 'images/football_helmet.jpeg'),
('Callaway Golf Clubs Set', 'Golf', 'Complete set of golf clubs for beginners', 24000.00, 10, 'images/golf_clubs.jpeg'),
('Mikasa Volleyball', 'Volleyball', 'Official size volleyball with soft touch', 1600.00, 70, 'images/volleyball.jpeg'),
('Bauer Hockey Stick', 'Hockey', 'Carbon fiber hockey stick for professional use', 8000.00, 15, 'images/hockeystick.png'),
('Gray-Nicolls Cricket Bat', 'Cricket', 'Professional-grade cricket bat made of willow', 4800.00, 25, 'images/cricket_bat.png'),
('Butterfly Table Tennis Paddle', 'Table Tennis', 'High-performance table tennis paddle with rubber grip', 1280.00, 60, 'images/table_tennis_paddle.jpeg'),
('High-tech Table Tennis Paddle', 'Table Tennis', 'High-performance table tennis paddle with rubber grip', 2280.00, 60, 'images/tt2.jpg'),
('Table Tennis table', 'Table Tennis', 'High-performance table tennis paddle with rubber grip', 10080.00, 60, 'images/tt3.jpg'),
('Skiing bag', 'Skiing', 'Large capacity skiing bag for all your essentials', 1280.00, 60, 'images/bag.jpg'),
('Skiing bag', 'Skiing', 'Large capacity skiing bag for all your essentials', 2280.00, 60, 'images/skiing2.jpg'),
('Skiing Shoes', 'Skiing', '', 3000.00, 60, 'images/skiing.jpg'),
('Wilson Basketball', 'Basketball', 'High-quality basketball made of durable material', 2500.00, 50, 'images/basketball.jpeg'),
('Chess Box', 'Chess', 'High Quality chess box made out of wood', 600.00, 60, 'images/chess.jpg'),
('Chess Box', 'Chess', 'High Quality chess box made out of wood', 700.00, 60, 'images/chess2.jpg'),
('Gym tshirt', 'Sport Apparels', 'Stay dry!', 780.00, 60, 'images/cloth1.jpg'),
('Gym tshirt', 'Sport Apparels', 'Stay dry!', 880.00, 60, 'images/cloth.jpg'),
('Chest fly machine', 'Gym Equipments', 'Has weight variations from 10kg to 50kg', 10080.00, 60, 'images/gym1.jpg'),
('Dumbelss Set', 'Gym Equipments', 'Available from 10kg to 100kg', 15000.00, 60, 'images/gym2.jpg'),
('Gym bicycle', 'Gym Equipments', 'Build some great legs with this', 10080.00, 60, 'images/gym3.jpg'),
('Barbell', 'Gym Equipments', 'For Chest Press', 5080.00, 60, 'images/gym4.jpg'),
('Rugby Ball', 'Rugby', '', 1280.00, 60, 'images/rr.jpg'),
('Rugby Helmet', 'Rugby', '', 1280.00, 60, 'images/rugby2.jpg'),
('Running Shoes', 'Running', '', 2000.00, 60, 'images/running.jpg'),
('Running Watch', 'Running', '', 5000.00, 60, 'images/running2.jpg'),
('Swimming goggles', 'Swimming', '', 1000.00, 60, 'images/swimming.jpg');


INSERT INTO Customer VALUES (1, 'Shrutya', "adsish", 'abcd1@gmail.com', 'abcd1', 0);
INSERT INTO Customer VALUES (2, 'Naman', "askdn", 'abcd2@gmail.com', 'abcd2', 0);
SELECT *
from Customer;
SELECT * FROM Product
