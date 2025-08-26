# SQL to dplyr

sql clause order of execution:

```sql
from
on
join
where
group by
having
select
order by
```

dplyr starts with from! following examples then filter next
be cool if sql queries followed this order...

## sql over dplyr

1.

```sql
select * 
from customers 
where country="usa";
```

```r
customers %>%
  filter(country == "usa")
```

```sql
where country="usa"
```

```r
filter(country == "usa")
```

2.

```sql
select count(*) 
from orders 
where status="completed";
```

```r
orders %>%
  filter(status == "completed") %>%
  summarize(count = n())
```

3.

```sql
select 
	customer_id
	, avg(amount) 
from orders 
group by customer_id;
```

```r
orders %>%
  group_by(customer_id) %>%
  summarize(avg_amount = mean(amount))
```

4.

```sql
select * 
from products 
where price between 50 and 100;
```

```r
products %>%
  filter(price >= 50, price <= 100)
```

5.

```sql
select 
	product_name
	, count() 
from order_items 
group by product_name 
order by count() desc;
```

```r
order_items %>%
  group_by(product_name) %>%
  summarize(count = n()) %>%
  arrange(desc(count))
```

## Alternative view

select ... from ... where ...
filter(...)

select ... from ... group by ...
group_by(...)

select ... from ... order by ...
arrange(...)

select ... from ... limit ...
slice(...)

select count(*) from ...
summarize(count = n())

select avg(...) from ...
summarize(avg = mean(...))

select sum(...) from ...
summarize(sum = sum(...))

select max(...) from ...
summarize(max = max(...))

select min(...) from ...
summarize(min = min(...))
