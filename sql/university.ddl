-- DDL File

drop database university;
create database university;
use university;

CREATE TABLE `university`.`student` (
  `student_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`student_id`));

CREATE TABLE `university`.`faculty` (
  `faculty_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`faculty_id`));

CREATE TABLE `university`.`admin` (
  `admin_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`admin_id`));