# Print the first 10 observations in the people_df DataFrame.
# Count the number of rows in the people_df DataFrame.
# How many columns does people_df DataFrame have and what are their names?



# Print the first 10 observations 
people_df.show(10)

# Count the number of rows 
print("There are {} rows in the people_df DataFrame.".format(people_df.count()))

# Count the number of columns and print their names
print("There are {} columns in the people_df DataFrame and their names are {}".format(len(people_df.columns), people_df.columns))