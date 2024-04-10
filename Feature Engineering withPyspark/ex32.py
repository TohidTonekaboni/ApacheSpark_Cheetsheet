# Import the following functions from pyspark.sql.functions to use later on: datediff(), to_date(), lit().
# Convert the date string '2017-12-10' to a pyspark date by first calling the literal function, lit() on it and then to_date()
# Create test_df by filtering OFFMKTDATE greater than or equal to the split_date and LISTDATE less than or equal to the split_date using where().
# Replace DAYSONMARKET by calculating a new column called DAYSONMARKET, the new column should be the difference between split_date and LISTDATE use datediff() to perform the date calculation. Inspect the new column and the original using the code provided.

from pyspark.sql.functions import datediff, to_date, lit

split_date = to_date(lit('2017-12-10'))
# Create Sequential Test set
test_df = df.where(df['OFFMKTDATE'] >= split_date).where(df['LISTDATE'] <= split_date)

# Create a copy of DAYSONMARKET to review later
test_df = test_df.withColumn('DAYSONMARKET_Original', test_df['DAYSONMARKET'])

# Recalculate DAYSONMARKET from what we know on our split date
test_df = test_df.withColumn('DAYSONMARKET', datediff(split_date, 'LISTDATE'))

# Review the difference
test_df[['LISTDATE', 'OFFMKTDATE', 'DAYSONMARKET_Original', 'DAYSONMARKET']].show()