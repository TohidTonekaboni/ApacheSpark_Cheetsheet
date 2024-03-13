# Find the number of partitions that support fileRDD RDD.
# Create an RDD named fileRDD_part from the file path but create 5 partitions.
# Confirm the number of partitions in the new fileRDD_part RDD.

# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions = 5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is", fileRDD_part.getNumPartitions())