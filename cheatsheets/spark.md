# spark.md

## About
**Name:** Apache Spark (the name "Spark" was chosen to evoke the idea of lightning-fast, in-memory data processing and analytics, like a spark igniting rapid computation.)

**Created:** Apache Spark was created in 2009 at UC Berkeley's AMPLab by Matei Zaharia and later donated to the Apache Software Foundation. Its purpose is to provide a fast, general-purpose engine for large-scale data processing, supporting both batch and streaming workloads.

**Similar Technologies:** Apache Hadoop MapReduce, Apache Flink, Dask, Presto, Apache Storm, Google Dataflow

**Plain Language Definition:**
Apache Spark is a tool that helps you process and analyze huge amounts of data very quickly, whether it's stored in files or coming in live, using simple code in languages like Python, Scala, or Java.

---

## Overview

Apache Spark is a unified compute engine for large-scale distributed data processing. It provides high-performance analytics for both batch and streaming data with support for multiple programming languages.

**Key Features:**
- In-memory computing for faster processing
- Unified platform for batch and streaming
- Support for SQL, ML, graph processing, and streaming
- Fault-tolerant distributed computing
- Multiple language APIs (Scala, Java, Python, R, SQL)

**Core Components:**
- **Spark Core**: Base engine with RDDs
- **Spark SQL**: Structured data processing with DataFrames/Datasets
- **Spark Streaming**: Real-time stream processing
- **MLlib**: Machine learning library
- **GraphX**: Graph processing

## Architecture

### Cluster Architecture

```
Driver Program → Cluster Manager → Worker Nodes
    ↓               (YARN/Standalone)      ↓
SparkContext    →    Worker Processes → Executors → Tasks
                        ↓                   ↓
                     Cache             Task Execution
```

**Components:**
- **Driver**: Runs main() function, creates SparkContext
- **Cluster Manager**: Allocates resources (YARN, Standalone, Mesos)
- **Worker Nodes**: Run executor processes
- **Executors**: Run tasks and store data in cache
- **Tasks**: Units of work sent to executors

### Execution Model

1. **Job**: Full program execution
2. **Stage**: Set of tasks that can run in parallel
3. **Task**: Unit of work sent to executor
4. **Partition**: Logical chunk of distributed dataset

## Installation & Setup

### Local Installation

```bash
# Download Spark
wget https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar -xzf spark-3.5.0-bin-hadoop3.tgz
export SPARK_HOME=/path/to/spark-3.5.0-bin-hadoop3
export PATH=$SPARK_HOME/bin:$PATH

# Start Spark Shell
spark-shell                    # Scala
pyspark                       # Python
sparkR                        # R
spark-sql                     # SQL

# Start Standalone Cluster
$SPARK_HOME/sbin/start-all.sh
```

### Cloud Options

**Databricks Community Edition:**
- Free cloud-based Spark environment
- Pre-configured clusters
- Notebook interface
- Built-in datasets

**AWS EMR, Google Dataproc, Azure HDInsight:**
- Managed Spark clusters
- Auto-scaling capabilities
- Integration with cloud storage

## Data Abstractions

### RDD (Resilient Distributed Dataset)

Low-level distributed collection of objects.

```python
# Create RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd = sc.textFile("hdfs://path/to/file.txt")

# Transformations (lazy)
rdd2 = rdd.map(lambda x: x * 2)
rdd3 = rdd.filter(lambda x: x > 3)
rdd4 = rdd.flatMap(lambda x: x.split(" "))

# Actions (trigger execution)
result = rdd.collect()          # Return all elements
count = rdd.count()             # Count elements
first = rdd.first()             # First element
sample = rdd.take(10)           # First 10 elements
rdd.saveAsTextFile("path")      # Save to file
```

### DataFrame

Structured data with named columns (like a table).

```python
# Create DataFrame
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# From file
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
df = spark.read.json("path/to/file.json")
df = spark.read.parquet("path/to/file.parquet")

# From RDD
rdd = sc.parallelize([(1, "Alice"), (2, "Bob")])
df = spark.createDataFrame(rdd, ["id", "name"])

# From list of dictionaries
data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
df = spark.createDataFrame(data)
```

### Dataset

Strongly-typed version of DataFrame (Scala/Java only).

```scala
// Scala example
case class Person(id: Int, name: String, age: Int)
val ds = spark.createDataset(Seq(Person(1, "Alice", 25), Person(2, "Bob", 30)))
```

## DataFrame Operations

### Basic Operations

