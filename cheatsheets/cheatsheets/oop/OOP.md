# OOP

## OOP Advantages

- Encapsulation of data and methods within the class.

  - The primary reason for using encapsulation is to achieve data hiding and abstraction. It allows you to bundle data (attributes) and methods (functions) together within a class, restricting direct access to the data from outside the class.

    The main purposes of encapsulation are:

    1. **Data Hiding**: Encapsulation helps to hide the internal implementation details of a class and expose only the necessary interfaces or methods to interact with the data. By encapsulating data, you can prevent direct manipulation of class attributes, ensuring data integrity and reducing the chances of accidental errors or misuse.

       Data hiding is *primarily about controlling the visibility and access to data*, ensuring that it can only be accessed through the defined methods or interfaces of the class.

       In Python, attributes defined within a class are accessed using the dot notation (`class_name.attribute_name`). By default, the attributes of a class are accessible outside the class, but by convention, attributes prefixed with a single underscore (`_attribute_name`) are considered as **"protected" attributes**, indicating that they should not be accessed directly. This is a form of naming convention to signal that these attributes are implementation details and not intended for external use. However, it's important to note that Python does not enforce strict access control like some other languages.

    2. **Abstraction**: Encapsulation enables abstraction by providing a high-level interface to interact with objects. It allows you to focus on the essential features and behaviors of an object while hiding the underlying complexity. Users of the class only need to know how to use the provided methods without worrying about the internal implementation.

    3. **Code Organization**: Encapsulation promotes better code organization and modularity. By grouping related data and methods together in a class, you can organize your code into logical units. This improves code readability, maintainability, and reusability.

    While encapsulation does provide some level of access control, it is not primarily intended for security purposes. In Python, there are naming conventions (e.g., using underscores) to indicate that certain attributes or methods should be considered as implementation details and should not be accessed directly. However, Python relies more on the developer's responsibility to follow conventions rather than strict access control mechanisms for security.

  By converting this code:

  ```python
  def hash_data(data):
      sha = hashlib.sha256()
      encoded_data = str(data).encode()
      sha.update(encoded_data)
      return sha.hexdigest()
  ```

   into a class and utilizing encapsulation, the following benefits can be achieved:

  1. **Data Integrity**: Encapsulation allows you to control how the `data` is accessed and modified within the class. You can enforce certain constraints or validations on the `data` before performing the hashing operation. For example, you can ensure that the `data` is always in a specific format or meets certain criteria before being processed.

     ``` python
     class DataHasher:
         def __init__(self, data):
             self.data = self._validate_data(data)
         
         def _validate_data(self, data):
             # data validation logic: e.g. ensure data data is non-empty string
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

  2. **Code Reusability**: Converting the code into a class promotes reusability. Once encapsulated within a class, the hashing functionality can be used across multiple instances of the class. Each instance can work with its own set of data, providing a modular and reusable solution.

     ``` python
     class DataHasher:
         def __init__(self, data):
             self.data = data
         
         def hash_data(self):
             sha = hashlib.sha256()
             encoded_data = str(self.data).encode()
             sha.update(encoded_data)
             return sha.hexdigest()
     
     # code reuse
     data1 = "Hello, World!"
     data2 = "OpenAI"
     
     hasher1 = DataHasher(data1)
     hashed_data1 = hasher1.hash_data()
     print(hashed_data1)
     
     hasher2 = DataHasher(data2)
     hashed_data2 = hasher2.hash_data()
     print(hashed_data2)
     ```

  3. **Code Organization**: Encapsulation helps organize related data and methods within a class. In this case, the `data` and the hashing functionality can be encapsulated within the class, making the code more readable and maintainable. Other related methods or attributes can also be added to the class, providing a cohesive structure.

     ``` python
     class DataHasher:
         def __init__(self, data):
             self.data = data
         
         def hash_data(self):
             sha = hashlib.sha256()
             encoded_data = str(self.data).encode()
             sha.update(encoded_data)
             return sha.hexdigest()
     
         def additional_method(self):
             # additional hashing methods
             pass
     ```

  4. **Abstraction**: Encapsulation enables abstraction by exposing a high-level interface to interact with the hashed data. Users of the class do not need to know the intricate details of the hashing algorithm or how the data is processed. They can simply create an object of the class and use the provided methods to get the hashed value.

     ``` python
     class DataHasher:
         def __init__(self, data):
             self.data = data
         
         def hash_data(self):
             sha = hashlib.sha256()
             encoded_data = str(self.data).encode()
             sha.update(encoded_data)
             return sha.hexdigest()
     
     # use
     data = "Hello, World!"
     hasher = DataHasher(data)
     hashed_data = hasher.hash_data()
     print(hashed_data)
     ```

  5. **Potential for Enhancement**: Converting the code into a class sets the groundwork for future enhancements. For example, you can easily extend the class to support different hashing algorithms or additional methods related to hashing. Inheritance and polymorphism can also be leveraged to create specialized subclasses with unique hashing behaviors.

     ``` python
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
             # additional hashing methods
             pass
     
     class SpecializedHasher(DataHasher):
         def additional_method(self):
             # implement a specialized version of additional_method
             pass
     ```

  ## Interface

  starting code:

  ``` python
  def hash_data(data):
      sha = hashlib.sha256()
      encoded_data = str(data).encode()
      sha.update(encoded_data)
      return sha.hexdigest()
  ```

  create an interface:

  ``` python
  import hashlib
  
  class DataHasherInterface:
      def hash_data(self, data):
          pass
  
  class DataHasher(DataHasherInterface):
      def hash_data(self, data):
          sha = hashlib.sha256()
          encoded_data = str(data).encode()
          sha.update(encoded_data)
          return sha.hexdigest()
  ```

  Here's how you can convert the given code into a class and implement a simple interface.

  First define `DataHasherInterface` interface, with a single method `hash_data()`. The method is left empty, serving as a placeholder that needs to be implemented by any class that implements the interface.

  Next, define the `DataHasher` class, which inherits from `DataHasherInterface`. By inheriting from the interface, the `DataHasher` class is required to implement the `hash_data()` method.

  ```python
  import hashlib
  
  # the interface
  class DataHasherInterface:
      def hash_data(self, data):
          pass
  
  class DataHasher(DataHasherInterface):
      def hash_data(self, data):
          sha = hashlib.sha256()
          encoded_data = str(data).encode()
          sha.update(encoded_data)
          return sha.hexdigest()
  ```

  Now, let's demonstrate how to use the class and interface:

  ```python
  data = "Hello, World!"
  
  hasher = DataHasher()
  hashed_data = hasher.hash_data(data)
  print(hashed_data)
  ```

  We create an instance of the `DataHasher` class and call the `hash_data()` method to hash the provided `data`. The implementation of `hash_data()` within the `DataHasher` class executes the same logic as in the original function.

  The use of the interface allows for a clear and standardized way to interact with different implementations of the `DataHasher` class. Any class that implements the `DataHasherInterface` can be used interchangeably with the `DataHasher` class, as long as it provides the required `hash_data()` method.

  This approach demonstrates the implementation of a simple interface in Python, providing a contract for classes to follow while enabling code flexibility and the ability to switch implementations seamlessly.