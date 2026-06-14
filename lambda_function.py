import json
import boto3
import csv
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get the bucket name and file key from the S3 event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        # Fetch the uploaded CSV file from the raw data bucket
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        lines = response['Body'].read().decode('utf-8').splitlines()
        
        # Read the CSV data
        reader = csv.reader(lines)
        header = next(reader)  # Extract the header row
        
        processed_rows = []
        
        # Filter out rows with missing values
        for row in reader:
            if all(row):
                processed_rows.append(row)
                
        # Write processed data back to a new CSV in memory
        output_csv = io.StringIO()
        writer = csv.writer(output_csv)
        writer.writerow(header)
        writer.writerows(processed_rows)
        
        # Upload the processed file to the processed data bucket
        processed_file_key = file_key.replace('raw/', 'processed/')
        s3.put_object(
            Bucket='csv-processed-data20',
            Key=processed_file_key,
            Body=output_csv.getvalue()
        )
        print(f"Processed file uploaded to: {processed_file_key}")
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        raise
