from minio import Minio
from dotenv import load_dotenv
import os

load_dotenv()

LOCAL_FILE_PATH = os.environ.get('LOCAL_FILE_PATH')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
MINIO_API_HOST = "http://localhost:9000"
MINIO_CLIENT = Minio("localhost:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)


print('executando ')
MINIO_CLIENT.fput_object("datalakehouse-raw", "bike-data/201508_station_data.csv", LOCAL_FILE_PATH,)
print("It is successfully uploaded to bucket")
