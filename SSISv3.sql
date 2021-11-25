-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.17-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for ssisv3
CREATE DATABASE IF NOT EXISTS `ssisv3` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ssisv3`;

-- Dumping structure for table ssisv3.college
CREATE TABLE IF NOT EXISTS `college` (
  `Code` varchar(50) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ssisv3.college: ~6 rows (approximately)
/*!40000 ALTER TABLE `college` DISABLE KEYS */;
REPLACE INTO `college` (`Code`, `Name`) VALUES
	('CASS', 'College of Arts and Social Studies'),
	('CBAA', 'College of Economics, Business and Accountancy'),
	('CCS', 'College in Computer Studies'),
	('CED', 'College of Education'),
	('COET', 'College of Engineering and Technology'),
	('CON', 'College of Nursing'),
	('CSM', 'College of Science and Mathematics');
/*!40000 ALTER TABLE `college` ENABLE KEYS */;

-- Dumping structure for table ssisv3.course
CREATE TABLE IF NOT EXISTS `course` (
  `Code` varchar(50) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `College` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  KEY `FK_course_college` (`College`),
  CONSTRAINT `FK_course_college` FOREIGN KEY (`College`) REFERENCES `college` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ssisv3.course: ~5 rows (approximately)
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
REPLACE INTO `course` (`Code`, `Name`, `College`) VALUES
	('BSCA', 'BS in Computer Application', 'CCS'),
	('BSCS', 'BS in Computer Science', 'CCS'),
	('BSIS', 'BS in Information System', 'CCS'),
	('BSIT', 'BS in Information Technology', 'CCS'),
	('BSSS', 'BS in Science and Science', 'CCS');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;

-- Dumping structure for table ssisv3.student
CREATE TABLE IF NOT EXISTS `student` (
  `ID` varchar(50) DEFAULT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `Course` varchar(50) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  `Gender` char(50) DEFAULT NULL,
  KEY `FK_student_course` (`Course`),
  CONSTRAINT `FK_student_course` FOREIGN KEY (`Course`) REFERENCES `course` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table ssisv3.student: ~3 rows (approximately)
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
REPLACE INTO `student` (`ID`, `FirstName`, `LastName`, `Course`, `Year`, `Gender`) VALUES
	('1233', 'dandasan', 'bonaparte', 'BSIT', 1, 'Male'),
	('0', 'Yu', 'Me', 'BSSS', 3, 'Female'),
	('0000-0001', 'Me', 'Yu', 'BSSS', 5, 'Male');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
