# python_apis_web.md

## API

### Parameters

Parameters can be specified in one of two ways. Parameters can follow / forward slashes
or be specified by parameter name and then by the parameter value.

```http
"/" = alternative param seperator
http://numbersapi.com/42
```

When used with parameter names, URL parameters have to be separated from the request
URL with the ? symbol.

```http
"?" = query starting here
"=" = the parameter's key value pair
http://api.worldbank.org/v2/country/us/indicator/NY.GDP.MKTP.CD?format=json
http://numbersapi.com/random?min=10
```

Multiple parameters can be passed in with the same URL by separating each parameter with
an & symbol

```http
"&" = param seperator
http://numbersapi.com/random?min=10&max=20
```

[Various success codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses)

Prettify json: https://jsonformatter.org/json-pretty-print

### Requests

[Python Request docs](https://docs.python-requests.org/en/master/user/quickstart/)

```python
import requests
url = "http://api.worldbank.org/v2/country/us/indicator/NY.GDP.MKTP.CD"
url = url + "?format=json"
response_data = requests.get(url)  # Store response as variable
response_content = response_data.content  # Get content
data = response_data.json()  # Formatting as json
print(json.dumps(data, indent=4))  #  format the JSON output
country = data[1][1]['country']['value']
```

Request URL parameters with python variables

```python
url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
results = requests.get(url).json()
```

Pull Alpaca price barset data, using Alpaca SDK

```python
# Create the Alpaca API object
alpaca = tradeapi.REST(
    alpaca_api_key,
    api_version="v2")
today = pd.Timestamp("2021-09-01", tz="America/New_York").isoformat()
tickers = ["FB", "TWTR"]
timeframe = "1D"

df_portfolio = alpaca.get_barset(
    tickers,
    end = today
).df

df_portfolio.index = df_portfolio.index.date
df_portfolio = df_portfolio.pct_change().dropna()
df_portfolio.plot(title="Daily Returns of FB and TWTR over the Last Year")
```

GET & POST requests are the majority of requests. GET requests are used to extract and acquire data from a server. POST requests are used to push new or updated data to the server. PUT requests are used to overwrite content on the server.

Typical API get request

```http
https://www.quandl.com/api/v3/datasets/OPEC/ORB.json?api_key=[YOUR-KEY-HERE]
```

## Email

send email
``` python
import win32com.client
inbox = win32com.client.gencache.EnsureDispatch("Outlook.Application").GetNamespace("MAPI")
#print(dir(inbox))
inbox = win32com.client.Dispatch("Outlook.Application")
#print(dir(inbox))
mail = inbox.CreateItem(0x0)
mail.To = "garth.mortensen@cool.com"
mail.Subject = "This is the Subject"
mail.Body = "This is the body"
mail.Send()
```

## Blockchain

Unconfirmed transactions are written to a mempool (a waiting room for transactions that haven't been added to a block). Aka "unconfirmed transactions pool"

``` python
from pathlib import Path  # for accessing dotenv location
import os  # access dotenv
from dotenv import load_dotenv  # read MNEMONIC 12 words
from mnemonic import Mnemonic  # to produce our phrase
from bip44 import Wallet  # to produce our wallet
from web3 import Account  # to create tha account
```