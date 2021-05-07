-- Insert valid emails accordingly for testing forgot password
INSERT INTO `university`.`faculty` (`faculty_id`, `name`, `emailid`, `password`, `address`, `DOB`) VALUES ('1', 'Shaan', 'sh@sh.com', '81dc9bdb52d04dc20036dbd8313ed055', '02-gandhi-marg new-delhi', '1980-12-30');
INSERT INTO `university`.`faculty` (`faculty_id`, `name`, `emailid`, `password`, `address`, `DOB`) VALUES ('2', 'Rohan', 'rr@trr.com', '81dc9bdb52d04dc20036dbd8313ed055', '02-Hauz-Khas new-delhi', '1965-12-30');

INSERT INTO `university`.`student` (`student_id`, `name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`) VALUES ('1', 'ron', 'ron@ron.com', '81dc9bdb52d04dc20036dbd8313ed055', '100-england', '2001-01-01', 'CSE', '4', '9.80');
INSERT INTO `university`.`student` (`student_id`, `name`, `emailid`, `password`, `address`, `DOB` , `branch`, `sem`, `cpi`) VALUES ('2', 'Ganguly', 'Ganguly@Ganguly.com', '81dc9bdb52d04dc20036dbd8313ed055', '100-london', '2004-02-21', 'EE', '2', '7.80');

INSERT INTO `university`.`admin` (`admin_id`, `name`, `emailid`, `password`) VALUES ('1', 'sqyw', 'sqyw@sqyw.com', '81dc9bdb52d04dc20036dbd8313ed055');
INSERT INTO `university`.`admin` (`admin_id`, `name`, `emailid`, `password`) VALUES ('2', 'qwsr', 'qwsr@qwsr.com', '81dc9bdb52d04dc20036dbd8313ed055');

INSERT INTO course (c_id, name, year, notes) VALUES ('1','MATHS',"2001-12-30","");
INSERT INTO course (c_id, name, year, notes) VALUES ('2','OS',"2006-06-24","");
INSERT INTO course (c_id, name, year, notes) VALUES ('3','DSA',"2006-06-24","");
INSERT INTO course (c_id, name, year, notes) VALUES ('4','Software Engg',"2009-01-30","");
INSERT INTO course (c_id, name, year, notes) VALUES ('5','IC211',"2009-01-01","");

INSERT INTO section (c_id, year, notes) VALUES ('1',"2009","");
INSERT INTO section (c_id, year, notes) VALUES ('1',"2021","");
INSERT INTO section (c_id, year, notes) VALUES ('2',"2020","");
INSERT INTO section (c_id, year, notes) VALUES ('3',"2009","");

INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','1',9.50,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('1','2',8.50,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','1',4.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('2','1',10.00,"");
INSERT INTO enroll (sec_id, student_id, grade, notes) VALUES ('3','2',9.00,"");

INSERT INTO teaches (faculty_id, c_id, year, notes) VALUES ('1','1',"2006-06-01","");
INSERT INTO teaches (faculty_id, c_id, year, notes) VALUES ('1','2',"2006-07-28","");
INSERT INTO teaches (faculty_id, c_id, year, notes) VALUES ('2','3',"2006-06-01","");
INSERT INTO teaches (faculty_id, c_id, year, notes) VALUES ('1','4',"2009-12-30","");
INSERT INTO teaches (faculty_id, c_id, year, notes) VALUES ('2','5',"2010-01-30","");

INSERT INTO assignment (c_id, faculty_id, created_at, end_at, text, marks_total) VALUES ('1','1',NOW(), NOW() + INTERVAL 1 DAY, 'Sort an array in O(n) using radix sort', '30');
INSERT INTO assignment (c_id, faculty_id, created_at, end_at, text, marks_total) VALUES ('2','1',NOW() - INTERVAL 2 DAY, NOW() - INTERVAL 1 DAY, 'reverse an array in O(n)', '10');
INSERT INTO assignment (c_id, faculty_id, created_at, end_at, text, marks_total) VALUES ('2','1',DATE_ADD(NOW(), INTERVAL 1 HOUR), DATE_ADD(NOW(), INTERVAL 3 HOUR), 'End semester exam', '60');
INSERT INTO assignment (c_id, faculty_id, created_at, end_at, text, marks_total) VALUES ('3','2',DATE_ADD(NOW(), INTERVAL 0 HOUR), DATE_ADD(NOW(), INTERVAL 3 HOUR), 'End semester exam', '100');

INSERT INTO submission (a_id, student_id, created_at, end_at, submitted_at, text, marks_got) VALUES ('1','1',NOW(), NOW() + INTERVAL 1 DAY, DATE_ADD(NOW(), INTERVAL 3 HOUR),'answer 1 text', '30');
INSERT INTO submission (a_id, student_id, created_at, end_at, submitted_at, text, marks_got) VALUES ('2','1',NOW() - INTERVAL 2 DAY, NOW() - INTERVAL 1 DAY, DATE_ADD(NOW(), INTERVAL 1 HOUR),'answer 2 text', '10');
INSERT INTO submission (a_id, student_id, created_at, end_at, submitted_at, text, marks_got) VALUES ('2','2',NOW(), NOW() + INTERVAL 1 DAY, DATE_ADD(NOW(), INTERVAL 3 HOUR),'answer 2 text', '5');



