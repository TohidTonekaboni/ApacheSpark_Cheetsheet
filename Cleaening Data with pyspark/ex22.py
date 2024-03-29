# Import the annotations.csv.gz file to a DataFrame and perform a row count. Specify a separator character of |.
# Query the data for the number of rows beginning with #.
# Import the file again to a new DataFrame, but specify the comment character in the options to remove any commented rows.
# Count the new DataFrame and verify the difference is as expected.

# Import the file to a DataFrame and perform a row count
annotations_df = spark.read.csv('annotations.csv.gz', sep='|')
full_count = annotations_df.count()

# Count the number of rows beginning with '#'
comment_count = annotations_df.where(col('_c0').startswith('#')).count()

# Import the file to a new DataFrame, without commented rows
no_comments_df = spark.read.csv('annotations.csv.gz', sep='|', comment='#')

# Count the new DataFrame and verify the difference is as expected
no_comments_count = no_comments_df.count()
print("Full count: %d\nComment count: %d\nRemaining count: %d" % (full_count, comment_count, no_comments_count))