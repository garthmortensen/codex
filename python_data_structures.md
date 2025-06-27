# python_data_structures.md

## Lists

List is a Python data structure that allows multiple values to be stored inside of it. List values can be retrieved, appended, removed, and iterated upon.

slicing

``` python
name_list = ['Elliot' ,'Darlene', 'Angela', 'Shayla']
name_list[0:2]
# ['Elliot' ,'Darlene']

name_list[2:4]
# ['Angela', 'Shayla']

# all equal
name_list[0:4:2]
name_list[:4:2]
name_list[::2]
# ['Elliot', 'Angela']

name_list[-2]
```

pop and remove

``` python
pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx"]

print("Removing 'Magikarp'...")
pokemon.remove("Magikarp")

print("Removing employee 'Bulbasaur' based off of its index")
bulbasaur_index = pokemon.index("Bulbasaur")
pokemon.pop(bulbasaur_index)
print(pokemon)
```

make a very long list:

``` python
k = list(range(1, 1000))
```

count occurences of element in list
``` python
listy = ["h", "p", "l", "m", "h", "p", "h"]
listy.count("h")
```

distinct a list, tho you lose order
``` python
my_list = list(set(my_list))
```

return flat list
see next
``` python
for text in texts:
    all_adjectives = all_adjectives + all_adj(text)
```

flatten a list of lists
see previous
``` python
flat_list = []
for sublist in events:
    for item in sublist:
        flat_list.append(item)
```

return list of lists
``` python
all_adjectives2 = []
for text in texts:
    all_adjectives2.append(all_adj(text))
```

write file list to txt
``` python
file_write = "C:/list_of_articles.txt"
with open(file_write, "w") as f:
    f.write("all_articles\n")
    for item in files_in_dir:
        f.write(item+"\n")
```

read csv 

``` python
alias = []
model_number = []
with open('auditingprojects/battlestar.csv', 'r') as file:
    csvfile = csv.reader(file, delimiter=',')
    # store a row in the spreadsheet in the variable `row` during each loop
    for row in csvfile:
        alias.append(row[0])
        model_number.append(row[1])  # second comma seperated column
```

pretty print a list

``` python
from pprint import pprint
pprint(listy)
```

https://stackoverflow.com/questions/4843158/how-to-check-if-a-string-is-a-substring-of-items-in-a-list-of-strings/25102099#25102099
check if substring exists in list:

``` python
v1 
some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
if any("abc" in s for s in some_list):
    # whatever

v2
matchers = ['abc','def']
matching = [s for s in my_list if any(xs in s for xs in matchers)]
```

search for multiple in list. fintech 12.2.2
``` python
terms = ["yen", "japan"]
def retrieve_docs(terms):
    result_docs = []
    for doc_id in money_news_ids:
        found_terms = [
            word
            for word in reuters.words(doc_id)
            if any(term in word.lower() for term in terms)
        ]
        if len(found_terms) > 0:
            result_docs.append(doc_id)
    return result_docs
```

List index work

``` python
pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Gyarados", "Dragonite", "Onyx"]
print(pokemon.index("Gyarados"))

bulbasaur_index = pokemon.index("Bulbasaur")
pokemon.pop(bulbasaur_index)
```

Iterate over a list

``` python
count = 0
total = 0
average = 0
minimum = 0
maximum = 0
cash_tips = [22, 10, 30, 45, 54, 60, 56]

for tip in cash_tips:

    # Cumulatively sum up the total and count of tips
    total += tip
    count = count + 1

    # Logic to determine minimum values
    if minimum == 0:  # which it is on first iteration
        minimum = tip  # anything larger than 0
    elif tip < minimum:
        minimum = tip

    # Logic to determine maximum values
    if tip > maximum:  # maximum set to 0
        maximum = tip
```

## Dictionaries

