# Initial Data
-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.19 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping data for table o_bloodbank.bloodtypes: ~0 rows (approximately)
DELETE FROM `bloodtypes`;
/*!40000 ALTER TABLE `bloodtypes` DISABLE KEYS */;
INSERT INTO `bloodtypes` (`id`, `name`, `milliliters_available`) VALUES
	(1, '0-', 0),
	(2, '0+', 0),
	(3, 'A-', 0),
	(4, 'A+', 0),
	(5, 'B-', 0),
	(6, 'B+', 0),
	(7, 'AB-', 0),
	(8, 'AB+', 0);
/*!40000 ALTER TABLE `bloodtypes` ENABLE KEYS */;


/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
