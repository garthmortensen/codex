# r_development.md

> Before I had studied Chan for thirty years, I saw mountains as mountains, and rivers as rivers. When I arrived at a more intimate knowledge, I came to the point where I saw that mountains are not mountains, and rivers are not rivers. But now that I have got its very substance I am at rest. For it's just that I see mountains once again as mountains, and rivers once again as rivers.

[TOC]

## Best Practices/Meta stuff

### Libraries

Equivalent to python pipfreeze's `requirements.txt`. This is not standard though, so see section Environments.

```R
install.packages("readr")
library(readr)

requirements <- read_lines("requirements.txt")
install.packages(requirements)
```

Single line library loading.

``` r
lapply(c("renv", "readr"), library, character.only = TRUE)
```

### Environments

Equivalent to `conda create -n dev python=3.7 anaconda` or `venv`.

Handling package versions with `R_LIBS` is manual in comparison to `renv` and `packrat` which take care of most things automatically. `renv` is the most recommended way to manage package dependencies in R projects, but seems very similar to `packrat`. Both were developed by RStudio, but `renv` is just a newer version and more maintained.

#### `renv`

To initialize a new project with `renv`, create a new directory and initialize `renv`:

``` R
# mkdir
dir.create("my_renv_project")
setwd("my_renv_project")

# initialize renv
renv::init()
```

then install packages into environment via:

``` R
install.packages("ggplot2")
```

the package will be installed to the above working directory. Snapshot your environment via `renv::snapshot()`.  This will update the `renv.lock` file, which you can then include in your repository. Restore via `renv::restore()`.

#### `packrat`

Same as `renv`:

``` R
# mkdir
dir.create("my_packrat_project")
setwd("my_packrat_project")

# initialize packrat
packrat::init()
```

then install packages into environment via:

``` R
install.packages("ggplot2")
```

the package will be installed to the above working directory. Snapshot your environment via `packrat::snapshot()`, and restore it via `packrat::restore()`. This will update the `packrat.lock` file, which you can then include in your repository. Restore it via `packrat::restore()`.

#### `R_LIBS`

`R_LIBS` is an environment variable that R uses to determine where to install and load packages from.

e.g., if you want to use a specific directory of packages, set `R_LIBS` to that dir:

```R
dir.create("my_r_libs_project")
setwd("my_r_libs_project")

# set R_LIBS
Sys.setenv(R_LIBS = "my_r_libs_project/library")
```

then install a package

``` r
install.packages("ggplot2")
```

the package will be installed to the above working directory. There is no lock file. Instead, manually track package versions by listing them in `README.md` or another text file. Get package versions via `packageVersion("packagename")`.

NB: setting `R_LIBS` this way only changes the environment variable for your current R session. Permanently? Set your system's environment variables, or set in your `.Renviron` file.

### Environment variables

environment variables.

``` R
# Set Environment Variables
# Sys.setenv(ALPACA_API_KEY = "your_api_key")
# Sys.setenv(ALPACA_SECRET_KEY = "your_secret_key")

# Get Environment Variables
alpaca_api_key <- Sys.getenv("ALPACA_API_KEY")
alpaca_secret_key <- Sys.getenv("ALPACA_SECRET_KEY")
```

and then...

1. find the location of your home directory in R with path.expand("~"). 
2. Create a file named `.Renviron` in your home directory, then:

```bash
ALPACA_API_KEY=your_api_key
ALPACA_SECRET_KEY=your_secret_key
```

Or, read creds as list.

``` R
json_headers <- list("Content-Type" = "application/json",
                     "pinata_api_key" = pinata_api_key,
                     "pinata_secret_api_key" = pinata_secret_api_key)
```

### `roxygen2` auto documentation

Python equivalent: docstring and `sphinx.ext.autodoc`.

In R, documentation is typically provided in a separate `.Rd` file or directly above the function in a `roxygen2` comment block. `roxygen2` is the modern and widely used approach. `roxygen2` is an R package that converts specially formatted comments into a `.Rd`. Example:

