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
  
CREATE TABLE course (
	c_id VARCHAR(45) NOT NULL,
    name VARCHAR(90) NOT NULL,
    year DATE NOT NULL,
    notes VARCHAR(200) NOT NULL,
    PRIMARY KEY(c_id));
    
CREATE TABLE enroll (
	c_id VARCHAR(45) NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    grade FLOAT NOT NULL,
    notes VARCHAR(200) NOT NULL,
    PRIMARY KEY(student_id, c_id));

CREATE TABLE teaches (
	c_id VARCHAR(45) NOT NULL,
    faculty_id VARCHAR(90) NOT NULL,
    year DATE NOT NULL,
    notes VARCHAR(200) NOT NULL,
    PRIMARY KEY(faculty_id, c_id));
    
CREATE TABLE assignment (
	a_id INT UNIQUE NOT NULL auto_increment,
    faculty_id VARCHAR(90) NOT NULL,
    c_id VARCHAR(90) NOT NULL,
    created_at DATETIME,
    end_at DATETIME,
    text VARCHAR(1000),
	marks_total INT,
    files_link DATE,
    notes VARCHAR(200),
    PRIMARY KEY(a_id));
    
CREATE TABLE submission (
	a_id VARCHAR(45) NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    submission_id INT UNIQUE NOT NULL auto_increment,
    created_at DATETIME ,
    end_at DATETIME ,
    submitted_at DATETIME ,
    text VARCHAR(1000) ,
    files_link DATE ,
	marks_got INT ,
    notes VARCHAR(200) ,
    PRIMARY KEY(submission_id));