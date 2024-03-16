# Edit the getFirstAndMiddle() function to return a space separated string of names, except the last entry in the names list.
# Define the function as a user-defined function. It should return a string type.
# Create a new column on voter_df called first_and_middle_name using your UDF.
# Show the Data Frame.

def getFirstAndMiddle(names):
  # Return a space separated string of names
  return ' '.join(names[:-1])

# Define the method as a UDF
udfFirstAndMiddle = F.udf(getFirstAndMiddle, StringType())

# Create a new column using your UDF
voter_df = voter_df.withColumn('first_and_middle_name', udfFirstAndMiddle(voter_df.splits))

# Show the DataFrame
voter_df.show()