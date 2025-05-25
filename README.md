# Yelp Business Reviews Analysis

## Description
This project analyzes Yelp reviews and business data using **sentiment analysis** and **SQL-based data processing**. The dataset consists of millions of Yelp reviews and related business information, stored in **Amazon S3** and processed in **Snowflake**.

## Workflow Overview
1. **Data Sources**
   - Yelp Reviews (5GB, ~7 million records)
   - Yelp Businesses (100MB)
2. **Data Processing Pipeline**
   - Extract JSON data using a Python program.
   - Store processed data in Amazon S3.
   - Load data into **Snowflake** for transformation.
3. **Transformations**
   - Flatten JSON structures in Snowflake.
   - Store cleaned data in **structured tables**.
4. **Analysis & Insights**
   - Apply **UDF-based sentiment analysis** on reviews.
   - Perform SQL-based data analysis.
   - Generate reports on customer feedback trends.

## Technologies Used
- **Python** (Data extraction & processing)
- **Amazon S3** (Data storage)
- **Snowflake** (Database management & transformations)
- **SQL** (Data querying & analysis)
- **User-Defined Functions (UDFs)** (Sentiment analysis)

## Project Architecture
![Project Architecture](https://github.com/user-attachments/assets/ce2eb537-2606-4e23-8cd9-ce67f892d004)



