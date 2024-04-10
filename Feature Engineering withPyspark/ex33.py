# Using the provided for loop that iterates through the list of binary columns, calculate the sum of the values in the column using the agg function. Use collect() to run the calculation immediately and save the results to obs_count.
# Compare obs_count to obs_threshold, the if statement should be true if obs_count is less than or equal to obs_threshold.
# Remove columns that have been appended to cols_to_remove list by using drop(). Recall that the * allows the list to be unpacked.
# Print the starting and ending shape of the PySpark dataframes by using count() for number of records and len() on df.columns or new_df.columns to find the number of columns.


obs_threshold = 30
cols_to_remove = list()
# Inspect first 10 binary columns in list
for col in binary_cols[0:10]:
  # Count the number of 1 values in the binary column
  obs_count = df.agg({col:'sum'}).collect()[0][0]
  # If less than our observation threshold, remove
  if obs_count <= obs_threshold:
    cols_to_remove.append(col)
    
# Drop columns and print starting and ending dataframe shapes
new_df = df.drop(*cols_to_remove)

print('Rows: ' + str(df.count()) + ' Columns: ' + str(len(df.columns)))
print('Rows: ' + str(new_df.count()) + ' Columns: ' + str(len(new_df.columns)))