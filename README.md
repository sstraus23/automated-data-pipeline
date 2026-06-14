# Automated Serverless Data Pipeline & Visual Analytics

## Overview
An end-to-end event-driven data pipeline built on AWS that automates raw data ingestion through schema transformation to live business intelligence dashboards. When a file is uploaded to S3, the pipeline automatically triggers, processes, and visualizes the data without any manual intervention.

## Architecture
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

Paste that into the README, commit it, then add the description and tags. Let me know when you're done and we'll move to the next one.You said: this is the page im staring at now whatthis is the page im staring at now what11:01 AMClaude responded: Perfect — your repo was created successfully.Perfect — your repo was created successfully. It's empty right now which is why you're seeing that setup screen. Here's exactly what to do:
Click "creating a new file" — that blue link in the middle of the page that says "Get started by creating a new file or uploading an existing file."
That will open a file editor. Name the file README.md at the top, then paste the README content I gave you into the body, scroll down and click "Commit new file."
That's your first step — do that and send me a screenshot of what you see next.You said: now whatnow what11:02 AMClaude responded: Perfect — you're in the right place.Perfect — you're in the right place. The file is already named README.md which is correct.
Now:

Click anywhere in the big black empty area where it says "Enter file contents here"
Select all that text and delete it
Paste the README content I gave you earlier

Then once it's pasted in, click the "Preview" tab to make sure it looks good, then hit the green "Commit changes" button in the top right.
Go ahead and paste it in and let me know what you see!Claude Fable 5 is currently unavailable.Learn more(opens in new tab)
Sonnet 4.6 Low
