-- creation de la table etudiants
CREATE TABLE eleve(
	identifiant SERIAL NOT NULL,
	first_name VARCHAR(30) NOT NULL,	
	last_name VARCHAR(30) NOT NULL,
	birth_date DATE NOT NULL
);
-- insertion des donnees
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('Marc','Benichou','02/11/1998');
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('Yoan','Cohen','03/12/2010');
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('Ici','Benichou','27/07/1987');
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('Amelie','Chef','07/04/1996');
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('David','Grez','14/06/2003');
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('Omer','Simpson','03/10/1980');
INSERT INTO etudiants(first_name,last_name,birth_date) VALUES('Some','Yelmani','23/02/1998');
-- Récupérer toutes les données de la table.
SELECT * FROM etudiants;
-- Récupérer tous les prénoms et noms de famille des étudiants .
SELECT first_name,last_name FROM etudiants;


