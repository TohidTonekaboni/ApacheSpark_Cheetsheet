# Filter the people table to select all rows where sex is female into people_female_df DataFrame.
# Filter the people table to select all rows where sex is male into people_male_df DataFrame.
# Count the number of rows in both people_female and people_male DataFrames.


# Filter the people table to select female sex 
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')

# Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')

# Count the number of rows in both people_df_female and people_male_df DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(people_female_df.count(), people_male_df.count()))