-- EX1
-- select first_name as Name,last_name as Last from employees
-- select employee_id from employees
-- select * from employees ORDER by first_name
-- select first_name, last_name, salary,round((salary*0.15),2) as PF from employees
-- select employee_id, first_name, last_name, salary from employees order by salary
-- select sum(salary) from employees
-- select max(salary) as max,min(salary) as min from employees
-- select round(avg(salary),2) from employees
-- select count(employee_id) from employees
-- select upper(first_name) from employees
-- select substr(first_name,1,3) from employees
-- select first_name||' '||last_name as full_name from employees
-- select length(first_name||' '||last_name),first_name||' '||last_name  as full_name from employees
-- select first_name from employees where first_name like '%[0-9]%'
-- select * from employees limit 10

-- EX2
-- select first_name, last_name, salary  from employees where salary>10000 and salary<15000
-- select first_name, last_name, hire_date  from employees where hire_date>'1987-01-01' and hire_date<'1987-12-31'
-- select first_name from employees where first_name ilike '%c%' and first_name ilike '%e%' 

-- select e.last_name, j.job_title, e.salary 
-- from employees as e
-- inner join jobs as j
-- on e.job_id = j.job_id
-- where (j.job_title != 'Programmer' and j.job_title != 'Shipping Clerks')
-- and e.salary not in (4500, 10000, 15000)

-- select last_name from employees where length(last_name) = 6

-- select employees.first_name, employees.last_name,jobs.job_id
-- from employees
-- join jobs
-- on jobs.job_id=employees.job_id

-- select * from employees where last_name = 'JONES' or last_name = 'BLAKE' or last_name = 'SCOTT' or last_name = 'KING' or last_name = 'FORD'



