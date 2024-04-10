# Create a new column using withColumn() called LOT_SIZE_SQFT and convert ACRES to square feet by multiplying by acres_to_sqfeet the conversion factor.
# Create another new column called YARD_SIZE by subtracting FOUNDATIONSIZE from LOT_SIZE_SQFT.
# Run corr() on each of the independent variables YARD_SIZE, FOUNDATIONSIZE, LOT_SIZE_SQFT against the dependent variable SALESCLOSEPRICE. Does new feature show a stronger correlation than either of its components?

# Lot size in square feet
acres_to_sqfeet = 43560
df = df.withColumn('LOT_SIZE_SQFT', df['ACRES'] * acres_to_sqfeet)

# Create new column YARD_SIZE
df = df.withColumn('YARD_SIZE', df['LOT_SIZE_SQFT'] - df['FOUNDATIONSIZE'])

# Corr of ACRES vs SALESCLOSEPRICE
print("Corr of ACRES vs SALESCLOSEPRICE: " + str(df.corr('ACRES', 'SALESCLOSEPRICE')))
# Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE
print("Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE: " + str(df.corr('FOUNDATIONSIZE', 'SALESCLOSEPRICE')))
# Corr of YARD_SIZE vs SALESCLOSEPRICE
print("Corr of YARD_SIZE vs SALESCLOSEPRICE: " + str(df.corr('YARD_SIZE', 'SALESCLOSEPRICE')))