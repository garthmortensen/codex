# graphql.md

## Basic Query Syntax

```graphql
# Simple query
query {
  user {
    id
    name
    email
  }
}

# Query with arguments
query {
  user(id: "123") {
    name
    email
    posts {
      title
      content
    }
  }
}

# Query with variables
query GetUser($userId: ID!) {
  user(id: $userId) {
    name
    email
  }
}
```

## Mutations

```graphql
# Create mutation
mutation {
  createUser(input: {
    name: "John Doe"
    email: "john@example.com"
  }) {
    id
    name
    email
  }
}

# Update mutation
mutation UpdateUser($id: ID!, $input: UserInput!) {
  updateUser(id: $id, input: $input) {
    id
    name
    email
    updatedAt
  }
}

# Delete mutation
mutation {
  deleteUser(id: "123") {
    success
    message
  }
}
```

## Schema Definition

```graphql
# Scalar types
scalar Date
scalar Upload

# Object types
type User {
  id: ID!
  name: String!
  email: String!
  age: Int
  isActive: Boolean!
  createdAt: Date!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  published: Boolean!
  tags: [String!]!
}

# Input types
input UserInput {
  name: String!
  email: String!
  age: Int
}

input PostInput {
  title: String!
  content: String!
  authorId: ID!
  tags: [String!]
}
```

## Query Operations

```graphql
# Root query type
type Query {
  users: [User!]!
  user(id: ID!): User
  posts(limit: Int, offset: Int): [Post!]!
  searchPosts(query: String!): [Post!]!
}

# Root mutation type
type Mutation {
  createUser(input: UserInput!): User!
  updateUser(id: ID!, input: UserInput!): User!
  deleteUser(id: ID!): DeleteResult!
  
  createPost(input: PostInput!): Post!
  publishPost(id: ID!): Post!
}

# Subscription type
type Subscription {
  postAdded: Post!
  userOnline(userId: ID!): User!
}
```

## Advanced Queries

```graphql
# Fragments
fragment UserInfo on User {
  id
  name
  email
}

query {
  user(id: "123") {
    ...UserInfo
    posts {
      title
    }
  }
}

# Inline fragments
query {
  search(term: "GraphQL") {
    ... on User {
      name
      email
    }
    ... on Post {
      title
      content
    }
  }
}

# Aliases
query {
  primaryUser: user(id: "123") {
    name
  }
  secondaryUser: user(id: "456") {
    name
  }
}
```

## Directives

```graphql
# Skip directive
query GetUser($includeEmail: Boolean!) {
  user(id: "123") {
    name
    email @skip(if: $includeEmail)
  }
}

# Include directive
query GetUser($includePosts: Boolean!) {
  user(id: "123") {
    name
    posts @include(if: $includePosts) {
      title
    }
  }
}

# Custom directives
directive @auth(role: String!) on FIELD_DEFINITION

type Query {
  sensitiveData: String @auth(role: "ADMIN")
}
```

## Error Handling

```graphql
# Error response format
{
  "data": {
    "user": null
  },
  "errors": [
    {
      "message": "User not found",
      "locations": [{"line": 2, "column": 3}],
      "path": ["user"],
      "extensions": {
        "code": "USER_NOT_FOUND"
      }
    }
  ]
}
```

## Data Science Examples

```graphql
# Analytics query
query DataAnalytics($dateRange: DateRange!) {
  analytics(dateRange: $dateRange) {
    totalUsers
    activeUsers
    avgSessionDuration
    topPages {
      path
      views
    }
  }
}

# ML model results
query ModelPredictions($input: PredictionInput!) {
  predict(input: $input) {
    prediction
    confidence
    features {
      name
      importance
    }
  }
}
```