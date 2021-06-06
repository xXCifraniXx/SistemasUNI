-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema sql10415824
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sql10415824
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sql10415824` DEFAULT CHARACTER SET latin1 ;
USE `sql10415824` ;

-- -----------------------------------------------------
-- Table `sql10415824`.`sucursala`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql10415824`.`sucursala` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nProducto` TEXT NULL DEFAULT NULL,
  `cantidad` INT(11) NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 27
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `sql10415824`.`sucursalb`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql10415824`.`sucursalb` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nProducto` TEXT NULL DEFAULT NULL,
  `cantidad` INT(11) NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `sql10415824`.`sucursalc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql10415824`.`sucursalc` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nProducto` TEXT NOT NULL,
  `cantidad` INT(11) NOT NULL,
  `precio` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `sql10415824`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sql10415824`.`usuarios` (
  `usuario` INT(11) NOT NULL,
  `password` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`usuario`),
  UNIQUE INDEX `usuario_UNIQUE` (`usuario` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
