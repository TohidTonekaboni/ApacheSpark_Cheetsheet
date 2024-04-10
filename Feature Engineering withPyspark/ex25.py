# Import the needed function when() from pyspark.sql.functions.
# Create a string matching condition using like() to look for for the string pattern Attached Garage in df['GARAGEDESCRIPTION'] and use wildcards % so it will match anywhere in the field.
# Similarly, create another condition using like() to find the string pattern Detached Garage in df['GARAGEDESCRIPTION'] and use wildcards % so it will match anywhere in the field.
# Create a new column has_attached_garage using when() to assign the value 1 if it has an attached garage, zero if detached and use otherwise() to assign null with None if it is neither.

# Import needed functions
from pyspark.sql.functions import when

# Create boolean conditions for string matches
has_attached_garage = df['GARAGEDESCRIPTION'].like('%Attached Garage%')
has_detached_garage = df['GARAGEDESCRIPTION'].like('%Detached Garage%')

# Conditional value assignment 
df = df.withColumn('has_attached_garage', (when(has_attached_garage, 1)
                                          .when(has_detached_garage, 0)
                                          .otherwise(None)))

# Inspect results
df[['GARAGEDESCRIPTION', 'has_attached_garage']].show(truncate=100)