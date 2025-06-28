# py_ml_ai.md

## Machine Learning Libraries

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
import tensorflow
import keras
import spacy
import nltk
```

## Environment Setup

### AI Environment
```bash
conda create --name ai python=3.7 anaconda
pip install --upgrade tensorflow  # The TensorFlow 2.0 package has several dependencies
conda list tensorflow  # 2.5 or higher
conda list keras  # Keras is included with TensorFlow 2.0
```

### NLP Environment
```bash
conda create --name nlpenv2 python=3.7 anaconda
python -c "import nltk;nltk.download('all')" -y
conda install -c conda-forge wordcloud -y
conda list wordcloud
pip install newsapi-python==0.2.5
conda list ibm-watson
conda install -c conda-forge spacy -y
python -m spacy download en_core_web_sm
conda list spacy
```

## Data Preprocessing

### Categorical Data Encoding

Many machine learning algorithms are sensitive to input features with wide ranges of numbers, so normalize all data to the same scale. This prevents any single feature from dominating others.

Label encoding - converts text to integers:

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

label_encoder = LabelEncoder()  # Creating an instance of label encoder
label_encoder.fit(loans_df["month"])  # Fitting the label encoder
list(label_encoder.classes_)  # List the classes identified by the label encoder

# Encode the months as an integer
loans_df["month_le"] = label_encoder.transform(loans_df["month"])
```

Manual encoding alternative:
```python
# Months dictionary
months_num = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12, }
```

Anonymous lambda function. Simply: month column is encoded using the lambda function, which looks for the dict value using the month column as key:
```python
print(months_num["January"])  # 1
print(months_num["February"])  # 2
print(months_num["March"])  # 3
loans_df["month_num"] = loans_df["month"].apply(lambda x: months_num[x])
```

### Dummy Encoding

Prevents models from treating categorical data as ordinal (e.g., treating month 12 as "greater" than month 1):

```python
loans_binary_encoded = pd.get_dummies(loans_df, columns=["gender"], drop_first=True)
```

**Dummy Variable Trap**: Avoid perfect correlation between dummy variables. If you have male/female columns, you only need one since they're mutually exclusive.

```python
loans_binary_encoded = pd.get_dummies(loans_df, columns=["education", "gender"], drop_first=True)
```

### Feature Scaling

Many models work better if numeric features are scaled to the same range. This ensures differences in scale don't sway predictions (e.g., income vs credit score).

**Standardization** - results in 0 mean with unit standard deviation:

```python
data_scaler = StandardScaler()
data_scaler.fit(loans_binary_encoded)
loans_data_scaled = data_scaler.transform(loans_binary_encoded)
```

### Data Reshaping

Reshape data to meet scikit-learn requirements:

```python
# Various ways to reshape target variable
y = df_loans["bad"].to_frame()  # DataFrame
y = df_loans["bad"].values.reshape(-1, 1)  # 2D array
y = df_loans["bad"].ravel()  # 1D array

# Reshape features for scikit-learn (X must be 2D, y can be 1D)
X_test = test["Lagged_Return"].to_frame()
```

## Model Creation and Evaluation

### Basic Model Setup

```python
# Create dataframe from model metrics
metrics = {k: v for k, v in zip(model.metrics_names, scores)}

# ROC curve data
roc_df_train = pd.DataFrame({"FPR Train": fpr_train, "TPR Train": tpr_train})

# Predictions dataframe
Results = y_test.to_frame()
Results["Predicted Return"] = predictions
```

### Model Evaluation Techniques

Apply functions to dataframes for preprocessing:

```python
def changeGender(gender):
    if gender == "Male":
        return 1
    else:
        return 0

df["Gender"] = df["Gender"].apply(changeGender)
```

### FastAPI ML Prediction Example

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame(data)
    model = LinearRegression()
    # Training and prediction logic
    predictions = model.predict(df)
    return {"predictions": predictions.tolist()}
```

## Key ML/AI Concepts

### Core Concepts Links
- **Everything**: https://www.kaggle.com/learn
- **OLS**: https://youtu.be/jEEJNz0RK4Q?t=193
- **K-means**: https://www.youtube.com/watch?v=4b5d3muPQmA
- **Lasso regularization**: https://www.youtube.com/watch?v=NGf0voTMlcs
- **PCA**: https://www.youtube.com/watch?v=FgakZw6K1QQ
- **SVM Part 1**: https://www.youtube.com/watch?v=3liCbRZPrZA
- **SVM Part 2**: https://www.youtube.com/watch?v=9NrALgHFwTo
- **Recall vs Precision**: https://www.youtube.com/watch?v=qWfzIYCvBqo
- **Tensors**: https://www.youtube.com/watch?v=f5liqUk0ZTw
- **Splines**: https://www.youtube.com/watch?v=EKDsH1uQing
- **POS Tagging**: https://spacy.io/api/data-formats#pos-tagging
- **ROC/AUC Curve**: https://www.youtube.com/watch?v=4jRBRDbJemM

### Important Notes
- **Selection bias** - Be aware of biases in your data
- **Perfect correlation problems**: When variables are perfectly correlated, algorithms can't determine causation
- **Normalization vs Standardization**: https://stats.stackexchange.com/questions/10289/whats-the-difference-between-normalization-and-standardization

## NLP Processing

### Text Processing Setup

```python
# Download NLTK data
python -c "import nltk;nltk.download('all')" -y

# spaCy model download
python -m spacy download en_core_web_sm
```

### Word Cloud Generation

```python
conda install -c conda-forge wordcloud -y
```

## Financial ML Applications

### Alpaca API Integration

```python
pip install alpaca-trade-api

# Environment variables for API keys
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
```

### Financial Data Processing

```python
# Portfolio evaluation metrics
columns = ["Backtest"]
metrics = ["Annualized Return", "Cumulative Returns", "Annual Volatility", "Sharpe Ratio", "Sortino Ratio"]
portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)
portfolio_evaluation_df.loc["Annualized Return"] = (signals_df["Portfolio Daily Returns"].mean() * 252)
```

## Best Practices

1. **Always scale features** when using algorithms sensitive to feature magnitude
2. **Avoid dummy variable trap** by dropping one category when creating dummy variables
3. **Handle missing data** appropriately before model training
4. **Validate data types** and convert as necessary
5. **Use cross-validation** for robust model evaluation
6. **Watch for selection bias** in your datasets
