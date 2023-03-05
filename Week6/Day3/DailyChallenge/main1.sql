-- create table customer(
-- 	id serial primary key,
-- 	first_name varchar (100) not null,
-- 	last_name varchar (100) not null
-- );

-- create table customer_profile(
-- 	id serial,
-- 	isLoggedIn bool default false,
-- 	customer_id int REFERENCES customer(id),
-- 	PRIMARY key (customer_id)
-- );

-- insert into customer (first_name, last_name)
-- values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- insert into customer_profile (isLoggedIn,customer_id )
-- values
-- (true, (select id from customer where first_name ='John' and last_name = 'Doe')),
-- (default, (select id from customer where first_name ='Jerome' and last_name = 'Lalu'))

-- select c.first_name
-- from customer as c
-- inner join customer_profile as cp
-- on c.id = cp.customer_id
-- where cp.isLoggedIn = true;


-- select c.first_name, cp.isLoggedIn
-- from customer as c
-- left join customer_profile as cp
-- on c.id = cp.customer_id;


-- select count(*)
-- from customer as c
-- inner join customer_profile as cp
-- on c.id = cp.customer_id
-- where cp.isLoggedIn = false;

-- PART 2
-- create table book(
-- 	book_id serial primary key,
-- 	title varchar (50) not null,
-- 	author varchar (50) not null
-- );

-- insert into book
-- values
-- (default,'Alice In Wonderland', 'Lewis Carroll'),
-- (default,'Harry Potter',' J.K Rowling'),
-- (default,'To kill a mockingbird','Harper Lee')


-- create table student(
-- 	student_id serial primary key,
-- 	name varchar (100) not null UNIQUE,
-- 	age int check (age <= 15)
-- );

-- insert into student
-- values
-- (default,'John', 12),
-- (default,'Lera', 11),
-- (default,'Patrick', 10),
-- (default,'Bob', 14);

-- create table Library(
-- 	book_id int REFERENCES book(book_id) on delete cascade,
-- 	student_id int references student(student_id) on delete cascade,
-- 	borrowed_date date	
-- );

-- insert into library(book_id,student_id,borrowed_date)
-- values
-- ((select book_id from book where title='Alice In Wonderland'),(select student_id from student where name='John'),
--  '2022-02-15'),
-- ((select book_id from book where title='To kill a mockingbird'),(select student_id from student where name='Bob'),
--  '2021-03-03'),
-- ((select book_id from book where title='Alice In Wonderland'),(select student_id from student where name='Lera'),
--  '2021-05-23'),
-- ((select book_id from book where title='Harry Potter'),(select student_id from student where name='Bob'),
--  '2021-08-12');













