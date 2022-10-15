SHOW DATABASES;
CREATE DATABASE dados_university;
USE dados_university;

CREATE TABLE course (
	course_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    rating INTEGER NOT NULL,
    diff INTEGER NOT NULL
);
desc course;

CREATE TABLE prof (
	prof_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    popularity INTEGER NOT NULL,
    teaching_ability INTEGER NOT NULL
    );
    
CREATE TABLE student (
	student_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    intelligence INTEGER NOT NULL,
    ranking INTEGER NOT NULL
    );
    
CREATE TABLE registration(
	course_id INTEGER,
    student_id INTEGER,
    grade INTEGER NOT NULL,
    sat INTEGER NOT NULL,
	PRIMARY KEY(course_id, student_id),
    constraint fk_course FOREIGN KEY (course_id) REFERENCES course(course_id),
    constraint fk_student FOREIGN KEY (student_id) REFERENCES student(student_id)
	);
    
CREATE TABLE ra (
	prof_id INTEGER,
    student_id INTEGER,
    capability INTEGER NOT NULL,
    salary ENUM("med", "high", "low"),
    PRIMARY KEY(prof_id, student_id),
    constraint fk_pror_ra FOREIGN KEY (prof_id) REFERENCES prof(prof_id),
    constraint fk_student_ra FOREIGN KEY (student_id) REFERENCES student(student_id)
	);