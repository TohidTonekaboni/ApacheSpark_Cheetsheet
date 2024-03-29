# Import the broadcast() method from pyspark.sql.functions.
# Create a new DataFrame broadcast_df by joining flights_df with airports_df, using the broadcasting.
# Show the query plan and consider differences from the original.

# Import the broadcast method from pyspark.sql.functions
from pyspark.sql.functions import broadcast

# Join the flights_df and airports_df DataFrames using broadcasting
broadcast_df = flights_df.join(broadcast(airports_df), \
    flights_df["Destination Airport"] == airports_df["IATA"] )

# Show the query plan and compare against the original
broadcast_df.explain()