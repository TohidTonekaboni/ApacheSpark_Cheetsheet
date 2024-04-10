# Convert walk_df['latitude'] and walk_df['longitude'] to type double by using cast('double') on the column and replacing the column in place withColumn().
# Round the columns in place with withColumn() and round('latitude', 5) and round('longitude', 5).
# Create the join condition of walk_df['latitude'] matching df['latitude'] and walk_df['longitude'] matching df['longitude'].
# Join df and walk_df together with join(), using the condition above and the left join type. Save the joined dataframe as join_df.

# Cast data types
walk_df = walk_df.withColumn('longitude', walk_df['longitude'].cast('double'))
walk_df = walk_df.withColumn('latitude', walk_df['latitude'].cast('double'))

# Round percision
df = df.withColumn('longitude', round(df['longitude'], 5))
df = df.withColumn('latitude', round(df['latitude'], 5))

# Create join condition
condition = [(df['longitude'] == walk_df['longitude']), (df['latitude'] == walk_df['latitude'])]

# Join the dataframes together
join_df = df.join(walk_df, on=condition, how='left')
# Count non-null records from new field
print(join_df.where(~join_df['walkscore'].isNull()).count())