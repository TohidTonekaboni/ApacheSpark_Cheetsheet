# Select the unique entries from the column VOTER NAME and create a new DataFrame called voter_df.
# Count the rows in the voter_df DataFrame.
# Add a ROW_ID column using the appropriate Spark function.
# Show the rows with the 10 highest ROW_IDs.


# Select all the unique council voters
voter_df = df.select(df["VOTER NAME"]).distinct()

# Count the rows in voter_df
print("\nThere are %d rows in the voter_df DataFrame.\n" % voter_df.count())

# Add a ROW_ID
voter_df = voter_df.withColumn('ROW_ID', F.monotonically_increasing_id())

# Show the rows with 10 highest IDs in the set
voter_df.orderBy(voter_df.ROW_ID.desc()).show(10)