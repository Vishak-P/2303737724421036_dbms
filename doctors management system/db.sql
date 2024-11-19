
CREATE DATABASE doctor_db;
USE doctor_db;
CREATE TABLE doctordetails (
    doctorid INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(100) NOT NULL,         
    email VARCHAR(100) NOT NULL UNIQUE, 
    specialty VARCHAR(100) NOT NULL     
);
INSERT INTO doctordetails (name, email, specialty)
VALUES 
('Vishak', 'vishak@example.com', 'Orthopedics'),
('Bobby', 'bobby@example.com', 'Pediatrics'),
('Vineeth', 'vineeth@example.com', 'Cardiology'),
('Jai', 'jai@example.com', 'Neurology'),
('Jana', 'jana@example.com', 'General Medicine');
select * from doctordetails;