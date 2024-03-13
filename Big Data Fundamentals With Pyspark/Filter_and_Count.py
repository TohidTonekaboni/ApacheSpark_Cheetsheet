# Create filter() transformation to select the lines containing the keyword Spark.
# How many lines in fileRDD_filter contain the keyword Spark?
# Print the first four lines of the resulting RDD.

# Filter the fileRDD to select lines with Spark keyword
fileRDD_filter = fileRDD.filter(lambda line: 'Spark' in line)

# How many lines are there in fileRDD?
print("The total number of lines with the keyword Spark is", fileRDD_filter.count())

# Print the first four lines of fileRDD
for line in fileRDD_filter.take(4):
  print(line)