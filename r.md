# r.md

## Basic Syntax

```r
# Variables and data types
x <- 5                       # Assignment
name <- "R Programming"      # Character
numbers <- c(1, 2, 3, 4)    # Vector
data <- data.frame(a = 1:3, b = letters[1:3])  # Data frame
```

## Data Structures

```r
# Vectors
numeric_vec <- c(1, 2, 3)
character_vec <- c("a", "b", "c")
logical_vec <- c(TRUE, FALSE, TRUE)

# Lists
my_list <- list(numbers = 1:5, letters = LETTERS[1:3])

# Matrices
matrix_data <- matrix(1:12, nrow = 3, ncol = 4)

# Data frames
df <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(25, 30, 35),
  city = c("NYC", "LA", "Chicago")
)
```

## Data Manipulation

```r
# Base R
df$new_column <- df$age * 2
subset(df, age > 25)
df[df$age > 25, ]

# dplyr
library(dplyr)
df %>%
  filter(age > 25) %>%
  mutate(age_squared = age^2) %>%
  select(name, age_squared) %>%
  arrange(desc(age_squared))
```

## Data Visualization

```r
# Base R plotting
plot(df$age, df$new_column)
hist(df$age)
boxplot(df$age)

# ggplot2
library(ggplot2)
ggplot(df, aes(x = age, y = new_column)) +
  geom_point() +
  geom_smooth(method = "lm") +
  labs(title = "Age vs New Column")
```

## Statistical Analysis

```r
# Descriptive statistics
summary(df)
mean(df$age)
sd(df$age)
cor(df$age, df$new_column)

# Linear regression
model <- lm(new_column ~ age, data = df)
summary(model)

# ANOVA
aov_result <- aov(age ~ city, data = df)
summary(aov_result)
```

## Package Management

```r
install.packages("package_name")  # Install package
library(package_name)             # Load package
update.packages()                 # Update all packages
remove.packages("package_name")   # Remove package
```