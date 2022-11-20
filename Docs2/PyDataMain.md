# Data & Python Docs

## General Skill Objectives

1. SETTING UP A PYTHON DATA SCIENCE ENVIRONMENT
   1. Select Python Data Science Tools
   2. Set Up an Environment Using Jupyter Notebook
2. MANAGING AND ANALYZING DATA WITH NUMPY
   1. Create NumPy Arrays
   2. Load and Save NumPy Data
   3. Analyze Data in NumPy Arrays
3. TRANSFORMING DATA WITH NUMPY
   1. Manipulate Data in NumPy Arrays
   2. Modify Data in NumPy Arrays
4. MANAGING AND ANALYZING DATA WITH PANDAS
   1. Create Series and DataFrames
   2. Load and Save pandas Data
   3. Analyze Data in DataFrames
   4. Slice and Filter Data in DataFrames
5. TRANSFORMING AND VISUALIZING DATA WITH PANDAS
   1. Manipulate Data in DataFrames
   2. Modify Data in DataFrames
   3. Plot DataFrame Data
6. VISUALIZING DATA WITH MATPLOTLIB AND SEABORN
   1. Create and Save Simple Line Plots
   2. Create Subplots
   3. Create Common Types of Plots
   4. Format Plots
   5. Streamline Plotting with Seaborn

### Core Modules

- data engineering
- data analysis
- data storage
- data visualization
- statistics

### General Python Skill Objectives

Declare and perform operations on simple data types, including strings, numbers, and dates.
Declare and perform operations on data structures, including lists, ranges, tuples, dictionaries, and sets.
Write conditional statements and loops.
Define and use functions, classes, and modules.
Manage files and directories through code.
Deal with exceptions.

1 - SETTING UP PYTHON AND DEVELOPING A SIMPLE APPLICATION
Set Up the Development Environment
Write Python StatementsCreate a Python Application
Prevent Errors
2 - PROCESSING SIMPLE DATA TYPES
Process Strings and Integers
Process Decimals, Floats, and Mixed Number Types
3 - PROCESSING DATA STRUCTURES
Process Ordered Data Structures
Process Unordered Data Structures
4 - WRITING CONDITIONAL STATEMENTS AND LOOPS IN PYTHON
Write a Conditional Statement
Write a Loop
5 - STRUCTURING CODE FOR REUSE
Define and Call a Function
Define and Instantiate a Class
Import and Use a Module
6 - WRITING CODE TO PROCESS FILES AND DIRECTORIES
Write to a Text File
Read from a Text File
Get the Contents of a Directory
Manage Files and Directories
7 - DEALING WITH EXCEPTIONS
Handle Exceptions
Raise Exceptions

### Advanced Programming Techniques with Python (v1.1)

Learning Objectives
In this course, you will expand your Python proficiencies. You will:

Select an object-oriented programming approach for Python applications.

Create object-oriented Python applications.

Create a desktop application.

Create a data-driven application.

Create and secure web service-connected applications.

Program Python for data science.

Implement unit testing and exception handling.

Package an application for distribution.

1 - SELECTING AN OBJECT-ORIENTED PROGRAMMING APPROACH FOR PYTHON APPLICATIONS
Topic A: Implement Object-Oriented Design
Topic B: Leverage the Benefits of Object-Oriented Programming
2 - CREATING OBJECT-ORIENTED PYTHON APPLICATIONS
Topic A: Create a Class
Topic B: Use Built-in Methods
Topic C: Implement the Factory Design Pattern
3 - CREATING A DESKTOP APPLICATION
Topic A: Design a Graphical User Interface (GUI)
Topic B: Create Interactive Applications
4 - CREATING DATA-DRIVEN APPLICATIONS
Topic A: Connect to Data
Topic B: Store, Update, and Delete Data in a Database
5 - CREATING AND SECURING A WEB SERVICE-CONNECTED APP
Topic A: Select a Network Application Protocol
Topic B: Create a RESTful Web Service
Topic C: Create a Web Service Client
Topic D: Secure Connected Applications
6 - PROGRAMMING PYTHON FOR DATA SCIENCE
Topic A: Clean Data with Python
Topic B: Visualize Data with Python
Topic C: Perform Linear Regression with Machine Learning
7 - IMPLEMENTING UNIT TESTING AND EXCEPTION HANDLING
Topic A: Handle Exceptions
Topic B: Write a Unit Test
Topic C: Execute a Unit Test
8 - PACKAGING AN APPLICATION FOR DISTRIBUTION
Topic A: Create and Install a Package
Topic B: Generate Alternative Distribution Files

___

## Pandas:  open source data analysis/manipulation

1. Tabular data w/ heterogeneously-typed columns
2. ordered/unordered time series data
3. matrix data w/ row/column labels
4. observational/stat data sets

- Primary data structures:

1. `Series` for 1-D labeled homogeneously-typed array
   1. container for scalars
2. `DataFrame` for 2-D labeled, size-mutable tabular structures with potentially heterog.-typed column
   1. container for Series

- Stages of working with data
  - munging & cleaning data
  - analyzing/modeling
  - organizing analytical results
    - To be plotted or used in tabular displays

- Data info
- index (rows, axis 0)
- columns (axis 1)

### Dependencies

- `Main`
  - _NumPy_:
  - _pytz_: accurate and cross platform timezone calculations
  - _python-dateutil_:  provides powerful extensions to the standard datetime module
    - computing of relative deltas and parsing of dates in string format

- `Testing`
  - _pytest_
  - _Hypothesis_

```py
import pytest
pd.test()
```

- `Computation`
  - _SciPy_:
  - _numba_
  - _xarray_
