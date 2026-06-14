# Automated Serverless Data Pipeline & Visual Analytics

## Overview
An end-to-end event-driven data pipeline built on AWS that automates raw data ingestion through schema transformation to live business intelligence dashboards. When a file is uploaded to S3, the pipeline automatically triggers, processes, and visualizes the data without any manual intervention.

## Architecture
![Architecture Diagram](architecture.jpg)
S3 Event Trigger → Lambda (Preprocessing) → AWS Glue ETL (Apache Spark) → Amazon QuickSight (SPICE Engine)

## AWS Services Used
- Amazon S3 — Raw data storage and event trigger source
- AWS Lambda (Python/Boto3) — Preprocessing and pipeline orchestration
- AWS Glue Visual ETL — Schema transformation using Apache Spark
- Amazon QuickSight — Live business intelligence dashboards via SPICE engine

## Key Skills Demonstrated
- Event-driven serverless architecture
- ETL pipeline design and implementation
- Apache Spark data transformation
- Cloud-native business intelligence and analytics
- Systematic debugging and root cause analysis

## Challenges & Solutions

### Challenge — Glue Bulk Output Formatting Failure
**The Problem:** AWS Glue exported compressed output files with non-standard filename hashes that lacked proper CSV signatures, causing downstream ingestion to fail silently.

**The Investigation:** Manually decoupled the compression streams to inspect raw output and validate schema mapping parity between source and target.

**The Solution:** Reprovisioned correct file extensions and output configurations to ensure clean downstream data ingestion into QuickSight.

## How to Deploy
1. Create an S3 bucket for raw data input
2. Deploy the Lambda preprocessing function
3. Configure AWS Glue Visual ETL job with Apache Spark
4. Connect QuickSight to the transformed data output via SPICE
5. Configure S3 event notifications to trigger the Lambda function on file upload
