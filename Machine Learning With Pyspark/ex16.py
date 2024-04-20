# Import the one-hot encoder class.
# Create a one-hot encoder instance, naming the input column org_idx and the output column org_dummy.
# Apply the one-hot encoder to the flights data.
# Generate a summary of the mapping from categorical values to binary encoded dummy variables. Include only unique values and order by org_idx.

# Import the one hot encoder class
from pyspark.ml.feature import OneHotEncoder

# Create an instance of the one hot encoder
onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])

# Apply the one hot encoder to the flights data
onehot = onehot.fit(flights)
flights_onehot = onehot.transform(flights)

# Check the results
flights_onehot.select('org', 'org_idx', 'org_dummy').distinct().sort('org_idx').show()