# mongodb.md

## About
**Name:** MongoDB (derived from 'humongous', reflecting its ability to handle huge amounts of data)

**Created:** Released in 2009 by 10gen (now MongoDB Inc.), MongoDB was created to provide a scalable, flexible, document-oriented database. Its purpose is to store data in a way that's easy to scale and work with, especially for modern web applications.

**Similar Technologies:** CouchDB, Cassandra, DynamoDB, Redis, PostgreSQL (with JSONB), Firebase

**Plain Language Definition:**
MongoDB is a database that stores information in a flexible, JSON-like format, making it easy to handle lots of different kinds of data and scale as your app grows.

---

# Comprehensive Reference Guide

## Overview

MongoDB is a NoSQL document database that provides high performance, high availability, and automatic scaling. It stores data in flexible, JSON-like documents called BSON (Binary JSON).

**Key Features:**
- Document-oriented storage
- Dynamic schemas
- Rich query language
- Built-in replication and sharding
- GridFS for large file storage
- Text search capabilities

## Installation & Setup

### MongoDB Atlas (Cloud)

1. Register at [cloud.mongodb.com](https://cloud.mongodb.com/)
2. Create a free "Shared Cluster"
3. Setup security:
   - Database Access: Create user with Atlas admin privileges
   - Network Access: Whitelist your IP address
4. Connect using provided connection string

### Local Installation

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mongodb

# macOS (using Homebrew)
brew tap mongodb/brew
brew install mongodb-community

# Start MongoDB service
sudo systemctl start mongodb  # Linux
brew services start mongodb-community  # macOS
```

## Connection

### MongoDB Shell (mongosh)

```bash
# Connect to local instance
mongosh

# Connect to Atlas cluster
mongosh "mongodb+srv://cluster.mongodb.net/myDatabase" --username myUser

# Connect with options
mongosh --host localhost --port 27017 --username admin --password
```

### Connection String Format

```
mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]

# Examples
mongodb://localhost:27017/mydb
mongodb://user:pass@localhost:27017/mydb?authSource=admin
mongodb+srv://user:pass@cluster.mongodb.net/mydb
```

## Database Operations

### Basic Commands

```javascript
// Show help
help

// Database operations
show dbs                    // List all databases
use myDatabase             // Switch to database (creates if not exists)
db                        // Show current database
db.dropDatabase()         // Delete current database

// Collection operations
show collections          // List collections in current database
db.createCollection("myCollection")  // Create collection explicitly
db.myCollection.drop()    // Delete collection

// Get database stats
db.stats()
db.myCollection.stats()
```

## CRUD Operations

### Create (Insert)

```javascript
// Insert single document
db.users.insertOne({
    name: "John Doe",
    email: "john@example.com",
    age: 30,
    tags: ["developer", "javascript"]
})

// Insert multiple documents
db.users.insertMany([
    {name: "Alice", email: "alice@example.com", age: 25},
    {name: "Bob", email: "bob@example.com", age: 35}
])

// Insert with custom _id
db.users.insertOne({
    _id: "user123",
    name: "Custom User",
    email: "custom@example.com"
})
```

### Read (Find)

```javascript
// Find all documents
db.users.find()
db.users.find().pretty()  // Formatted output

// Find with conditions
db.users.findOne({name: "John Doe"})  // First matching document
db.users.find({age: {$gt: 25}})       // Age greater than 25
db.users.find({age: {$gte: 25, $lt: 40}})  // Age between 25-40

// Projection (select specific fields)
db.users.find({}, {name: 1, email: 1, _id: 0})  // Include name, email; exclude _id
db.users.find({age: {$gt: 25}}, {name: 1})      // Conditional with projection

// Sorting and limiting
db.users.find().sort({age: 1})        // Sort by age ascending
db.users.find().sort({age: -1})       // Sort by age descending
db.users.find().limit(5)              // Limit to 5 results
db.users.find().skip(10).limit(5)     // Pagination

// Count documents
db.users.countDocuments()             // Count all
db.users.countDocuments({age: {$gt: 25}})  // Count with condition
```

### Update

```javascript
// Update single document
db.users.updateOne(
    {name: "John Doe"},                    // Filter
    {$set: {age: 31, city: "New York"}}   // Update
)

// Update multiple documents
db.users.updateMany(
    {age: {$lt: 30}},
    {$set: {category: "young"}}
)

// Replace entire document
db.users.replaceOne(
    {name: "John Doe"},
    {name: "John Smith", email: "john.smith@example.com", age: 32}
)

