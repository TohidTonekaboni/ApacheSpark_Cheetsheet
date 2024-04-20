# Create an empty parameter grid.
# Create objects for building and evaluating a linear regression model. The model should predict the "duration" field.
# Create a cross-validator object. Provide values for the estimator, estimatorParamMaps and evaluator arguments. Choose 5-fold cross validation.
# Train and test the model across multiple folds of the training data.

# Create an empty parameter grid
params = ParamGridBuilder().build()

# Create objects for building and evaluating a regression model
regression = LinearRegression(labelCol='duration')
evaluator = RegressionEvaluator(labelCol='duration')

# Create a cross validator
cv = CrossValidator(estimator=regression, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)

# Train and test model on multiple folds of the training data
cv = cv.fit(flights_train)

# NOTE: Since cross-valdiation builds multiple models, the fit() method can take a little while to complete.