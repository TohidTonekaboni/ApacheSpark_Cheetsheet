# Create a Python list named numb containing the numbers 1 to 100.
# Load the list into Spark using Spark Context's parallelize method and assign it to a variable spark_data.

# Create a Python list of numbers from 1 to 100 
numb = range(1, 100)

# Load the list into PySpark  
spark_data = sc.parallelize(numb)