- `Optimization`
- _numexpr_: accelerates numerical ops by using multiple cores, smart chunking & caching
- _bottleneck_: accelerates nan evals by using specialized cython routines
- _zlib_, _brotli_: compression
- `HTML`, `Excel`
  - _BeautifulSoup4_ (BS4), _html5lib_, _lxml_ => HTML parsers for read_html
    - read_html(), read_xml
  - _openpyzl_: Reading / writing for xlsx files

```py
>>> pd.read_excel('tmp.xlsx', index_col=0)  # doctest: +SKIP
       Name  Value
0   string1      1
1   string2      2
2  #Comment      3
>>> pd.read_excel(open('tmp.xlsx', 'rb'),
...               sheet_name='Sheet3')  # doctest: +SKIP
   Unnamed: 0      Name  Value
0           0   string1      1
1           1   string2      2
2           2  #Comment      3
Index and header can be specified via the index_col and header arguments

>>> pd.read_excel('tmp.xlsx', index_col=None, header=None)  # doctest: +SKIP
     0         1      2
0  NaN      Name  Value
1  0.0   string1      1
2  1.0   string2      2
3  2.0  #Comment      3
Column types are inferred but can be explicitly specified

>>> pd.read_excel('tmp.xlsx', index_col=0,
...               dtype={'Name': str, 'Value': float})  # doctest: +SKIP
       Name  Value
0   string1    1.0
1   string2    2.0
2  #Comment    3.0
True, False, and NA values, and thousands separators have defaults, but can be explicitly specified, too. Supply the values you would like as strings or lists of strings!

>>> pd.read_excel('tmp.xlsx', index_col=0,
...               na_values=['string1', 'string2'])  # doctest: +SKIP
       Name  Value
0       NaN      1
1       NaN      2
2  #Comment      3

```

- `SQL DB`
  - _SQLAlchemy_: SQL support for db other than sqlite
    - SQLAlchemy: _ORM_ for RDB that workss with SQLite, MySQL, Postgres
      - SQLAlch Core: schema centric SQLA ORM: object centric
      - schema/types, eSQL Expression lang., engine, connection pooling, dialect, DBAPI
    - psycopg2, pymysql
    - PostgreSQL and MySQL engines

- `Visualization`
  - _Matplotlib_: plotting lib
  - _jinja2_: Conditional formatting with DataFrame.style
  - _tabulate_: printing in MD format

## Matplotlib

## SciPy

## NumPy

## Azure Data SaaS & General Steps

1. Ingest and transform data
a. Misusing values, scaling data so it’s same metrics w/ Jupiter notebooks, ipynb, batch processing
b. Initial step in data engineering pipelines
c. Using Apache spark, data factory, data bricks, az ml studio
d. Can use open data sets for practice then convert it to a data frame and manipulate the data
2. Design and develop batch processing solution
a. Schedule jobs that scale up and respond to job, batch are finite and differ from streaming processing
b. Have a data source like blob storage or sql as data storage
c. Move data into batch processing system like hive or spark that can process both compute and storage in parallel to dist load to diff nodes
d. Endpoint would be analytical data store like a Cosmos or Spark based data warehouse solution. Allows you to query data and send BI reports
e. E.G. logs from web server copied to folder and processed to create reports on activity
f. Data workflow initiated via jobs that orchestrate data pipelines

3. Stream processing solution
a. Highly available distributed solution
b. Data is constantly streamed from data source like Jaya warehousing system into stream processing app that filters, cleans, integrates the data.
c. You query the data and analyze it (time series predictive models) and interpret the info to then make BI  actions on it and send to targets or store the filtered data
d. Microsoft’s 8 rules of streaming

4. Manage batches and pipelines
a. ETL pipeline
b. Highly aware of monitoring to distribute systems
c. Dashboard, monitoring alerting via feedback system

## Azure Cert Info

 • Functional groups
  ○ Describe core data concepts (25—30%)
   § Describe ways to represent data
   § Describe features of structured data
   § Describe features of semi-structured
   § Describe features of unstructured data
  ○ Identify options for data storage •
   § Describe common formats for data files •
   § Describe types of databases
  ○ Describe common data workloads
   § Describe features of transactional workloads
   § Describe features of analytical workloads
  ○ Identify roles and responsibilities for data workloads
   § Describe responsibilities for database administrators
   § Describe responsibilities for data engineer
   § Describe responsibilities for data analysts

- Identify considerations for relational data on Azure (20—25%)
- Describe relational concepts
- Identify features of relational data
- Describe normalization and why it is used
- Identify common structured query language (SQL) statements
- Identify common database objects Describe relational Azure data services
- Describe the Azure SQL family of products including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines
- Identify Azure database services for open-source database systems
- Describe considerations for working with non-relational data on Azure (15—20%)
- Describe capabilities of Azure storage
- Describe Azure Blob storage
- Describe Azure File storage
- Describe Azure Table storage

- Exam DP-900: Microsoft Azure Data Fundamentals 9
  - Describe capabilities and features of Azure Cosmos DB
  - Identify use cases for Azure Cosmos DB
  - Describe Azure Cosmos DB APIs Describe an analytics workload on Azure (25—30%) Describe common elements of large-scale analytics • Describe considerations for data ingestion and processing • Describe options for analytical data stores • Describe Azure services for data warehousing, including Azure Synapse Analytics, Azure Databricks, Azure HDInsight, and Azure Data Factory Describe consideration for real-time data analytics • Describe the difference between batch and streaming data  • Describe technologies for real-time analytics including Azure Stream Analytics, Azure Synapse Data Explorer, and Spark structured streaming Describe data visualization in Microsoft Power BI • Identify capabilities of Power BI • Describe features of data models in Power BI • Identify appropriate visualizations for data
