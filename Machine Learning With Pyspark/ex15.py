# Split the data into training and testing sets in a 4:1 ratio. Set the random number seed to 13 to ensure repeatability.
# Create a LogisticRegression object and fit it to the training data.
# Generate predictions on the testing data.
# Use the predictions to form a confusion matrix.

# Split the data into training and testing sets
sms_train, sms_test = sms.randomSplit([0.8,0.2], seed=13)

# Fit a Logistic Regression model to the training data
logistic = LogisticRegression(regParam=0.2).fit(sms_train)

# Make predictions on the testing data
prediction = logistic.transform(sms_test)

# Create a confusion matrix, comparing predictions to known labels
prediction.groupBy('label', 'prediction').count().show()