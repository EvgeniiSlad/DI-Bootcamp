-- 1
select name from language;

-- 2
select f.title, f.description, l.name 
from film as f
right join language as l
-- left join language as l
on l.language_id = f.language_id;

-- 3
create table new_film(
	id serial primary key,
	name varchar (100) not null
);
insert into new_film
values
(default, 'new film 1'),
(default, 'new film 2'),
(default, 'new film 3');

-- 4
create table customer_review(
	review_id serial primary key,
	film_id int not null,
	language_id int not null,
	title varchar (200) not null,
	score int not null,
	review_text varchar (65535) not null,
	last_update date not null,
	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 5
insert into customer_review
values
(	default, 
	(select id from new_film where name = 'new film 2'),
 	(select language_id from language where name ='English'),
 	'Not Bad',
	4, 
	'bla bla bla bla bla bla bla',
 	'01.01.2001'
),
(	default, 
	(select id from new_film where name = 'new film 1'),
 	(select language_id from language where name ='English'),
 	'Bad',
	1, 
	'bla bla bla bla bla bla la bla bla bl bla bla la bla bla bla bla bla bla',
 	'04.04.2004'
);

-- 6
delete from new_film
where name = 'new film 1';
