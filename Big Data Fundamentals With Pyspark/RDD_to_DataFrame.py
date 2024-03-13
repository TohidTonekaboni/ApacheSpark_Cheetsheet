# Create an RDD from the sample_list.
# Create a PySpark DataFrame using the above RDD and schema.
# Confirm the output as PySpark DataFrame.

# Create an RDD from the list
rdd = sc.parallelize(sample_list)

# Create a PySpark DataFrame
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])

# Check the type of names_df
print("The type of names_df is", type(names_df))

