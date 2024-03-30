DROP DATABASE IF EXISTS `sql_store`;
CREATE DATABASE `sql_store`;
USE `sql_store`;

CREATE TABLE `products` (
	`barcode` int AUTO_INCREMENT,
    `product_name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(9, 2) NOT NULL,
    `quantity` INT,
	
    PRIMARY KEY (`barcode`),
    
    CHECK (`price` > 0),
    
    #Product names should be unique
    CONSTRAINT UC_Product UNIQUE(`product_name`)
);

-- STORED PROCEDURES -- 

DELIMITER $$

CREATE PROCEDURE add_new_product (IN param_productName VARCHAR(100), IN param_productPrice DECIMAL(9,2), IN param_productQuantity INT)
BEGIN
	INSERT INTO `products` (product_name, price, quantity) VALUES (param_productName, param_productPrice, param_productQuantity);
END$$

DELIMITER $$

CREATE PROCEDURE find_product(IN param_productBarcode INT, param_productName VARCHAR(100))
BEGIN
    SELECT barcode, product_name, price, quantity FROM `products` WHERE barcode = param_productBarcode OR product_name = param_productName;
END$$

DELIMITER ;


-- TRIGGERS --

DELIMITER $$

CREATE TRIGGER before_insert_products
BEFORE INSERT ON products
FOR EACH ROW
BEGIN
    IF NEW.price <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid price: Price must be greater than 0.';
    END IF;

    -- Check for uniqueness of product_name
    IF EXISTS (SELECT 1 FROM products WHERE product_name = NEW.product_name) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate product name: Product names must be unique.';
    END IF;
END$$

DELIMITER ;

-- EXEC STATEMENTS --

INSERT INTO `products` VALUES (1, 'Rose Apple 1kg', 5.99, 10);
INSERT INTO `products` VALUES (2, 'Milo Duo Cereal Family Pack', 7.99, 30) ;
INSERT INTO `products` VALUES (3, 'Anchor Butter 500g', 4.99, 200);