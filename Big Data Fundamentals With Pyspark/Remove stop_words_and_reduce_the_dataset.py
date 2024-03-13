# Convert the words in splitRDD in lower case and then remove stop words from stop_words curated list. Think carefully about which function to use here.
# Create a pair RDD tuple containing the word and the number 1 from each word element in splitRDD.
# Get the count of the number of occurrences of each word (word frequency) in the pair RDD. Use a transformation which operates on key, value (k,v) pairs. Think carefully about which function to use here.

# Convert the words in lower case and remove stop words from the stop_words curated list
splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1 
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)