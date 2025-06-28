# py_pandas.md

## DataFrames

### Basics

Create df:
```python
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
```

Create a df by hand:
```python
columns = ["Backtest"]
metrics = ["Annualized Return", "Cumulative Returns", "Annual Volatility", "Sharpe Ratio", "Sortino Ratio",]
portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)
portfolio_evaluation_df.loc["Annualized Return"] = (signals_df["Portfolio Daily Returns"].mean() * 252)
```

Create dataframe from dictionary, which is created from lists:
```python
roc_df_train = pd.DataFrame({"FPR Train": fpr_train, "TPR Train": tpr_train,})
```

Construct an empty df to append results to:
```python
all_actuals = pd.DataFrame(columns=["Actual Returns"])
for i in range(0, timeframe):
    actuals = pd.DataFrame(y_test, index=y_test.index)
    actuals.columns = ["Actual Returns"]
    all_actuals = all_actuals.append(actuals)
```

Construct a dataframe from two series:
```python
# from 10.3
Results = y_test.to_frame()
Results["Predicted Return"] = predictions
```

Read csv:
```python
sales_data = pd.read_csv(csvpath)
sales_data = pd.read_csv(csvpath, header=None)
sales_data = pd.read_csv(csv_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
sales_data = pd.read_csv(csv_path, index_col='CustomerID')
```

Describe the data:
```python
sales_data.describe()
sales_data.describe(include='all')
```

Get info about the dataframe:
```python
df.info()
```

Quick sample check of 5 rows:
```python
csv_data.sample(5)
```

N largest:
```python
result = df.nlargest(20, 'Market_Cap')
```

Rename specific columns:
```python
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

Rewrite column names:
```python
columns = ["Full Name", "Email", "Address", "Zip Code", "Credit Card Number"]
sales_data.columns = columns
```

Reorder columns [[ ]]:
```python
customer_dataframe = customer_dataframe[['credit_card_number', 'Account Balance', 'full_name', 'Email', 'Address', 'Zip Code']]
customer_dataframe.head()
```

Create columns:
```python
customer_dataframe["Balance (1k)"] = customer_dataframe["Account Balance"] / 1000
```

Split columns:
```python
names = customer_dataframe["full_name"].str.split(" ", expand=True)
customer_dataframe["first_name"] = names[0]
customer_dataframe["last_name"] = names[1]
```

Delete columns:
```python
customer_dataframe = customer_dataframe.drop(columns=["full_name"])
```

### Data Cleaning

Data cleaning is important because it removes all of the issues and errors that would block or inhibit computation.

Identify DataFrame Data Types. It's **crucial** to review data types after loading data into a DataFrame, as Pandas automatically assigns a data type to a Series. Sometimes Pandas can't infer the data type.

In these instances, you can convert the series:
```python
csv_data.dtypes
# customer_no    object
# order_total    object
# order_date     object
# dtype: object
```

Identify Series count:
```python
csv_data.count()
# customer_no    7
# order_total    7
# order_date     8
# dtype: int64
```

Identify frequency values, reveals how many times a value occurs in a Series, with the most occurring value first:
```python
csv_data["customer_no"].value_counts()
```

Check for null values:
```python
csv_data.isnull()
```

Check for nulls in entire df:
```python
df_2019.isnull().sum()
```

Determine percentage of nulls. Determine what should be done with the nulls:
```python
csv_data.isnull().mean() * 100
```

Determine number of nulls. This serves as a **unit test** of the dropna function:
```python
csv_data.isnull().sum()
```

**Fix nulls** by filling with na:
```python
csv_data["customer_no"] = csv_data["customer_no"].fillna("Unknown")
```

Cleanse nulls from DataFrame by dropping:
```python
csv_data = csv_data.dropna().copy()
```

Check duplicates:
```python
csv_data.duplicated()  # all fields
csv_data["customer_no"].duplicated()  # specific field
```

Dedupe / remove duplicates:
```python
csv_data = csv_data.drop_duplicates().copy()
csv_data["customer_no"].duplicated()
```

Assess data quality:
```python
csv_data.head()
```

Remove $ symbol, but regex warning [here](https://stackoverflow.com/questions/66603854/futurewarning-the-default-value-of-regex-will-change-from-true-to-false-in-a-fu). Then follow up with astype("float"):
```python
csv_data["order_total"] = csv_data["order_total"].str.replace("$", "", regex=True)
# FutureWarning: The default value of regex will change from True to False in a future version
```

Convert column from `object` to `float`:
```python
csv_data["order_total"] = csv_data["order_total"].astype("float")
```

### Advanced Operations

Copy:
The copy function is used to decouple original dfs from dfs indexed by `set_index`. This prevents changes made to the indexed df from being made to the original df, ensuring that the state of the original df is preserved. This is Pandas' way of implementing version control on df.

The alternative to using the copy function is to use the `inplace=True` parameter with the `set_index` function. `inplace=True` tells Pandas not to create a copy of the df when setting the index:
```python
df.copy()
```

Sort df:
```python
df_all = df_all.sort_values(by=['fname', 'lname', 'age', 'weight', 'ver2'], ascending=False)
```

Loop through xlsx folder and append to big df:
```python
df_all = pd.DataFrame()
for file in os.listdir(filepath):
    if file.startswith('20') and file.endswith('.xlsx'):
        df = pd.read_excel(filepath + file, header=0)
        df_all = df_all.append(df)
        print("Appended: " + file.split("_")[0])
