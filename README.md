# Stock-data-project ETL

## Overview
For my third ETL project I wanted to create something that has a bit more utility and would be able to be automated outside of my personal computer. 
This script extracts data from the free Alphavantage api every week. It transforms the data into a consistent format and loads it into a new or existing database
located in the file tree. 

The execution and scheduling is automated with Apache Airflow and containerized with Docker. See attached pictures below for the process in Airflow and Docker.
### Airflow DAG
<img width="1463" height="703" alt="image" src="https://github.com/user-attachments/assets/7894d277-ce78-4d51-867b-65bae7babc11" />

### Docker Environment
<img width="1497" height="535" alt="image" src="https://github.com/user-attachments/assets/9f66691b-20e4-45f7-b606-87e03540c63c" />

## Key Stages
- Extraction: Stock data from the following tickers is requested from Alphavantage: IBM, AMZN, GOOG, MCSFT
- Transformation: Records are pulled and standardized
- Load: Processed data is stored in a database for analysis
- Automation: The pipeline is automated and scheduled using Apache Airflow, containerized with Docker

  
