# Check the caching status on the departures_df DataFrame.
# Remove the departures_df DataFrame from the cache.
# Validate the caching status again.

# Determine if departures_df is in the cache
print("Is departures_df cached?: %s" % departures_df.is_cached)
print("Removing departures_df from cache")

# Remove departures_df from the cache
departures_df.unpersist()

# Check the cache status again
print("Is departures_df cached?: %s" % departures_df.is_cached)