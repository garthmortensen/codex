# Database Cheatsheet

## About
**Created:** Database concepts emerged in the 1960s to organize and manage large amounts of information efficiently. They were created to solve problems of data redundancy, inconsistency, and difficulty in accessing information in early computer systems.

**Similar Technologies:** Data warehouses, data lakes, file systems, spreadsheets, NoSQL stores, in-memory databases

**Plain Language Definition:** A database is like a digital filing cabinet that stores information in an organized way. It lets you quickly find, add, update, or remove data, and ensures multiple people can access the same information without conflicts.

---

# database.md

Databases appear to be simple at first, but the more you learn about them, the more complex they become.

A db is similar to many Excel workbooks, connected by `vlookup()`.

Or, it's all dataframes, and almost everything is DIY.

## Why important

Almost all data is housed on databases. Websites, apps, APIs. 

## High level

### Roles

Many roles in database world.

- db admin
- data modeler
- ETL
- QA
- analyst
- BI (dashboarding)

### Systems

Different database *systems*:

- OLTP (online transactional processing)

  https://voiceofthedba.files.wordpress.com/2022/02/adw_er_thumb.png

- OLAP (online analytical processing), "star schema" standard. Image search

  https://s33046.pcdn.co/wp-content/uploads/2020/02/star-schema-for-the-selected-data-source-view-.png

### NoSQL

- Not Only SQL

  - relational databases

    - https://survey.stackoverflow.co/2022/#section-most-popular-technologies-databases

    - typically hold core datatypes, but can also handle unconventional dtypes like blobs (binary objects, images/audio).

      ```sql
      SELECT DISTINCT 
      	c.CompanyName
      FROM customers AS c
      INNER JOIN orders AS o 
      	ON (c.CustomerID = o.CustomerID)
      INNER JOIN order_details AS od 
      	ON (o.OrderID = od.OrderID)
      INNER JOIN products AS p 
      	ON (od.ProductID = p.ProductID)
      WHERE p.ProductName = 'Chocolate';
      ```
  
  - non-relational databases
  
    - document
  
      - Mongo = document database. .json -> .bson. pk = ObjectID
  
        ```json
        $ db.countries.find().pretty()
        {
                "_id" : "us",
                "name" : "United States",
                "exports" : {
                        "foods" : [
                                {
                                        "name" : "bacon",
                                        "tasty" : true
                                },
                                {
                                        "name" : "burgers"
                                }
                        ]
                }
        }
        {
                "_id" : "ca",
                "name" : "Canada",
                "exports" : {
                        "foods" : [
                                {
                                        "name" : "bacon",
                                        "tasty" : false
                                },
                                {
                                        "name" : "syrup",
                                        "tasty" : true
                                }
                        ]
                }
        }
        {
                "_id" : "mx",
                "name" : "Mexico",
                "exports" : {
                        "foods" : [
                                {
                                        "name" : "salsa",
                                        "tasty" : true,
                                        "condiment" : true
                                }
                        ]
                }
        }
        ```
  
    - columnar (HBase, Cassandra)
  
      ```hbase
      $ get 'users', 'Skrahimi'
      COLUMN                                           CELL
       ename:fname                                     timestamp=1587237947937, value=SAEED
       ename:lname                                     timestamp=1587237947803, value=Rahimi
       ename:mi                                        timestamp=1587237947870, value=K
      3 row(s) in 0.1960 seconds
      ```
  
    - graph (neo4j)
  
      ```cypher
      -- cypher
      MATCH 
      (p:Product {productName:"Chocolade"})<-[:PRODUCT]-(:Order)<-[:PURCHASED]-(c:Customer)
      RETURN distinct c.companyName;
      ```
  

## Object Relational Model

Tables and rows are like classes and instances.

Table = class/object ("car")

Column = attribute ("wheel count")

Row = instance ("ford 150")

## SQL Operations

May ANSI-SQL standards.

Main ones are SQL-92, and after. https://en.wikipedia.org/wiki/SQL-92

### Create db

Many ways to create a databases, tables, etc.

- GUI
- CLI (UI)
- SQL
- programming languages
- import database
  - **Sakila db** used here.
    history = https://dev.mysql.com/doc/sakila/en/
    download link = https://dev.mysql.com/doc/index-other.html
    db restore process = https://www.postgresqltutorial.com/postgresql-getting-started/load-postgresql-sample-database/
    **ERD** = https://www.postgresqltutorial.com/postgresql-sample-database/ 
    **data dictionary** = https://dataedo.com/asset/img/kb/db-tools/mysql_workbench/output/wb_datadict.html
  - adventureworks = https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms
    ERD = https://akela.mendelu.cz/~jprich/vyuka/db2/AdventureWorks2008_db_diagram.pdf
  - many more...

