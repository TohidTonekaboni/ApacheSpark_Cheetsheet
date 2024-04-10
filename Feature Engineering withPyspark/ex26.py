# Import the needed functions split() and explode() from pyspark.sql.functions
# Use split() to create a new column garage_list by splitting df['GARAGEDESCRIPTION'] on ', ' which is both a comma and a space.
# Create a new record for each value in the df['garage_list'] using explode() and assign it a new column ex_garage_list
# Use distinct() to get unique values of ex_garage_list and show the 100 first rows, truncating them at 50 characters to display the values.




# Import needed functions
from pyspark.sql.functions import split, explode

# Convert string to list-like array
df = df.withColumn('garage_list', split(df['GARAGEDESCRIPTION'], ', '))

# Explode the values into new records
ex_df = df.withColumn('ex_garage_list', explode(df['garage_list']))

# Inspect the values
ex_df[['ex_garage_list']].distinct().show(100, truncate=50)