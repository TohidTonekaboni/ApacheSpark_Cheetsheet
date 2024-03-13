# Select 'name', 'sex', and 'date of birth' columns from people_df and create people_df_sub DataFrame.
# Print the first 10 observations in the people_df_sub DataFrame.
# Remove duplicate entries from people_df_sub DataFrame and create people_df_sub_nodup DataFrame.
# How many rows are there before and after duplicates are removed?


# Select name, sex and date of birth columns
people_df_sub = people_df.select('name', 'sex', 'date of birth')

# Print the first 10 observations from people_df_sub
people_df_sub.show(10)

# Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(people_df_sub.count(), people_df_sub_nodup.count()))