DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;

CREATE TABLE users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(75) NOT NULL UNIQUE,
    company_name VARCHAR(50) NULL,
    address1 VARCHAR(45) NOT NULL,
    address2 VARCHAR(45) NULL,
    city VARCHAR(45) NOT NULL,
    state VARCHAR(45) NOT NULL,
    zip_code VARCHAR(5) NOT NULL,
    country VARCHAR(45) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    customer_status VARCHAR(8) NOT NULL
);

CREATE TABLE products (
    productId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    product VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
