# Retrieve the best model.
# Look at the stages in the best model.
# Isolate the linear regression stage and extract its parameters.
# Use the best model to generate predictions on the testing data and calculate the RMSE.

# Get the best model from cross validation
best_model = cv.bestModel

# Look at the stages in the best model
print(best_model.stages)

# Get the parameters for the LinearRegression object in the best model
best_model.stages[3].extractParamMap()

# Generate predictions on testing data using the best model then calculate RMSE
predictions = best_model.transform(flights_test)
print("RMSE =", evaluator.evaluate(predictions))