#### Data modeling

Creating a database is an **art** typically done by data modelers. **Expertise** in the database subject is valuable.

The work involves creating:

1. conceptual model
2. logical model
3. physical model

Each model adds more information. You start basic and iterate: 
https://www.guru99.com/data-modelling-conceptual-logical.html

#### Normalization

Not in the normalization/standardizing sense of squashing numbers within a range.

It's about restructuring the data. Similar to R's tidy data. Goal is to minimize redundancies/inconsistencies.

Mainly OLTP task.

1NF

- all rows distinct

- each cell contains one value.

  ["Cat, dog, mouse"] 1x1 = ["Cat", "dog", "mouse"] 1x3

2NF, 3NF, ...perhaps ~6-11 total.

https://en.wikipedia.org/wiki/Database_normalization#Normal_forms

### Relational

Normalization introduces many tables, requiring joins, using primary key, foreign key.

https://w3cschoool.com/public/file/DBMS/foreign-key-in-dbms3.png

```sql
-- only overlap
select
	a.stud_id			as student_stud_id
	, b.stud_id			as department_stud_id
from student as a
INNER join department as b
	on a.stud_id = b.stud_id
;

-- everything on left, add right where available. Good for adding info for analyitical queries
select
	a.stud_id			as student_stud_id
	, b.stud_id			as department_stud_id
from student as a
LEFT join department as b
	on a.stud_id = b.stud_id
;

-- this now behaves as inner join
select
	a.stud_id			as student_stud_id
	, b.stud_id			as department_stud_id
from student as a
LEFT join department as b
	on a.stud_id = b.stud_id
where b.stud_id is not null
;
```

#### ERD notation

Entity Relationship Diagram

Entity = table

Relationship = PK-FK.

Some common notation styles are "Crows feet" and "Chen's" (1...N)

Many PK-FK relationship types.

0 to many, 1 to many, many to many

https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/erd-symbols/ERD-Notation.PNG

#### Junction tables.

For many-to-many joins.

#### Keys

Many types of keys. PK, FK, composite key, surrogate key, etc. uuid/guid, etc.

### DDL vs DML vs others

https://media.geeksforgeeks.org/wp-content/uploads/20210920153429/new.png

#### DDL

Data definition language

```sql
CREATE TABLE

DROP TABLE

ALTER TABLE

TRUNCATE TABLE
```

#### DML

data manipulation language

```sql
INSERT INTO

UPDATE 

DELETE 

CALL

EXPLAIN CALL

LOCK
```

#### Other

```sql
GRANT
REVOKE
COMMIT
```

#### CRUD = common operations

Strangely named.

```sql
-- CREATE:
insert into table1 
	(column1, column2, column3) 
values 
	(value1, value2, value3)
;

-- READ:
select fname, lname from table1;

-- wildcards
select * from table1;

-- UPDATE:
update table1 
set fname = 'gandalf'
where age = 999;

-- DELETE:
delete from table1 where age = 999;
```

#### Create table.

This is useful for querying, because you can save the results of your analysis.

```sql
create table table1 as 
(
    fname varchar(30)
    , lname varchar(30)
    , gender varchar(30)
    , age int
)
;
```

## Querying

### Basic Query

Some good practices.

```sql
create table table2 as 
select * 
from table1
; -- 9 mins
-- 2021.01.01 = 123
-- 2021.02.01 = 52443232
```

### All clauses, ordered

```sql
SELECT 
	, a.fname
	, a.lname
	, b.city
FROM table1 as a
INNER JOIN table2 as b 
	ON a.pk = b.fk
WHERE 
GROUP BY 
HAVING 
ORDER BY
;
```

### Views

From user perspective, a table

They run a saved query on execution.

```sql
-- user
select * from actor_info;

-- see whats behind the view
-- https://stackoverflow.com/a/14634672/5825523
select pg_get_viewdef('actor_info', true);

-- creator
SELECT 
	a.actor_id
	, a.first_name
	, a.last_name
	-- || is concat operator
	, group_concat(DISTINCT (c.name::text || ': '::text) || 
			(
				(
				SELECT group_concat(f.title::text) AS group_concat
				FROM film f
				JOIN film_category fc_1 
					ON f.film_id = fc_1.film_id
				JOIN film_actor fa_1 
					ON f.film_id = fa_1.film_id
				WHERE fc_1.category_id = c.category_id 
				AND fa_1.actor_id = a.actor_id
				GROUP BY fa_1.actor_id
				)
			)
		) AS film_info
FROM actor a
LEFT JOIN film_actor fa 
	ON a.actor_id = fa.actor_id
LEFT JOIN film_category fc 
	ON fa.film_id = fc.film_id
LEFT JOIN category c 
	ON fc.category_id = c.category_id
GROUP BY 
	a.actor_id
	, a.first_name
	, a.last_name
;
```

