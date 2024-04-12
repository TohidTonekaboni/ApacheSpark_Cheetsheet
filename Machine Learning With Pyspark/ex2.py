# Read data from a CSV file called 'flights.csv'. Assign data types to columns automatically. Deal with missing data.
# How many records are in the data?
# Take a look at the first five records.
# What data types have been assigned to the columns? Do these look correct?

# Read data from CSV file
flights = spark.read.csv('flights.csv',
                         sep=',',
                         header=True,
                         inferSchema=True,
                         nullValue='NA')

# Get number of records
print("The data contain %d records." % flights.count())

# View the first five records
flights.show(5)

# Check column data types
print(flights.dtypes)