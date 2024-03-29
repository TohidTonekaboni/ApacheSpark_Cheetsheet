# Add a column to voter_df named random_val with the results of the F.rand()
# method for any voter with the title Councilmember.
# Show some of the DataFrame rows, noting whether the .when() clause worked.


# Add a column to voter_df for any voter with the title **Councilmember**
voter_df = voter_df.withColumn('random_val',
                               when(voter_df.TITLE == 'Councilmember', F.rand()))

# Show some of the DataFrame rows, noting whether the when clause worked
voter_df.show()