```r
#' Add two numbers
#'
#' @param x A number.
#' @param y A number.
#' @return The sum of \code{x} and \code{y}.
#' @examples
#' add_numbers(1, 2)
#' @export
add_numbers <- function(x, y) {
  return(x + y)
}
```

`#'` starts a roxygen2 comment block.

`@examples` provides examples of how to use the function.

`@export` tells `roxygen2` to make the function available to package users.

Then use `devtools::document()` to generate `.Rd` files. These files can be used to create a manual or website for your package, and the help system in R can extract the relevant documentation when a user asks for help on one of your functions.

#### generate on commit

**NB:** so after thinking on this, i dont think this is the best way. Pretty sure tests are ok to be run automatically in pre-commit, but i think autodocs and autoformat should NOT. Imagine if you add a b c, then commit. The autodoc and autoformat changes havent been added to staging, so they'd be skipped. Better just create a bash command. I still need to let the thought simmer.

anyways, bc everything has been setup above...

In order to run all autodocs on commit...

Save this script in your package root (or wherever i guess). `generate_docs.R`. 

``` r
library(roxygen2)
library(devtools)
load_all('.')  # Loads all functions, data, etc. of the current package
roxygen2::roxygenise('.')
```

then alias it:

``` bash
alias generateDocs='Rscript /path/to/generate_docs.R'
```

### autoformat

```r
install.packages("styler")
```

2. Use the `style_file` function to style a specific file:

```r
styler::style_file("path/to/your/file.R")
```

modifies the file in-place to meet the style guide. If you want to see the changes without modifying the file, you can use `style_text` to style a string of code, or `style_dir` to style a dir.

You can customize via:

`tidyverse_style()` to generate a style guide that fits your needs, and then use the `style_text()`, `style_file()`, or `style_dir()` functions to apply.

```r
# Define a custom style guide
my_style <- styler::tidyverse_style(
  scope = "tokens",  # specify what to style: "spaces", "tokens", or "indention"
  strict = TRUE,  # should strict enforcement be used?
  indent_by = 2,  # how many spaces
  start_comments_with_one_space = TRUE,  # comments start with a space
  reindention = styler::tidyverse_reindention()  # reindention rules?
)

# apply
styler::style_file("path/to/your/file.R", transformers = my_style)
```

Now apply it to a directory from bash:

``` r
args <- commandArgs(trailingOnly = TRUE)
directory <- args[1]

library(styler)
style_dir(directory)
```

then

``` bash
Rscript /path/to/style_directory.R /path/to/your/directory/
```

### magic potion

even cooler, get it all into a single bash command:

``` bash
alias magic_potion='\
python3 /path/to/generate_python_docs.py && \
Rscript /path/to/generate_r_docs.R && \
Rscript /path/to/style_directory.R && \
pytest /path/to/tests/ && \
black /path/to/your/code/ \
'
# autodoc, test, format, eh?
```

### `testthat`

#### unit testing

##### AAA

1. **Arrange**: set up the test conditions. Create objects, mock data, or setup the environment. This is where you ensure you have everything you need to perform the test.
2. **Act**: Perform the action you're testing. Calling a function, performing a calculation, or otherwise manipulating your data.
3. **Assert**: After the action, check the expected results.

##### Simple setup

A simple test case is as follows:

``` r
# the function to square a number
square_number <- function(n) {
  return(n^2)
}

# the unit test
library(testthat)
test_that("Check square of a number", {
  n <- 2  # Arrange
  result <- square_number(n)  # Act
  expect_equal(result, 4)  # Assert
})
```

##### framework commands

If testing a package, place tests inside `tests/testthat/`, then use `devtools::test()` to run them. 

If not testing a package, use `testthat::test_file()` to run a single file of tests.

Run tests as follows:

``` r
library(testthat)
test_result <- test_file("test_square.R")
summary(test_result)
```

#### Logging

There isn't a specific tidyverse logging standard. Here's an example of how you can achieve logging to `.log` files and streaming to standard output and standard error.

