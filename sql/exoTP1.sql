CREATE TABLE Departements (
	 ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	 Departement_ID INT NOT NULL,
	 Departement_Name VARCHAR(30) NOT NULL,
	 Manager_ID INT,
	 Location_ID INT
);