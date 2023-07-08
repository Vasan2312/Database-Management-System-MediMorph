SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `mydb` ;

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

DROP TABLE IF EXISTS `mydb`.`patient` ;

CREATE TABLE IF NOT EXISTS `mydb`.`patient` (
  `user_id` INT NOT NULL,
  `first_name` VARCHAR(20) NOT NULL,
  `middle_name` VARCHAR(20) NULL,
  `last_name` VARCHAR(20) NOT NULL,
  `city` VARCHAR(40) NOT NULL,
  `state` VARCHAR(20) NOT NULL,
  `p_gender` VARCHAR(20) NOT NULL,
  `p_age` INT NOT NULL,
  `p_phone_number` VARCHAR(30) NOT NULL,
  `p_date_joined` VARCHAR(20) NOT NULL,
  `p_email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb`.`phone_number` ;

CREATE TABLE IF NOT EXISTS `mydb`.`phone_number` (
  `user_id` INT NOT NULL,
  `p_phone_number` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`user_id`, `p_phone_number`),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`patient` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb`.`management` ;

CREATE TABLE IF NOT EXISTS `mydb`.`management` (
  `employee_id` INT NOT NULL,
  `employee_name` VARCHAR(30) NOT NULL,
  `employee_shift` VARCHAR(10) NOT NULL,
  `employee_phone` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`employee_id`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb`.`Supplier` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Supplier` (
  `supplier_id` INT NOT NULL,
  `s_delivery_charge` DOUBLE NOT NULL,
  `s_delivery_time` INT NOT NULL,
  `s_location` VARCHAR(45) NOT NULL,
  `s_prices` DOUBLE NOT NULL,
  `employee_id` INT NULL,
  PRIMARY KEY (`supplier_id`),
  INDEX `employee_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `employee`
    FOREIGN KEY (`employee_id`)
    REFERENCES `mydb`.`management` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb`.`Medicine` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Medicine` (
  `medicine_id` INT NOT NULL,
  `m_storage_temp` INT NOT NULL,
  `m_concentration` DOUBLE NOT NULL,
  `m_name` VARCHAR(45) NULL,
  `m_price` DOUBLE NOT NULL,
  `m_expiry_data` VARCHAR(45) NOT NULL,
  `m_recommended_dosage` INT NOT NULL,
  `m_quantity` INT NOT NULL,
  `supplier_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`medicine_id`),
  INDEX `supplier_idx` (`supplier_id` ASC) VISIBLE,
  INDEX `emplo_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `supplier`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `mydb`.`Supplier` (`supplier_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `emplo`
    FOREIGN KEY (`employee_id`)
    REFERENCES `mydb`.`management` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`Get Lab Tests` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Get Lab Tests` (
  `get_lab_test_id` INT NOT NULL,
  `glt_time` VARCHAR(45) NOT NULL,
  `glt_location` VARCHAR(20) NOT NULL,
  `glt_fasting_time` INT NULL,
  `glt_type` VARCHAR(30) NOT NULL,
  `glt_data` VARCHAR(45) NULL,
  `glt_mode` VARCHAR(10) NOT NULL,
  `glt_cost` DOUBLE NOT NULL,
  PRIMARY KEY (`get_lab_test_id`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `mydb`.`employee_phone` ;

CREATE TABLE IF NOT EXISTS `mydb`.`employee_phone` (
  `employee_id` INT NOT NULL,
  `employee_phone_number` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`employee_id`, `employee_phone_number`),
  CONSTRAINT `employee_id`
    FOREIGN KEY (`employee_id`)
    REFERENCES `mydb`.`management` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`Doctor` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Doctor` (
  `doctor_id` INT NOT NULL,
  `d_name` VARCHAR(20) NOT NULL,
  `d_fees` DOUBLE NOT NULL,
  `d_qualification` VARCHAR(20) NOT NULL,
  `d_experience` INT NOT NULL,
  `d_address` VARCHAR(45) NOT NULL,
  `mode` VARCHAR(20) NOT NULL,
  `timings` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`doctor_id`))
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`other_institution` ;

CREATE TABLE IF NOT EXISTS `mydb`.`other_institution` (
  `other_user_id` INT NOT NULL,
  `other_user_affiliation` VARCHAR(45) NULL,
  PRIMARY KEY (`other_user_id`))
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`doctor_cart` ;

CREATE TABLE IF NOT EXISTS `mydb`.`doctor_cart` (
  `user_id` INT NOT NULL,
  `doctor_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `doctor_id`),
  INDEX `doctor_id_idx` (`doctor_id` ASC) VISIBLE,
  CONSTRAINT `user_id(1)`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`patient` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `doctor_id(1)`
    FOREIGN KEY (`doctor_id`)
    REFERENCES `mydb`.`Doctor` (`doctor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`medicine_id` ;

CREATE TABLE IF NOT EXISTS `mydb`.`medicine_id` (
  `medicine_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `quantity` INT NULL,
  PRIMARY KEY (`user_id`, `medicine_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `medicine_id(1)`
    FOREIGN KEY (`medicine_id`)
    REFERENCES `mydb`.`Medicine` (`medicine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `user_id(2)`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`patient` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`lab_cart` ;

CREATE TABLE IF NOT EXISTS `mydb`.`lab_cart` (
  `get_lab_test_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `l_quantity` INT NULL,
  PRIMARY KEY (`user_id`, `get_lab_test_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id(4)`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`patient` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `get_lab_test_id(1)`
    FOREIGN KEY (`get_lab_test_id`)
    REFERENCES `mydb`.`Get Lab Tests` (`get_lab_test_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS `mydb`.`Order_History` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Order_History` (
  `user_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  `type` VARCHAR(45) NULL,
  `quantity` INT NULL,
  `identifying_id` INT NULL,
  PRIMARY KEY (`order_id`),
  CONSTRAINT `user_iid`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`patient` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TRIGGER IF EXISTS trigger1;

CREATE TRIGGER trigger1
BEFORE INSERT ON medicine
FOR EACH ROW
BEGIN
    IF NEW.m_quantity >= 100 THEN
        SET NEW.m_price = NEW.m_price * 0.5;
    END IF;
END;


DROP TRIGGER IF EXISTS trigger2;
CREATE TRIGGER trigger2
BEFORE INSERT ON supplier
FOR EACH ROW
BEGIN
IF NEW.s_delivery_time>=5 THEN
        IF NEW.s_prices>300 THEN
SET NEW.s_prices = 300;
END IF;
END IF;
END;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;