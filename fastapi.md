# fastapi.md

## Basic Setup

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Item):
    return item
```

## Running the Server

```bash
uvicorn main:app --reload      # Development server with auto-reload
uvicorn main:app --host 0.0.0.0 --port 8000  # Custom host/port
fastapi dev main.py            # FastAPI development command
fastapi run main.py            # Production server
```

## Path Parameters & Query Parameters

```python
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Long description"})
    return item
```

## Request Body & Response Models

```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    # Save user logic here
    return {"id": 1, "name": user.name, "email": user.email}
```

## Dependency Injection

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```

## Data Science API Example

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