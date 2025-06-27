# r_basics.md

> Before I had studied Chan for thirty years, I saw mountains as mountains, and rivers as rivers. When I arrived at a more intimate knowledge, I came to the point where I saw that mountains are not mountains, and rivers are not rivers. But now that I have got its very substance I am at rest. For it's just that I see mountains once again as mountains, and rivers once again as rivers.

[TOC]

## Data types

1. **Numerics**
    - Integer:
        - Python: `int`
        - R: `integer`
    
    - Floating point:
        - Python: `float`
        - R: `numeric` or `double`
    
    - Complex numbers:
        - Python: `complex`
        - R: `complex`
    
2. **Sequences**
    - Strings:
        - Python: `str`
        - R: `character`
    
    - Lists (ordered, changeable/mutable, allows duplicate members):
        - Python: `list`
        - R: `list`
    
    - Arrays (ordered collection of items of the same type):
        - Python: `array` (or `numpy.array` in NumPy)
        - R: `vector` or `matrix` or `array`
    
    - Tuple (ordered, unchangeable/immutable, allows duplicate members):
        - Python: `tuple`
        - R: No exact equivalent, but you could use `list` or `vector`
    
    - Range (immutable sequence of numbers):
        - Python: `range`
        - R: `seq` or `:` operator
    
3. **Set Types** (unordered collection of unique elements):
    - Set:
        - Python: `set`
        - R: No built-in set type, but can be emulated using `vector` and some functions
    
4. **Mapping Types**

    - Dictionary (unordered, changeable/mutable, indexed, does not allow duplicates):
        - Python: `dict`
        - R: `list` (especially named lists) or `environment`

5. **Boolean Type**

    - Python: `bool` (`True`, `False`)
    - R: `logical` (`TRUE`, `FALSE`)

6. **Other Types**

    - Null/None value:
        - Python: `None`
        - R: `NULL`

7. **Data Frames**

    - Python: `pandas.DataFrame`
    - R: `data.frame`

8. **Factors**
    - Python: No equivalent, but `pandas.Categorical` can be used as a similar feature.
    - R: `factor`

In R, vectors and lists are the fundamental data structures and many other types are built on top of them. For example, a data frame in R is essentially a list of vectors of the same length. R also has a few data types not present in Python, such as factors, which are used to handle categorical data.

Here's a table showing the equivalent data types and structures in Python and R:

| Python             | R                                               |
| ------------------ | ----------------------------------------------- |
| int                | integer                                         |
| float              | numeric / double                                |
| complex            | complex                                         |
| str                | character                                       |
| list               | list                                            |
| array              | vector / matrix / array                         |
| tuple              | list / vector (no exact equivalent)             |
| range              | seq / : operator                                |
| set                | vector with unique values (no exact equivalent) |
| dict               | list (especially named lists) / environment     |
| bool               | logical                                         |
| None               | NULL                                            |
| pandas.DataFrame   | data.frame                                      |
| pandas.Categorical | factor                                          |

### Primitives

#### Integer

``` r
a <- 10
```

Common methods include: `as.numeric()`, `is.numeric()`, `round()`, `ceiling()`, `floor()`.

#### numeric/double = L

``` r
b <- 10L
```

`as.integer()`, `is.integer()`

#### character

``` r
d <- "Hello, world!"
```

`as.character()`, `is.character()`, `nchar()`, `substr()`, `strsplit()`, `paste()`, `paste0()`

#### logical

``` r
e <- TRUE
```

 `as.logical()`, `is.logical()`, `any()`, `all()`, `which()`, `!()`, `&()`, `|()`

### Data Structures

For holding collections of primitives or other data structures.

#### vector

``` r
v1 <- c(1, 2, 3)
```

#### matrix

``` r
m1 <- matrix(1:6, nrow = 2, ncol = 3)
```

#### array

n-dimensional matrix

``` r
a1 <- array(data = 1:24, dim = c(4,3,2))
```

#### list

``` r
# hetero
l1 <- list(Numbers = 1:4, Letters = LETTERS[1:4], Another_List = list(10, "Hello"))
```

##### Iterate through a named list:

emulate the following py code:

``` python
for k, v in dict.items():  # dict.items() is the view
	print(k, v)
```

in r:

``` r
# create named list (like py dict)
my_list <- list("a" = 1, "b" = 2, "c" = 3)

for (name in names(my_list)) {
  value <- my_list[[name]]
  print(paste(name, value))
}
```

Tidyverse encourages purrr though:

``` r
library(purrr)
my_list <- list("a" = 1, "b" = 2, "c" = 3)
# v1
walk2(names(my_list), my_list, ~print(paste(.x, .y)))
# v2
walk2(names(my_list), my_list, ~print(paste(key = .x, value = .y)))
```

`walk2` is a variant of `map2` designed for functions with side effects like printing. It iterates over two inputs (in this case, the names and values of `my_list`). The `~print(paste(.x, .y))` part is shorthand for a function that takes two args.

##### define named list

the py:

``` py
raw_tx = {
    "to": receiver,
    "from": account.address,
    "value": wei_value,
}
```

the r:

``` r
receiver <- "receiver_address"
account_address <- "account_address"
wei_value <- 1000000

raw_tx <- list(
  "to" = receiver,
  "from" = account_address,
  "value" = wei_value,
)
```

`list()` is analogous to py `{}`. The `=` operator is used for assigning values to names within the list, similar to the `:` operator in Python dictionaries.

##### Add new key-value pair

the py:

``` python
# Add a new key-value pair
trading_pnl["04-07-2019"] = 413
```

the r:

``` r
# Add a new key-value pair
trading_pnl <- list("01-01-2019" = 100, "02-01-2019" = 200)
trading_pnl["04-07-2019"] <- 413
```

##### list of lists

the py:

``` python
battlestars =
[{'Ship': 'Pegasus',
  'Commander': 'Admiral Helena Cain',
  'Pilots': ['Whiplash', 'Thumper']},
 {'Ship': 'Galactica',
  'Commander': 'Admiral William Adama',
  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}]

battlestars[1]
# {'Ship': 'Galactica',
#  'Commander': 'Admiral William Adama',
#  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}

battlestars[1]['Pilots']
# ['Starbuck', 'Apollo', 'Helo', 'Athena']

battlestars[1]['Pilots'][1]
# 'Apollo'
```

the r:

``` r
# Define the data structure
battlestars <- list(
  list(
    Ship = "Pegasus",
    Commander = "Admiral Helena Cain",
    Pilots = c("Whiplash", "Thumper")
  ),
  list(
    Ship = "Galactica",
    Commander = "Admiral William Adama",
    Pilots = c("Starbuck", "Apollo", "Helo", "Athena")
  )
)

# Access elements of the list
battlestars[[1]]
# $Ship
# [1] "Pegasus"
#
# $Commander
# [1] "Admiral Helena Cain"
#
# $Pilots
# [1] "Whiplash" "Thumper" 

battlestars[[1]]$Pilots
# [1] "Whiplash" "Thumper"

battlestars[[1]]$Pilots[1]
# [1] "Whiplash"
```

##### Create dataframe from lists (05.2)

py:

```python
value_data = {
"MSFT": [msft_value],
"AAPL": [aapl_value]
}
df_value = pd.DataFrame(value_data)
```

r:

``` r
msft_value <- c(123.45, 125.67, 127.89)
aapl_value <- c(234.56, 236.78, 238.90)

value_data <- list(
  MSFT = c(msft_value),
  AAPL = c(aapl_value)
)
df_value <- data.frame(value_data)
```

In R, lists are called vectors, and instead of Python's list operations, R has built-in functions that can be used to achieve the same result. The following is how the Python code you provided can be rewritten in R (tidyverse).

##### Slicing

py comments over r

```r
# name_list = ['Elliot' ,'Darlene', 'Angela', 'Shayla']
name_vector <- c('Elliot' ,'Darlene', 'Angela', 'Shayla')

# name_list[0:2]
name_vector[1:2]
# ['Elliot' ,'Darlene']

# name_list[2:4]
name_vector[3:4]
# ['Angela', 'Shayla']

# name_list[0:4:2]
name_vector[seq(1, 4, 2)]
# ['Elliot', 'Angela']
```

Pop and remove:

```r
# pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx"]
pokemon <- c("Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx")

# pokemon.remove("Magikarp") or pop
pokemon <- pokemon[!(pokemon %in% "Magikarp")]
```

Create a very long list:

```r
# k = list(range(1, 1000))
k <- seq(1, 1000)
```

Count occurrences of an element in a list:

```r
# listy = ["h", "p", "l", "m", "h", "p", "h"]
listy <- c("h", "p", "l", "m", "h", "p", "h")

# listy.count("h")
sum(listy == "h")
```

Make a list distinct. R is much nicer here!

```r
# my_list = list(set(my_list))
my_list <- unique(my_list)
```

Flatten a list of lists:

