# Import GBTRegressor from pyspark.ml.regression which you will notice is the same module as RandomForestRegressor.
# Instantiate GBTRegressor with featuresCol set to the vector column of our features named, features, labelCol set to our dependent variable, SALESCLOSEPRICE and the random seed to 42
# Train the model by calling fit() on gbt with the imported training data, train_df.

from pyspark.ml.regression import GBTRegressor

# Train a Gradient Boosted Trees (GBT) model.
gbt = GBTRegressor(featuresCol="features",
                           labelCol="SALESCLOSEPRICE",
                           predictionCol="Prediction_Price",
                           seed=42
                           )

# Train model.
model = gbt.fit(train_df)