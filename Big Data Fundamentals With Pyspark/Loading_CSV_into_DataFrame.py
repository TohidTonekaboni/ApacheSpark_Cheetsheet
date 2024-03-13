# Create a DataFrame from file_path variable which is the path to the people.csv file.
# Confirm the output as PySpark DataFrame.


# Create an DataFrame from file_path
people_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Check the type of people_df
print("The type of people_df is", type(people_df))