`logging` vs `log4r`?

```R
library(logging)
library(futile.logger)

# initialize logging configurations
file_appender <- fileAppender("logfile.log")
stream_appender <- consoleAppender()
options(error = expression(logError()))

# set log levels and appenders
log_threshold <- "INFO"
log_threshold <- setLogThreshold(log_threshold)
log_additivity(FALSE)
log_doTrace(FALSE)
addAppender(file_appender)
addAppender(stream_appender)

# example
loginfo("This is an informational message.")
logwarn("This is a warning message.")
logerror("This is an error message.")

# stop logging
removeAppender(file_appender)
removeAppender(stream_appender)
```

Use `fileAppender` to log messages to a file, and a console appender using `consoleAppender` to stream messages to standard output. The `options(error = expression(logError()))` line sets up error handling to log errors.

You can use various logging functions, such as `loginfo()`, `logwarn()`, and `logerror()`, to log messages at different levels (info, warning, and error, respectively). Adjust the log threshold to control which messages are logged based on their level.

Finally, you can remove the appenders using `removeAppender()` to stop logging.

### Repos

``` R

```

## Filesystem

### Paths

1. Absolute path

   R doesnt have a built-in equivalent to Python's `pathlib`, but the `tidyverse` `readr` package has `read_file`.
```r
library(readr)
absolute_filepath <- "/Users/Desktop/Resources/file.txt"
file_content <- read_file(absolute_filepath)
```

2. Relative path
```r
relative_filepath <- "Resources/file.txt"
file_content <- read_file(relative_filepath)
# print current working directory with getwd()
print(paste0("Current Working Directory: ", getwd()))
```

Write to path

```r
output_path <- "output.txt"
text <- "Hello, world!"
write("This is an output file.", output_path)
write(text, output_path, append = TRUE)
```

Read file using a loop

```r
file_conn <- file(output_path, open = "r")
line_num <- 1

# loop through each line in the file
while(TRUE) {
  line <- readLines(file_conn, n = 1)
  if(length(line) == 0) { # End of file
    break
  }
  print(paste0("line ", line_num, ": ", line))
  line_num <- line_num + 1
}

close(file_conn)
```

Make relative path to current script location. Use `here` package to make paths relative to the current script location.

```r
library(here)
library(readr)

filepath <- here("data_dir", "input_dir")
filename <- "OnlineNewsPopularity.csv"
df <- read_csv(file.path(filepath, filename))
```

The `here()` function creates file paths that are relative to the top-level directory of your project. The top-level directory is usually the first parent directory that contains a `.Rproj` file, but it could also be any directory that contains a `.here` file or a `.git` file, or any directory that is recognized as a package by the `devtools` package.

### OS / File operations

These operations can be done using base R and the tidyverse `fs` library. The `fs` library provides a consistent, cross-platform API to replace many of the functions in base R for paths, directories, files, links, and so on.

#### Running processes

R doesn't have an equivalent of Python's `subprocess`, but does have `system` or `system2` functions from base R.

```r
pscp_cmd <- "pscp server-ssh:/path/test_file1.txt C:/cats/dogs"
system(pscp_cmd)
```

#### Get file size

```r
library(fs)
file_info("path/to/your/file")$size
```

#### Determine file size of everything in dir

```r
library(fs)
files <- dir_ls("C:/creds/")
file_info(files)$size
```

#### List all files in immediate subdirectory

```r
library(fs)
outbound <- "C:/Outbound"
subfolders <- dir_ls(outbound, recurse = 1)  # recurse = depth of subdirectories
for(subfolder in subfolders){
  files <- dir_ls(subfolder)
  for(file in files){
    if(str_detect(file, ".txt$")){
      print(file)
    }
  }
}
```

#### Copy files and preserve metadata