### Metadata

Like accessing data behind the views, we can access metadata (data about data).

```sql
-- table owner
select * from pg_tables where tablename = 'film';

-- all tables owned by 'postgres'
select * from pg_tables where tableowner = 'postgres';

-- dump of index stats and metadata
SELECT 
	*
	, pg_size_pretty(pg_relation_size(indexrelname::text))
FROM pg_stat_all_indexes 
WHERE schemaname = 'public'
;
```

### Wildcards

```sql
select *
from table1
where fname like "%andal%" -- many letters
or lname like "_ray" -- single letter
;
```

### Agg functions

Aggregate functions in sql;

```sql
select 
	sum(amount)	as total_paid
from payment
group by customer_id
;
```

- **count(*)** - the most common
- sum()
- avg()
- min()
- max()

Aggregate functions in python:

```python
df['total_paid'] = payment.groupby('customer_id')['amount'].sum()
```

Where.

```sql
select 
	customer_id
	, sum(amount) as payment_sum
from payment
where customer_id > 20
group by customer_id
;
```

Having.

```sql
select 
	customer_id
	, sum(amount) as payment_sum
from payment

where customer_id > 20
where sum(amount) > 100 -- NO!

group by customer_id
having sum(amount) > 100 -- YES!
;
```

### Subqueries

PROTIP: intellisense:

```sql
select 
	film_id
	, a.(place cursor here and push + control-space)
from film as a
;
```

The alias a is required before intellisense.

#### WHERE subquery

```sql
-- to make things simpler, use intermediary step
create table good_staff as
select * from staff
where first_name = 'Vinni'
;

-- one subquery
select 
	sum(amount) as total_rental_value
from payment
where staff_id in 
	(
	select staff_id 
	from good_staff
	) a
; -- 30252.12
```

#### FROM subquery

```sql
-- or, nest everything
select 
	sum(amount) as total_rental_value
from payment
where staff_id in 
	(
	select staff_id 
	from a
		(
		select * from staff
		where first_name = 'Vinni'
		)
	)
; -- 30252.12

-- NOT IN
select 
	sum(amount) as total_rental_value
from payment
where staff_id not in 
	(
	select staff_id 
	from a
		(
		select * from staff
		where first_name = 'Vinni'
		)
	)
; -- 31059.92

-- the query above was contrived
-- an easier query
select 
	sum(amount) as total_rental_value
from payment
where staff_id not in 
	(
	select staff_id 
	from staff
	where first_name = 'Vinni'
	)
;
```

If something wrong with staff, you need to disassemble entire query to debug.

#### SELECT subquery

```sql
select
	(select count(distinct actor_id) from film_actor) 		as total_actors
	, (select count(distinct customer_id) from customer) 	as total_customers
	, count(distinct payment_id) 							as total_payments
from payment
;
```

### Sample queries

https://www.geeksforgeeks.org/postgresql-subquery/

films returned between 2005-05-29 and 2005-05-30

```sql
SELECT
    film_id
    , title
FROM film
WHERE film_id IN (
        SELECT inventory.film_id
        FROM rental
        INNER JOIN inventory 
			ON inventory.inventory_id = rental.inventory_id
        WHERE return_date 
			BETWEEN '2005-05-29'
			AND '2005-05-30'
    )
;
```

https://stackoverflow.com/a/2594879/5825523

```sql
DELETE d
FROM @YourTable d
INNER JOIN 
	(
	SELECT
		y.id
		,y.name
		,y.email
		,ROW_NUMBER() OVER(PARTITION BY y.name,y.email ORDER BY y.name,y.email,y.id) AS RowRank
	FROM @YourTable y
	INNER JOIN 
		(
		SELECT
			name
			,email
			, COUNT(*) AS CountOf
		FROM @YourTable
		GROUP BY name,email
		HAVING COUNT(*) > 1
		) dt 
		ON y.name = dt.name 
        AND y.email = dt.email
	) dt2 
	ON d.id=dt2.id
WHERE dt2.RowRank != 1
;
```

## Automated db pseudocode

