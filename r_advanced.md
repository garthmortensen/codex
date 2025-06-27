# r_advanced.md

> Before I had studied Chan for thirty years, I saw mountains as mountains, and rivers as rivers. When I arrived at a more intimate knowledge, I came to the point where I saw that mountains are not mountains, and rivers are not rivers. But now that I have got its very substance I am at rest. For it's just that I see mountains once again as mountains, and rivers once again as rivers.

[TOC]

## Data Analysis & Statistics

### Statistical Functions

Basic statistical operations in R:

```r
# Basic statistics
data <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mean(data)
median(data)
sd(data)  # standard deviation
var(data)  # variance
quantile(data, c(0.25, 0.5, 0.75))
summary(data)
```

### Correlation and Regression

```r
# Correlation
cor(mtcars$mpg, mtcars$wt)
cor(mtcars[, c("mpg", "wt", "hp")])

# Linear regression
model <- lm(mpg ~ wt + hp, data = mtcars)
summary(model)
plot(model)

# Predictions
predict(model, newdata = data.frame(wt = 3.2, hp = 120))
```

### Hypothesis Testing

```r
# t-test
t.test(mtcars$mpg[mtcars$am == 0], mtcars$mpg[mtcars$am == 1])

# chi-square test
chisq.test(table(mtcars$am, mtcars$vs))

# ANOVA
aov_model <- aov(mpg ~ factor(cyl), data = mtcars)
summary(aov_model)
```

## Data Visualization

### Base R Plotting

```r
# Basic plots
plot(mtcars$wt, mtcars$mpg)
hist(mtcars$mpg)
boxplot(mpg ~ cyl, data = mtcars)
barplot(table(mtcars$cyl))

# Customization
plot(mtcars$wt, mtcars$mpg, 
     main = "MPG vs Weight", 
     xlab = "Weight", 
     ylab = "Miles per Gallon",
     col = "blue", 
     pch = 19)
```

### ggplot2 Advanced

```r
library(ggplot2)
library(dplyr)

# Basic ggplot
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm") +
  labs(title = "MPG vs Weight", x = "Weight", y = "Miles per Gallon")

# Faceting
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  facet_wrap(~ cyl) +
  theme_minimal()

# Multiple aesthetics
ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl), size = hp)) +
  geom_point(alpha = 0.7) +
  scale_color_viridis_d() +
  theme_classic()
```

### Interactive Visualizations

```r
library(plotly)

# Convert ggplot to interactive
p <- ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point()
ggplotly(p)

# Direct plotly
plot_ly(mtcars, x = ~wt, y = ~mpg, color = ~factor(cyl), type = "scatter", mode = "markers")
```

## Data Manipulation Advanced

### dplyr Advanced Operations

```r
library(dplyr)
library(tidyr)

# Complex grouping and summarizing
mtcars %>%
  group_by(cyl, am) %>%
  summarise(
    mean_mpg = mean(mpg),
    sd_mpg = sd(mpg),
    count = n(),
    .groups = "drop"
  ) %>%
  arrange(desc(mean_mpg))

# Window functions
mtcars %>%
  group_by(cyl) %>%
  mutate(
    mpg_rank = rank(desc(mpg)),
    mpg_percentile = percent_rank(mpg),
    running_avg = cumsum(mpg) / row_number()
  )

# Complex joins
left_join(df1, df2, by = c("key1", "key2"))
anti_join(df1, df2, by = "key")  # rows in df1 not in df2
```

### Data Reshaping

```r
library(tidyr)

# Pivot operations
data_wide <- mtcars %>%
  rownames_to_column("car") %>%
  select(car, cyl, mpg, hp) %>%
  pivot_wider(names_from = cyl, values_from = c(mpg, hp))

data_long <- data_wide %>%
  pivot_longer(cols = -car, 
               names_to = c(".value", "cylinder"), 
               names_sep = "_")

# Nesting data
nested_data <- mtcars %>%
  group_by(cyl) %>%
  nest()

# Apply functions to nested data
nested_results <- nested_data %>%
  mutate(
    models = map(data, ~ lm(mpg ~ wt, data = .x)),
    summaries = map(models, summary),
    r_squared = map_dbl(summaries, ~ .x$r.squared)
  )
```

## String Processing

### stringr Package

```r
library(stringr)

# String detection and extraction
text <- c("apple", "banana", "cherry", "date")
str_detect(text, "a")
str_extract(text, "[aeiou]")
str_extract_all(text, "[aeiou]")

# String manipulation
str_to_upper(text)
str_to_lower(text)
str_to_title(text)
str_length(text)
str_sub(text, 1, 3)

# Pattern replacement
str_replace(text, "a", "X")
str_replace_all(text, "[aeiou]", "X")

# String splitting and combining
str_split("a,b,c", ",")
str_c(text, collapse = ", ")
```