```r
library(fs)
i <- 0
for(subfolder in subfolders){
  files <- dir_ls(subfolder)
  for(file in files){
    if(str_detect(file, ".ORIGINAL.") & str_detect(file, ".xml$")){
      i <- i + 1
      print(i)
      print(paste0("copy from: ", subfolder, "/", file))
      print(paste0("copy to: ", filepath, file))
      # file_copy() preserves metadata
      file_copy(paste0(subfolder, "/", file), paste0(filepath, file))
    }
  }
}
```

#### Copy file to diff dir

```r
library(fs)
for(file in dir_ls(dir1)){
  if(str_detect(file, "cats.xlsx$", ignore.case = TRUE)){
    file_copy(paste0(dir1, file), paste0(dir2, file))
  }
}
```

#### List files in the source directory

```r
library(fs)
path_source <- "C:/1999"
source_charts <- dir_ls(path_source)
```

### write to file

#### write to csv, timestamped

`T` is a literal 'T' character (as per the ISO 8601 standard). It indicates the start of the time component.

``` r
library(tidyverse)

# write df to YYYY-MM-DDTHH:MM:SS
timestamp <- format(Sys.time(), "%Y-%m-%dT%H:%M:%S")
# however, some OS dont allow : and -, so remove bc ISO is dumb
timestamp <- format(Sys.time(), "%Y%m%dT%H%M%S")
filename <- paste0("my_df_", timestamp, ".csv")
write_csv(df, filename)
```

## Database

### various db connection settings

To connect to different databases, we can use the `DBI` package in conjunction with the specific DBI-compliant package.

1. PostgreSQL:

```r
library(DBI)
library(RPostgres)
con <- dbConnect(RPostgres::Postgres(), 
                 dbname = "your_database_name",
                 host = "localhost", 
                 port = 5432,
                 user = "your_username",
                 password = "your_password")
```

2. MySQL:

```r
library(DBI)
library(RMySQL)
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "your_database_name",
                 host = "localhost", 
                 port = 3306,
                 user = "your_username",
                 password = "your_password")
```

3. SQLite:

```r
library(DBI)
library(RSQLite)
con <- dbConnect(RSQLite::SQLite(), "your_database_name.sqlite")
```

4. MS SQL Server:

```r
library(DBI)
library(odbc)
con <- dbConnect(odbc::odbc(), 
                 Driver = "ODBC Driver 17 for SQL Server",
                 Server = "localhost", 
                 Database = "your_database_name",
                 UID = "your_username",
                 PWD = "your_password")
```

5. Oracle:

```r
library(DBI)
library(odbc)
con <- dbConnect(odbc::odbc(), 
                 Driver = "Oracle 12c ODBC driver",
                 DBQ = "localhost:1521/your_database_name", 
                 UID = "your_username",
                 PWD = "your_password")
```

Ensure you have ODBC drivers.

Also disconnect:

```r
dbDisconnect(con)
```

Depending, you might need to provide other arguments or use other methods for authentication, e.g. if SSL connection.

### full query (postgres)

``` r
library(DBI)
library(RPostgres)

con <- dbConnect(RPostgres::Postgres(),
                 dbname = "dvdrental",
                 host = "localhost", 
                 port = 5432,
                 user = POSTGRES_USERNAME,
                 password = POSTGRES_PASSWORD)

query <- "
        select
            a.title
        from film a
        "

film_df <- dbGetQuery(con, query)
dbDisconnect(con)
```

### full query (best practices)

`Sys.getenv()` to access creds as env variables. Do this bc sometimes things like connection strings or username password may change, prompting code changes. Also keeps it out of git.

Also, you should always handle exceptions when dealing with connections or IO. Disconnect from the db even if error, using `finally`.

Also, `tidyverse`.

