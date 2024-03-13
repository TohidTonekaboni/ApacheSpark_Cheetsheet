# Create a PySpark DataFrame from file_path (which is the path to the Fifa2018_dataset.csv file).
# Print the schema of the DataFrame.
# Print the first 10 observations.
# How many rows are in there in the DataFrame?


# Load the Dataframe
fifa_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Check the schema of columns
fifa_df.printSchema()

# Show the first 10 observations
fifa_df.show(10)

# Print the total number of rows
print("There are {} rows in the fifa_df DataFrame".format(fifa_df.count()))