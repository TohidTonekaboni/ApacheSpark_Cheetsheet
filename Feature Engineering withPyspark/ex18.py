# Create a join between df_orig, the dataframe before its precision was corrected, and walk_df that matches on longitude and latitude in the respective dataframes.
# Count the number of missing values with where() isNull() on df['walkscore'] and correct_join['walkscore']. You should notice that there are many missing values because our datatypes and precision do not match.
# Create a join between df and walk_df that only matches on longitude
# Count the number of records with count(): few_keys_df and correct_join_df. You should notice that there are many more values as we have not constrained our matching correctly.

# Join on mismatched keys precision 
wrong_prec_cond = [df_orig['longitude'] == walk_df['longitude'], df_orig['latitude'] == walk_df['latitude']]
wrong_prec_df = df_orig.join(walk_df, on=wrong_prec_cond, how='left')

# Compare bad join to the correct one
print(wrong_prec_df.where(wrong_prec_df['walkscore'].isNull()).count())
print(correct_join_df.where(correct_join_df['walkscore'].isNull()).count())

# Create a join on too few keys
few_keys_cond = [df['longitude'] == walk_df['longitude']]
few_keys_df = df.join(walk_df, on=few_keys_cond, how='left')

# Compare bad join to the correct one
print("Record Count of the Too Few Keys Join Example: " + str(few_keys_df.count()))
print("Record Count of the Correct Join Example: " + str(correct_join_df.count()))