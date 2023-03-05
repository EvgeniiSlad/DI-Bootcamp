-- select first_name||' '||last_name as full_name from customer;

-- select create_date from customer;

-- select DISTINCT create_date from customer

-- select * from customer order by first_name desc

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate asc

-- select address, phone from address where district = 'Texas'

-- select * from film where film_id = 15 or film_id = 150

--SELECT film_id, title, description, length, rental_rate 
--FROM film 
--where title ilike '%dynamite%'

--SELECT film_id, title, description, length, rental_rate 
--FROM film 
--where title ilike 'st%'

-- select * from film  order by rental_rate asc limit 10

-- select * from film  order by rental_rate asc offset 10 rows fetch next 10 rows only

-- select p.amount, p.payment_date
-- from customer as C
-- inner join payment as P 
-- on p.rental_id = c.customer_id
-- order by c.customer_id asc

-- select film_id from film where not exists (select film_id from inventory)

-- select city.city, country.country
-- from city
-- inner join country
-- on city.country_id = country.country_id


-- select c.first_name ||' '|| c.last_name as customer_name, s.first_name ||' '|| s.last_name as staff_name
-- from customer as c
-- inner join staff as s
-- on s.store_id = s.store_id