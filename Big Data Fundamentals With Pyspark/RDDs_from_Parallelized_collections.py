# Create a RDD named RDD from a Python list of words.
# Confirm the object created is RDD.


# Create an RDD from a list of words
RDD = sc.parallelize(["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))