# Use the aggregate function skewness() to verify that 'YEARBUILT' has negative skew.
# Use the withColumn() to create a new column 'Reflect_YearBuilt' and reflect the values of 'YEARBUILT'.
# Using 'Reflect_YearBuilt' column, create another column 'adj_yearbuilt' by taking 1/log() of the values.


from pyspark.sql.functions import log

# Compute the skewness
print(df.agg({'YEARBUILT': 'skewness'}).collect())

# Calculate the max year
max_year = df.agg({'YEARBUILT': 'max'}).collect()[0][0]

# Create a new column of reflected data
df = df.withColumn('Reflect_YearBuilt', (max_year + 1) - df['YEARBUILT'])

# Create a new column based reflected data
df = df.withColumn('adj_yearbuilt', 1 / log(df['Reflect_YearBuilt']))