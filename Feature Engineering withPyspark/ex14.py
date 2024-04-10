# Get a count of the missing values in the column 'PDOM' using where(), isNull() and count().
# Calculate the mean value of 'PDOM' using the aggregate function mean().
# Use fillna() with the value set to the 'PDOM' mean value and only apply it to the column 'PDOM' using the subset parameter.

# Count missing rows
missing = df.where(df['PDOM'].isNull()).count()

# Calculate the mean value
col_mean = df.agg({'PDOM': 'mean'}).collect()[0][0]

# Replacing with the mean value for that column
df.fillna(col_mean, subset=['PDOM'])