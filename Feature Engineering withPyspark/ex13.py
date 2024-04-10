# Use select() to subset the dataframe df with the list of columns columns and Sample with the provided sample() function, and assign this dataframe to the variable sample_df.
# Convert the Subset dataframe to a pandas dataframe pandas_df, and use pandas isnull() to convert it DataFrame into True/False. Store this result in tf_df.
# Use seaborn's heatmap() to plot tf_df.
# Hit "Run Code" to view the plot. Then assign the name of the variable with most missing values to answer.

# Sample the dataframe and convert to Pandas
sample_df = df.select(columns).sample(False, 0.1, 42)
pandas_df = sample_df.toPandas()

# Convert all values to T/F
tf_df = pandas_df.isnull()

# Plot it
sns.heatmap(data=tf_df)
plt.xticks(rotation=30, fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.show()

# Set the answer to the column with the most missing data
answer = 'BACKONMARKETDATE'