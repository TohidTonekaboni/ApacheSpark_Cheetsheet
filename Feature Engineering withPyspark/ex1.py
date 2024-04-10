# From the listed columns above, identify which one we will use as our dependent variable $Y$.
# Using the loaded data set df, filter it down to our dependent variable with select(). Store this dataframe in the variable Y_df.
# Display summary statistics for the dependent variable using describe() on Y_df and calling show() to display it.


# Select our dependent variable
Y_df = df.select(['SALESCLOSEPRICE'])

# Display summary statistics
Y_df.describe().show()