// Upsert (update or insert)
db.users.updateOne(
    {email: "new@example.com"},
    {$set: {name: "New User", age: 25}},
    {upsert: true}
)

// Update operators
db.users.updateOne({name: "John"}, {$inc: {age: 1}})        // Increment
db.users.updateOne({name: "John"}, {$push: {tags: "senior"}}) // Add to array
db.users.updateOne({name: "John"}, {$pull: {tags: "junior"}}) // Remove from array
db.users.updateOne({name: "John"}, {$unset: {category: ""}})  // Remove field
```

### Delete

```javascript
// Delete single document
db.users.deleteOne({name: "John Doe"})

// Delete multiple documents
db.users.deleteMany({age: {$lt: 18}})

// Delete all documents in collection
db.users.deleteMany({})
```

## Query Operators

### Comparison Operators

```javascript
// Basic comparisons
db.products.find({price: {$eq: 100}})     // Equal to
db.products.find({price: {$ne: 100}})     // Not equal to
db.products.find({price: {$gt: 50}})      // Greater than
db.products.find({price: {$gte: 50}})     // Greater than or equal
db.products.find({price: {$lt: 100}})     // Less than
db.products.find({price: {$lte: 100}})    // Less than or equal
db.products.find({category: {$in: ["electronics", "books"]}})    // In array
db.products.find({category: {$nin: ["electronics", "books"]}})   // Not in array
```

### Logical Operators

```javascript
// AND (default behavior)
db.products.find({price: {$gt: 50}, category: "electronics"})

// OR
db.products.find({
    $or: [
        {price: {$lt: 50}},
        {category: "books"}
    ]
})

// NOT
db.products.find({price: {$not: {$gt: 100}}})

// NOR
db.products.find({
    $nor: [
        {price: {$lt: 50}},
        {category: "electronics"}
    ]
})
```

### Element Operators

```javascript
// Check if field exists
db.products.find({discount: {$exists: true}})
db.products.find({discount: {$exists: false}})

// Check field type
db.products.find({price: {$type: "number"}})
db.products.find({price: {$type: "string"}})
```

### Array Operators

```javascript
// Array contains element
db.products.find({tags: "electronics"})

// All elements in array
db.products.find({tags: {$all: ["electronics", "mobile"]}})

// Array size
db.products.find({tags: {$size: 3}})

// Element match in array of objects
db.products.find({
    reviews: {
        $elemMatch: {
            rating: {$gte: 4},
            author: "John"
        }
    }
})
```

### Text Search

```javascript
// Create text index
db.articles.createIndex({title: "text", content: "text"})

// Text search
db.articles.find({$text: {$search: "mongodb database"}})

// Text search with score
db.articles.find(
    {$text: {$search: "mongodb"}},
    {score: {$meta: "textScore"}}
).sort({score: {$meta: "textScore"}})
```

## Indexing

### Create Indexes

```javascript
// Single field index
db.users.createIndex({email: 1})        // Ascending
db.users.createIndex({age: -1})         // Descending

// Compound index
db.users.createIndex({age: 1, name: 1})

// Text index
db.articles.createIndex({title: "text", content: "text"})

// Partial index
db.users.createIndex(
    {email: 1},
    {partialFilterExpression: {age: {$gte: 18}}}
)

// Unique index
db.users.createIndex({email: 1}, {unique: true})

// TTL index (expires documents)
db.sessions.createIndex({createdAt: 1}, {expireAfterSeconds: 3600})
```

### Index Management

```javascript
// List indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex({email: 1})
db.users.dropIndex("email_1")

// Rebuild indexes
db.users.reIndex()

// Get index stats
db.users.aggregate([{$indexStats: {}}])
```

## Aggregation Pipeline

### Basic Aggregation

```javascript
// Simple aggregation
db.orders.aggregate([
    {$match: {status: "completed"}},
    {$group: {_id: "$customerId", total: {$sum: "$amount"}}},
    {$sort: {total: -1}}
])
```

### Aggregation Stages

```javascript
// $match - Filter documents
db.sales.aggregate([
    {$match: {date: {$gte: new Date("2023-01-01")}}}
])

// $group - Group and accumulate
db.sales.aggregate([
    {$group: {
        _id: "$product",
        totalSales: {$sum: "$amount"},
        avgPrice: {$avg: "$price"},
        count: {$sum: 1}
    }}
])

