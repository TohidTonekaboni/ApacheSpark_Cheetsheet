# Create a bucketizer object with bin boundaries at 0, 3, 6, …, 24 which correspond to times 0:00, 03:00, 06:00, …, 24:00. Specify input column as depart and output column as depart_bucket.
# Bucket the departure times in the flights data. Show the first five values for depart and depart_bucket.
# Create a one-hot encoder object. Specify output column as depart_dummy.
# Train the encoder on the data and then use it to convert the bucketed departure times to dummy variables. Show the first five values for depart, depart_bucket and depart_dummy

from pyspark.ml.feature import Bucketizer, OneHotEncoder

# Create buckets at 3 hour intervals through the day
buckets = Bucketizer(splits=[0, 3, 6, 9, 12, 15, 18, 21, 24], inputCol='depart', outputCol='depart_bucket')

# Bucket the departure times
bucketed = buckets.transform(flights)
bucketed.select('depart', 'depart_bucket').show(5)

# Create a one-hot encoder
onehot = OneHotEncoder(inputCols=['depart_bucket'], outputCols=['depart_dummy'])

# One-hot encode the bucketed departure times
flights_onehot = onehot.fit(bucketed).transform(bucketed)
flights_onehot.select('depart', 'depart_bucket', 'depart_dummy').show(5)