# Import the file 2015-departures.csv.gz to a DataFrame. Note the header is already defined.
# Filter the DataFrame to contain only flights with a duration over 0 minutes. Use the index of the column, not the column name (remember to use .printSchema() to see the column names / order).
# Add an ID column.
# Write the file out as a JSON document named output.json.


# Import the data to a DataFrame
departures_df = spark.read.csv('2015-departures.csv.gz', header=True)

# Remove any duration of 0
departures_df = departures_df.filter(departures_df[3] > 0)

# Add an ID column
departures_df = departures_df.withColumn('id', F.monotonically_increasing_id())

# Write the file out to JSON format
departures_df.write.json('output.json', mode='overwrite')