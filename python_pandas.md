# python_pandas.md

## DataFrames

### Basics

create df
``` python
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
```

create a df by hand
``` python
columns = ["Backtest"]
metrics = ["Annualized Return", "Cumulative Returns", "Annual Volatility", "Sharpe Ratio", "Sortino Ratio",]
portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)
portfolio_evaluation_df.loc["Annualized Return"] = (signals_df["Portfolio Daily Returns"].mean() * 252)
```

create dataframe from dictionary, which is created from lists
``` python
roc_df_train = pd.DataFrame({"FPR Train": fpr_train, "TPR Train": tpr_train,})
```

Construct an empty df to append results to
``` python
all_actuals = pd.DataFrame(columns=["Actual Returns"])
for i in range(0, timeframe):
    actuals = pd.DataFrame(y_test, index=y_test.index)
    actuals.columns = ["Actual Returns"]
    all_actuals = all_actuals.append(actuals)
```

Construct a dataframe from two series.

```python
# from 10.3
Results = y_test.to_frame()
Results["Predicted Return"] = predictions
```

Read csv

``` python
sales_data = pd.read_csv(csvpath)
sales_data = pd.read_csv(csvpath, header=None)
sales_data = pd.read_csv(csv_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
sales_data = pd.read_csv(csv_path, index_col='CustomerID')
```

Describe the data

``` python
sales_data.describe()
sales_data.describe(include='all')
```

Get info about the dataframe.

```python
df.info()
```

Quick sample check of 5 rows

``` python
csv_data.sample(5)
```

N largest

``` python
result = df.nlargest(20, 'Market_Cap')
```

Rename specific columns

``` python
# style 1
all_df.rename(columns={'Relative_Risk1': 'Relative_Risk',
    'dda': 'clean',
    'oof': 'viola',
    'dnjdajda': 'nice',
    'fjanfa': 'nice2'},
    inplace=True)

# style 2
customer_dataframe = customer_dataframe.rename(columns={
    "Full Name": "full_name",
    "Credit Card Number": "credit_card_number"
})
```

Rewrite column names

``` python
columns = ["Full Name", "Email", "Address", "Zip Code", "Credit Card Number"]
sales_data.columns = columns
```

Reorder columns [[ ]]

``` python
customer_dataframe = customer_dataframe[['credit_card_number', 'Account Balance', 'full_name', 'Email', 'Address', 'Zip Code']]
customer_dataframe.head()
```

Create columns

``` python
customer_dataframe["Balance (1k)"] = customer_dataframe["Account Balance"] / 1000
```

Split columns

``` python
names = customer_dataframe["full_name"].str.split(" ", expand=True)
customer_dataframe["first_name"] = names[0]
customer_dataframe["last_name"] = names[1]
```

Delete columns

``` python
customer_dataframe = customer_dataframe.drop(columns=["full_name"])
```

### Data cleaning

Data cleaning is important because it removes all of the issues and errors that would block
or inhibit computation.

Identify DataFrame Data Types. It's **crucial** to review data types after loading data into a DataFrame, as Pandas automatically assigns a data type to a Series. Sometimes Pandas can't infer the data type. 

In these instances, you can convert the series.

``` python
csv_data.dtypes
# customer_no    object
# order_total    object
# order_date     object
# dtype: object
```

Identify Series count

``` python
csv_data.count()
# customer_no    7
# order_total    7
# order_date     8
# dtype: int64
```

Identify frequency values, reveals how many times a value occurs in a Series, with the most occurring
value first.

``` python
csv_data["customer_no"].value_counts()
```

Check for null values

``` python
csv_data.isnull()
```

check for nulls in entire df

``` python
df_2019.isnull().sum()
```

Determine percentage of nulls. Determine what should be done with the nulls

``` python
csv_data.isnull().mean() * 100
```

Determine number of nulls. This serves as a **unit test** of the dropna function.

``` python
csv_data.isnull().sum()
```

**Fix nulls** by filling with na

``` python
csv_data["customer_no"] = csv_data["customer_no"].fillna("Unknown")
```

Cleanse nulls from DataFrame by dropping

