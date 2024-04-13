# Import a function which will allow you to round a number to a specific number of decimal places.
# Derive a new km column from the mile column, rounding to zero decimal places. One mile is 1.60934 km.
# Remove the mile column.
# Create a label column with a value of 1 indicating the delay was 15 minutes or more and 0 otherwise. Think carefully about the logical condition.

# Import the required function
from pyspark.sql.functions import round

# Convert 'mile' to 'km' and drop 'mile' column (1 mile is equivalent to 1.60934 km)
flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0)) \
                    .drop('mile')

# Create 'label' column indicating whether flight delayed (1) or not (0)
flights_km = flights_km.withColumn('label', (flights_km.delay >= 15).cast('integer'))

# Check first five records
flights_km.show(5)