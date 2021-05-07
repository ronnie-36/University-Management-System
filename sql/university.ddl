-- DDL File

drop database university;
create database university;
use university;

CREATE TABLE `university`.`student` (
  `student_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `emailid` VARCHAR(90) NOT NULL,
  `address` VARCHAR(200),
  `DOB` DATE DEFAULT '2001-08-28',
  `password` VARCHAR(90) NOT NULL,
  sem INT DEFAULT 1,
  cpi FLOAT DEFAULT 0.00,
  branch VARCHAR(5),
  PRIMARY KEY (`student_id`));

CREATE TABLE `university`.`faculty` (
  `faculty_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `address` VARCHAR(200),
  `DOB` DATE DEFAULT '2001-08-28',
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

-- this is the current years courses, stores years
CREATE TABLE section (
	sec_id INT NOT NULL auto_increment,
	c_id VARCHAR(45) NOT NULL,
    year VARCHAR(11) DEFAULT '2021',
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY section(c_id) references course(c_id),
    PRIMARY KEY(sec_id));

CREATE TABLE enroll (
	sec_id INT NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    grade FLOAT NOT NULL,
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY enroll(sec_id) references section(sec_id),
    FOREIGN KEY enroll(student_id) references student(student_id),
    PRIMARY KEY(student_id, sec_id));

CREATE TABLE teaches (
	c_id VARCHAR(45) NOT NULL,
    faculty_id VARCHAR(90) NOT NULL,
    year DATE NOT NULL,
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY teaches(c_id) references course(c_id),
    FOREIGN KEY teaches(faculty_id) references faculty(faculty_id),
    PRIMARY KEY(faculty_id, c_id));
    
CREATE TABLE assignment (
	a_id INT UNIQUE NOT NULL auto_increment,
    faculty_id VARCHAR(90) NOT NULL,
	c_id VARCHAR(45) NOT NULL,
    created_at DATETIME,
    end_at DATETIME,
    text VARCHAR(1000),
	marks_total INT,
    files_link DATE,
    notes VARCHAR(200),
    FOREIGN KEY (faculty_id) references faculty(faculty_id),
    FOREIGN KEY (c_id) references course(c_id),
    PRIMARY KEY(a_id));
    
CREATE TABLE submission (
	a_id INT NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    submission_id INT UNIQUE NOT NULL auto_increment,
    created_at DATETIME ,
    end_at DATETIME ,
    submitted_at DATETIME ,
    text VARCHAR(1000) ,
    files_link DATE ,
	marks_got INT ,
    notes VARCHAR(200) ,
    FOREIGN KEY (a_id) references assignment(a_id),
    FOREIGN KEY (student_id) references student(student_id),
    PRIMARY KEY(submission_id));