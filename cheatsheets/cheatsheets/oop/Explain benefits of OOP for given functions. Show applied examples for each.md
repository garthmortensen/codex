

# Explain benefits of OOP for given functions. Show applied examples for each

## Overview

By converting this code into a class and utilizing encapsulation, the following benefits can be achieved:

1. **Data Integrity**: Encapsulation allows you to control how the `data` is accessed and modified within the class. You can enforce certain constraints or validations on the `data` before performing the hashing operation. For example, you can ensure that the `data` is always in a specific format or meets certain criteria before being processed.

2. **Code Reusability**: Converting the code into a class promotes reusability. Once encapsulated within a class, the hashing functionality can be used across multiple instances of the class. Each instance can work with its own set of data, providing a modular and reusable solution.

3. **Code Organization**: Encapsulation helps organize related data and methods within a class. In this case, the `data` and the hashing functionality can be encapsulated within the class, making the code more readable and maintainable. Other related methods or attributes can also be added to the class, providing a cohesive structure.

4. **Abstraction**: Encapsulation enables abstraction by exposing a high-level interface to interact with the hashed data. Users of the class do not need to know the intricate details of the hashing algorithm or how the data is processed. They can simply create an object of the class and use the provided methods to get the hashed value.

5. **Potential for Enhancement**: Converting the code into a class sets the groundwork for future enhancements. For example, you can easily extend the class to support different hashing algorithms or additional methods related to hashing. Inheritance and polymorphism can also be leveraged to create specialized subclasses with unique hashing behaviors.

By utilizing encapsulation and converting the code into a class, you can improve the structure, maintainability, and flexibility of the code, while also enabling code reusability and abstraction.

## e.g. 1

In the given code:

```python
def hash_data(data):
    sha = hashlib.sha256()
    encoded_data = str(data).encode()
    sha.update(encoded_data)
    return sha.hexdigest()
```

The code defines a function `hash_data` that takes `data` as input, hashes it using the SHA-256 algorithm, and returns the resulting digest.

Here's how you can convert the given code into a class, addressing each numbered bullet point:

1. **Data Integrity**:

```python
import hashlib

class DataHasher:
    def __init__(self, data):
        self.data = self._validate_data(data)
    
    def _validate_data(self, data):
        # Implement your data validation logic here
        # For example, ensure the data is a non-empty string
        if isinstance(data, str) and data:
            return data
        else:
            raise ValueError("Invalid data. Please provide a non-empty string.")

    def hash_data(self):
        sha = hashlib.sha256()
        encoded_data = str(self.data).encode()
        sha.update(encoded_data)
        return sha.hexdigest()
```

In this example, we've added an `_validate_data` method within the class to perform data validation. This method is called within the constructor (`__init__`) to ensure that the `data` provided is a non-empty string. If the data is invalid, a `ValueError` is raised.

2. **Code Reusability**:

```python
import hashlib

class DataHasher:
    def __init__(self, data):
        self.data = data
    
    def hash_data(self):
        sha = hashlib.sha256()
        encoded_data = str(self.data).encode()
        sha.update(encoded_data)
        return sha.hexdigest()

# Usage
data1 = "Hello, World!"
data2 = "OpenAI"

hasher1 = DataHasher(data1)
hashed_data1 = hasher1.hash_data()
print(hashed_data1)

hasher2 = DataHasher(data2)
hashed_data2 = hasher2.hash_data()
print(hashed_data2)
```

In this example, we create two instances of the `DataHasher` class, `hasher1` and `hasher2`, each with its own `data` attribute. The `hash_data` method is then called on each instance to perform the hashing operation.

3. **Code Organization**:

```python
import hashlib

class DataHasher:
    def __init__(self, data):
        self.data = data
    
    def hash_data(self):
        sha = hashlib.sha256()
        encoded_data = str(self.data).encode()
        sha.update(encoded_data)
        return sha.hexdigest()

    def additional_method(self):
        # Implement additional methods related to hashing
        pass
```

In this example, we've added an `additional_method` to the `DataHasher` class. This demonstrates how you can extend the class by adding more methods related to hashing or other functionality.

4. **Abstraction**:

```python
import hashlib

class DataHasher:
    def __init__(self, data):
        self.data = data
    
    def hash_data(self):
        sha = hashlib.sha256()
        encoded_data = str(self.data).encode()
        sha.update(encoded_data)
        return sha.hexdigest()

# Usage
data = "Hello, World!"

hasher = DataHasher(data)
hashed_data = hasher.hash_data()
print(hashed_data)
```

In this example, we create an instance of the `DataHasher` class and use the `hash_data` method to get the hashed value. The user does not need to know the internal details of the hashing process; they simply interact with the class's interface.

5. **Potential for Enhancement**:

```python
import hashlib

class DataHasher:
    def __init__(self, data):
        self.data = data
    
    def hash_data(self):
        sha = hashlib.sha256()
        encoded_data = str(self.data).encode()
        sha.update(encoded_data)
        return sha.hexdigest()

   

 def additional_method(self):
        # Implement additional methods related to hashing
        pass

class SpecializedHasher(DataHasher):
    def additional_method(self):
        # Implement a specialized version of additional_method
        pass
```

