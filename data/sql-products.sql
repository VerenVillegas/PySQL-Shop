DROP DATABASE IF EXISTS `sql_store`;
CREATE DATABASE `sql_store`;
USE `sql_store`;

CREATE TABLE `products` (
	`barcode` int AUTO_INCREMENT,
    `product_name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(9, 2) NOT NULL,
    `quantity` INT,
	
    PRIMARY KEY (`barcode`),
    
    CHECK (`price` > 0)
);
INSERT INTO `products` VALUES (1, 'Rose Apple 1kg', 5.99, 10);
INSERT INTO `products` VALUES (2, 'Milo Duo Cereal Family Pack', 7.99, 30) ;
INSERT INTO `products` VALUES (3, 'Anchor Butter 500g', 4.99, 200);

DELIMITER $$

CREATE PROCEDURE add_new_product (IN param_productName VARCHAR(100), IN param_productPrice DECIMAL(9,2), IN param_productQuantity INT)
BEGIN
	INSERT INTO `products` (product_name, price, quantity) VALUES (param_productName, param_productPrice, param_productQuantity);
END$$

DELIMITER ;

CALL add_new_product('Spongecake', 8.99, 30)