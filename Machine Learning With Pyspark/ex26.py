# Import the class for creating a pipeline.
# Create a pipeline object and specify the indexer, onehot, assembler and regression stages, in this order.
# Train the pipeline on the training data.
# Make predictions on the testing data.

# Import class for creating a pipeline
from pyspark.ml import Pipeline

# Construct a pipeline
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])

# Train the pipeline on the training data
pipeline = pipeline.fit(flights_train)

# Make predictions on the testing data
predictions = pipeline.transform(flights_test)