# Instantiate a StringIndexer transformer called string_indexer with SCHOOLDISTRICTNUMBER as the input and School_Index as the output.
# Apply the transformer string_indexer to df with fit() and transform(). Store the transformed dataframe in indexed_df.
# Create a OneHotEncoder transformer called encoder using School_Index as the input and School_Vec as the output.
# Apply the transformation to indexed_df using transform(). Inspect the iterative steps of the transformation with the supplied code.


from pyspark.ml.feature import OneHotEncoder, StringIndexer

# Map strings to numbers with string indexer
string_indexer = StringIndexer(inputCol='SCHOOLDISTRICTNUMBER', outputCol='School_Index')
indexed_df = string_indexer.fit(df).transform(df)

# Onehot encode indexed values
encoder = OneHotEncoder(inputCol='School_Index', outputCol='School_Vec')
encoded_df = encoder.transform(indexed_df)

# Inspect the transformation steps
encoded_df[['SCHOOLDISTRICTNUMBER', 'School_Index', 'School_Vec']].show(truncate=100)