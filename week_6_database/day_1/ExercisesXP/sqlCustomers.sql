-- creation de la table client
CREATE TABLE customers(
id_customers SERIAL NOT NULL,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL
);
-- insertion des donnees
INSERT INTO customers(first_name,last_name) VALUES('Greg','Jones');
INSERT INTO customers(first_name,last_name) VALUES('Sandra','Jones');
INSERT INTO customers (first_name ,last_name) VALUES('Scott','Scott');
INSERT INTO customers(first_name,last_name) VALUES('Trevor','Vert');
INSERT INTO customers(first_name,last_name) VALUES('melanie','Johnson');
-- Tous les clients dont le nom de famille est « Smith » (Quel sera votre résultat ?).
SELECT last_name FROM customers WHERE last_name='Smith'
-- Tous les clients dont le nom de famille est 'Jones'.
SELECT first_name,last_name FROM customers WHERE last_name='Jones';
-- Tous les clients dont le prénom n'est pas 'Scott'.
SELECT first_name,last_name FROM customers WHERE last_name !='Scott';


