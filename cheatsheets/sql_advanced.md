# sql_advanced.md

## Window Functions

Window functions perform calculations across a set of table rows that are somehow related to the current row.

### Basic Syntax
```sql
select 
    column1,
    column2,
    window_function() over (
        [partition by column]
        [order by column]
        [rows/range frame_specification]
    ) as window_result
from table_name;
```

### Ranking Functions

```sql
-- row_number: assigns unique sequential integers
select 
    employee_id,
    department,
    salary,
    row_number() over (partition by department order by salary desc) as rank_in_dept
from employees;

-- rank: assigns ranks with gaps for ties
select 
    product_name,
    category,
    price,
    rank() over (order by price desc) as price_rank
from products;

-- dense_rank: assigns ranks without gaps for ties
select 
    student_name,
    score,
    dense_rank() over (order by score desc) as dense_rank
from exam_results;

-- ntile: divides rows into n buckets
select 
    customer_id,
    revenue,
    ntile(4) over (order by revenue) as quartile
from customer_revenue;
```

### Aggregate Window Functions

```sql
-- running totals
select 
    order_date,
    order_amount,
    sum(order_amount) over (order by order_date) as running_total
from orders;

-- moving averages
select 
    date,
    sales,
    avg(sales) over (
        order by date 
        rows between 6 preceding and current row
    ) as moving_avg_7_days
from daily_sales;

-- cumulative percentage
select 
    product,
    sales,
    sales / sum(sales) over () * 100 as pct_of_total,
    sum(sales) over (order by sales desc) / sum(sales) over () * 100 as cumulative_pct
from product_sales;
```

### Lead and Lag Functions

```sql
-- lag: access previous row values
select 
    date,
    stock_price,
    lag(stock_price, 1) over (order by date) as prev_price,
    stock_price - lag(stock_price, 1) over (order by date) as price_change
from stock_prices;

-- lead: access next row values
select 
    employee_id,
    start_date,
    end_date,
    lead(start_date, 1) over (order by start_date) as next_start_date
from employee_positions;

-- multiple lag periods
select 
    month,
    revenue,
    lag(revenue, 1) over (order by month) as prev_month,
    lag(revenue, 12) over (order by month) as same_month_prev_year
from monthly_revenue;
```

### First/Last Value Functions

```sql
-- first_value and last_value
select 
    department,
    employee_name,
    salary,
    first_value(employee_name) over (
        partition by department 
        order by salary desc
    ) as highest_paid,
    last_value(employee_name) over (
        partition by department 
        order by salary desc
        rows between unbounded preceding and unbounded following
    ) as lowest_paid
from employees;
```

### Frame Specifications

```sql
-- different frame types
select 
    date,
    sales,
    -- current row only
    sum(sales) over (order by date rows current row) as current_only,
    
    -- unbounded preceding to current
    sum(sales) over (order by date rows unbounded preceding) as running_total,
    
    -- 3 rows before to 1 row after
    sum(sales) over (order by date rows between 3 preceding and 1 following) as windowed_sum,
    
    -- range-based (value-based window)
    avg(sales) over (order by date range between interval '7' day preceding and current row) as week_avg
from daily_sales;
```

## Common Table Expressions (CTEs)

### Basic CTE
```sql
with high_value_customers as (
    select 
        customer_id,
        sum(order_amount) as total_spent
    from orders
    group by customer_id
    having sum(order_amount) > 10000
)
select 
    c.customer_name,
    hvc.total_spent
from customers c
join high_value_customers hvc on c.customer_id = hvc.customer_id;
```

### Recursive CTE
```sql
-- employee hierarchy
with recursive employee_hierarchy as (
    -- anchor: top-level managers
    select 
        employee_id,
        employee_name,
        manager_id,
        1 as level,
        cast(employee_name as varchar(1000)) as path
    from employees
    where manager_id is null
    
    union all
    
    -- recursive: subordinates
    select 
        e.employee_id,
        e.employee_name,
        e.manager_id,
        eh.level + 1,
        concat(eh.path, ' -> ', e.employee_name)
    from employees e
    join employee_hierarchy eh on e.manager_id = eh.employee_id
)
select * from employee_hierarchy
order by level, employee_name;

-- date series generation
with recursive date_series as (
    select date '2024-01-01' as date_value
    union all
    select date_value + interval '1 day'
    from date_series
    where date_value < date '2024-12-31'
)
select * from date_series;
```

### Multiple CTEs
```sql
with 
monthly_sales as (
    select 
        date_trunc('month', order_date) as month,
        sum(amount) as monthly_total
    from orders
    group by date_trunc('month', order_date)
),
sales_growth as (
    select 
        month,
        monthly_total,
        lag(monthly_total) over (order by month) as prev_month_total,
        (monthly_total - lag(monthly_total) over (order by month)) / 
        lag(monthly_total) over (order by month) * 100 as growth_rate
    from monthly_sales
)
select * from sales_growth
where growth_rate > 10;
```