``` r
library(DBI)
library(RPostgres)
library(dplyr)
library(dbplyr)

# get externalized creds
POSTGRES_USERNAME <- Sys.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD <- Sys.getenv("POSTGRES_PASSWORD")

# check creds found
if (POSTGRES_USERNAME == "" | POSTGRES_PASSWORD == "") {
  stop("db creds not found.")
}

con <- NULL
tryCatch({
  con <- dbConnect(RPostgres::Postgres(),
                   dbname = "dvdrental",
                   host = "localhost", 
                   port = 5432,
                   user = POSTGRES_USERNAME,
                   password = POSTGRES_PASSWORD)
  # sql free
  film_df <- tbl(con, "film") %>%
              select(title, rating) %>%
              collect()
}, error = function(e) {
  print(paste("An error has occurred:", e$message))
}, finally = {
  if (!is.null(con)) {
    dbDisconnect(con)
  }
})
```

### Read data in chunks for faster results

`dplyr` and `dbplyr` don't have built-in functions to read data in chunks, so use lower-level DBI functions.

``` r
library(DBI)
library(RPostgres)
con <- dbConnect(RPostgres::Postgres(), 
                 dbname = "dvdrental",
                 host = "localhost", 
                 port = 5432,
                 user = "your_username",
                 password = "your_password")

rs <- dbSendQuery(con, "SELECT title, rating FROM film")
while(!dbHasCompleted(rs)) {
  chunk <- dbFetch(rs, n = 100)
  # replace with your processing function
}

dbClearResult(rs)
dbDisconnect(con)
```

### make sure to filter for fast retrieval

``` r
con <- dbConnect(RPostgres::Postgres(), 
                 # ...
                )

df <- tbl(con, "film") %>% 
  filter(rating == 'PG', length < 120) %>%
  collect()
dbDisconnect(con)
```

## Speed enhancements

### fast

`.fst` is a binary data file format specifically designed to store df. It serializes/deserializes, while the format allows for random access to rows within the file.

Main benefit of `fst` is speed, and also supports multi-threaded operation for even faster performance.

``` r
if (!require(fst)) {
  install.packages("fst")
}
library(fst)

write_fst(mtcars, "mtcars.fst")  # export df to .fst
mtcars2 <- read_fst("mtcars.fst")  # import df from .fst

# mtcars2 remains identical to mtcars
identical(mtcars, mtcars2)  # TRUE
```

`read_fst` does read rows in the same order each time. The 'random access' feature doesn't mean that data is read in a nonsequential order by default, but rather gives the option to access any subset of rows directly, in any order you want.

To control what rows it accesses, use:

``` r
# read rows 500,001 to 600,000
data_subset <- read_fst("my_data.fst", from = 500001, to = 600000)
```

## Utility

### memory, cpu

``` r
library(pryr)

# print CPU usage
cpu_percent <- Sys.getloadavg()[1] * 100
cat("CPU Usage %:", cpu_percent, "\n")

# print memory usage
memory_info <- mem_used()
memory_percent <- memory_info * 100 / mem_total()
cat("Memory Usage %:", memory_percent, "\n")
```

- The `Sys.getloadavg()[1]` function returns the CPU load average, and multiplying it by 100 gives the CPU usage percentage.

### beep boop beep

``` r
library(beepr)
beep(sound = 5, duration = 0.015)
```

### timer / stopwatch

``` r
t1 <- Sys.time()
# Perform operations here
t2 <- Sys.time()
execution_time <- t2 - t1
cat("\nexecution_time:", execution_time, "\n")
```

### Archive / zip

`utils` package for archiving, and `readr` package for reading and writing CSV files.

#### Extract zip content, unzip:

```R
filepath <- "C:/scripts/"
filename <- "file.zip"
wanted_zip_content <- "file.xlsx"

# extract the desired file
unzip(filepath + filename, files = wanted_zip_content, exdir = ".", overwrite = TRUE)
```

#### Zip a data frame or CSV:

```R
library(readr)
library(utils)

# define path, name, and compression options
filepath <- "path/to/destination/"
pull_date <- "2023-06-09"
table <- "your_table_name"
compression_options <- "zip"

# write df to csv
write_csv(df_all, file.path(filepath, paste0(pull_date, "_", table, ".csv")))
# archive csv
zip(filepath, paste0(pull_date, "_", table, ".csv"), compression = compression_options)
```

### Email

#### Send an email

