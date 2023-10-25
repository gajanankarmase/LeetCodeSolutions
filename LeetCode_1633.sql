with cte as(
select contest_id, count(*) as contest_count
from register
group by contest_id),

cte2 as
(select contest_id, round(((contest_count / (select distinct (count(user_id)) from users)) * 100),2) as percentage
from cte)
select * from cte2
order by percentage desc, contest_id asc;
