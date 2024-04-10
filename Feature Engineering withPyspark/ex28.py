# Import the feature transformer Binarizer from pyspark and the ml.feature module.
# Create the transformer using Binarizer() with the threshold for setting the value to 1 as anything after Friday, 5.0, then set the input column as List_Day_of_Week and output column as Listed_On_Weekend.
# Apply the binarizer transformation on df using transform().
# Verify the transformation worked correctly by selecting the List_Day_of_Week and Listed_On_Weekend columns with show().


# Import transformer
from pyspark.ml.feature import Binarizer

# Create the transformer
binarizer = Binarizer(threshold=5.0, inputCol='List_Day_of_Week', outputCol='Listed_On_Weekend')

# Apply the transformation to df
df = binarizer.transform(df)

# Verify transformation
df[['List_Day_of_Week', 'Listed_On_Weekend']].show()