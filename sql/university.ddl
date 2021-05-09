-- DDL File

drop database university;
create database university;
use university;

CREATE TABLE program (
	name VARCHAR(100) NOT NULL,
    duration INT NOT NULL,
    PRIMARY KEY(name)
);

CREATE TABLE `university`.`faculty` (
  `faculty_id` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(90) NOT NULL,
  `last_name` VARCHAR(90) DEFAULT '',
  `address` VARCHAR(200),
  `phone` VARCHAR(10),
  `gender` VARCHAR(10) DEFAULT 'Male',
  `DOB` DATE DEFAULT '2001-08-28',
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  salary INT NOT NULL,
  research_interests VARCHAR(200) NULL,
  position VARCHAR(90) NOT NULL,
  PRIMARY KEY (`faculty_id`));

CREATE TABLE department (
	dept_id VARCHAR(45) NOT NULL,
    name VARCHAR(200) NOT NULL,
    budget INT DEFAULT 0,
    hod_id VARCHAR(45) NOT NULL,
    contact_no VARCHAR(45) NOT NULL,
    foreign key department(hod_id) references faculty(faculty_id) on update cascade on delete cascade,
    PRIMARY KEY(dept_id)
); 

CREATE TABLE course (
	c_id VARCHAR(45) NOT NULL,
    name VARCHAR(90) NOT NULL,
    description VARCHAR(200) NULL,
    syllabus VARCHAR(700) NULL,
    credits VARCHAR(45) NOT NULL,
    year DATE NOT NULL,
    notes VARCHAR(200) NOT NULL,
    PRIMARY KEY(c_id));


