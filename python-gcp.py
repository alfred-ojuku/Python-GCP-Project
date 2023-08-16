import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Roam\\data-warehouse-355508-4c99e2f51463.json"

def check_vin_exists(vin):
    try:
        # Initialize BigQuery client
        client = bigquery.Client()
        

        # Construct and execute the query
        query = f"SELECT serial_no FROM dbt_alfred.mrt_vin_table WHERE serial_no = '{vin}'"
        query_job = client.query(query)
        results = query_job.result()
    
        
        # Check if there's a matching VIN
        return any(row.serial_no == vin for row in results)

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    entered_vin = input("Enter the VIN to check: ")
    vin_exists = check_vin_exists(entered_vin)

    if vin_exists:
        print("VIN exists in the table.")
    else:
        print("VIN does not exist in the table.")
