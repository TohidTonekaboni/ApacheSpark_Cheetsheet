# Import mean() and stddev() from pyspark.sql.functions.
# Use agg() to calculate the mean and standard deviation for 'log_SalesClosePrice' with the imported functions.
# Create the upper and lower bounds by taking mean_val +/- 3 times stddev_val.
# Create a where() filter for 'log_SalesClosePrice' using both low_bound and hi_bound.

from pyspark.sql.functions import mean, stddev

# Calculate values used for outlier filtering
mean_val = df.agg({'log_SalesClosePrice': 'mean'}).collect()[0][0]
stddev_val = df.agg({'log_SalesClosePrice': 'stddev'}).collect()[0][0]

# Create three standard deviation (μ ± 3σ) lower and upper bounds for data
low_bound = mean_val - (3 * stddev_val)
hi_bound = mean_val + (3 * stddev_val)

# Filter the data to fit between the lower and upper bounds
df = df.where((df['log_SalesClosePrice'] < hi_bound) & (df['log_SalesClosePrice'] > low_bound))