``` r
library(RDCOMClient)
# create an Outlook application object
outlook_app <- COMCreate("Outlook.Application")
# create a mail item
mail <- outlook_app$CreateItem(0)

mail[["To"]] <- "garth.mortensen@cool.com"
mail[["Subject"]] <- "This is the Subject"
mail[["Body"]] <- "This is the body"

# send
mail$Send()
# Release the Outlook application object
outlook_app$Release()
```

## APIs

### Create APIs

`api.R`:

``` r
library(plumber)

#* @get /square
function(n=1){
  as.numeric(n)^2
}
```

`r console` or from another script:

``` r
r <- plumb("api.R")
r$run(port=8000)
```

then go to `localhost:8000/square?n=10` and get `100` back. done.

### Consume APIs

The most common library, which is also part of tidyverse, is `httr`.

``` r
# install.packages(c("httr", "jsonlite"))
library(httr)

# define endpoint
url <- "http://localhost:8000/square"
query_params <- list(n = 5)
response <- GET(url, query = query_params)
print(http_status(response)$message)

# if request successful, print
if(http_status(response)$category == "Success"){
  print(content(response, "text", encoding = "UTF-8"))
}
```

Make a standard request.

``` r
library(httr)
library(jsonlite)

url <- "http://api.worldbank.org/v2/country/us/indicator/NY.GDP.MKTP.CD?format=json"
response <- GET(url)

# get and parse the data
response_content <- content(response, as = "text")
data <- fromJSON(response_content)

# print the formatted JSON output
cat(toJSON(data, auto_unbox = TRUE, pretty = TRUE))
# extract the country value
country <- data[[2]][[2]]$country$value
```

## Heroku 12 factors, applied

Though I've addressed some of these above, I haven't finished with all. 

`logging` vs `log4r`?

The 12-factor methodology is a set of best practices for building scalable and maintainable web apps.

1. **Codebase**: Keep your codebase in a version control system like Git.
2. **Dependencies**: Use a package management system like CRAN or Bioconductor to manage your R package dependencies. Specify the required packages in your project's `DESCRIPTION` file or using a package management tool like `renv`.
3. **Config**: Store your application configuration, such as API keys or database URLs, in environment variables. Access environment variables using `Sys.getenv()`.
4. **Backing services**: Treat any external services your application depends on, like databases or APIs, as attached resources. Use appropriate R packages (e.g., `DBI` for databases) to connect and interact with these services. Store the service connection details in the configuration (env vars) and access them within your R code.
5. **Build, release, run**: Separate the build, release, and run stages of your application. Use tools like `devtools` to build and package your R application. Release the packaged application, and then use it to run in your target environment.
6. **Processes**: Execute your R application as stateless processes. In tidyverse-based applications, you typically have scripts or functions that can be executed independently. Avoid storing application state in memory or relying on global variables.
7. **Port binding**: R applications, especially web-based ones, can be hosted using frameworks like Shiny or Plumber. These frameworks handle the port binding for you.
8. **Concurrency**: R is primarily a single-threaded language, but you can leverage parallel processing using packages like `parallel` or `future`. If your application requires concurrent execution, design your code to work with these parallelization libraries.
9. **Disposability**: Design your application to be easily started and stopped. In the tidyverse, this can mean encapsulating your code within functions that can be called on-demand. Make sure any temporary or cached files are properly managed and cleaned up.
10. **Dev/prod parity**: Aim for consistency between development, staging, and production environments. Use tools like `renv` or `packrat` to manage the exact versions of packages used in different environments. Ensure your application can easily transition between these environments without unexpected behavior.
11. **Logs**: Implement logging in your R application to capture relevant information and errors. Packages like `logging` or `log4r` can help you manage and output log messages. Consider using a centralized log management solution for storing and analyzing logs.
12. **Admin processes**: Provide administrative and management tasks as one-off processes, also known as "admin scripts." These scripts can perform tasks like database migrations or data import/export. Use R scripts or functions that can be executed independently to perform these tasks.