In this example, we create a specialized subclass `SpecializedHasher` that inherits from `DataHasher`. The `SpecializedHasher` class can override the `additional_method` inherited from the base class to provide a unique implementation. This showcases the potential for inheritance and polymorphism in object-oriented programming.

By converting the code into a class as shown above, you achieve the benefits of encapsulation, including improved data integrity, code reusability, code organization, abstraction, and the potential for future enhancements.

## e.g. 2

repeat the process for the following 

```python
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

Certainly! Here's how you can convert the given code into a class, addressing each numbered bullet point:

1. **Data Integrity**:

```python
import re
from nltk.corpus import reuters

class DocumentRetriever:
    def __init__(self, terms):
        self.terms = self._validate_terms(terms)
    
    def _validate_terms(self, terms):
        # Implement your terms validation logic here
        # For example, ensure the terms are non-empty strings
        if isinstance(terms, list) and all(isinstance(term, str) and term for term in terms):
            return terms
        else:
            raise ValueError("Invalid terms. Please provide a non-empty list of strings.")

    def retrieve_docs(self):
        result_docs = []
        for doc_id in money_news_ids:
            found_terms = [
                word
                for word in reuters.words(doc_id)
                if any(term in word.lower() for term in self.terms)
            ]
            if len(found_terms) > 0:
                result_docs.append(doc_id)
        return result_docs
```

In this example, we've added an `_validate_terms` method within the class to perform validation on the `terms` provided. This method is called within the constructor (`__init__`) to ensure that the `terms` are a non-empty list of strings. If the terms are invalid, a `ValueError` is raised.

2. **Code Reusability**:

```python
import re
from nltk.corpus import reuters

class DocumentRetriever:
    def __init__(self, terms):
        self.terms = terms
    
    def retrieve_docs(self):
        result_docs = []
        for doc_id in money_news_ids:
            found_terms = [
                word
                for word in reuters.words(doc_id)
                if any(term in word.lower() for term in self.terms)
            ]
            if len(found_terms) > 0:
                result_docs.append(doc_id)
        return result_docs

# Usage
terms1 = ["yen", "japan"]
terms2 = ["dollar", "economy"]

retriever1 = DocumentRetriever(terms1)
retrieved_docs1 = retriever1.retrieve_docs()
print(retrieved_docs1)

retriever2 = DocumentRetriever(terms2)
retrieved_docs2 = retriever2.retrieve_docs()
print(retrieved_docs2)
```

In this example, we create two instances of the `DocumentRetriever` class, `retriever1` and `retriever2`, each with its own `terms` attribute. The `retrieve_docs` method is then called on each instance to retrieve the relevant documents.

3. **Code Organization**:

```python
import re
from nltk.corpus import reuters

class DocumentRetriever:
    def __init__(self, terms):
        self.terms = terms
    
    def retrieve_docs(self):
        result_docs = []
        for doc_id in money_news_ids:
            found_terms = [
                word
                for word in reuters.words(doc_id)
                if any(term in word.lower() for term in self.terms)
            ]
            if len(found_terms) > 0:
                result_docs.append(doc_id)
        return result_docs

    def additional_method(self):
        # Implement additional methods related to document retrieval
        pass
```

In this example, we've added an `additional_method` to the `DocumentRetriever` class. This demonstrates how you can extend the class by adding more methods related to document retrieval or other functionality.

4. **Abstraction**:

```python
import re
from nltk.corpus import reuters

class

 DocumentRetriever:
    def __init__(self, terms):
        self.terms = terms
    
    def retrieve_docs(self):
        result_docs = []
        for doc_id in money_news_ids:
            found_terms = [
                word
                for word in reuters.words(doc_id)
                if any(term in word.lower() for term in self.terms)
            ]
            if len(found_terms) > 0:
                result_docs.append(doc_id)

        return result_docs

# Usage
terms = ["yen", "japan"]

retriever = DocumentRetriever(terms)
retrieved_docs = retriever.retrieve_docs()
print(retrieved_docs)
```

In this example, we create an instance of the `DocumentRetriever` class and use the `retrieve_docs` method to retrieve the relevant documents. The user does not need to know the internal details of the retrieval process; they simply interact with the class's interface.

5. **Potential for Enhancement**:

```python
import re
from nltk.corpus import reuters

class DocumentRetriever:
    def __init__(self, terms):
        self.terms = terms
    
    def retrieve_docs(self):
        result_docs = []
        for doc_id in money_news_ids:
            found_terms = [
                word
                for word in reuters.words(doc_id)
                if any(term in word.lower() for term in self.terms)
            ]
            if len(found_terms) > 0:
                result_docs.append(doc_id)

        def additional_method(self):
            # Implement additional methods related to document retrieval
            pass

class SpecializedRetriever(DocumentRetriever):
    def additional_method(self):
        # Implement a specialized version of additional_method
        pass
```

In this example, we create a specialized subclass `SpecializedRetriever` that inherits from `DocumentRetriever`. The `SpecializedRetriever` class can override the `additional_method` inherited from the base class to provide a unique implementation. This showcases the potential for inheritance and polymorphism in object-oriented programming.

By converting the code into a class as shown above, you achieve the benefits of encapsulation, including improved data integrity, code reusability, code organization, abstraction, and the potential for future enhancements.