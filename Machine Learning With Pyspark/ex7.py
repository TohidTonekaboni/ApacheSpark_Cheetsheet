# Import the class which will assemble the predictors.
# Create an assembler object that will allow you to merge the predictors columns into a single column.
# Use the assembler to generate a new consolidated column.

# Import the necessary class
from pyspark.ml.feature import VectorAssembler

# Create an assembler object
assembler = VectorAssembler(inputCols=[
    'mon', 'dom', 'dow', 'carrier_idx', 'org_idx', 'km', 'depart', 'duration'
], outputCol='features')

# Consolidate predictor columns
flights_assembled = assembler.transform(flights)

# Check the resulting column
flights_assembled.select('features', 'delay').show(5, truncate=False)