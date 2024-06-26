# Create a function train_test_split_date() that takes in a dataframe, df, the date column to use for splitting split_col and the number of days to use for the test set, test_days and set it to have a default value of 45.
# Find the min and max dates for split_col using ,().
# Find the date to split the test and training sets using max_date and subtract test_days from it by using timedelta() which takes a days parameter, in this case, pass in `test_days,
# Using OFFMKTDATE as the split_col find split_date and use it to filter the dataframe into two new ones, train_df and test_df, Where test_df is only the last 45 days of the data. Additionally, ensure that the test_df only contains homes listed as of the split date by filtering df['LISTDATE'] less than or equal to the split_date.

def train_test_split_date(df, split_col, test_days=45):
  """Calculate the date to split test and training sets"""
  # Find how many days our data spans
  max_date = df.agg({split_col: 'max'}).collect()[0][0]
  min_date = df.agg({split_col: 'min'}).collect()[0][0]
  # Subtract an integer number of days from the last date in dataset
  split_date = max_date - timedelta(days=test_days)
  return split_date

# Find the date to use in spitting test and train
split_date = train_test_split_date(df, 'OFFMKTDATE')

# Create Sequential Test and Training Sets
train_df = df.where(df['OFFMKTDATE'] < split_date)
test_df = df.where(df['OFFMKTDATE'] >= split_date).where(df['LISTDATE'] <= split_date) 