-- this is the current years courses, stores years
CREATE TABLE section (
	sec_id INT NOT NULL auto_increment,
	c_id VARCHAR(45) NOT NULL,
    year VARCHAR(11) DEFAULT '2021',
    sem VARCHAR(45) NOT NULL,
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY section(c_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(sec_id));

CREATE TABLE `university`.`student` (
  `student_id` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(90) NOT NULL,
  `last_name` VARCHAR(90),
  `emailid` VARCHAR(90),
  `address` VARCHAR(200),
  `gender` VARCHAR(10) DEFAULT 'Male',
  `phone` VARCHAR(10),
  `DOB` DATE DEFAULT '2001-08-28',
  `password` VARCHAR(90) NOT NULL,
  sem INT DEFAULT 1,
  cpi FLOAT DEFAULT 0.00,
  branch VARCHAR(45) NOT NULL,
  program VARCHAR(100) DEFAULT 'btech',
  advisor_id VARCHAR(45),
  TAsec_id INT,
  CONSTRAINT advisor foreign key student(advisor_id) references faculty(faculty_id) on update cascade on delete cascade,
  CONSTRAINT stud_prog foreign key student(program) references program(name) on update cascade on delete cascade,
  CONSTRAINT stud_dept foreign key student(branch) references department(dept_id) on update cascade on delete cascade,
  CONSTRAINT sec_ta foreign key student(TAsec_id) references section(sec_id) on update cascade on delete cascade,
  PRIMARY KEY (`student_id`));

CREATE TABLE `university`.`admin` (
  `admin_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(90) NOT NULL,
  `emailid` VARCHAR(90) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`admin_id`));
  
CREATE TABLE enroll (
	sec_id INT NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    grade FLOAT NOT NULL,
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY enroll(sec_id) references section(sec_id) on update cascade on delete cascade,
    FOREIGN KEY enroll(student_id) references student(student_id) on update cascade on delete cascade,
    PRIMARY KEY(student_id, sec_id));

CREATE TABLE teaches (
	sec_id INT NOT NULL,
    faculty_id VARCHAR(90) NOT NULL,
    year DATE NOT NULL,
    notes VARCHAR(200) NOT NULL,
    FOREIGN KEY teaches(sec_id) references section(sec_id) on update cascade on delete cascade,
    FOREIGN KEY teaches(faculty_id) references faculty(faculty_id) on update cascade on delete cascade,
    PRIMARY KEY(faculty_id, sec_id));
    
CREATE TABLE assignment (
	a_id INT UNIQUE NOT NULL auto_increment,
    faculty_id VARCHAR(90) NOT NULL,
	sec_id INT NOT NULL,
    created_at DATETIME,
    start_at DATETIME,
    end_at DATETIME,
    text VARCHAR(1000),
	marks_total INT,
    files_link VARCHAR(150),
    notes VARCHAR(200),
    FOREIGN KEY (faculty_id) references faculty(faculty_id) on update cascade on delete cascade,
    FOREIGN KEY (sec_id) references section(sec_id) on update cascade on delete cascade,
    PRIMARY KEY(a_id));
    
-- This is student assg in ER
CREATE TABLE submission (
	a_id INT NOT NULL,
    student_id VARCHAR(90) NOT NULL,
    submission_id INT UNIQUE NOT NULL auto_increment,
    submitted_at DATETIME ,
    text VARCHAR(1000) ,
    files_link VARCHAR(150) ,
	marks_got INT ,
    notes VARCHAR(200) ,
    FOREIGN KEY (a_id) references assignment(a_id) on update cascade on delete cascade,
    FOREIGN KEY (student_id) references student(student_id) on update cascade on delete cascade,
    PRIMARY KEY(submission_id));

CREATE TABLE has_course(
	program VARCHAR(100),
	c_id VARCHAR(45) NOT NULL,
    sem INT DEFAULT 1,
    branch VARCHAR(100) DEFAULT 'cse',
    foreign key has_course(program) references program(name) on update cascade on delete cascade,
    foreign key has_course(c_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(program, c_id)
);

CREATE TABLE final_grade(
	student_id VARCHAR(90) NOT NULL,
    c_id VARCHAR(45) NOT NULL,
    grades FLOAT DEFAULT 0.00,
    foreign key final_course(student_id) references student(student_id) on update cascade on delete cascade,
    foreign key final_course(c_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(student_id, c_id)
);

CREATE TABLE classroom(
	class_id varchar(45) NOT NULL,
    building varchar(90) NOT NULL,
    capacity INT NOT NULL,
    roomno VARCHAR(45) NOT NULL,
    PRIMARY KEY (class_id)
);

CREATE TABLE section_room(
	sec_id INT NOT NULL,
    class_id VARCHAR(45) NOT NULL,
    start_time INT NOT NULL,
    end_time INT NOT NULL,
    day INT NOT NULL,
	foreign key section_room(sec_id) references section(sec_id) on update cascade on delete cascade,
    foreign key section_room(class_id) references classroom(class_id) on update cascade on delete cascade,
    PRIMARY KEY (sec_id, class_id)
);

CREATE TABLE works(
	faculty_id VARCHAR(90) NOT NULL,
    dept_id VARCHAR(45) NOT NULL,
    role VARCHAR(200) DEFAULT "faculty",
	foreign key works(faculty_id) references faculty(faculty_id) on update cascade on delete cascade,
    foreign key works(dept_id) references department(dept_id) on update cascade on delete cascade,
    PRIMARY KEY(faculty_id, dept_id)
);

CREATE TABLE offer_course (
	c_id VARCHAR(45) NOT NULL,
    dept_id VARCHAR(45) NOT NULL,
    notes VARCHAR(45),
    foreign key offer_course(c_id) references course(c_id) on update cascade on delete cascade,
    foreign key offer_course(dept_id) references department(dept_id) on update cascade on delete cascade,
    PRIMARY KEY(c_id, dept_id)
);

CREATE TABLE has_program (
	program VARCHAR(100) NOT NULL,
    dept_id VARCHAR(45) NOT NULL,
    notes VARCHAR(45),
    foreign key has_program(program) references program(name) on update cascade on delete cascade,
    foreign key has_program(dept_id) references department(dept_id) on update cascade on delete cascade,
    PRIMARY KEY(program, dept_id)
);

CREATE TABLE requires (
	prereq_id VARCHAR(45) NOT NULL,
    maincourse_id VARCHAR(45) NOT NULL,
    notes VARCHAR(45),
    foreign key requires(prereq_id) references course(c_id) on update cascade on delete cascade,
    foreign key requires(maincourse_id) references course(c_id) on update cascade on delete cascade,
    PRIMARY KEY(prereq_id, maincourse_id)
);