## Slowly Changing Dimensions (SCD)

### Type 1 SCD - Overwrite
```sql
-- Simple update overwrites old values
update customer_dim 
set 
    address = 'New Address',
    city = 'New City',
    last_updated = current_timestamp
where customer_id = 123;
```

### Type 2 SCD - Historical Tracking
```sql
-- Table structure for Type 2 SCD
create table customer_dim_scd2 (
    surrogate_key serial primary key,
    customer_id int not null,
    customer_name varchar(100),
    address varchar(200),
    city varchar(50),
    effective_date date not null,
    expiration_date date,
    is_current boolean default true,
    created_timestamp timestamp default current_timestamp
);

-- Insert new record and expire old one
begin;

-- Expire the current record
update customer_dim_scd2 
set 
    expiration_date = current_date - interval '1 day',
    is_current = false
where customer_id = 123 and is_current = true;

-- Insert new current record
insert into customer_dim_scd2 (
    customer_id, customer_name, address, city, effective_date, is_current
) values (
    123, 'John Smith', 'New Address', 'New City', current_date, true
);

commit;

-- Query current records
select * from customer_dim_scd2 
where is_current = true;

-- Query historical data
select * from customer_dim_scd2 
where customer_id = 123 
order by effective_date;
```

### Type 3 SCD - Limited History
```sql
-- Table with current and previous values
create table customer_dim_scd3 (
    customer_id int primary key,
    customer_name varchar(100),
    current_address varchar(200),
    previous_address varchar(200),
    current_city varchar(50),
    previous_city varchar(50),
    address_change_date date,
    last_updated timestamp default current_timestamp
);

-- Update with history preservation
update customer_dim_scd3 
set 
    previous_address = current_address,
    current_address = 'New Address',
    previous_city = current_city,
    current_city = 'New City',
    address_change_date = current_date,
    last_updated = current_timestamp
where customer_id = 123;
```

## Advanced Joins

### Self Joins
```sql
-- Find employees and their managers
select 
    e.employee_name as employee,
    m.employee_name as manager
from employees e
left join employees m on e.manager_id = m.employee_id;

-- Find products in same category with higher price
select 
    p1.product_name,
    p1.price,
    p2.product_name as higher_priced_product,
    p2.price as higher_price
from products p1
join products p2 on p1.category = p2.category 
    and p1.price < p2.price;
```

### Cross Apply (SQL Server) / Lateral Joins (PostgreSQL)
```sql
-- PostgreSQL LATERAL join
select 
    d.department_name,
    top_emp.employee_name,
    top_emp.salary
from departments d
cross join lateral (
    select employee_name, salary
    from employees e
    where e.department_id = d.department_id
    order by salary desc
    limit 3
) top_emp;

-- SQL Server CROSS APPLY
select 
    d.department_name,
    top_emp.employee_name,
    top_emp.salary
from departments d
cross apply (
    select top 3 employee_name, salary
    from employees e
    where e.department_id = d.department_id
    order by salary desc
) top_emp;
```

## Advanced Aggregations

### GROUPING SETS
```sql
-- Multiple grouping levels in one query
select 
    region,
    product_category,
    sum(sales) as total_sales,
    count(*) as order_count
from sales_data
group by grouping sets (
    (region, product_category),  -- By region and category
    (region),                    -- By region only
    (product_category),          -- By category only
    ()                          -- Grand total
);
```

### ROLLUP
```sql
-- Hierarchical totals (year -> quarter -> month)
select 
    extract(year from order_date) as year,
    extract(quarter from order_date) as quarter,
    extract(month from order_date) as month,
    sum(amount) as total_sales
from orders
group by rollup(
    extract(year from order_date),
    extract(quarter from order_date),
    extract(month from order_date)
);
```

### CUBE
```sql
-- All possible combinations of groupings
select 
    region,
    product_type,
    channel,
    sum(sales) as total_sales
from sales_data
group by cube(region, product_type, channel);
```

### Conditional Aggregation
```sql
select 
    product_category,
    sum(case when region = 'North' then sales else 0 end) as north_sales,
    sum(case when region = 'South' then sales else 0 end) as south_sales,
    sum(case when region = 'East' then sales else 0 end) as east_sales,
    sum(case when region = 'West' then sales else 0 end) as west_sales,
    count(distinct customer_id) as unique_customers,
    avg(case when order_amount > 1000 then order_amount end) as avg_large_orders
from sales_data
group by product_category;
```

## Pivot and Unpivot Operations