```

Search df for string and return location, then extract values to right of that location:
```python
search = "Market"
hit = np.where(df.values == search)
row_index, col_index = hit[0][0], hit[1][0]  # extract values
header_market = df.iloc[row_index, col_index + 1]
header_market_months = df.iloc[row_index, col_index + 2]
header_market_time = df.iloc[row_index, col_index + 3]
```

Dataframe lookup:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html
```python
df.at[4, 'B'] > 2
# or index at
df1.iat[0,0] = "yo"
```

Search df for string:
https://stackoverflow.com/questions/11350770/select-by-partial-string-from-a-pandas-dataframe
```python
df[df["col_A"].str.contains("Totals", case=False, na=False)]
```

Find dataframe dupes:
```python
df_shopping['Gender'].duplicated().sum()  # single column dupes
df_shopping.duplicated().sum()  # across all column dupes
```

### Grouping

Note: FinTech 03.3

The groupby function requires a function or aggregation to proceed it.

Whenever a function is not chained to a groupby function, the output will be a DataFrameGroupBy object rather than an actual DataFrame. DataFrameGroupBy objects must be aggregated before they can be used.

Group by crypto data by cryptocurrency and perform count:
```python
crypto_data_grp = crypto_data.groupby('cryptocurrency').count()
crypto_data_mean = crypto_data.groupby('cryptocurrency').mean()
```

Group DataFrame without aggregate function:
```python
crypto_data_grp = crypto_data.groupby('cryptocurrency')
```

Group by more than one column:
```python
multi_group = crypto_data.groupby(['cryptocurrency','data_priceUsd'])['data_priceUsd'].count()
```

Round column to 2 decimal places:
```python
rounded_crypto_data = crypto_data.round({'data_priceUsd': 2})
```

Compare one column group with multiple column group:
```python
single_group = crypto_data.groupby('cryptocurrency')['data_priceUsd'].count()
```

Plot grouped data to generate more than one line on the same chart:
```python
grouped_cryptos = crypto_data.groupby('cryptocurrency')['data_priceUsd'].plot(legend=True)
```

### Row Operations

Inserting "garth rulz" into 2nd column:
```python
df.insert(2, "header_name", "garth rulz")
```

Count rows:
```python
row_count = predictions_joined.shape[0]  # row count
```

Drop rows where chart_loc = non_overlap:
```python
df_2019 = df_2019[df_2019['chart_loc'] != "non_overlap"]
```

Produce a frequency count for each location, so i can filter using some count threshold and decrease cardinality:
```python
df["freq"] = d.groupby("Chart_Loc")["Chart_Loc"].transform('count')
```

### iloc

df.iloc[rows:rows, columns:columns]

iloc is like `df.head()`, but more customizable.

Select the first row of the DataFrame & the second row of the DataFrame:
```python
people_csv.iloc[0]
people_csv.iloc[1]
```

Select the first 10 rows of the DataFrame:
```python
people_csv.iloc[0:10]
```

Select the last row of the DataFrame:
```python
people_csv.iloc[-1]
```

Select the first column of the DataFrame:
```python
people_csv.iloc[:,0].head()
```

Select the first two columns of the DataFrame, with all rows:
```python
people_csv.iloc[:, 0:2].head()
```

Select the first 5 rows of the 3rd, 4th, and 5th columns of the DataFrame:
```python
people_csv.iloc[0:5, 2:5] 
```

Show slice of df:
```python
display(class_encoded_df.iloc[1:3])
display(class_encoded_df.iloc[80:82])
display(class_encoded_df.iloc[100:102])
```

First 3 rows, first 4 columns:
```python
data.iloc[0:3, 0:4]
```

Modify the 'first_name' column value of the first row. Sometimes this may cause a SettingWithCopyWarning, where Pandas tries to set values on a copy of a slice of a df. Therefore, use the copy() function to establish a concrete object––rather than a pointer to an object––to fix the error:
```python
people_csv.iloc[0, people_csv.columns.get_loc('first_name')] = 'Arya'
```

### loc

**@NOTE**: To use the loc function on the df index, string values need to be set as the index using the `set_index()` function. `set_index` does not return a new df, but rather creates a copy of the original. Any changes made to the indexed df will be passed on to the original df.

Slice the data to output a range of rows based on the index:
```python
people_csv.loc['Aleshia':'Svetlana'].head()
```

Filter rows based on a column value conditional:
```python
people_csv.loc[people_csv['gender'] == 'M'].head()
```

Modify the 'first_name' value of the row with the index 'Yun':
```python
people_csv.loc['Yun', 'first_name'] = 'Yuna'
```

Find Daily Returns values less than 0, square those values, and add them to the Downside Returns column:
```python
df.loc[df["Daily Returns"] < 0, "Downside Returns"] = df["Daily Returns"]**2
```

This is a slice where returns are +:
```python
signals_df.loc[(signals_df["Actual Returns"] >= 0)]
```

In the slice, we assign 1 to column Signal:
```python
signals_df.loc[(signals_df["Actual Returns"] >= 0), "Signal"] = 1
```

Select only certain columns:
```python
data_to_plot = df[["Year", "PopulationCount", "Latitude", "Longitude"]]
```

Select only where statedesc column = california:
```python
filtered_data = df[df["StateDesc"] == "California"]
```

Select rows where freq > 10:
```python
top_words = money_news_df[money_news_df["Frequency"] >= 10]
```

Select rows where freq > 10 and < 30. Top words will be those with a frequency between 10 and 30 (thumb rule):
```python
top_words = money_news_df[(money_news_df["Frequency"] >= 10) & (money_news_df["Frequency"] <= 30)]
```

### NumPy where

np where - if provider has at least 50 charts, use provider name, else use bin name:
```python
df["Loc_new"] = np.where(
    df["freq"] >= 50
    ,  df["Loc"]
    , "small_location")
```

e.g.:
```python
df["buy"] = np.where(df["delta"] > 0,  1, 0)
df["sell"] = np.where(df["delta"] < 0,  1, 0)
```

np where - 2 conditions/conditionals. If overlap, and location has less than 50 charts, name it "less than 50":
```python
df["location_new"] = np.where(
    (df["location"] != "non_overlap") & (df["Loc_new"] == "small_location")
    ,  "small_location"
    , df["location"])
```

```python
df_test["buy"] = np.where(
    (df_test["Predicted"] - df_test["Real"] < 0) | (df_test["Predicted"] == 0)
    , 1
    , 0)
```

### Row-based Slicing

```python
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