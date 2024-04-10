# Read the list of column descriptions above and explore their top 30 values with show(), the dataframe is already filtered to the listed columns as df
# Create a list of two columns to drop based on their lack of relevance to predicting house prices called cols_to_drop. Recall that computers only interpret numbers explicitly and don't understand context.
# Use the drop() function to remove the columns in the list cols_to_drop from the dataframe df

# Show top 30 records
df.show(30)

# List of columns to remove from dataset
cols_to_drop = ['STREETNUMBERNUMERIC', 'LOTSIZEDIMENSIONS']

# Drop columns in list
df = df.drop(*cols_to_drop)