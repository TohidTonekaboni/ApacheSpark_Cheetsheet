# Find the RMSE for predictions on the testing data.
# Find the average time spent on the ground for flights departing from OGG between 21:00 and 24:00.
# Find the average time spent on the ground for flights departing from OGG between 03:00 and 06:00.
# Find the average time spent on the ground for flights departing from JFK between 03:00 and 06:00.

# Find the RMSE on testing data
from pyspark.ml.evaluation import RegressionEvaluator
rmse = RegressionEvaluator(labelCol='duration').evaluate(predictions)
print("The test RMSE is", rmse)

# Average minutes on ground at OGG for flights departing between 21:00 and 24:00
avg_eve_ogg = regression.intercept
print(avg_eve_ogg)

# Average minutes on ground at OGG for flights departing between 03:00 and 06:00
avg_night_ogg = regression.intercept + regression.coefficients[9]
print(avg_night_ogg)

# Average minutes on ground at JFK for flights departing between 03:00 and 06:00
avg_night_jfk = regression.intercept + regression.coefficients[9] + regression.coefficients[3]
print(avg_night_jfk)