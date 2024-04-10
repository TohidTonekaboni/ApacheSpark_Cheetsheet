# Import RandomForestRegressionModel from pyspark.ml.regression.
# Using the model in memory called model call the save() method on it and name the model rfr_no_listprice.
# Reload the saved model file rfr_no_listprice by calling load() on RandomForestRegressionModel and storing it into loaded_model.

from pyspark.ml.regression import RandomForestRegressionModel

# Save model
model.save('rfr_no_listprice')

# Load model
loaded_model = RandomForestRegressionModel.load('rfr_no_listprice')