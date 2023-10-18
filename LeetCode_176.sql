with cte as
(select *, (dense_rank() over(order by salary desc)) salary_rank
from employee)

select case when salary_rank = 2 then salary 
            when count(salary) = 0 then Null
      end as SecondHighestSalary
from cte
where salary_rank = 2
