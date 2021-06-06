-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema inventario
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema inventario
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `inventario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `inventario` ;

-- -----------------------------------------------------
-- Table `inventario`.`sucursala`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`sucursala` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nProducto` TEXT NULL DEFAULT NULL,
  `cantidad` INT NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`sucursalb`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`sucursalb` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nProducto` TEXT NULL DEFAULT NULL,
  `cantidad` INT NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`sucursalc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`sucursalc` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nProducto` TEXT NOT NULL,
  `cantidad` INT NOT NULL,
  `precio` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `inventario`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventario`.`usuarios` (
  `usuario` INT NOT NULL,
  `password` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`usuario`),
  UNIQUE INDEX `usuario_UNIQUE` (`usuario` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