```python
# Display data
df.show()                       # Show first 20 rows
df.show(10, truncate=False)     # Show 10 rows, don't truncate
df.printSchema()                # Show schema
df.describe().show()            # Summary statistics
df.count()                      # Row count
df.columns                      # Column names

# Schema and types
df.dtypes                       # Column types
df.schema                       # Full schema
```

### Selection and Filtering

```python
# Select columns
df.select("name", "age").show()
df.select(df.name, df.age + 1).show()

# Filter rows
df.filter(df.age > 25).show()
df.filter("age > 25").show()
df.where(df.name.like("A%")).show()

# Multiple conditions
df.filter((df.age > 25) & (df.name.like("A%"))).show()
df.filter((df.age > 25) | (df.salary > 50000)).show()
```

### Transformations

```python
# Add/modify columns
from pyspark.sql.functions import *

df.withColumn("age_plus_one", df.age + 1)
df.withColumn("full_name", concat(df.first_name, lit(" "), df.last_name))
df.withColumnRenamed("old_name", "new_name")

# Drop columns
df.drop("column_name")
df.drop("col1", "col2")

# Handle null values
df.na.drop()                    # Drop rows with any null
df.na.drop(subset=["name"])     # Drop rows with null in specific columns
df.na.fill(0)                   # Fill nulls with 0
df.na.fill({"age": 0, "name": "Unknown"})  # Fill with different values
```

### Grouping and Aggregation

```python
# Group by
df.groupBy("department").count().show()
df.groupBy("department").avg("salary").show()
df.groupBy("department").agg(
    avg("salary").alias("avg_salary"),
    max("age").alias("max_age"),
    count("*").alias("count")
).show()

# Window functions
from pyspark.sql.window import Window

window = Window.partitionBy("department").orderBy("salary")
df.withColumn("rank", row_number().over(window)).show()
df.withColumn("running_total", sum("salary").over(window)).show()
```

### Joins

```python
# Inner join (default)
df1.join(df2, "common_column").show()
df1.join(df2, df1.id == df2.user_id).show()

# Different join types
df1.join(df2, "id", "inner")
df1.join(df2, "id", "left")
df1.join(df2, "id", "right")
df1.join(df2, "id", "outer")
df1.join(df2, "id", "left_semi")    # Like EXISTS
df1.join(df2, "id", "left_anti")    # Like NOT EXISTS
```

### Sorting and Ordering

```python
# Sort
df.orderBy("age").show()
df.orderBy(df.age.desc()).show()
df.orderBy("department", "salary").show()
df.sort("age", ascending=False).show()
```

## Spark SQL

### Creating Temporary Views

```python
# Register DataFrame as temporary table
df.createOrReplaceTempView("employees")
df.createGlobalTempView("global_employees")

# Use SQL
result = spark.sql("SELECT * FROM employees WHERE age > 25")
result.show()
```

### SQL Operations

```sql
-- Basic queries
SELECT name, age, salary FROM employees WHERE age > 25;

-- Aggregations
SELECT department, 
       AVG(salary) as avg_salary,
       COUNT(*) as count
FROM employees 
GROUP BY department;

-- Window functions
SELECT name, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM employees;

-- Joins
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;

-- Subqueries
SELECT * FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### Advanced SQL Features

```sql
-- Common Table Expressions (CTEs)
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 75000
)
SELECT department, COUNT(*) FROM high_earners GROUP BY department;

-- CASE statements
SELECT name, 
       CASE 
           WHEN age < 30 THEN 'Young'
           WHEN age < 50 THEN 'Middle'
           ELSE 'Senior'
       END as age_group
FROM employees;

-- Array and map operations
SELECT name, size(skills) as skill_count FROM employees;
SELECT name, explode(skills) as skill FROM employees;
```

## Functions and Expressions

### Column Functions

```python
from pyspark.sql.functions import *

# String functions
df.select(upper("name"), lower("email"), length("description"))
df.select(substring("name", 1, 3), concat("first_name", "last_name"))
df.select(regexp_replace("phone", "[^0-9]", ""))  # Remove non-digits

# Numeric functions
df.select(round("price", 2), ceil("rating"), floor("score"))
df.select(abs("balance"), sqrt("area"), pow("base", "exponent"))

# Date functions
df.select(current_date(), current_timestamp())
df.select(year("date_col"), month("date_col"), dayofweek("date_col"))
df.select(date_add("date_col", 30), date_sub("date_col", 7))

