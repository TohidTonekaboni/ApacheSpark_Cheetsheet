# Create a pair RDD named Rdd with tuples (1,2),(3,4),(3,6),(4,5).
# Transform the Rdd with reduceByKey() into a pair RDD Rdd_Reduced by adding the values with the same key.
# Collect the contents of pair RDD Rdd_Reduced and iterate to print the output.


# Create PairRDD Rdd with key value pairs
Rdd = sc.parallelize([(1,2), (3,4), (3,6), (4,5)])

# Apply reduceByKey() operation on Rdd
Rdd_Reduced = Rdd.reduceByKey(lambda x, y: x + y)

# Iterate over the result and print the output
for num in Rdd_Reduced.collect(): 
  print("Key {} has {} Counts".format(num[0], num[1]))