```r
# flat_list = []
# for sublist in events:
#     for item in sublist:
#         flat_list.append(item)
flat_list <- unlist(events)
```

Writing list to a file:

```r
# file_write = "C:/list_of_articles.txt"
# with open(file_write, "w") as f:
#     f.write("all_articles\n")
#     for item in files_in_dir:
#         f.write(item+"\n")
file_write <- "C:/list_of_articles.txt"
writeLines(c("all_articles", files_in_dir), file_write)
```

#### factor

``` r
f1 <- factor(c("male", "female", "female", "male"))
```

#### dataframe

``` r
df <- data.frame(Numbers = 1:4, Letters = LETTERS[1:4])
```

#### tibble

Tibbles are a part of the `tidyverse`. A modern reimagining of the df. More user-friendly.

**Printing**: Tibbles have a nicer print method. They show only the first 10 rows and all columns.

**Subsetting**: With tibbles, if you try to access a column that doesn't exist, error. In base R data frames, it returns `NULL`.

**Row names**: By default, tibbles do not have row names. They do allow row names for compatibility with existing code, but discouraged.

**Compatibility**: Tibbles work with other `tidyverse` packages. For example, if you use `dplyr` functions like `mutate()`, `select()`, `filter()`, result in a tibble.

``` r
library(tidyverse)
tb1 <- tibble(Numbers = 1:4, Letters = LETTERS[1:4])
```

### Nested structures

#### python's list of lists

py:

``` python
ceo_nested_list = [
    ["Warren Buffet", 88, "CEO of Berkshire Hathaway"],
    ["Jeff Bezos", 55, "CEO of Amazon"],
    ["Harry Markowitz", 91, "Professor of Finance"]
]
```

r - this is the same as dictionary of lists and nested dict. It's all pretty much covered by tidyverse...

``` r
ceo_nested_df <- data.frame(
  name = c("Warren Buffet", "Jeff Bezos", "Harry Markowitz"),
  age = c(88, 55, 91),
  occupation = c("CEO of Berkshire Hathaway", "CEO of Amazon", "Professor of Finance")
)
```

tidy:

``` r
ceo_nested_tibble <- tibble(
  name = c("Warren Buffet", "Jeff Bezos", "Harry Markowitz"),
  age = c(88, 55, 91),
  occupation = c("CEO of Berkshire Hathaway", "CEO of Amazon", "Professor of Finance")
)
```

#### python's nested dict

r - this is the same as dictionary of lists and nested dict. It's all pretty much covered by tidyverse...

``` r
stocks_nested_df <- tibble(
  ticker = c("APPL", "MU", "AMD", "TWTR"),
  name = c("Apple", "Micron Technology", "Advanced Micro Devices", "Twitter"),
  exchange = c("NASDAQ", "NASDAQ", "NASDAQ", "NASDAQ"),
  market_cap = c(937.7, 48.03, 29.94, 26.42)
)

twitter_market_cap <- filter(stocks_nested_df, ticker == "TWTR")$market_cap

print(paste0("Name of TWTR ticker is ", filter(stocks_nested_df, ticker == "TWTR")$name, 
              ". TWTR is available on ", filter(stocks_nested_df, ticker == "TWTR")$exchange, 
              ", and it currently has a market capitalization of ", twitter_market_cap, "."))
```

#### python's list of dictionaries

r - this is the same as dictionary of lists and nested dict. It's all pretty much covered by tidyverse...

``` r
ceo_nested_df <- tibble(
  name = c("Warren Buffet", "Jeff Bezos", "Harry Markowitz"),
  age = c(88, 55, 91),
  occupation = c("CEO of Berkshire Hathaway", "CEO of Amazon", "Professor of Finance")
)

second_entry_occupation <- ceo_nested_df$occupation[2]

print(paste0("The second entry in ceo_nested_dict is ", ceo_nested_df$name[2], 
              ", a ", ceo_nested_df$age[2], " year old ", second_entry_occupation, "."))

```

## Conditionals

Nested if statements with insurance premium predictor.

``` r
accident <- TRUE
at_fault <- FALSE
accident_forgiveness <- TRUE
elite_status <- TRUE
increase_insurance_premium <- TRUE

# Nested Conditional Statements
# Insurance premium will increase. True or False?
if (accident) {
    if (at_fault & accident_forgiveness) {
        increase_insurance_premium <- FALSE
    } else if (at_fault & !accident_forgiveness & !elite_status) {
        increase_insurance_premium <- TRUE
    } else {
        increase_insurance_premium <- FALSE
    }
} else if (!accident & elite_status) {
    increase_insurance_premium <- FALSE
} else {
    increase_insurance_premium <- TRUE
}

# cat prints to console
cat(paste0("Prediction: ", increase_insurance_premium), "\n")
```