### Regular Expressions

```r
# Common regex patterns
email_pattern <- "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"
phone_pattern <- "\\(?\\d{3}\\)?[-.]?\\d{3}[-.]?\\d{4}"
url_pattern <- "https?://[\\w\\.-]+\\.[a-zA-Z]{2,}"

# Extract patterns
text <- "Contact me at john@example.com or 555-123-4567"
str_extract_all(text, email_pattern)
str_extract_all(text, phone_pattern)
```

## Functional Programming

### purrr Package

```r
library(purrr)

# Map functions
numbers <- 1:5
map(numbers, ~ .x^2)
map_dbl(numbers, ~ .x^2)
map_chr(numbers, ~ paste("Number", .x))

# Map over multiple inputs
map2(1:3, 4:6, ~ .x + .y)
pmap(list(a = 1:3, b = 4:6, c = 7:9), ~ ..1 + ..2 + ..3)

# Functional composition
add_one <- function(x) x + 1
multiply_by_two <- function(x) x * 2
composed_func <- compose(multiply_by_two, add_one)
composed_func(5)  # (5 + 1) * 2 = 12

# Safely handle errors
safe_log <- safely(log)
safe_log(-1)  # Returns list with result and error
```

### Advanced Function Techniques

```r
# Function factories
make_power_function <- function(exponent) {
  function(x) {
    x^exponent
  }
}

square <- make_power_function(2)
cube <- make_power_function(3)
square(4)  # 16
cube(4)   # 64

# Closures
make_counter <- function() {
  count <- 0
  function() {
    count <<- count + 1
    count
  }
}

counter1 <- make_counter()
counter1()  # 1
counter1()  # 2
```

## Object-Oriented Programming

### S3 Classes

```r
# Create S3 class
person <- function(name, age) {
  structure(
    list(name = name, age = age),
    class = "person"
  )
}

# S3 methods
print.person <- function(x, ...) {
  cat("Person:", x$name, "- Age:", x$age, "\n")
}

summary.person <- function(object, ...) {
  cat("Summary of person:\n")
  cat("Name:", object$name, "\n")
  cat("Age:", object$age, "\n")
  if (object$age >= 18) {
    cat("Status: Adult\n")
  } else {
    cat("Status: Minor\n")
  }
}

# Usage
john <- person("John", 25)
print(john)
summary(john)
```

### R6 Classes

```r
library(R6)

# Define R6 class
Person <- R6Class("Person",
  public = list(
    name = NULL,
    age = NULL,
    
    initialize = function(name, age) {
      self$name <- name
      self$age <- age
    },
    
    greet = function() {
      cat("Hello, my name is", self$name, "\n")
    },
    
    have_birthday = function() {
      self$age <- self$age + 1
      cat("Happy birthday! Now", self$age, "years old.\n")
    }
  ),
  
  private = list(
    secret = "This is private"
  ),
  
  active = list(
    status = function() {
      if (self$age >= 18) "Adult" else "Minor"
    }
  )
)

# Usage
john <- Person$new("John", 25)
john$greet()
john$have_birthday()
cat("Status:", john$status, "\n")
```

## Time Series Analysis

### Basic Time Series

```r
# Create time series
ts_data <- ts(c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), start = c(2020, 1), frequency = 12)

# Time series operations
plot(ts_data)
decompose(ts_data)
diff(ts_data)  # First difference

# Moving averages
library(forecast)
ma(ts_data, order = 3)  # 3-period moving average
```

### lubridate for Dates

```r
library(lubridate)

# Parse dates
dates <- c("2023-01-15", "15/01/2023", "January 15, 2023")
ymd(dates[1])
dmy(dates[2])
mdy("01/15/2023")

# Date arithmetic
today() + days(30)
now() + hours(2)
floor_date(now(), "month")
ceiling_date(now(), "month")

# Extract components
date <- ymd_hms("2023-01-15 14:30:00")
year(date)
month(date)
day(date)
hour(date)
wday(date, label = TRUE)
```

## Performance Optimization

### Profiling Code

```r
# Profile code performance
library(profvis)

profvis({
  # Your code here
  x <- rnorm(1000000)
  y <- x^2
  z <- sum(y)
})

# Benchmark functions
library(microbenchmark)

microbenchmark(
  method1 = sum(1:1000),
  method2 = Reduce("+", 1:1000),
  times = 100
)
```

