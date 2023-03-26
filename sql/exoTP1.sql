-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour region_job
CREATE DATABASE IF NOT EXISTS `region_job` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `region_job`;

-- Listage de la structure de table region_job. countries
CREATE TABLE IF NOT EXISTS `countries` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Countrie_ID` char(2) NOT NULL,
  `Countrie_NAME` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table region_job. departements
CREATE TABLE IF NOT EXISTS `departements` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Departement_ID` int NOT NULL,
  `Departement_Name` varchar(30) NOT NULL,
  `Manager_ID` int DEFAULT NULL,
  `Location_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table region_job. employees
CREATE TABLE IF NOT EXISTS `employees` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Employee_ID` int NOT NULL,
  `First_Name` varchar(20) DEFAULT NULL,
  `Last_Name` varchar(25) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Phone_Number` varchar(20) DEFAULT NULL,
  `Hire_Date` date NOT NULL,
  `JOB_ID` varchar(10) NOT NULL,
  `Salary` float DEFAULT NULL,
  `Commission_PCT` float DEFAULT NULL,
  `Manager_ID` int DEFAULT NULL,
  `Departement_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table region_job. jobs
CREATE TABLE IF NOT EXISTS `jobs` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `JOB_ID` varchar(10) NOT NULL,
  `JOB_Tittle` varchar(10) DEFAULT NULL,
  `MIN_Salary` int DEFAULT NULL,
  `MAX_Salary` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table region_job. job_history
CREATE TABLE IF NOT EXISTS `job_history` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Employee_ID` int NOT NULL,
  `Start_Date` int NOT NULL,
  `End_Date` int NOT NULL,
  `JOB_ID` varchar(10) NOT NULL,
  `Departement_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table region_job. locations
CREATE TABLE IF NOT EXISTS `locations` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Location_ID` int NOT NULL,
  `Stree_Address` varchar(40) DEFAULT NULL,
  `Postal_Code` varchar(12) DEFAULT NULL,
  `City` varchar(30) NOT NULL,
  `State_Province` varchar(25) DEFAULT NULL,
  `Countrie_ID` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table region_job. region
CREATE TABLE IF NOT EXISTS `region` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Region_ID` int NOT NULL DEFAULT '0',
  `Region_NAME` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Les données exportées n'étaient pas sélectionnées.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
