# Replace the values in WALKSCORE and BIKESCORE with -1 using fillna() and the subset parameter.
# Create a list of StringIndexers by using list comprehension to iterate over each column in categorical_cols.
# Apply fit() and transform() to the pipeline indexer_pipeline.
# Drop the categorical_cols using drop() since they are no longer needed. Inspect the result data types using dtypes.


# Replace missing values
df = df.fillna(-1, subset=['WALKSCORE', 'BIKESCORE'])

# Create list of StringIndexers using list comprehension
indexers = [StringIndexer(inputCol=col, outputCol=col+"_IDX")\
            .setHandleInvalid("keep") for col in categorical_cols]
# Create pipeline of indexers
indexer_pipeline = Pipeline(stages=indexers)
# Fit and Transform the pipeline to the original data
df_indexed = indexer_pipeline.fit(df).transform(df)

# Clean up redundant columns
df_indexed = df_indexed.drop(*categorical_cols)
# Inspect data transformations
print(df_indexed.dtypes)