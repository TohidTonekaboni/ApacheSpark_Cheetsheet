# Sample 50% of the dataframe df with sample() making sure to not use replacement and setting the random seed to 42.
# Convert the Spark DataFrame to a pandas.DataFrame() with toPandas().
# Plot a distribution plot using seaborn's distplot() method.
# Import the skewness() function from pyspark.sql.functions and compute it on the aggregate of the 'LISTPRICE' column with the agg() method. Remember to collect() your result to evaluate the computation.

# Select a single column and sample and convert to pandas
sample_df = df.select(['LISTPRICE']).sample(False, 0.5, 42)
pandas_df = sample_df.toPandas()

# Plot distribution of pandas_df and display plot
sns.distplot(pandas_df)
plt.show()

# Import skewness function
from pyspark.sql.functions import skewness

# Compute and print skewness of LISTPRICE
print(df.agg({'LISTPRICE': 'skewness'}).collect())