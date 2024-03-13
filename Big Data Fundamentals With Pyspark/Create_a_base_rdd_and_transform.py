# Create a RDD called baseRDD that reads lines from file_path.
# Transform the baseRDD into a long list of words and create a new splitRDD.
# Count the total number words in splitRDD.




# Create a baseRDD from the file path
baseRDD = sc.textFile(file_path)

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())