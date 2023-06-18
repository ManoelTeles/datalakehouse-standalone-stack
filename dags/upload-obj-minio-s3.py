from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.S3_hook import S3Hook
import requests
import pandas as pd

def api_call(**kwargs):
    ti = kwargs['ti']
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url).json()
    df = pd.DataFrame(response['entries'])
    ti.xcom_push(key = 'final_data' , value = df.to_csv(index=False))

def upload_to_s3(string_data: str, key: str, bucket_name: str) -> None:
    hook = S3Hook('s3_conn')
    hook.load_string(string_data=string_data, key=key, bucket_name=bucket_name)

with DAG(
    dag_id='s3_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 6, 16),
    catchup=False
) as dag:

    api_hit_task = PythonOperator(
        task_id = 'API-Call',
        python_callable = api_call,
        provide_context = True,
        
    )

    task_upload_to_s3 = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={
            'string_data': "{{ ti.xcom_pull(key='final_data') }}",
            'key': "publicapis/entries/final_data.csv",
            'bucket_name': "datalakehouse-raw"
            
        }
    )

    api_hit_task >> task_upload_to_s3