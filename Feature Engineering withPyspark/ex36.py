# Import RegressionEvaluator from pyspark.ml.evaluation so it is available for use later.
# Initialize RegressionEvaluator by setting labelCol to our actual data, SALESCLOSEPRICE and predictionCol to our predicted data, Prediction_Price
# To calculate our metrics, call evaluate on evaluator with the prediction values preds and create a dictionary with key evaluator.metricName and value of rmse, do the same for the r2 metric.

from pyspark.ml.evaluation import RegressionEvaluator

# Select columns to compute test error
evaluator = RegressionEvaluator(labelCol="SALESCLOSEPRICE", 
                                predictionCol="Prediction_Price")
# Dictionary of model predictions to loop over
models = {'Gradient Boosted Trees': gbt_predictions, 'Random Forest Regression': rfr_predictions}
for key, preds in models.items():
  # Create evaluation metrics
  rmse = evaluator.evaluate(preds, {evaluator.metricName: "rmse"})
  r2 = evaluator.evaluate(preds, {evaluator.metricName: "r2"})

  # Print Model Metrics
  print(key + ' RMSE: ' + str(rmse))
  print(key + ' R^2: ' + str(r2))