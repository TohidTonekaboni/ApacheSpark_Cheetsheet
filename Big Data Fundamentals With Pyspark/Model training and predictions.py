# Train ALS algorithm with training data and configured parameters (rank = 10 and iterations = 10).
# Drop the rating column in the test data, which is the third column.
# Test the model by predicting the rating from the test data.
# Return a list of two rows of the predicted ratings.

# Create the ALS model on the training data
model = ALS.train(training_data, rank=10, iterations=10)

# Drop the ratings column 
testdata_no_rating = test_data.map(lambda p: (p[0], p[1]))

# Predict the model  
predictions = model.predictAll(testdata_no_rating)

# Return the first 2 rows of the RDD
predictions.take(2)