// $project - Reshape documents
db.users.aggregate([
    {$project: {
        fullName: {$concat: ["$firstName", " ", "$lastName"]},
        age: 1,
        _id: 0
    }}
])

// $sort - Sort documents
db.products.aggregate([
    {$sort: {price: -1, name: 1}}
])

// $limit and $skip - Pagination
db.products.aggregate([
    {$skip: 20},
    {$limit: 10}
])

// $lookup - Join collections
db.orders.aggregate([
    {$lookup: {
        from: "customers",
        localField: "customerId",
        foreignField: "_id",
        as: "customer"
    }}
])

// $unwind - Deconstruct arrays
db.products.aggregate([
    {$unwind: "$tags"}
])

// $addFields - Add new fields
db.products.aggregate([
    {$addFields: {
        discountPrice: {$multiply: ["$price", 0.9]}
    }}
])
```

### Complex Aggregation Examples

```javascript
// Sales report with multiple stages
db.sales.aggregate([
    {$match: {date: {$gte: new Date("2023-01-01")}}},
    {$lookup: {
        from: "products",
        localField: "productId",
        foreignField: "_id",
        as: "product"
    }},
    {$unwind: "$product"},
    {$group: {
        _id: {
            category: "$product.category",
            month: {$month: "$date"}
        },
        totalRevenue: {$sum: "$amount"},
        totalQuantity: {$sum: "$quantity"}
    }},
    {$sort: {"_id.month": 1, "totalRevenue": -1}}
])
```

## Data Modeling

### Embedded Documents

```javascript
// User with embedded address
{
    _id: ObjectId("..."),
    name: "John Doe",
    email: "john@example.com",
    address: {
        street: "123 Main St",
        city: "New York",
        state: "NY",
        zipCode: "10001"
    }
}

// Blog post with embedded comments
{
    _id: ObjectId("..."),
    title: "MongoDB Tutorial",
    content: "...",
    author: "John Doe",
    comments: [
        {
            author: "Alice",
            text: "Great post!",
            date: ISODate("2023-01-01")
        },
        {
            author: "Bob",
            text: "Very helpful",
            date: ISODate("2023-01-02")
        }
    ]
}
```

### References

```javascript
// User document
{
    _id: ObjectId("user123"),
    name: "John Doe",
    email: "john@example.com"
}

// Order document referencing user
{
    _id: ObjectId("order456"),
    userId: ObjectId("user123"),  // Reference to user
    items: [...],
    total: 150.00
}
```

## Schema Validation

```javascript
// Create collection with schema validation
db.createCollection("products", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["name", "price", "category"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "must be a string and is required"
                },
                price: {
                    bsonType: "number",
                    minimum: 0,
                    description: "must be a positive number and is required"
                },
                category: {
                    bsonType: "string",
                    enum: ["electronics", "books", "clothing"],
                    description: "must be one of the enum values and is required"
                }
            }
        }
    }
})
```

## Transactions

```javascript
// Multi-document transaction
const session = db.getMongo().startSession();
session.startTransaction();

try {
    const accountsCol = session.getDatabase("banking").accounts;
    const transfersCol = session.getDatabase("banking").transfers;
    
    // Transfer money between accounts
    accountsCol.updateOne(
        {_id: "account1"},
        {$inc: {balance: -100}},
        {session: session}
    );
    
    accountsCol.updateOne(
        {_id: "account2"},
        {$inc: {balance: 100}},
        {session: session}
    );
    
    transfersCol.insertOne(
        {from: "account1", to: "account2", amount: 100},
        {session: session}
    );
    
    session.commitTransaction();
} catch (error) {
    session.abortTransaction();
    throw error;
} finally {
    session.endSession();
}
```

## Performance Optimization

### Query Optimization

```javascript
// Use explain() to analyze query performance
db.users.find({age: {$gt: 25}}).explain("executionStats")

// Create appropriate indexes
db.users.createIndex({age: 1})

// Use projection to limit returned fields
db.users.find({age: {$gt: 25}}, {name: 1, email: 1})

// Use limit() to restrict result set
db.users.find({age: {$gt: 25}}).limit(100)
```

### Bulk Operations

```javascript
// Bulk insert
db.products.insertMany([
    {name: "Product 1", price: 10},
    {name: "Product 2", price: 20},
    // ... more documents
], {ordered: false})  // Unordered for better performance

