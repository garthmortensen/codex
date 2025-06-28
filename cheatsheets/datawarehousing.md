# datawarehousing.md

## About
**Name:** Data Warehousing (the term comes from the analogy of a warehouse—a place to store goods; here, it means a central place to store and organize data for analysis)

**Created:** The concept of data warehousing emerged in the late 1980s and early 1990s to address the need for organizations to consolidate data from multiple sources for business intelligence and analytics. Its purpose is to provide a central repository for historical and current data, enabling complex queries and reporting.

**Similar Technologies:** Data lakes, OLAP cubes, ETL tools, business intelligence platforms, cloud data warehouses (e.g., Snowflake, BigQuery, Redshift)

**Plain Language Definition:**
A data warehouse is a system that collects and stores data from different sources in one place, making it easy for organizations to analyze trends, generate reports, and make business decisions based on all their data.

---

## Overview

Data warehousing is a technology that aggregates structured data from one or more sources so that it can be compared and analyzed for greater business intelligence.

Key characteristics of a Data Warehouse Environment (DWE):
- **Subject-oriented**: Organized around business subjects (customers, products, sales)
- **Integrated**: Data from multiple sources combined consistently  
- **Non-volatile**: Data is stable, not updated in place
- **Time-variant**: Historical data preserved with time stamps

## Core Concepts

### OLTP vs OLAP

**OLTP (Online Transaction Processing)**
- Optimized for transaction processing
- Current, detailed data
- Normalized structures (3NF)
- High concurrency, fast response
- Used for day-to-day operations

**OLAP (Online Analytical Processing)**  
- Optimized for analysis and reporting
- Historical, summarized data
- Denormalized structures (star/snowflake schemas)
- Complex queries, batch processing
- Used for decision support

### Star Schema vs Snowflake Schema

**Star Schema**
- Central fact table surrounded by dimension tables
- Dimension tables are denormalized
- Simple structure, easier to understand
- Better query performance
- Preferred approach in most cases

**Snowflake Schema**
- Normalized dimension tables
- More complex structure with sub-dimensions
- Saves storage space
- Used in Inmon's approach for the "one true DW"

### Fact Tables and Dimension Tables

**Fact Tables**
- Contain numeric, measurable data (facts)
- Usually contain foreign keys to dimensions
- Examples: sales amounts, quantities, counts
- Types: additive, semi-additive, non-additive

**Dimension Tables**
- Contain descriptive attributes (dimensions)
- Provide context for facts
- Examples: customer info, product details, time periods
- Often contain hierarchies

## Modeling Techniques

### Multidimensional Model (MDM)

The foundation for organizing facts and dimensions:
- **Facts**: Numeric measures (sales, quantities)
- **Dimensions**: Descriptive attributes (customer, product, time)
- **Hierarchies**: Natural drill-down paths in dimensions

### Special Dimension Types

**Degenerate Dimensions**
- Dimension attributes stored in fact table
- No separate dimension table
- Examples: transaction numbers, invoice numbers

**Role-Playing Dimensions**
- Same dimension used multiple times in different contexts
- Example: Date dimension used as order_date, ship_date, due_date

**Junk Dimensions**
- Collection of miscellaneous flags and indicators
- Reduces proliferation of small dimension tables

**Slowly Changing Dimensions (SCDs)**
- **Type 1**: Overwrite old values (no history)
- **Type 2**: Create new record (preserve history) - most common
- **Type 3**: Add new column (limited history)

## Architectural Approaches

### Inmon's Approach (Top-Down)

**Philosophy**: Build enterprise data warehouse first, then data marts

**Architecture**:
1. **One True DW**: Enterprise-wide, 3NF normalized
2. **Data Marts**: Subject-specific, denormalized from DW
3. **Subject Area Models**: High-level enterprise view

**Process**:
1. Enterprise-wide analysis (first pass)
2. Detailed data mart design (second pass)
3. Prevents "stovepipes" through central control

**Advantages**:
- Consistent enterprise view
- Prevents data inconsistencies
- Single source of truth

**Disadvantages**:
- High upfront cost and complexity
- Longer time to deliver value
- Requires significant organizational commitment

### Kimball's Approach (Bottom-Up)

**Philosophy**: Build data marts first, integrate into enterprise view

**Architecture**:
1. **Data Marts**: Independent dimensional models
2. **Conformed Dimensions**: Shared dimensions across marts
3. **Data Warehouse Bus**: Logical integration layer

**Key Tool - The Matrix**:
- Maps which dimensions participate in which data marts
- Foundation of the "bus architecture"
- Guides integration across the enterprise

**Process**:
1. Identify all facts and dimensions (first pass)
2. Build individual data marts (second pass)
3. Use conformed dimensions for integration

**Advantages**:
- Faster time to value
- Lower initial investment
- Incremental approach

**Disadvantages**:
- Risk of inconsistencies
- Requires discipline with conformed dimensions

## ETL (Extract, Transform, Load)

### Overview
- Consumes 60-70% of DW project budget and effort
- Most risky and complex part of DW implementation
- Approximately 6 person-months per business process/data mart

### ETL Components

**Extraction**
- Pull data from source systems
- Handle different data formats and systems
- Manage timing and dependencies

**Transformation**
- Data type conversions
- Business rule applications
- Data integration and aggregation
- Cleansing and quality improvements

**Loading**
- Insert data into target systems
- Handle incremental vs. full loads
- Manage indexes and constraints

### Data Staging

**Kimball's Distributed Staging Area (DSA)**
- Back-room area for ETL processing
- No direct business user access
- Flexible architecture (multiple systems)
- Models transition from source-like to target-like

