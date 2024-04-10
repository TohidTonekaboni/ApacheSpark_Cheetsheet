# Using the loaded data set df filter it down to the columns 'SALESCLOSEPRICE' and 'LIVINGAREA' with select().
# Sample 50% of the dataframe with sample() making sure to not use replacement and setting the random seed to 42.
# Convert the Spark DataFrame to a pandas.DataFrame() with toPandas().
# Using 'SALESCLOSEPRICE' as your dependent variable and 'LIVINGAREA' as your independent, plot a linear model plot using seaborn lmplot().

# Select a the relevant columns and sample
sample_df = df.select(['SALESCLOSEPRICE', 'LIVINGAREA']).sample(False, 0.5, 42)

# Convert to pandas dataframe
pandas_df = sample_df.toPandas()

# Linear model plot of pandas_df
sns.lmplot(x= 'LIVINGAREA', y='SALESCLOSEPRICE', data=pandas_df)
plt.show()