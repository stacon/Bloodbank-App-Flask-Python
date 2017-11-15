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


-- Dumping database structure for o_bloodbank
DROP DATABASE IF EXISTS `o_bloodbank`;
CREATE DATABASE IF NOT EXISTS `o_bloodbank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `o_bloodbank`;

-- Dumping structure for table o_bloodbank.bloodtypes
DROP TABLE IF EXISTS `bloodtypes`;
CREATE TABLE IF NOT EXISTS `bloodtypes` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(3) COLLATE utf8mb4_bin NOT NULL,
  `milliliters_available` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Data exporting was unselected.
-- Dumping structure for table o_bloodbank.donors
DROP TABLE IF EXISTS `donors`;
CREATE TABLE IF NOT EXISTS `donors` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `gender` char(3) COLLATE utf8mb4_bin NOT NULL COMMENT 'values can be ''M'' = male, ''F'' = female, ''TXM'' = Transgender ex male, ''TXF'' = Transgender ex female',
  `dob` date NOT NULL,
  `bloodtype_id` int(10) unsigned DEFAULT NULL,
  `address` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `city` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `state` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `zip_code` varchar(7) COLLATE utf8mb4_bin NOT NULL,
  `contact_number` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `milliliters_deposited` int(4) unsigned DEFAULT '0',
  `milliliters_withdrawn` int(4) unsigned DEFAULT '0',
  `soft_deleted` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bloodtype_foreign_key` (`bloodtype_id`),
  CONSTRAINT `bloodtype_foreign_key` FOREIGN KEY (`bloodtype_id`) REFERENCES `bloodtypes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Data exporting was unselected.
-- Dumping structure for table o_bloodbank.transactions
DROP TABLE IF EXISTS `transactions`;
CREATE TABLE IF NOT EXISTS `transactions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `donor_id` int(10) unsigned NOT NULL,
  `transaction_type` char(1) COLLATE utf8mb4_bin NOT NULL COMMENT '''D'' = deposit, ''W'' = withdrawal',
  `bloodtype_id` int(10) unsigned NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `soft_deleted` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_donor_id` (`donor_id`),
  KEY `fk_bloodtype_id` (`bloodtype_id`),
  CONSTRAINT `fk_bloodtype_id` FOREIGN KEY (`bloodtype_id`) REFERENCES `bloodtypes` (`id`),
  CONSTRAINT `fk_donor_id` FOREIGN KEY (`donor_id`) REFERENCES `donors` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Data exporting was unselected.
-- Dumping structure for table o_bloodbank.users
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(15) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(80) COLLATE utf8mb4_bin NOT NULL,
  `priviledges_level` int(3) unsigned NOT NULL DEFAULT '1',
  `soft_deleted` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
