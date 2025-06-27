# py_environment_setup.md

## Conda

During Anaconda Install, you'll eventually get to a screen that asks if you would like to set your PATH environment variable using the installation wizard. Do NOT check this box. Leave BOTH boxes are unchecked.

RESIST this next step unless you need it. It seems I've not needed to do this yet...After installing Anaconda3, add to path:

```cmd
C:\Users\garth\anaconda3
C:\Users\garth\anaconda3\Scripts
```

Initialize in bash.

```bash
conda init bash  # close git and reopen
```

Update conda and all.

```bash
conda update conda
conda update anaconda
```

### Conda environments

``` bash
python3.8 -m venv ocrenv2
source ocrenv2/bin/activate
python3.8 -m pip install --upgrade pip
```

create conda virtual environment
``` bash
conda create -n dev python=3.7 anaconda
conda create --name dev python=3.7 anaconda
conda activate dev
```

list conda environments
``` bash
conda env list
conda list tensorflow
conda info -e  # whats this?
```

someday when youre ready to update conda on VM:
``` bash
conda update --force conda
conda update anaconda
conda update conda
conda update --all
conda install(?) spyder=5.0.0
```

ai env
``` bash
conda create --name ai python=3.7 anaconda
pip install --upgrade tensorflow  # The TensorFlow 2.0 package has several dependencies which should already be installed in the default conda environment
conda list tensorflow  # 2.5 or higher
conda list keras  # Keras is a popular deep learning framework that serves as a high-level API for TensorFlow. Keras is now included with TensorFlow 2.0, so run the following commnand to verify that the package is available:
```

NLP env
``` bash
conda create --name blockchainenv python=3.7 anaconda
conda create --name nlpenv2 python=3.7 anaconda
python -c "import nltk;nltk.download('all')" -y
conda install -c conda-forge wordcloud -y
conda list wordcloud
pip install newsapi-python==0.2.5
conda list ibm-watson
conda install -c conda-forge spacy -y
python -m spacy download en_core_web_sm
conda list spacy
pip install alpaca-trade-api
```

PyViz env

```bash
conda update anaconda
conda create -n pyvizenv python=3.7 anaconda -y
conda activate pyvizenv
pip install python-dotenv
conda install -c anaconda nb_conda -y
conda install -c conda-forge nodejs=12 -y
conda install -c pyviz holoviz -y
conda install -c plotly plotly -y
conda install -c conda-forge jupyterlab=2.2 -y
pip install numpy==1.19
pip install matplotlib==3.0.3
pip install pandas==1.1.5
set NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install jupyterlab-plotly --no-build
jupyter labextension install plotlywidget --no-build
jupyter labextension install @pyviz/jupyterlab_pyviz --no-build
jupyter lab build
set NODE_OPTIONS=  # correct
```

determine requirements

``` cmd
PS C:\lab_new\edge_raider> pipreqs
INFO: Successfully saved requirements file in C:\lab_new\edge_raider\requirements.txt
```

also 
``` bash
pip freeze
```

## Environment variables

environment variables
``` python
import os  # for loading env variables
from dotenv import load_dotenv  # for loading env variables. pip install python-dotenv
from pathlib import Path
home = Path.home() / ".env"  # windows 1/2
load_dotenv(home)  # windows 2/2
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
# path = "C:/users/garth/.env"
```

read env vars as dict
``` python
json_headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}
```

## Jupyter labs / notebooks

In cell, to split single cell into another cell, place cursor at split and push `control-shift-minus`.

notebook create red text
``` python
<font color='red'>@@@</font> <font color='red'>@@@</font>
```

print current file dir
``` python
import os; print(os.path.dirname(os.getcwd()).split('\\')[-1])
```

get current working directory
``` python
import os; os.path.realpath(file)
this? http://www.faqs.org/docs/diveintopython/regression_path.html
```

Setting these options will allow for reviewing more of the DataFrames
``` python
pd.set_option("display.max_rows", 2000)
pd.set_option("display.max_columns", 2000)
pd.set_option("display.width", 1000)
```

get magic functions. i think this is like %matplotlib inline
``` python
get_ipython().run_line_magic("matplotlib", "inline")
```

tab complete in juypyter
``` python
pd.options.<TAB>
```

jupyter notebook merge current cell with next:
`shift-m`

Setting the %matplotlib inline feature is necessary for displaying the plots in the notebook.

``` python
%matplotlib inline
```

## Database

07.3

https://app.quickdatabasediagrams.com/ 07.3 contains sample code to make ERD

read db credentials, oracle
``` python
filepath = "/creds/"
filename = "db_info.txt"
read lines and extract as variables
lines = open(filepath + filename, "r").readlines()
login, passw, connt = lines[0].strip(), lines[1].strip(), lines[2].strip()
# oracle and sqlchemy connection strings
connection_string_or = login + '/' + passw + '@' + connt
connection_string_sa = 'oracle://' + login + ':' + passw + '@' + connt
```

full postgresql query
``` python
home = Path.home() / ".env"
load_dotenv(home)
POSTGRES_USERNAME = os.getenv("postgres_username")
POSTGRES_PASSWORD = os.getenv("postgres_password")
# dialect+driver://username:password@host:port/db
engine = create_engine(f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@localhost:5432/dvdrental")  # "db url"
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

film_df.hvplot.bar(
    x="title",
    y="length",
    title="whatever",
    color="length",
)
```

df to db table
``` python
import pandas as pd
import cx_Oracle
import sqlalchemy as sa
oracle_db = sa.create_engine('oracle://username:pass@op01ardb01')
connection = oracle_db.connect()
df = pd.read_csv(r'\\file.csv', keep_default_na=False)
titanic = pd.read_csv (r'C:\bleh\titanic.csv') 
df.to_sql('table', connection, schema='schema', if_exists='replace', index=False)
```

db to df table
``` python
import pandas as pd
import cx_Oracle
import sqlalchemy as sa
oracle_db = sa.create_engine('oracle:n//user:pass@dbconnectionstring)
connection = oracle_db.connect()

# write to local, since df.to_sql is way to slow
compression_options = dict(method='zip', archive_name=pull_date + "_" + table + ".csv")
df_all.to_csv(filepath + "/" + pull_date + "_" + table + ".zip", compression=compression_options)
```

## Linux

ssh
``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# If you are using a legacy system that doesn't support the Ed25519 algorithm, use:
ssh-keygen –t rsa –b 4096 –C "YOURGITHUBEMAIL@PLACEHOLDER.NET"
```

create and checkout branch
-b = create the new branch and immediately switch to it.i want to eat a pizza
``` bash
git checkout -b add-new-python-script
```

create a new branch which doesn't exist, switch to it
-c = create new branch
``` bash
git switch -c new-branch
```

log into the SAS server in Putty, then type:
``` bash
/usr/bin/python3.6
```
then write your hello world program

``` cmd
cd c:\program files\gnuwin32\bin
wget -m -A txt http://aleph.gutenberg.org/
```

## Repos

https://www.mkdocs.org/getting-started/
``` bash
pip install -r requirements.txt  # ?
pip install mkdocs
```

``` bash
mkdocs new my-project
cd my-project
mkdocs serve  # ?
```

## Django

``` bash
python -m pip install python

# create project folder called meeting_planner. this is the core folder
django-admin startproject meeting_planner

# start dev server
cd meeting_planner
python manage.py runserver

# create app. delete migrations folder, and all files but __init__.py, views.py
python manage.py startapp website
```