```python
import pandas as pd
import time
import pyscop2  # for postgres

query1 = \
	f"""
	insert into table1 
		(
		select 
			today() as timestamp
			, count(*) as n
		from {tablename}
		)
	"""

query2 = read_text("path/query2.sql")
connection_str = pyscop2("connection_string")

dbnames = ["animals", "humans"]
tablenames = ["cats", "dogs"]

for dbname in dbnames:
	for tablename in tablenames:
		df = pd.read_sql(query, connection_str)
		df.to_csv(filestamp)

		df_all.append(df)

	if df[0] != df[1]:
        print("tables are not equal")
```

## Programmatic db without SQL

https://github.com/garthmortensen/oop_ideas/blob/main/db.py

```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sqlalchemy import Table, Column, Integer, DateTime
from sqlalchemy import select, insert, update, delete
from sqlalchemy import func  # agg calcs, count, sum, min
import random  # for dice rolling


def setup_db(in_memory: bool=True):
    """CREATE DATABASE function.
        Input: Set boolean to determine if db should be in_memory (default),
        or sqlite.
        Output: engine, metadata
    """

    if in_memory:
        engine = create_engine('sqlite:///:memory:')  # better for git, dev
    else:
        engine = create_engine('sqlite:///db.sqlite')  # approach 1 //// for abs path
    
    # Create a metadata object
    metadata = MetaData()

    return engine, metadata


def setup_tables(engine, metadata):
    """CREATE TABLE function.
        Input: Provide engine and metadata
        Output: Returns engine, metadata and table
    """

    # Build a census table
    rolls = Table('rolls', metadata,
                   # pk autoincrement so you can skip assigning pk value in insert
                   Column('id', 
                          Integer(), 
                          primary_key=True, 
                          autoincrement=True),
                   Column('roll_value', 
                          Integer(), 
                          nullable=False),
                   Column('timestamp_created', 
                          DateTime(timezone=True),
                          # leave timestamp to db to calc, else latency issues
                          server_default=func.now(),
                          # anytime row updates, inserts new timestamp
                          onupdate=func.now()
                          ))
    
    # Create the table in the database
    # metadata.create_all(engine)  # method 1
    rolls.create(engine)  # method 2
    
    insp = inspect(engine)
    print(insp.get_table_names())

    return engine, metadata, rolls


def insert_rows(engine, tablename):
    """INSERT INTO function. 
        Input: engine, tablename
        Output: None
    """

    roll_value = random.randint(1, 100)
    data = [
              {'roll_value': roll_value}
            , {'roll_value': roll_value}
            ]
    
    insert_statement = insert(tablename)
    # Use values_list to insert data
    results = engine.execute(insert_statement, data)
    print(results.rowcount)  # row count


def update_rows(engine, tablename):
    """UPDATE function. 
        Input: engine, tablename
        Output: None
    """

    update_statement = update(tablename).values(roll_value='99')
    update_statement = update_statement.where(tablename.columns.id == 1)
    # results = engine.execute(update_statement)


def select_rows(engine, tablename):
    """SELECT function. 
        Input: engine, tablename
        Output: None
    """

    select_statement = select([tablename])
    results = engine.execute(select_statement).fetchmany(size=100)
    print(select_statement)
    print(results)


def count_rows(engine, tablename) -> int:
    """SELECT count(*) function. Executes on database side, instead of len()
        Input: engine, tablename
        Output: row_count int
    """

    count_statement = func.count(rolls.columns.id)
    row_count = engine.execute(count_statement).scalar()
    print(row_count)

    return row_count


def delete_rows_all(engine, tablename):
    """DELETE FROM function.
        Input: engine, tablename
        Output: None
    """

    delete_statement = delete(rolls)
    print(delete_statement)
    # results = engine.execute(delete_statement)
    print(engine.execute(select([tablename])).fetchall())


engine, metadata = setup_db()
engine, metadata, rolls = setup_tables(engine, metadata)
insert_rows(engine, rolls)
update_rows(engine, rolls)
select_rows(engine, rolls)
row_count = count_rows(engine, rolls)
delete_rows_all(engine, rolls)
```

## Resources

https://sqlzoo.net/wiki/SQL_Tutorial

https://www.amazon.com/Head-First-SQL-Brain-Learners/dp/0596526849

https://www.amazon.com/SQL-Cookbook-Query-Solutions-Techniques/dp/1492077445/ref=sr_1_1?crid=2ICR6FQMEFNYN&keywords=sql+cookbook&qid=1660602094&s=books&sprefix=sql+cookbook%2Cstripbooks%2C73&sr=1-1

https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802/ref=asc_df_1118530802/?tag=hyprod-20&linkCode=df0&hvadid=312128454859&hvpos=&hvnetw=g&hvrand=11244859012842285371&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019538&hvtargid=pla-396828635481&psc=1

https://www.amazon.com/Essential-SQLAlchemy-Mapping-Python-Databases/dp/149191646X