-- CREATE table items(
-- id serial primary key,
-- name varchar(10),
-- price int
-- );

-- CREATE table customers(
-- id serial primary key,
-- name varchar(10),
-- lastname varchar(20)
-- );

-- insert into items(name,price)
-- values
-- ('Small Desk', 100),
-- ('Large desk', 300),
-- ('Fan', 80);

-- insert into customers(name,lastname)
-- VALUES
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where lastname = 'Smith';
select * from customers where lastname = 'Jones';
select * from customers where name != 'Scott';