### Parallel Processing

```r
library(parallel)
library(foreach)
library(doParallel)

# Detect cores
detectCores()

# Parallel apply
cl <- makeCluster(4)
parLapply(cl, 1:10, function(x) x^2)
stopCluster(cl)

# foreach parallel
registerDoParallel(cores = 4)
result <- foreach(i = 1:10, .combine = c) %dopar% {
  i^2
}

# Future package
library(future)
plan(multisession)
future_map(1:10, ~ .x^2)
```

### Memory Management

```r
# Check memory usage
object.size(mtcars)
pryr::object_size(mtcars)

# Memory profiling
library(profmem)
p <- profmem({
  x <- rnorm(1000)
  y <- x^2
})

# Garbage collection
gc()

# Memory-efficient operations
# Use data.table for large datasets
library(data.table)
dt <- as.data.table(mtcars)
dt[, mean_mpg := mean(mpg), by = cyl]  # More memory efficient than dplyr for large data
```

## Web Scraping & APIs

### rvest for Web Scraping

```r
library(rvest)

# Scrape a webpage
url <- "https://example.com"
page <- read_html(url)

# Extract elements
titles <- page %>%
  html_elements("h1") %>%
  html_text()

links <- page %>%
  html_elements("a") %>%
  html_attr("href")

# Extract tables
tables <- page %>%
  html_table()
```

### Advanced API Consumption

```r
library(httr)
library(jsonlite)

# API with authentication
api_key <- "your_api_key"
headers <- add_headers(Authorization = paste("Bearer", api_key))

response <- GET("https://api.example.com/data", headers)

# Handle pagination
get_all_pages <- function(base_url) {
  all_data <- list()
  page <- 1
  
  repeat {
    response <- GET(paste0(base_url, "?page=", page))
    data <- fromJSON(content(response, "text"))
    
    if (length(data$results) == 0) break
    
    all_data[[page]] <- data$results
    page <- page + 1
  }
  
  bind_rows(all_data)
}
```

## Machine Learning Basics

### Basic ML with caret

```r
library(caret)

# Data preparation
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = 0.8, list = FALSE)
train_data <- iris[trainIndex, ]
test_data <- iris[-trainIndex, ]

# Train model
model <- train(Species ~ ., 
               data = train_data, 
               method = "rf",
               trControl = trainControl(method = "cv", number = 5))

# Predictions
predictions <- predict(model, test_data)
confusionMatrix(predictions, test_data$Species)
```

### tidymodels Framework

```r
library(tidymodels)

# Define recipe
recipe <- recipe(Species ~ ., data = iris) %>%
  step_normalize(all_numeric()) %>%
  step_dummy(all_nominal(), -all_outcomes())

# Define model
rf_model <- rand_forest() %>%
  set_engine("ranger") %>%
  set_mode("classification")

# Create workflow
workflow <- workflow() %>%
  add_recipe(recipe) %>%
  add_model(rf_model)

# Fit model
fit <- workflow %>%
  fit(data = iris)

# Predictions
predictions <- fit %>%
  predict(new_data = iris)
```

## Package Development

### Creating Packages

```r
library(devtools)
library(usethis)

# Create new package
create_package("~/mypackage")

# Add functions
use_r("my_function")

# Add dependencies
use_package("dplyr")
use_pipe()  # Add %>% operator

# Documentation
use_roxygen_md()
document()

# Testing
use_testthat()
use_test("my_function")

# Vignettes
use_vignette("introduction")

# Check package
check()

# Install locally
install()
```

### Package Structure Best Practices

```r
# Typical package structure:
# mypackage/
# ├── DESCRIPTION
# ├── NAMESPACE
# ├── R/
# │   ├── function1.R
# │   └── function2.R
# ├── man/
# ├── tests/
# │   └── testthat/
# ├── vignettes/
# └── README.md

# Good function documentation
#' Calculate the mean of numeric values
#'
#' This function calculates the arithmetic mean of a numeric vector,
#' with options for handling missing values.
#'
#' @param x A numeric vector
#' @param na.rm Logical. Should missing values be removed?
#' @return The arithmetic mean of x
#' @examples
#' my_mean(c(1, 2, 3, 4, 5))
#' my_mean(c(1, 2, NA, 4, 5), na.rm = TRUE)
#' @export
my_mean <- function(x, na.rm = FALSE) {
  if (!is.numeric(x)) {
    stop("x must be numeric")
  }
  sum(x, na.rm = na.rm) / length(x[!is.na(x)])
}
```