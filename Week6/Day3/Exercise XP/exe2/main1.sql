-- 1
-- update language
-- set language.name = 'French'
-- from language
-- inner join film as f
-- on language.language_id = f.language_id
-- where f.title = 'Alone Trip';


-- drop table customer_review;


-- select sum(case when return_date is null then 1 else 0 end) count_nulls
-- from rental;


-- select f.title, f.rental_rate
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- where return_date is null
-- order by f.rental_rate desc 
-- limit 30;

-- 6.1
-- select f.title, f.description, a.first_name, a.last_name
-- from film as f
-- inner join film_actor as fa
-- on f.film_id = fa.film_id
-- inner join actor as a
-- on fa.actor_id = a.actor_id
-- where (a.first_name = 'Penelope' and a.last_name = 'Monroe')
-- and f.description like '%Sumo%' and f.description like  '%Wrestler%';

-- 6.2
select f.title, c.name, f.rating
from film as f
inner join film_category as fc
on f.film_id = fc.film_id
inner join category as c
on fc.category_id = c.category_id
where f.length < 60 and f.rating = 'R' and c.name = 'Documentary';

-- -- 6.3
-- select f.title, f.rental_rate, r.return_date, c.first_name, c.last_name
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- inner join customer as c
-- on c.customer_id = r.customer_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan'
-- and f.rental_rate > 4
-- and r.return_date between '2005-07-28' and '2005-08-01';

-- -- 6.4
-- select f.title, f.rental_rate, r.return_date, c.first_name, c.last_name
-- from film as f
-- inner join inventory as i
-- on f.film_id = i.film_id
-- inner join rental as r
-- on i.inventory_id = r.inventory_id
-- inner join customer as c
-- on c.customer_id = r.customer_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan'
-- and f.description like '%Boat%' or f.title like '%Boat%'
-- order by rental_rate desc limit 1