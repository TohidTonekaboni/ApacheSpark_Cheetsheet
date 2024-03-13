# Load the ratings.csv dataset into an RDD.
# Split the RDD using , as a delimiter.
# For each line of the RDD, using Rating() class create a tuple of userID, productID, rating.
# Randomly split the data into training data and test data (0.8 and 0.2).


# Load the data into RDD
data = sc.textFile(file_path)

# Split the RDD 
ratings = data.map(lambda l: l.split(','))

# Transform the ratings RDD
ratings_final = ratings.map(lambda line: Rating(int(line[0]), int(line[1]), float(line[2])))

# Split the data into training and test
training_data, test_data = ratings_final.randomSplit([0.8, 0.2])