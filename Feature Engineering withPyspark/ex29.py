# Plot a distribution plot of the pandas dataframe sample_df using Seaborn distplot().
# Given it looks like there is a long tail of infrequent values after 5, create the bucket splits of 1, 2, 3, 4, 5+
# Create the transformer buck by instantiating Bucketizer() with the splits for setting the buckets, then set the input column as BEDROOMS and output column as bedrooms.
# Apply the Bucketizer transformation on df using transform() and assign the result to df_bucket. Then verify the results with show()


from pyspark.ml.feature import Bucketizer

# Plot distribution of sample_df
sns.distplot(sample_df, axlabel='BEDROOMS')
plt.show()

# Create the bucket splits and bucketizer
splits = [0, 1, 2, 3, 4, 5, float('Inf')]
buck = Bucketizer(splits=splits, inputCol='BEDROOMS', outputCol='bedrooms')

# Apply the transformation to df: df_bucket
df_bucket = buck.transform(df)

# Display results
df_bucket[['BEDROOMS', 'bedrooms']].show()