# Conditional functions
df.select(when(col("age") > 18, "Adult").otherwise("Minor").alias("category"))
df.select(coalesce("preferred_name", "first_name").alias("display_name"))
```

### Aggregate Functions

```python
# Basic aggregations
df.agg(
    count("*").alias("total_count"),
    sum("amount").alias("total_amount"),
    avg("rating").alias("avg_rating"),
    min("created_date").alias("earliest"),
    max("created_date").alias("latest")
)

# Advanced aggregations
df.agg(
    stddev("price").alias("price_stddev"),
    variance("score").alias("score_variance"),
    collect_list("category").alias("all_categories"),
    collect_set("category").alias("unique_categories")
)
```

## Performance Optimization

### Caching and Persistence

```python
# Cache DataFrame in memory
df.cache()
df.persist()

# Different storage levels
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK)
df.persist(StorageLevel.MEMORY_ONLY_SER)  # Serialized
df.persist(StorageLevel.DISK_ONLY)

# Remove from cache
df.unpersist()
```

### Partitioning

```python
# Check current partitions
df.rdd.getNumPartitions()

# Repartition (shuffle)
df_repartitioned = df.repartition(4)
df_repartitioned = df.repartition("department")  # By column

# Coalesce (reduce partitions without shuffle)
df_coalesced = df.coalesce(2)

# Write with partitioning
df.write.partitionBy("year", "month").parquet("path/to/output")
```

### Query Optimization

```python
# Explain query plan
df.explain()
df.explain(True)  # Verbose

# Enable adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

# Broadcast small tables
from pyspark.sql.functions import broadcast
large_df.join(broadcast(small_df), "key")
```

### Indexing and Bucketing

```python
# Write with bucketing
df.write \
  .bucketBy(10, "user_id") \
  .sortBy("timestamp") \
  .saveAsTable("bucketed_table")

# Z-ordering (Delta Lake)
df.write.format("delta").option("dataChange", "false").mode("overwrite").save("path")
spark.sql("OPTIMIZE delta_table ZORDER BY (column1, column2)")
```

## Streaming

### Structured Streaming Basics

```python
# Read streaming data
streaming_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic_name") \
    .load()

# File streaming
streaming_df = spark \
    .readStream \
    .format("json") \
    .schema(schema) \
    .option("path", "input_directory") \
    .load()
```

### Stream Processing

```python
# Transform streaming data
processed_stream = streaming_df \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .filter(col("amount") > 100) \
    .groupBy("category") \
    .agg(sum("amount").alias("total"))

# Windowed aggregations
windowed_stream = streaming_df \
    .groupBy(
        window(col("timestamp"), "10 minutes", "5 minutes"),
        col("category")
    ) \
    .agg(count("*").alias("count"))
```

### Stream Output

```python
# Console output
query = processed_stream \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .trigger(processingTime="10 seconds") \
    .start()

# File output
query = processed_stream \
    .writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "output_directory") \
    .option("checkpointLocation", "checkpoint_directory") \
    .start()

# Kafka output
query = processed_stream \
    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "output_topic") \
    .start()

# Wait for termination
query.awaitTermination()
```

### Stream Monitoring

```python
# Query status
query.status
query.lastProgress
query.recentProgress

# Stop query
query.stop()

# Exception handling
try:
    query.awaitTermination()
except Exception as e:
    print(f"Query failed: {e}")
    query.stop()
```

## File Formats and I/O

### Reading Data

```python
# CSV
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ",") \
    .csv("path/to/file.csv")

# JSON
df = spark.read.json("path/to/file.json")
df = spark.read.option("multiline", "true").json("path/to/file.json")

# Parquet
df = spark.read.parquet("path/to/file.parquet")

# Delta Lake
df = spark.read.format("delta").load("path/to/delta_table")

# Database
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/mydb") \
    .option("dbtable", "table_name") \
    .option("user", "username") \
    .option("password", "password") \
    .load()
```

### Writing Data

```python
# CSV
df.write \
    .option("header", "true") \
    .mode("overwrite") \
    .csv("path/to/output")

# Parquet with partitioning
df.write \
    .partitionBy("year", "month") \
    .mode("overwrite") \
    .parquet("path/to/output")

# Delta Lake
df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("path/to/delta_table")

# Database
df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/mydb") \
    .option("dbtable", "output_table") \
    .option("user", "username") \
    .option("password", "password") \
    .mode("overwrite") \
    .save()
```

### Write Modes

```python
# Append: Add new records
df.write.mode("append").parquet("path")

# Overwrite: Replace all data
df.write.mode("overwrite").parquet("path")

# ErrorIfExists: Fail if path exists (default)
df.write.mode("error").parquet("path")

