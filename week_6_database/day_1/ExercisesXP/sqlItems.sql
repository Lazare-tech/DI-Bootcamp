-- creation de la tablle
CREATE TABLE items(
id_items SERIAL NOT NULL,
nom VARCHAR(30) NOT NULL,
prix INT NOT NULL
);
-- Insertion des donnees
INSERT INTO items(nom,prix) VALUES('Petit bureau',100);
INSERT INTO items(nom,prix) VALUES('Grand bureau',300);
INSERT INTO items(nom,prix) VALUES('Ventilateur',80);
-- //recuperation de tous les articles
SELECT * FROM items;
-- Tous les articles dont le prix est supérieur à 80 (80 non inclus).
SELECT * FROM items WHERE prix>80;
-- Tous les articles dont le prix est inférieur à 300. (300 inclus)
SELECT * FROM items WHERE prix>=300;

