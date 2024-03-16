# Add a column to voter_df named random_val with the results of the F.rand() method for any voter with the title Councilmember. Set random_val to 2 for the Mayor. Set any other title to the value 0.
# Show some of the Data Frame rows, noting whether the clauses worked.
# Use the .filter clause to find 0 in random_val.

# Add a column to voter_df for a voter based on their position
voter_df = voter_df.withColumn('random_val',
                               when(voter_df.TITLE == 'Councilmember', F.rand())
                               .when(voter_df.TITLE == 'Mayor', 2)
                               .otherwise(0))

# Show some of the DataFrame rows
voter_df.show()

# Use the .filter() clause with random_val
voter_df.filter(voter_df.random_val == 0).show()