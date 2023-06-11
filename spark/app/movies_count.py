import sys
from pyspark.sql import SparkSession, functions
from pyspark.sql.types import StringType
from modules import moduleExample

# Create spark session
spark = (SparkSession
    .builder
    .getOrCreate()
)
sc = spark.sparkContext
sc.setLogLevel("WARN")

####################################
# Parameters
####################################
csv_file = sys.argv[1]

####################################
# Read CSV Data
####################################
print("######################################")
print("READING CSV FILE")
print("######################################")

df_csv = (
    spark.read
    .format("csv")
    .option("header", True)
    .load(csv_file)
)

df_csv.show(5)