// Bulk write operations
db.products.bulkWrite([
    {insertOne: {document: {name: "New Product", price: 15}}},
    {updateOne: {filter: {name: "Product 1"}, update: {$set: {price: 12}}}},
    {deleteOne: {filter: {name: "Old Product"}}}
])
```

## Administration

### Database Administration

```javascript
// User management
db.createUser({
    user: "appUser",
    pwd: "password123",
    roles: [{role: "readWrite", db: "myDatabase"}]
})

db.dropUser("appUser")

// Show current operations
db.currentOp()

// Kill operation
db.killOp(operationId)

// Database profiling
db.setProfilingLevel(2)  // Profile all operations
db.system.profile.find().pretty()

// Replica set status (if applicable)
rs.status()
rs.conf()
```

### Backup and Restore

```bash
# Export database to JSON
mongoexport --db myDatabase --collection users --out users.json

# Import from JSON
mongoimport --db myDatabase --collection users --file users.json

# Dump entire database
mongodump --db myDatabase --out /backup/path

# Restore from dump
mongorestore --db myDatabase /backup/path/myDatabase
```

## GridFS (Large File Storage)

```javascript
// Store file in GridFS
mongofiles -d myDatabase put myfile.pdf

// List files in GridFS
mongofiles -d myDatabase list

// Retrieve file from GridFS
mongofiles -d myDatabase get myfile.pdf

// Delete file from GridFS
mongofiles -d myDatabase delete myfile.pdf
```

## MongoDB with Programming Languages

### Node.js Example

```javascript
const { MongoClient } = require('mongodb');

async function main() {
    const uri = "mongodb://localhost:27017";
    const client = new MongoClient(uri);
    
    try {
        await client.connect();
        const database = client.db('myDatabase');
        const collection = database.collection('users');
        
        // Insert document
        const result = await collection.insertOne({
            name: "John Doe",
            email: "john@example.com"
        });
        
        // Find documents
        const users = await collection.find({}).toArray();
        console.log(users);
        
    } finally {
        await client.close();
    }
}
```

### Python Example

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['myDatabase']
collection = db['users']

# Insert document
result = collection.insert_one({
    'name': 'John Doe',
    'email': 'john@example.com'
})

# Find documents
users = collection.find({})
for user in users:
    print(user)

# Close connection
client.close()
```

## Best Practices

### Schema Design
- Embed when data is accessed together
- Reference when data grows unbounded
- Avoid deep nesting (limit to 3-4 levels)
- Design for your query patterns

### Performance
- Create indexes for frequently queried fields
- Use compound indexes for multi-field queries
- Avoid large documents (>16MB limit)
- Use projection to limit returned data
- Consider read preferences for replica sets

### Security
- Enable authentication
- Use role-based access control
- Encrypt data in transit and at rest
- Keep MongoDB updated
- Monitor database access

### Operations
- Set up monitoring and alerting
- Implement regular backups
- Use connection pooling
- Plan for scaling (sharding)
- Document your schema and indexes

## Common Patterns

### Polymorphic Pattern
```javascript
// Different document types in same collection
{type: "article", title: "...", content: "..."}
{type: "video", title: "...", duration: 120}
{type: "image", title: "...", resolution: "1920x1080"}
```

### Bucket Pattern
```javascript
// Time-series data bucketing
{
    _id: ObjectId("..."),
    sensor_id: 123,
    timestamp: ISODate("2023-01-01T00:00:00Z"),
    measurements: [
        {time: 0, temperature: 20.1},
        {time: 60, temperature: 20.3},
        // ... more measurements
    ]
}
```

### Computed Pattern
```javascript
// Pre-computed aggregations
{
    _id: ObjectId("..."),
    product_id: "prod123",
    daily_stats: {
        date: "2023-01-01",
        total_sales: 1500,
        total_quantity: 75,
        average_price: 20.00
    }
}
```

## Troubleshooting

### Common Issues

**Connection Problems:**
- Check network connectivity
- Verify authentication credentials
- Ensure MongoDB service is running
- Check firewall settings

**Performance Issues:**
- Use `explain()` to analyze slow queries
- Check for missing indexes
- Monitor memory usage
- Consider query optimization

**Data Consistency:**
- Use transactions for multi-document operations
- Implement proper error handling
- Consider read/write concerns
- Monitor replica set lag

### Monitoring Commands

```javascript
// Server status
db.serverStatus()

// Collection stats
db.myCollection.stats()

// Index usage statistics
db.myCollection.aggregate([{$indexStats: {}}])

// Current operations
db.currentOp({active: true})
```

