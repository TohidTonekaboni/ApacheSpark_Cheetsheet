# Use a for loop iterate through the columns.
# In each loop cycle, compute the correlation between the current column and 'SALESCLOSEPRICE' using the corr() method.
# Create logic to update the maximum observed correlation and with which column.
# Print out the name of the column that has the maximum correlation with 'SALESCLOSEPRICE'.


# Name and value of col with max corr
corr_max = 0
corr_max_col = columns[0]

# Loop to check all columns contained in list
for col in columns:
    # Check the correlation of a pair of columns
    corr_val = df.corr('SALESCLOSEPRICE', col)
    # Logic to compare corr_max with current corr_val
    if corr_val > corr_max:
        # Update the column name and corr value
        corr_max = corr_val
        corr_max_col = col

print(corr_max_col)
