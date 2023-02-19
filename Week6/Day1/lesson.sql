create table house_expenses (
id int,
date_pai date,
water float,
electicity float,
paid_by varchar(20)
);

insert into house_expenses (id,date_pai,water,electicity,paid_by)
values
(1,'2010-03-11',55.5,44.32,'Zhenia');

insert into house_expenses (id,date_pai,water,electicity,paid_by)
values
(2,'2011-02-11',37.8,50.2,'Sasha'),
(3,'2011-02-12',29.9,62.86,'Zhenia'),
(4,'2011-02-13',52.5,54.0,'Dima'),
(5,'2011-02-14',48.5,40.2,'Misha'),
(6,'2011-02-18',48.5,50.2,'Zhenia');

-- select * from house_expenses;

-- select electicity from house_expenses;

-- select electicity,water from house_expenses;

-- select * from house_expenses where id=1;
-- select * from house_expenses where id=1 or id =2;
-- select * from house_expenses where id in(1,2);

-- select max(water) from house_expenses;
-- select min(water) from house_expenses;
-- select sum(electicity) from house_expenses where paid_by!='Zhenia'

-- select paid_by, sum(water+electicity) from house_expenses
-- group by paid_by;

-- select paid_by, max(water+electicity) from house_expenses
-- group by paid_by;

-- update house_expenses 
-- set paid_by='Sasha' where id=1;
-- update house_expenses 
-- set electicity=0 where paid_by='Dima';
-- update house_expenses 
-- set electicity=33, water=25 where id=2;
-- select electicity,water,paid_by from house_expenses;

-- delete from house_expenses where electicity<50;
delete from house_expenses where date_pai='2011-02-12';
select * from house_expenses