### Manual Pivot
```sql
-- Transform rows to columns
select 
    customer_id,
    sum(case when product_type = 'Electronics' then amount else 0 end) as electronics,
    sum(case when product_type = 'Clothing' then amount else 0 end) as clothing,
    sum(case when product_type = 'Books' then amount else 0 end) as books
from orders
group by customer_id;
```

### SQL Server PIVOT
```sql
-- Using PIVOT operator
select 
    customer_id,
    [Electronics],
    [Clothing],
    [Books]
from (
    select customer_id, product_type, amount
    from orders
) as source_table
pivot (
    sum(amount)
    for product_type in ([Electronics], [Clothing], [Books])
) as pivot_table;
```

### PostgreSQL Crosstab
```sql
-- Using crosstab extension
select *
from crosstab(
    'select customer_id, product_type, sum(amount) 
     from orders 
     group by customer_id, product_type 
     order by customer_id, product_type',
    'values (''Electronics''), (''Clothing''), (''Books'')'
) as ct(customer_id int, electronics numeric, clothing numeric, books numeric);
```

## Performance Optimization

### Index Optimization
```sql
-- Composite index for common query patterns
create index idx_orders_customer_date 
on orders (customer_id, order_date desc);

-- Partial index for specific conditions
create index idx_orders_large_amount 
on orders (order_date) 
where amount > 1000;

-- Covering index (includes non-key columns)
create index idx_orders_covering 
on orders (customer_id, order_date) 
include (amount, product_id);
```

### Query Hints and Optimization
```sql
-- Force index usage (SQL Server)
select * from orders with (index(idx_orders_customer_date))
where customer_id = 123;

-- Parallel query hint
select /*+ parallel(4) */ customer_id, sum(amount)
from orders
group by customer_id;

-- Use of EXPLAIN for query analysis
explain (analyze, buffers) 
select 
    c.customer_name,
    sum(o.amount) as total_spent
from customers c
join orders o on c.customer_id = o.customer_id
where o.order_date >= '2024-01-01'
group by c.customer_id, c.customer_name;
```

### Partitioning Examples
```sql
-- Range partitioning by date
create table orders_partitioned (
    order_id serial,
    customer_id int,
    order_date date,
    amount decimal(10,2)
) partition by range (order_date);

-- Create partitions
create table orders_2023 partition of orders_partitioned
    for values from ('2023-01-01') to ('2024-01-01');

create table orders_2024 partition of orders_partitioned
    for values from ('2024-01-01') to ('2025-01-01');

-- Hash partitioning
create table customers_partitioned (
    customer_id serial,
    customer_name varchar(100),
    region varchar(50)
) partition by hash (customer_id);

create table customers_part1 partition of customers_partitioned
    for values with (modulus 4, remainder 0);
```

## Data Quality and Validation

### Data Profiling Queries
```sql
-- Column completeness
select 
    'customer_name' as column_name,
    count(*) as total_rows,
    count(customer_name) as non_null_count,
    count(*) - count(customer_name) as null_count,
    round(count(customer_name) * 100.0 / count(*), 2) as completeness_pct
from customers

union all

select 
    'email',
    count(*),
    count(email),
    count(*) - count(email),
    round(count(email) * 100.0 / count(*), 2)
from customers;

-- Duplicate detection
select 
    customer_name,
    email,
    count(*) as duplicate_count
from customers
group by customer_name, email
having count(*) > 1;

-- Data distribution analysis
select 
    region,
    count(*) as count,
    round(count(*) * 100.0 / sum(count(*)) over (), 2) as percentage
from customers
group by region
order by count desc;

-- Outlier detection using IQR
with quartiles as (
    select 
        percentile_cont(0.25) within group (order by amount) as q1,
        percentile_cont(0.75) within group (order by amount) as q3
    from orders
),
outlier_bounds as (
    select 
        q1,
        q3,
        q1 - 1.5 * (q3 - q1) as lower_bound,
        q3 + 1.5 * (q3 - q1) as upper_bound
    from quartiles
)
select 
    order_id,
    amount,
    case 
        when amount < lower_bound then 'Low Outlier'
        when amount > upper_bound then 'High Outlier'
        else 'Normal'
    end as outlier_type
from orders, outlier_bounds
where amount < lower_bound or amount > upper_bound;
```

### Data Validation Rules
```sql
-- Constraint validation
alter table customers 
add constraint chk_email_format 
check (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

-- Custom validation functions
create or replace function validate_phone_number(phone varchar)
returns boolean as $$
begin
    return phone ~* '^\+?[1-9]\d{1,14}$';
end;
$$ language plpgsql;

-- Data quality audit table
create table data_quality_audit (
    audit_id serial primary key,
    table_name varchar(100),
    column_name varchar(100),
    rule_name varchar(100),
    failed_count int,
    total_count int,
    failure_rate decimal(5,2),
    audit_date timestamp default current_timestamp
);
```

