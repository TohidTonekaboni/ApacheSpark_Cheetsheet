# Store the number of partitions in departures_df in the variable before.
# Change the spark.sql.shuffle.partitions configuration to 500 partitions.
# Recreate the departures_df DataFrame reading the distinct rows from the departures file.
# Print the number of partitions from before and after the configuration change.


# Store the number of partitions in variable
before = departures_df.rdd.getNumPartitions()

# Configure Spark to use 500 partitions
spark.conf.set('spark.sql.shuffle.partitions', 500)

# Recreate the DataFrame using the departures data file
departures_df = spark.read.csv('departures.txt.gz').distinct()

# Print the number of partitions for each instance
print("Partition count before change: %d" % before)
print("Partition count after change: %d" % departures_df.rdd.getNumPartitions())