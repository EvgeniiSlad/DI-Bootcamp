-- create table students(
-- id serial primary key, 
-- last_name varchar(20),
-- first_name varchar(10),
-- birth_date date);

-- insert into students (first_name,last_name,birth_date)
-- values
-- ('Marc', 'Benichou', '11/02/1998'),
-- ('Yoan', 'Cohen', '12/03/2010'),
-- ('Lea', 'Benichou', '07/27/1987'),
-- ('Amelia', 'Dux', '04/07/1996'),
-- ('David', 'Grez', '06/14/2003'),
-- ('Omer', 'Simpson', '10/03/1980');


select * from students;
select first_name,last_name from students;
select first_name,last_name from students where id=2;
select first_name,last_name from students where last_name='Benichou' and first_name='Marc';
select first_name, last_name from students where first_name ilike '%a%';
select first_name, last_name from students where first_name ilike 'a%';
select first_name, last_name from students where first_name ilike '%a';
select first_name, last_name from students where first_name ilike '%a_';
select first_name, last_name from students where id = 1 and id = 3;
select * from students where birth_date >= '01/01/2000';
