# Import to_date() and dayofweek() functions from pyspark.sql.functions
# Use the to_date() function to convert LISTDATE to a Spark date type, save the converted column in place using withColumn()
# Create a new column using LISTDATE and dayofweek() then save it as List_Day_of_Week using withColumn()
# Sample half the dataframe and convert it to a pandas dataframe with toPandas() and plot the count of the pandas dataframe's List_Day_of_Week column by using seaborn countplot() where x = List_Day_of_Week.


# Import needed functions
from pyspark.sql.functions import to_date, dayofweek

# Convert to date type
df = df.withColumn('LISTDATE', to_date('LISTDATE'))

# Get the day of the week
df = df.withColumn('List_Day_of_Week', dayofweek('LISTDATE'))

# Sample and convert to pandas dataframe
sample_df = df.sample(False, 0.5, 42).toPandas()

# Plot count plot of of day of week
ax = sns.countplot(x="List_Day_of_Week", data=sample_df)
plt.show()