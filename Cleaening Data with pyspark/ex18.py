# Create a new DataFrame normal_df by joining flights_df with airports_df.
# Determine which type of join is used in the query plan.


# Join the flights_df and aiports_df DataFrames
normal_df = flights_df.join(airports_df, \
    flights_df["Destination Airport"] == airports_df["IATA"] )

# Show the query plan
normal_df.explain()