Another name for dictionary/dict is [Associative Array](https://en.wikipedia.org/wiki/Associative_array).

View objects - these create a dynamic view of referenced objects.
```python
for k, v in dict.items():  # dict.items() is the view
	print(k, v)
```

dictionary creation 1
``` python
raw_tx = {
    "to": receiver,
    "from": account.address,
    "value": wei_value,
    "gas": gas_estimate,
    "gasPrice": 0,
    "nonce": w3.eth.getTransactionCount(account.address)
}
```

Various dictionary techniques

``` python
top_traders_2019 = {
    "january" : "Karen",
    "february" : "Harold",
    "march" : "Sam"
    }

trading_pnl = {
    "title": "Trading Log",
    "03-18-2019": -224,
    "03-19-2019": 352,
    "03-20-2019": 252,
    }

# Print out dictionary
print(f"Dictionary: {trading_pnl}")

# Print out specific value of a key
print(f"03-31-2019: {trading_pnl['03-31-2019']}")

# Add a new key-value pair
trading_pnl["04-07-2019"] = 413

# Modify a key value
trading_pnl["04-07-2019"] = 542

# Delete a key-value pair
del trading_pnl["04-07-2019"]

# Check if key exists
if "04-03-2019" in trading_pnl:
    print("Yes, '04-03-2019' is one of the keys in the trading_pnl dictionary")
    
# Print out dict keys via a for loop
for key in trading_pnl:
    print(f"Key: {key}")

# Print out dict values
for key in trading_pnl:
    print(f"Value: {trading_pnl[key]}")

# Print out dict key-value pairs
for key, value in trading_pnl.items():
    print(f"{key} : {value}")
```

Access nested dictionary

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

Create dataframe from lists (05.2)

```python
value_data = {
"MSFT": [msft_value],
"AAPL": [aapl_value]
}
df_value = pd.DataFrame(value_data)
```

## Other datatypes, permutations, counters, collections, etc

itertools.permutations() generates permutations for an iterable. e.g. Brute-force a password
``` python
import itertools
for p in itertools.permutations('ABCD'):
     print(p)
('A', 'B', 'C', 'D')
('A', 'B', 'D', 'C')
('A', 'C', 'B', 'D')
```

find the most common elements in an iterable
``` python
import collections
c = collections.Counter('helloworld')
Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
c.most_common(3)
[('l', 3), ('o', 2), ('e', 1)]
```

set unions
``` python
A = {2, 3, 5}
B = {1, 3, 5}
C = A.union(B)
{2, 3, 5, 1}
```

## Nested lists and dicts

list of lists

``` python
ceo_nested_list = [
    ["Warren Buffet", 88, "CEO of Berkshire Hathaway"],
    ["Jeff Bezos", 55, "CEO of Amazon"],
    ["Harry Markowitz", 91, "Professor of Finance"]
]

# Retrieve occupation of first entry
first_entry_occupation = ceo_nested_list[0][2]
```

dict of dict

``` python
stocks_nested_dict = {
    "APPL": {
        "name": "Apple",
        "exchange": "NASDAQ",
        "market_cap": 937.7
    },
    "MU": {
        "name": "Micron Technology",
        "exchange": "NASDAQ",
        "market_cap": 48.03
    },
    "AMD": {
        "name": "Advanced Micro Devices",
        "exchange": "NASDAQ",
        "market_cap": 29.94
    },
    "TWTR": {
        "name": "Twitter",
        "exchange": "NASDAQ",
        "market_cap": 26.42
    }
}

twitter_market_cap = stocks_nested_dict["TWTR"]["market_cap"]

# Print results to screen
print(f"Name of TWTR ticker is {twitter_name}. TWTR is available on {twitter_exchange}, and it currently has a market capitalization of {twitter_market_cap}.")
```

list of dict

``` python
ceo_nested_dict = [
    {
        "name": "Warren Buffet",
        "age": 88,
        "occupation": "CEO of Berkshire Hathaway"
    },
    {
        "name": "Jeff Bezos",
        "age": 55,
        "occupation": "CEO of Amazon"
    },
    {
        "name": "Harry Markowitz",
        "age": 91,
        "occupation": "Professor of Finance"
    }
]

second_entry_occupation = ceo_nested_dict[1]["occupation"]
print(f"The second entry in ceo_nested_dict is {second_entry_name}, a {second_entry_age} year old {second_entry_occupation}.")
```

dict of lists

``` python
stocks_nested_list = {
    "APPL": ["Apple", 101.32, "NASDAQ", 937.7],
    "MU": ["Micron Technology", 32.12, "NASDAQ", 48.03],
    "AMD": ["Advanced Micro Devices", 23.12, "NASDAQ", 29.94],
    "TWTR": ["Twitter", 34.40, "NASDAQ", 26.42]
}
appl_exchange = stocks_nested_list["APPL"][2]
print(f"APPL ticker stands for {appl_name}. APPL stock price is currently {appl_stock_price}, and it is available on {appl_exchange}.")
```