# Register the Dataframes as SparkSQL tables with createOrReplaceTempView, name them the df and walk_df respectively.
# In the join_sql string, set the left table to df and the right table to walk_df
# Call spark.sql() on the join_sql string to perform the join.

# Register dataframes as tables
df.createOrReplaceTempView("df")
walk_df.createOrReplaceTempView("walk_df")

# SQL to join dataframes
join_sql = 	"""
			SELECT 
				*
			FROM df
			LEFT JOIN walk_df
			ON df.longitude = walk_df.longitude
			AND df.latitude = walk_df.latitude
			"""
# Perform sql join
joined_df = spark.sql(join_sql)