# Ignore: Do nothing if path exists
df.write.mode("ignore").parquet("path")
```

## Configuration and Tuning

### Spark Configuration

```python
# Set configuration
spark.conf.set("spark.sql.shuffle.partitions", "200")
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")

# Get configuration
spark.conf.get("spark.sql.shuffle.partitions")

# SparkSession with configuration
spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()
```

### Memory Management

```bash
# Spark Submit with memory settings
spark-submit \
    --driver-memory 2g \
    --executor-memory 4g \
    --executor-cores 2 \
    --num-executors 10 \
    --conf spark.sql.adaptive.enabled=true \
    my_app.py
```

### Common Performance Settings

```python
# Adaptive Query Execution
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# Shuffle optimization
spark.conf.set("spark.sql.shuffle.partitions", "200")  # Adjust based on data size
spark.conf.set("spark.sql.files.maxPartitionBytes", "134217728")  # 128MB

# Broadcast threshold
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "10485760")  # 10MB

# Dynamic allocation
spark.conf.set("spark.dynamicAllocation.enabled", "true")
spark.conf.set("spark.dynamicAllocation.minExecutors", "1")
spark.conf.set("spark.dynamicAllocation.maxExecutors", "20")
```

## Machine Learning with MLlib

### Basic ML Pipeline

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Prepare features
assembler = VectorAssembler(
    inputCols=["feature1", "feature2", "feature3"],
    outputCol="features"
)

# String indexer for categorical target
indexer = StringIndexer(inputCol="label", outputCol="indexed_label")

# Create model
lr = LogisticRegression(
    featuresCol="features",
    labelCol="indexed_label"
)

# Create pipeline
pipeline = Pipeline(stages=[assembler, indexer, lr])

# Split data
train_data, test_data = df.randomSplit([0.8, 0.2])

# Train model
model = pipeline.fit(train_data)

# Make predictions
predictions = model.transform(test_data)

# Evaluate
evaluator = BinaryClassificationEvaluator(
    labelCol="indexed_label",
    rawPredictionCol="rawPrediction"
)
auc = evaluator.evaluate(predictions)
```

## Best Practices

### Development Best Practices

1. **Use DataFrames over RDDs** for structured data
2. **Cache frequently accessed datasets** to avoid recomputation
3. **Use appropriate file formats** (Parquet for analytics, Delta for ACID transactions)
4. **Partition data** based on query patterns
5. **Avoid wide transformations** when possible
6. **Use broadcast joins** for small lookup tables

### Performance Best Practices

1. **Right-size your cluster** - balance cost and performance
2. **Monitor and tune garbage collection** settings
3. **Use columnar formats** (Parquet, ORC) for analytics
4. **Implement proper data skew handling**
5. **Use pushdown predicates** to filter early
6. **Optimize join strategies** based on data sizes

### Code Organization

```python
# Good: Modular and reusable
def clean_data(df):
    return df.filter(df.value.isNotNull()) \
            .withColumn("clean_value", trim(df.value))

def aggregate_data(df):
    return df.groupBy("category") \
            .agg(sum("amount").alias("total"))

# Usage
cleaned_df = clean_data(raw_df)
result_df = aggregate_data(cleaned_df)
```

### Error Handling

```python
try:
    df = spark.read.parquet("path/to/data")
    result = df.filter(df.amount > 0).collect()
except Exception as e:
    print(f"Error processing data: {e}")
    # Handle error appropriately
finally:
    spark.stop()
```

## Troubleshooting

### Common Issues

**Out of Memory Errors:**
- Increase executor memory
- Reduce data per partition
- Use more partitions
- Enable dynamic allocation

**Slow Performance:**
- Check for data skew
- Optimize join strategies
- Use appropriate caching
- Tune shuffle partitions

**Serialization Errors:**
- Use Kryo serializer
- Make UDFs serializable
- Avoid closures with non-serializable objects

### Monitoring and Debugging

```python
# Check execution plan
df.explain(True)

# Monitor job progress
spark.sparkContext.statusTracker()

# Access Spark UI
# http://driver-node:4040

# Enable event logging
spark.conf.set("spark.eventLog.enabled", "true")
spark.conf.set("spark.eventLog.dir", "hdfs://path/to/logs")
```

### Useful Spark Submit Options

```bash
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 2g \
    --executor-memory 4g \
    --executor-cores 2 \
    --num-executors 10 \
    --conf spark.sql.adaptive.enabled=true \
    --conf spark.sql.adaptive.coalescePartitions.enabled=true \
    --files config.properties \
    --py-files dependencies.zip \
    my_spark_app.py
```
