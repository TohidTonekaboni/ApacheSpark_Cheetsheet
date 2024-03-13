# Filter the people_df DataFrame to select all rows where sex is female into people_df_female DataFrame.
# Filter the people_df DataFrame to select all rows where sex is male into people_df_male DataFrame.
# Count the number of rows in people_df_female and people_df_male DataFrames.


# Filter people_df to select females 
people_df_female = people_df.filter(people_df.sex == "female")

# Filter people_df to select males
people_df_male = people_df.filter(people_df.sex == "male")

# Count the number of rows 
print("There are {} rows in the people_df_female DataFrame and {} rows in the people_df_male DataFrame".format(people_df_female.count(), people_df_male.count()))