# py_db.md

## Database Connections

### PostgreSQL

Full postgresql query with environment variables:

```python
from pathlib import Path
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

home = Path.home() / ".env"
load_dotenv(home)
POSTGRES_USERNAME = os.getenv("postgres_username")
POSTGRES_PASSWORD = os.getenv("postgres_password")

# dialect+driver://username:password@host:port/db
engine = create_engine(f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@localhost:5432/dvdrental")

query = """
        select
            a.title
            , a.fulltext
            , c.first_name
            , c.last_name
            , a.length
            , a.rating
        from film a
        inner join film_actor b
            on a.film_id = b.film_id
        inner join actor c
            on b.actor_id = c.actor_id
        -- reducing rows for simplicity
        where substring(title, 1, 1) in ('A', 'B')
        order by substring(title, 1, 1)
        """
film_df = pd.read_sql(query, engine)

# Plotting with hvplot
film_df.hvplot.bar(
    x="title",
    y="length",
    title="whatever",
    color="length",
)
```

### Oracle

Read database credentials from file:

```python
filepath = "/creds/"
filename = "db_info.txt"
# read lines and extract as variables
lines = open(filepath + filename, "r").readlines()
login, passw, connt = lines[0].strip(), lines[1].strip(), lines[2].strip()

# oracle and sqlalchemy connection strings
connection_string_or = login + '/' + passw + '@' + connt
connection_string_sa = 'oracle://' + login + ':' + passw + '@' + connt
```

Oracle connection with pandas and sqlalchemy:

```python
import pandas as pd
import cx_Oracle
import sqlalchemy as sa

oracle_db = sa.create_engine('oracle://username:pass@op01ardb01')
connection = oracle_db.connect()
```

### DataFrame to Database

Write DataFrame to database table:

```python
import pandas as pd
import cx_Oracle
import sqlalchemy as sa

oracle_db = sa.create_engine('oracle://username:pass@op01ardb01')
connection = oracle_db.connect()

df = pd.read_csv(r'\\file.csv', keep_default_na=False)
titanic = pd.read_csv(r'C:\bleh\titanic.csv') 

df.to_sql('table', connection, schema='schema', if_exists='replace', index=False)
```

### Database to DataFrame

Read from database to DataFrame:

```python
import pandas as pd
import cx_Oracle
import sqlalchemy as sa

oracle_db = sa.create_engine('oracle://user:pass@dbconnectionstring')
connection = oracle_db.connect()

# write to local, since df.to_sql is way too slow
compression_options = dict(method='zip', archive_name=pull_date + "_" + table + ".csv")
df_all.to_csv(filepath + "/" + pull_date + "_" + table + ".zip", compression=compression_options)
```

## Database Tools

### ERD Creation

Create Entity Relationship Diagrams:

https://app.quickdatabasediagrams.com/ - Contains sample code to make ERD diagrams

## Best Practices

1. **Always use environment variables** for database credentials
2. **Use connection pooling** for production applications
3. **Close connections** properly to avoid resource leaks
4. **Use parameterized queries** to prevent SQL injection
5. **Consider using compression** when exporting large datasets