## Exceptions (with logs)

Here, error is sent both to log file and the standard output by using two separate `cat()` functions. The `error_message` variable stores the formatted error message, which is then passed to `cat()` with the `file` argument set to `log_conn` to write it to the log file. `cat()` is used again without the `file` argument to write the error message to the standard output (stdout).

``` r
library(tidyverse)

convert <- function(x) {
  as.numeric(x)
}

log_file <- "error.log"
log_conn <- file(log_file, open = "a")

tryCatch(
  {
    # call the function
    convert(temps1)
    convert(temps2)
  },
  error = function(e) {
    error_message <- paste("There was an error:", conditionMessage(e))
    cat(error_message, "\n", file = log_conn)
    cat(error_message, "\n")
  }
)
close(log_conn)
```

## Loops

### range loops

The `:` operator generates a sequence from the first number to the second number, inclusive. It's equivalent to the Python `range()` function. `seq()`is more flexible and can generate sequences with a specified increment.

``` r
# basic loop 1
for (x in 0:4) {
  print(x)
}

# basic loop 2
for (x in 2:6) {
  print(x)
}

```

### loop while

svDialogs has been added to support user input/interactivity.

``` r
library(svDialogs)

# Loop while a condition is being met
run <- TRUE
while (run) {
  message("Hi!")
  run <- dlg_input("To run again. Enter 'y'")$res == "y"
}
```

### for loops

``` r
# typical technique:
colors <- c("red", "green", "blue", "purple")
for (color in colors) {
  print(color)
}

# c style loop allows us to loop over a list and retrieve both the index and value:
presidents <- c("Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson")
for (i in seq_along(presidents)) {
  print(paste("President", i, ":", presidents[i]))
}
```

### purrr loops

Using the same code as for loops section, converted to use purrr library.

``` r
library(purrr)

# typical technique:
colors <- c("red", "green", "blue", "purple")
walk(colors, print)

# c style loop allows us to loop over a list and retrieve both the index and value:
presidents <- c("Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson")
walk(seq_along(presidents), ~print(paste("President", .x, ":", presidents[.x])))
```

### breaks

``` r
desired_number <- 5
for (x in 0:9) {
  if (x == desired_number) {
    break
  }
  print(x)
}
```

### loop with increment

``` r
i <- 1
while (i < 6) {
  print(i)
  i <- i + 1
}
```

### stoppable while true

```r
uniform <- TRUE
while (uniform) {
  print("Ring up customers")
}
```

## functions

### simple

``` r
something <- function(article) {
  output <- article
  return(output)
}

crude_oil_articles <- "your_articles_here"

result <- something(crude_oil_articles)
```

### Single line functions

#### lapply

This is similar to python list comprehensions...but you still need to define the function elsewhere.

``` r
coding_complete <- c("file1", "file2", "file3")
coding_complete_pdf <- lapply(coding_complete, function(do_something) paste0(do_something, ".pdf"))
```

#### purrr

``` r
library(purrr)
coding_complete <- c("file1", "file2", "file3")
coding_complete_pdf <- map_chr(coding_complete, ~paste0(.x, ".pdf"))
```

### dictionary comprehension equivalent

the python

``` python
metrics = {k: v for k, v in zip(model.metrics_names, scores)}
```

the r

``` r
model_metrics_names <- c("name1", "name2", "name3")
scores <- c(1, 2, 3)
metrics <- setNames(object = scores, nm = model_metrics_names)
```

above, `metrics` is a datatype called "named vector". Keys are called "names", and values are called "components".

**name: components**

### apply function to dataframe column

this section is an evolution from starting python to modern r.

#### my python

``` python
def changeGender(gender):
    if gender == "Male":
        return 1
    else:
        return 0
df["Gender"] = df["Gender"].apply(changeGender)
```

#### first python to r approach

``` r
changeGender <- function(gender) {
  ifelse(gender == "Male", 1, 0)
}

df$Gender <- sapply(df$Gender, changeGender)
```

#### base r

``` r
df$Gender <- ifelse(df$Gender == "Male", 1, 0)
```

#### tidyverse approach

``` r
library(dplyr)

df <- df %>%
  mutate(Gender = if_else(Gender == "Male", 1, 0))
```