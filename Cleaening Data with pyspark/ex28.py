# Select the column representing the dog details from the DataFrame and show the first 10 un-truncated rows.
# Create a new schema as you've done before, using breed, start_x, start_y, end_x, and end_y as the names. Make sure to 
# specify the proper data types for each field in the schema (any number value is an integer).


# Select the dog details and show 10 untruncated rows
print(joined_df.select('dog_list').show(10, truncate=False))

# Define a schema type for the details in the dog list
DogType = StructType([
	StructField("breed", StringType(), False),
    StructField("start_x", IntegerType(), False),
    StructField("start_y", IntegerType(), False),
    StructField("end_x", IntegerType(), False),
    StructField("end_y", IntegerType(), False)
])