**Benefits**:
- Information hiding/encapsulation
- Development flexibility
- Platform independence

### ETL Design Decisions

**Tool Decisions: Build vs Buy**

*Build Advantages*:
- Lower initial licensing costs
- Exact fit to requirements
- Familiar technology stack
- Easy customization

*Build Disadvantages*:
- Development time and cost
- Limited features (threading, memory management)
- Ongoing maintenance burden

*Buy Advantages*:
- Rich feature sets
- Proven scalability
- Vendor support
- Advanced cleansing capabilities

*Buy Disadvantages*:
- High licensing costs
- Learning curve complexity
- Vendor dependency

**Cleansing Locations**

1. **Source Systems** (Best but often impractical)
   - Benefits entire downstream pipeline
   - Often blocked by production concerns

2. **ETL Process** (On-the-fly)
   - Good for simple transformations
   - No storage overhead
   - Performance impact for complex rules

3. **Staging Area** (Often most practical)
   - Balance of capability and safety
   - Can store intermediate results

4. **Data Marts** (Inefficient)
   - Must repeat for each mart
   - Late in the process

5. **Reports/Queries** (Worst option)
   - Must repeat for every report
   - Latest possible point

### Mapping Strategies

**Definitive Source Mapping**
- Single authoritative source per attribute
- Clear ownership and responsibility
- Simpler to implement and maintain

**Candidate Source Mapping**
- Ranked list of potential sources
- Fallback options for availability
- More complex but more resilient

### Data Quality Techniques

**Domain Studies**
```sql
-- Check distinct values and frequencies
SELECT column_name, COUNT(*) as frequency
FROM table_name
GROUP BY column_name
ORDER BY frequency DESC;

-- Check for nulls
SELECT SUM(CASE WHEN column_name IS NULL THEN 1 ELSE 0 END) as null_count
FROM table_name;
```

**Cross Footing**
- Compare record counts between source and destination
- Verify data integrity across transformations
- Understand differences (duplicates, filters, joins)

## Semantic Impedance

### Definition
Measure of opposition to exchanging data between systems due to:
- Different data modeling approaches
- Varying business definitions
- Technical platform differences
- Organizational silos

### Causes
- Different modeling technologies (relational, hierarchical, network)
- Different modeling levels (conceptual, logical, physical)
- Corporate mergers and acquisitions
- Legacy system migrations
- Multiple applications for same business area

### Mitigation Strategies
- Enterprise-wide data modeling standards
- Conformed dimensions (Kimball)
- Subject area models (Inmon)
- Comprehensive documentation
- Cross-functional teams

## Analysis and Design

### Enterprise Readiness Assessment

**Bad Signs** (Address before proceeding):
- **Lone Zealot**: Only one person driving initiative
- **Too Much Demand**: Conflicting requirements, unrealistic expectations
- **In Search of Demand**: Unclear business requirements

**Good Signs** (Green lights for success):
- **Strong Management Sponsorship** (Most important)
- **Compelling Business Motivations** (Clear ROI)
- **Good IT/Business Cooperation**
- **Current Analytic Culture**
- **General Feasibility**

### Project Planning

**Kimball Lifecycle Approach**:
1. Project planning and management
2. Business requirements definition
3. Dimensional modeling
4. Physical design
5. ETL design and development
6. Application specification and development
7. Testing and deployment
8. Maintenance and growth

## Implementation Best Practices

### Development Guidelines
- Be thorough, skeptical, and systematic
- Use domain studies and cross footing
- Document everything for future maintainers
- Create translations and cookbooks
- Implement version control
- Establish review processes
- Use metadata-driven approaches

### SQL Server Tools (for implementation)

**SQL Server Integration Services (SSIS)**
- ETL tool for extraction, transformation, loading
- Visual development environment
- Extensive connectivity options

**SQL Server Analysis Services (SSAS)**
- OLAP cube processing engine
- MDX query language support
- Integration with Excel and other tools

**SQL Server Reporting Services (SSRS)**
- Report development and deployment
- Web-based report server
- Integration with data sources

## Key Performance Considerations

### Data Latency
- Time between source system update and DW availability
- Critical for operational vs. strategic decisions
- Balance between freshness and processing time

### Query Performance
- Proper indexing strategies
- Appropriate aggregation levels
- Partitioning for large datasets

### Scalability
- Plan for data volume growth
- Consider parallel processing capabilities
- Design for incremental loads

## Common Challenges

### Technical Challenges
- Data quality issues
- Performance optimization
- Integration complexity
- Platform migrations

### Organizational Challenges
- User adoption
- Change management
- Resource allocation
- Ongoing maintenance

### Business Challenges
- Changing requirements
- ROI measurement
- Cross-departmental coordination
- Executive sponsorship

## Success Factors

1. **Executive Sponsorship**: Strong business leadership support
2. **Clear Requirements**: Well-defined business objectives
3. **Realistic Scope**: Incremental, manageable implementations
4. **Quality Focus**: Emphasis on data quality and governance
5. **User Involvement**: Business users engaged throughout process
6. **Technical Excellence**: Proper architecture and design practices
7. **Change Management**: Support for organizational adaptation

## Conclusion

Data warehousing success requires careful attention to:
- Architectural decisions (Inmon vs. Kimball)
- Data modeling best practices
- ETL design and implementation
- Data quality and governance
- Organizational readiness and support

The choice between approaches should be based on organizational culture, resources, timeline, and specific business needs. Both Inmon and Kimball approaches can be successful when properly implemented with appropriate organizational support.