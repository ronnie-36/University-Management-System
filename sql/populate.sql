-- Insert valid emails accordingly for testing forgot password

INSERT INTO program (name,duration) VALUES ('btech',4);
INSERT INTO program (name,duration) VALUES ('mtech',2);
INSERT INTO program (name,duration) VALUES ('ms',2);
INSERT INTO program (name,duration) VALUES ('phd',6);
INSERT INTO program (name,duration) VALUES ('bsc',4);
INSERT INTO program (name,duration) VALUES ('msc',2);
INSERT INTO program (name,duration) VALUES ('mba',2);

INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('1', 'Shaan', 'sh@sh.com', '81dc9bdb52d04dc20036dbd8313ed055', '02-gandhi-marg new-delhi', '1980-12-30', 80000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('2', 'Rohan', 'rr@trr.com', '81dc9bdb52d04dc20036dbd8313ed055', '02-Hauz-Khas new-delhi', '1965-12-30', 85000, 'Assistant Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('3', 'Mohan', 'sha@sh.com', '81dc9bdb52d04dc20036dbd8313ed055', '082-gandhi-marg new-delhi', '1990-12-30', 90000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('4', 'Sohan', 'rar@trr.com', '81dc9bdb52d04dc20036dbd8313ed055', '012-Hauz-Khas new-delhi', '1975-12-07', 80000, 'Associate Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('5', 'Soham', 'shm@trr.com', '81dc9bdb52d04dc134236dbd8313ed055', '21-ranjit-nagar new-delhi', '1995-12-07', 60000, 'Associate Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('6', 'Ram', 'rm@trr.com', '81dc9bdb52d023424bd8313ed055', '211-dugri- new-delhi', '1976-12-07', 80000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('7', 'Dinesh', 'dnsh@trr.com', '81dc9bdb234244dc20036dbd8313ed055', '32-old-delhi new-delhi', '1985-12-07', 85000, 'Professor');
INSERT INTO `faculty` (`faculty_id`, `first_name`, `emailid`, `password`, `address`, `DOB`, salary, position) VALUES ('8', 'Archana', 'rch@trr.com', '81dc9bdb5223424dc20036dbd8313ed055', '221-ansal-plaze new-delhi', '1978-12-07', 65000, 'Associate Professor');

INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('cse','Computer Science and Engineering',120000,'1','98765');
INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('mech','Mechanical Engineering',120000,'2','98765');
INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('ee','Electrical Engineering',120000,'3','98765');
INSERT INTO department (dept_id, name, budget, hod_id, contact_no) VALUES ('ce','Civil Engineering',120000,'4','98765');

INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('1','MATHS',"2001-12-30","",3,'3-1-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('2','OS',"2006-06-24","",3,'2-1-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('3','DSA',"2006-06-24","",4,'4-0-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('4','Software Engg',"2009-01-30","",1.50,'3-1-0');
INSERT INTO course (c_id, name, year, notes, credits, hours) VALUES ('5','IC211',"2009-01-01","",3,'3-0-0');

INSERT INTO section (c_id, year, notes, sem) VALUES ('1',"2009","",'4');
INSERT INTO section (c_id, year, notes, sem) VALUES ('1',"2021","",'2');
INSERT INTO section (c_id, year, notes, sem) VALUES ('2',"2020","",'4');
INSERT INTO section (c_id, year, notes, sem) VALUES ('3',"2009","",'4');
INSERT INTO section (c_id, year, notes, sem) VALUES ('4',"2009","",'1');
INSERT INTO section (c_id, year, notes, sem) VALUES ('3',"2009","",'1');
INSERT INTO section (c_id, year, notes, sem) VALUES ('4',"2009","",'2');

INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('1', 'ron', 'ron@ron.com', '81dc9bdb52d04dc20036dbd8313ed055', '100-england', '2001-01-01', 'cse', '4', '9.80','btech','1');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('2', 'Ganguly', 'Ganguly@Ganguly.com', '81dc9bdb52d04dc20036dbd8313ed055', '100-london', '2004-02-21', 'cse', '2', '7.80','btech','2');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('3', 'sachin', 'sachin@sachin.com', '81dc2343rffergd433vgrsf13ed055', '100-london', '2004-02-01', 'mech', '2', '7.85','btech','2');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('4', 'virat', 'virat@virat.com', '81dcfdghdfhrertewrtv6dbd8313ed055', '103-avon', '2005-04-21', 'ee', '3', '9.80','btech','3');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('5', 'sundar', 'sundar@sundar.com', '8dsghdfghfghc20036dbd8313ed055', '6-ropar', '2004-06-23', 'cse', '3', '8.80','btech','3');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('6', 'hina', 'hina@hina.com', '81dc9bdb52d0rwqerwdbd8313ed055', '69-delhi', '2003-09-26', 'cse', '2', '7.81','btech','4');
INSERT INTO `student` (`student_id`, `first_name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`, `program`, advisor_id) VALUES ('7', 'ritu', 'ritu@Gritu.com', '81dc9bdb52d04dc2gdgdf6dbd8313ed055', '71-ldh', '2003-01-27', 'ce', '2', '7.00','btech','4');


INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('1', 'sqyw', 'sqyw@sqyw.com', '81dc9bdb52d04dc20036dbd8313ed055', 'acad');
INSERT INTO `admin` (`admin_id`, `name`, `emailid`, `password`, role) VALUES ('2', 'qwsr', 'qwsr@qwsr.com', '81dc9bdb52d04dc20036dbd8313ed055', 'acad');


INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','1',9.50,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','2',8.50,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','1',4.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('2','1',10.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','2',9.00,"");

INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('1','1',"2006-06-01","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('1','2',"2006-07-28","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('2','3',"2006-06-01","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('1','4',"2009-12-30","");
INSERT INTO teaches (faculty_id, sec_id, year, notes) VALUES ('2','2',"2010-01-30","");

INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total) VALUES ('1','1',NOW(),DATE_ADD(NOW(), INTERVAL 3 HOUR), NOW() + INTERVAL 1 DAY, 'Sort an array in O(n) using radix sort', '30');
INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total) VALUES ('2','1',NOW() - INTERVAL 3 DAY, NOW() - INTERVAL 2 DAY,NOW() - INTERVAL 1 DAY, 'reverse an array in O(n)', '10');
INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total) VALUES ('2','1',NOW()- INTERVAL 2 DAY,DATE_ADD(NOW(), INTERVAL 1 HOUR), DATE_ADD(NOW(), INTERVAL 3 HOUR), 'End semester exam', '60');
INSERT INTO assignment (sec_id, faculty_id, created_at, start_at, end_at, text, marks_total) VALUES ('3','2',NOW()- INTERVAL 1 DAY,DATE_ADD(NOW(), INTERVAL 0 HOUR), DATE_ADD(NOW(), INTERVAL 3 HOUR), 'End semester exam', '100');

INSERT INTO submission (a_id, student_id, submitted_at, text, marks_got) VALUES ('1','1', DATE_ADD(NOW(), INTERVAL 3 HOUR),'answer 1 text', '30');
INSERT INTO submission (a_id, student_id, submitted_at, text, marks_got) VALUES ('2','1', DATE_ADD(NOW(), INTERVAL 1 HOUR),'answer 2 text', '10');
INSERT INTO submission (a_id, student_id, submitted_at, text, marks_got) VALUES ('2','2', DATE_ADD(NOW(), INTERVAL 3 HOUR),'answer 2 text', '5');

INSERT INTO has_course (program, c_id, sem, branch) VALUES ('btech','1',4,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('btech','2',2,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('btech','3',4,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('phd','2',4,'cse');
INSERT INTO has_course (program, c_id, sem, branch) VALUES ('mtech','2',2,'cse');

INSERT INTO final_grade (student_id, c_id, grades) VALUES ('1','1','8.00');
INSERT INTO final_grade (student_id, c_id, grades) VALUES ('1','2','4.00');
INSERT INTO final_grade (student_id, c_id, grades) VALUES ('2','3','5.00');
INSERT INTO final_grade (student_id, c_id, grades) VALUES ('2','1','10.00');

INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('1','L01','a',200);
INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('2','C03','b',80);
INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('3','L04','c',100);
INSERT INTO classroom (class_id, roomno, building, capacity) VALUES ('4','L02','d',90);

INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('1','1',7,8,1);
INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('1','2',13,14,5);
INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('2','2',7,9,2);
INSERT INTO section_room(sec_id, class_id, start_time, end_time, day) VALUES ('3','3',10,12,4);

INSERT INTO works (faculty_id, dept_id) VALUES ('1','cse');
INSERT INTO works (faculty_id, dept_id) VALUES ('2','ee');
INSERT INTO works (faculty_id, dept_id) VALUES ('3','ce');
INSERT INTO works (faculty_id, dept_id) VALUES ('4','cse');

INSERT INTO offer_course (dept_id, c_id) VALUES ('cse','1');
INSERT INTO offer_course (dept_id, c_id) VALUES ('cse','2');
INSERT INTO offer_course (dept_id, c_id) VALUES ('cse','3');
INSERT INTO offer_course (dept_id, c_id) VALUES ('ee','3');

INSERT INTO has_program (program, dept_id) VALUES ('btech','cse');
INSERT INTO has_program (program, dept_id) VALUES ('btech','ee');
INSERT INTO has_program (program, dept_id) VALUES ('btech','ce');
INSERT INTO has_program (program, dept_id) VALUES ('mtech','ce');

INSERT INTO requires (prereq_id, maincourse_id) VALUES ('1','3');

INSERT INTO requests (id, name, dob, notes) VALUES ('1','ron','2021-02-20 12:00:00', 'request for OS course.');
INSERT INTO requests (id, name, dob, notes) VALUES ('1','ron','2020-02-20 13:00:00', 'request dropping MATHS course.');
INSERT INTO requests (id, name, dob, notes) VALUES ('2','Shyam','2021-02-20 12:00:00', 'request for login access admin.');