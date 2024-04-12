# Import the SparkSession class from pyspark.sql.
# Create a SparkSession object connected to a local cluster. Use all available cores. Name the application 'test'.
# Use the version attribute on the SparkSession object to retrieve the version of Spark running on the cluster. Note: The version might be different to the one that's used in the presentation (it gets updated from time to time).
# Shut down the cluster.

# Import the SparkSession class
from pyspark.sql import SparkSession

# Create SparkSession object
spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()

# What version of Spark?
print(spark.version)

# Terminate the cluster
spark.stop()