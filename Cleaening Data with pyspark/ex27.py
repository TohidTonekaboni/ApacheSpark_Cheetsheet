# Determine the row counts for each DataFrame.
# Create a DataFrame containing only the invalid rows.
# Validate the count of the new DataFrame is as expected.
# Determine the number of distinct folder rows removed.


# Determine the row counts for each DataFrame
split_count = split_df.count()
joined_count = joined_df.count()

# Create a DataFrame containing the invalid rows
invalid_df = split_df.join(F.broadcast(joined_df), 'folder', 'left_anti')

# Validate the count of the new DataFrame is as expected
invalid_count = invalid_df.count()
print(" split_df:\t%d\n joined_df:\t%d\n invalid_df: \t%d" % (split_count, joined_count, invalid_count))

# Determine the number of distinct folder rows removed
invalid_folder_count = invalid_df.select('folder').distinct().count()
print("%d distinct invalid folders found" % invalid_folder_count)