``` python
csv_data = csv_data.dropna().copy()
```

Check duplicates

``` python
csv_data.duplicated()  # all fields
csv_data["customer_no"].duplicated()  # specific field
```

Dedupe / remove duplicates

``` python
csv_data = csv_data.drop_duplicates().copy()
csv_data["customer_no"].duplicated()
```

Assess data quality

``` python
csv_data.head()
```

Remove $ symbol, but regex warning [here](https://stackoverflow.com/questions/66603854/futurewarning-the-default-value-of-regex-will-change-from-true-to-false-in-a-fu). Then follow up with astype("float")

``` python
csv_data["order_total"] = csv_data["order_total"].str.replace("$", "", regex=True)
# FutureWarning: The default value of regex will change from True to False in a future version
```

Convert column from `object` to `float`

``` python
csv_data["order_total"] = csv_data["order_total"].astype("float")
```

### Advanced

Copy

The copy function is used to decouple original dfs from dfs indexed by `set_index` . This prevents changes made to the indexed df from being made to the original df, ensuring that the state of the original df is preserved. This is Pandas' way of implementing version control on df.

The alternative to using the copy function is to use the `inplace=True` parameter with the `set_index` function. `inplace=True` tells Pandas not to create a copy of the df when setting the index

``` python
df.copy()
```

sort df

``` python
df_all = df_all.sort_values(by=['fname', 'lname', 'age', 'weight', 'ver2'], ascending=False)
```

loop through xlsx folder and append to big df
``` python
df_all = pd.DataFrame()
for file in os.listdir(filepath):
    if file.startswith('20') and file.endswith('.xlsx'):
        df = pd.read_excel(filepath + file, header=0)
        df_all = df_all.append(df)
        print("Appended: " + file.split("_")[0])
```

search df for string and return location, then extract values to right of that location
``` python
search = "Market"
hit = np.where(df.values == search)
row_index, col_index = hit[0][0], hit[1][0]  # extract values
header_market = df.iloc[row_index, col_index + 1]
header_market_months = df.iloc[row_index, col_index + 2]
header_market_time = df.iloc[row_index, col_index + 3]
```
dataframe lookup 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html

``` python
df.at[4, 'B'] > 2
or index at
df1.iat[0,0] = "yo"
```

search df for string 
https://stackoverflow.com/questions/11350770/select-by-partial-string-from-a-pandas-dataframe

``` python
df[df["col_A"].str.contains("Totals", case=False, na=False)]
```

find dataframe dupes
``` python
df_shopping['Gender'].duplicated().sum()  # single column dupes
df_shopping.duplicated().sum()  # across all column dupes
```

### Grouping

Note: FinTech 03.3

The groupby function requires a function or aggregation to proceed it.

Whenever a function is not chained to a groupby function, the output will be a DataFrameGroupBy object rather than an actual DataFrame. DataFrameGroupBy objects must be aggregated before they can be used.

Group by crypto data by cryptocurrency and perform count

``` python
crypto_data_grp = crypto_data.groupby('cryptocurrency').count()
crypto_data_mean = crypto_data.groupby('cryptocurrency').mean()
```

Group DataFrame without aggregate function

``` python
crypto_data_grp = crypto_data.groupby('cryptocurrency')
```

Group by more than one column

``` python
multi_group = crypto_data.groupby(['cryptocurrency','data_priceUsd'])['data_priceUsd'].count()
```

Round column to 2 decimal places

``` python
rounded_crypto_data = crypto_data.round({'data_priceUsd': 2})
```

Compare one column group with multiple column group

``` python
single_group = crypto_data.groupby('cryptocurrency')['data_priceUsd'].count()
```

Plot grouped data to generate more than one line on the same chart

``` python
grouped_cryptos = crypto_data.groupby('cryptocurrency')['data_priceUsd'].plot(legend=True)
```

### Rows

inserting "garth rulz" into 2nd column

``` python
df.insert(2, "header_name", "garth rulz")
```

count rows
``` python
row_count = predictions_joined.shape[0]  # row count
```

drop rows where chart_loc = non_overlap
``` python
df_2019 = df_2019[df_2019['chart_loc'] != "non_overlap"]
```

produce a frequency count for each location, so i can filter using some count threshhold and decrease cardinality
``` python
df["freq"] = d.groupby("Chart_Loc")["Chart_Loc"].transform('count')
```

### iloc

df.iloc[rows:rows, columns:columns]

iloc is like `df.head()`, but more customizable.

Select the first row of the DataFrame & the second row of the DataFrame

``` python
people_csv.iloc[0]
people_csv.iloc[1]
```

Select the first 10 rows of the DataFrame

``` python
people_csv.iloc[0:10]
```

Select the last row of the DataFrame

``` python
people_csv.iloc[-1]
```

Select the first column of the DataFrame

``` python
people_csv.iloc[:,0].head()
```

Select the first two columns of the DataFrame, with all rows

``` python
people_csv.iloc[:, 0:2].head()
```

Select the first 5 rows of the 3rd, 4th, and 5th columns of the DataFrame

``` python
people_csv.iloc[0:5, 2:5] 
```

show slice of df

``` python
display(class_encoded_df.iloc[1:3])
display(class_encoded_df.iloc[80:82])
display(class_encoded_df.iloc[100:102])
```

first 3 rows, first 4 columns
``` python
data.iloc[0:3, 0:4]
```

Modify the 'first_name' column value of the first row. Sometimes this may cause a SettingWithCopyWarning , where Pandas tries to set values on a copy of a slice of a df. Therefore, use the copy() function to establish a concrete object––rather than a pointer to an object––to fix the error.

``` python
people_csv.iloc[0, people_csv.columns.get_loc('first_name')] = 'Arya'
```

### loc

**@NOTE**: To use the loc function on the df index, string values need to be set as the index using the `set_index()` function. `set_index` does not return a new df, but rather creates a copy of the original. Any changes made to the indexed df will be passed on to the original df.

Slice the data to output a range of rows based on the index

``` python
people_csv.loc['Aleshia':'Svetlana'].head()
```

Filter rows based on a column value conditional

``` python
people_csv.loc[people_csv['gender'] == 'M'].head()
```

Modify the 'first_name' value of the row with the index 'Yun'

``` python
people_csv.loc['Yun', 'first_name'] = 'Yuna'
```

Find Daily Returns values less than 0,
square those values, and add them to the Downside Returns column

``` python
df.loc[df["Daily Returns"] < 0, "Downside Returns"] = df["Daily Returns"]**2
```

this is a slice where returns are +
``` python
signals_df.loc[(signals_df["Actual Returns"] >= 0)]
```

in the slice, we assign 1 to column Signal
``` python
signals_df.loc[(signals_df["Actual Returns"] >= 0), "Signal"] = 1
```

select only certain columns
``` python
data_to_plot = df[["Year", "PopulationCount", "Latitude", "Longitude"]]
```

select only where statedesc column = california
``` python
filtered_data = df[df["StateDesc"] == "California"]
```

select rows where freq > 10
``` python
top_words = money_news_df[money_news_df["Frequency"] >= 10]
```

select rows where freq > 10 and < 30
Top words will be those with a frequency between 10 ans 30 (thumb rule)
``` python
top_words = money_news_df[(money_news_df["Frequency"] >= 10) & (money_news_df["Frequency"] <= 30)]
```

np where - if provider has at least 50 charts, use provider name, else use bin name
see below
``` python
df["Loc_new"] = np.where(
    df["freq"] >= 50
    ,  df["Loc"]
    , "small_location")
```

e.g.
``` python
df["buy"] = np.where(df["delta"] > 0,  1, 0)
df["sell"] = np.where(df["delta"] < 0,  1, 0)
```

np where - 2 conditions/conditionals
if overlap, and location has less than 50 charts, name it "less than 50"
see below
``` python
df["location_new"] = np.where(
    (df["location"] != "non_overlap") & (df["Loc_new"] == "small_location")
    ,  "small_location"
    , df["location"])
```

``` python
df_test["buy"] = np.where(
    (df_test["Predicted"] - df_test["Real"] < 0) | (df_test["Predicted"] == 0)
    , 1
    , 0)
```

row based slicing
``` python
# 1
home_sale_prices = home_sale_prices.loc[
    (home_sale_prices["saleDate"] > "2019-06-01")
    & (home_sale_prices["saleDate"] < "2019-06-31")
]
# 2
first_route = places_of_interest[
(places_of_interest["Name"].str.contains("Airport"))
]
# 3
first_route = places_of_interest[
    (places_of_interest["Name"].str.contains("Airport"))
    | (places_of_interest["Name"].isin(["Aqueduct Race Track", "Astoria Park"]))
]
```

### Columns

any column has na, drop row
``` python
df = df_2019.dropna()
```

replace infinity with nan
``` python
df = df.replace(-np.inf, np.nan)
```

give column name
``` python
predicted_df.columns = ['predicted']
```

print column names
``` python
for label, content in df.iteritems():
    print(label)
```

search if df column contains string
``` python
df['column1'].str.contains('Garth').any()
```

add column of 0s
``` python
df['zeroes'] = 0
```

add nan column
``` python
fntk_df["nan"] = np.nan
```

create column from math calculations
``` python
df["km"] = df["meters"] / 1000
```

dummy the cats. Do not dummy the dummies
``` python
x = pd.get_dummies(df_2019, columns=cat_cols)	
```

create new column called new_column
taking from original_column, only the first row
all other rows in new_column = nan
``` python
df["new_column"] = df.loc[:0, "original_column"]
```

replace nan with ''
``` python
df["new_column"] = df["new_column"].fillna('')
```

Filling missing values with the previous ones
https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html

``` python
gold_df = gold_df.fillna(method ='pad')
```

replace NANs in a column with 0. Oracle doesnt allow nan, so doing this replacement
``` python
df_all['hhs_transfer'].replace(to_replace=np.nan, value=0, inplace=True)
```

replace nan in all integer columns with 0 and str with ""
``` python
df_all[columns_int] = df_all[columns_int].replace(np.nan, 0)
df_all[columns_str] = df_all[columns_str].replace(np.nan, "")
```

convert all named colunmms to specific data type
``` python
df_all[columns_str] = df_all[columns_str].astype(str)
df_all[columns_int] = df_all[columns_int].astype(int)
```

Find null values
``` python
for column in df.columns:
    print(f"{df[column].isnull().sum()} nulls in: {column}")  # edited
```

unique/distinct sorted values in column. 
``` python
sorted(df["quality"].unique())
```

### Index

When working with indexes, its a common practice to clean data before setting indexes. E.g., a Series being used as an index should not have any NaN values. These can be handled by first executing dropna against a DataFrame. The set_index function can then be used set the index

Read with index set

``` python
ice_cream = pd.read_csv(ice_cream_data, index_col="Month")
```

Display index

``` python
ticker_data.index
```

Index Selection Using loc

``` python
people_csv = people_csv.set_index(people_csv['first_name'])
# or
people_csv.set_index(people_csv['first_name'], inplace=True)
```

reset row index

``` python
premium_df.reset_index(drop=True, inplace=True)  
```

reset col index
``` python
premium_df.columns = range(premium_df.columns.size)  
```

attach index of business days to df
``` python
df.index = pd.bdate_range(start='2019-09-09', periods=10)
```

Return Series/DataFrame with requested index / column level(s) removed.
``` python
df = df.droplevel(axis=1, level=0)
```

pandas timestamp
``` python
current_date = pd.Timestamp(datetime.now(), tz="America/New_York").isoformat()
```

pandas timestamp delta
``` python
last_month = pd.Timestamp(datetime.now() - timedelta(30), tz="America/New_York").isoformat()
```

#### Multilevel Index

Multi-indexing is the process of indexing a dataset by more than one value. Multi-indexing is like using two bookmarks in a book. Each bookmark is an index, and depending on which index you go to, you'll get different content.

Multi-indexing is sometimes referred to as hierarchical indexing, as relationships can exist between indexes. For example, a state can be one index and a city can be another. Because a city belongs to a state, these indexes would be hierarchical.

Multiple indexes are valuable because they enable dimensional data to be grouped and retrieved.

Essentially, multi-indexing improves data storage, lookup, and manipulation/assignment.

drop multilevel index 
https://stackoverflow.com/questions/22233488/pandas-drop-a-level-from-a-multi-level-column-index

``` python
df.columns = df.columns.droplevel()
```

Group by year, month, and day and grab first of each group

``` python
df_grp = df.groupby([df.index.year, df.index.month, df.index.day]).first()
df_grp = df.groupby([df.index.year, df.index.month, df.index.day]).mean()
df_grp = df.groupby([df.index.year, df.index.month, df.index.day]).last()
```

Group by year and month and take the last value of each group

``` python
df_2 =df.groupby([df.index.year,df.index.month]).last()
```

Drill down through dataframe that has 2 levels of index headers. See Alpaca API code.

``` python
msft_price = float(df_portfolio["MSFT"]["close"])
```

Access dataframe column that has 2 levels of index headers. See Alpaca API code.

``` python
msft_value = msft_price * df_shares.loc["MSFT"]["shares"]
```

### Joins

Read dfs with indices set

``` python
customer_data = pd.read_csv(customer_data_path, index_col='CustomerID')
products_data = pd.read_csv(products_data_path, index_col='CustomerID')
```

inner join by rows or columns If you want all columns, join on columns. If you want all rows, join on rows. Rows = union.

``` python
joined_df = pd.concat([df1, df2, df3], axis="rows", join="inner")  # union
joined_df = pd.concat([df1, df2, df3], axis="columns", join="inner")
```

daisy chain the joins

``` python
title_sentiment_df = pd.DataFrame(title_sent)
text_sentiment_df = pd.DataFrame(text_sent)
news_en_df = news_en_df.join(title_sentiment_df).join(text_sentiment_df)
```

## Series

find overlap between two series so that we can mark all non-overlap as "other". 
https://stackoverflow.com/a/21175114/5825523

``` python
overlap = pd.Series(np.intersect1d(series1.values, series2.values))
overlap = pd.DataFrame(overlap)
overlap.columns = ['Chart_Loc']
```

## Iterate

iterate/loop through df, examine each index and corresponding row value. perform calc, construct new df
15.2.3 algo trading

``` python
for index, row in df.iterrows():
    if row["Entry/Exit"] == 1:
        entry_date = index
        entry_portfolio_holding = row["Portfolio Holdings"]
        share_size = row["Entry/Exit Position"]
        entry_share_price = row["close"]
```

\15-Algorithmic-Trading\1\Activities\02-Ins_Intro_Algo_Trading\Solved
Loop through the df and initiate a trade each iteration
``` python
for index, row in fntk_df.iterrows():
    # buy if the previous_price is 0, in other words, buy on the first day
    if previous_price == 0:
        fntk_df.loc[index, "trade_type"] = "buy"
    # update the previous_price to the current row's price
    previous_price = row["close"]
    # if the index is the last index of the DataFrame, sell
    if index == fntk_df.index[-1]:
        fntk_df.loc[index, "trade_type"] = "sell"
```

## Visualizations

plot a df

``` python
gold_csv.plot()
```

Convert date strings into datetime objects and set the datetime as the index

``` python
gold_csv.set_index(pd.to_datetime(gold_csv['Date'], infer_datetime_format=True), inplace=True)
gold_csv.plot()
```

Plot a bar chart of the data

``` python
gold_csv.plot(kind='bar', figsize=(20,10))
```

Plot two series overlaid

``` python
# Set figure of the daily closing prices of Tesla
ax = tsla_df.plot()

# Plot 180-Day Rolling Mean on the same figure
tsla_df.rolling(window=180).mean().plot(ax=ax)

ax.legend(["TSLA", "TSLA 180 Day Mean"]);
```

## Shift

Calculate returns

``` python
daily_returns = (sp500_csv - sp500_csv.shift(1)) / sp500_csv.shift(1)
# or
daily_returns = sp500_csv.pct_change()
daily_returns.plot(figsize=(10,5))
```