--CREATE DATABASE carsales;

--DROP DATABASE IF EXISTS carsales;
CREATE DATABASE carsales;
\c carsales
CREATE TABLE IF NOT EXISTS transactions (
  id serial PRIMARY KEY,
  sales_date DATE NOT NULL,
  quantity INT NOT NULL,
  customer_id INT NOT NULL,
  car_id INT NOT NULL,
  salesperson_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS cars (
id serial PRIMARY KEY,
manufacturer VARCHAR(100) NOT NULL,
model_name VARCHAR(255),
serial_number VARCHAR(255),
weight VARCHAR(50),
price NUMERIC(15,6) NOT NULL

);

CREATE TABLE IF NOT EXISTS customers (
id serial PRIMARY KEY,
phone_number VARCHAR(100),
email VARCHAR(255),
created_on timestamp NOT NULL
);


CREATE TABLE IF NOT EXISTS salespersons (
  id serial PRIMARY KEY,
  name VARCHAR(255),
  phone_number VARCHAR(100),
  email VARCHAR(255),
  date_joined DATE NOT NULL,
  create_on timestamp
)


-- SELECT c.name, SUM(t.price)
-- from transactions t
-- group by customer_id
-- LEFT JOIN customers c
-- ON t.customer_id = c.id
--
--
-- SELECT
