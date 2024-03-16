# Import * from the pyspark.sql.types library.
# Define a new schema using the StructType method.
# Define a StructField for name, age, 
# and city. Each field should correspond to the correct datatype and not be nullable.


# Import the pyspark.sql.types library
from pyspark.sql.types import *

# Define a new schema using the StructType method
people_schema = StructType([
  # Define a StructField for each field
  StructField('name', StringType(), False),
  StructField('age', IntegerType(), False),
  StructField('city', StringType(), False)
])