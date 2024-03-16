# Load the Data Frame.
# Add the transformation for F.lower() to the Destination Airport column.
# Drop the Destination Airport column from the Data Frame aa_dfw_df. Note the time for these operations to complete.
# Show the Data Frame, noting the time difference for this action to complete.


# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(Header=True).load('AA_DFW_2018.csv.gz')

# Add the airport column using the F.lower() method
aa_dfw_df = aa_dfw_df.withColumn('airport', F.lower(aa_dfw_df['Destination Airport']))

# Drop the Destination Airport column
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])

# Show the DataFrame
aa_dfw_df.show()