## Advanced String Operations

### Pattern Matching and Regex
```sql
-- Extract domains from email addresses
select 
    email,
    substring(email from '@(.+)$') as domain
from customers;

-- Clean and standardize phone numbers
select 
    phone_raw,
    regexp_replace(
        regexp_replace(phone_raw, '[^0-9]', '', 'g'),
        '^1?(\d{3})(\d{3})(\d{4})$',
        '(\1) \2-\3'
    ) as phone_formatted
from customers;

-- Parse JSON data
select 
    order_id,
    json_extract_path_text(metadata, 'source') as order_source,
    json_extract_path_text(metadata, 'campaign_id') as campaign_id
from orders
where metadata is not null;
```

### Text Analytics
```sql
-- Word frequency analysis
with words as (
    select 
        product_id,
        lower(trim(unnest(string_to_array(description, ' ')))) as word
    from products
    where description is not null
),
word_counts as (
    select 
        word,
        count(*) as frequency
    from words
    where length(word) > 3  -- Filter short words
    and word not in ('the', 'and', 'or', 'but', 'with', 'for')  -- Stop words
    group by word
)
select 
    word,
    frequency,
    rank() over (order by frequency desc) as rank
from word_counts
order by frequency desc
limit 20;
```

## Time Series Analysis

### Gap and Island Problems
```sql
-- Find consecutive date ranges (islands)
with date_groups as (
    select 
        customer_id,
        visit_date,
        visit_date - interval '1 day' * 
            row_number() over (partition by customer_id order by visit_date) as group_date
    from customer_visits
),
consecutive_periods as (
    select 
        customer_id,
        min(visit_date) as period_start,
        max(visit_date) as period_end,
        count(*) as consecutive_days
    from date_groups
    group by customer_id, group_date
)
select * from consecutive_periods
where consecutive_days >= 7;  -- 7+ consecutive days

-- Find gaps in data
with date_series as (
    select generate_series(
        (select min(order_date) from orders),
        (select max(order_date) from orders),
        interval '1 day'
    )::date as date_value
),
missing_dates as (
    select ds.date_value
    from date_series ds
    left join orders o on ds.date_value = o.order_date
    where o.order_date is null
)
select 
    date_value as missing_date,
    lag(date_value) over (order by date_value) as prev_missing_date
from missing_dates;
```

### Moving Calculations
```sql
-- Moving statistics
select 
    date,
    revenue,
    -- Simple moving average
    avg(revenue) over (
        order by date 
        rows between 6 preceding and current row
    ) as sma_7,
    
    -- Exponential moving average (approximation)
    revenue * 0.2 + lag(revenue) over (order by date) * 0.8 as ema_approx,
    
    -- Moving standard deviation
    stddev(revenue) over (
        order by date 
        rows between 6 preceding and current row
    ) as moving_stddev,
    
    -- Bollinger bands
    avg(revenue) over (order by date rows between 19 preceding and current row) +
    2 * stddev(revenue) over (order by date rows between 19 preceding and current row) as upper_band,
    
    avg(revenue) over (order by date rows between 19 preceding and current row) -
    2 * stddev(revenue) over (order by date rows between 19 preceding and current row) as lower_band
from daily_revenue
order by date;
```

## Best Practices

### Query Writing Guidelines
```sql
-- Use meaningful aliases
select 
    c.customer_name,
    c.registration_date,
    sum(o.amount) as total_lifetime_value,
    count(o.order_id) as total_orders
from customers c
left join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name, c.registration_date;

-- Use CTEs for complex logic
with customer_segments as (
    select 
        customer_id,
        case 
            when total_spent >= 10000 then 'VIP'
            when total_spent >= 5000 then 'Premium'
            when total_spent >= 1000 then 'Regular'
            else 'Basic'
        end as segment
    from customer_totals
),
segment_metrics as (
    select 
        segment,
        count(*) as customer_count,
        avg(total_spent) as avg_spent
    from customer_segments cs
    join customer_totals ct on cs.customer_id = ct.customer_id
    group by segment
)
select * from segment_metrics
order by avg_spent desc;
```

### Error Handling
```sql
-- Safe division
select 
    product_id,
    total_revenue,
    total_quantity,
    case 
        when total_quantity = 0 then null
        else total_revenue / total_quantity
    end as avg_price_per_unit
from product_summary;

-- Null handling
select 
    customer_id,
    coalesce(phone, 'No phone provided') as phone_display,
    nullif(email, '') as clean_email,  -- Convert empty strings to NULL
    case 
        when last_order_date is null then 'Never ordered'
        when last_order_date < current_date - interval '1 year' then 'Inactive'
        else 'Active'
    end as customer_status
from customers;
```