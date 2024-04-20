# Create a string indexer. Specify the input and output fields as org and org_idx.
# Create a one-hot encoder. Name the output field org_dummy.
# Assemble the km and org_dummy fields into a single field called features.
# Create a pipeline using the following operations: string indexer, one-hot encoder, assembler and linear regression. Use this to create a cross-validator.
# Create an indexer for the org field
indexer = StringIndexer(inputCol='org', outputCol='org_idx')

# Create an one-hot encoder for the indexed org field
onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])

# Assemble the km and one-hot encoded fields
assembler = VectorAssembler(inputCols=['km', 'org_dummy'], outputCol='features')

# Create a pipeline and cross-validator.
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])
cv = CrossValidator(estimator=pipeline,
                    estimatorParamMaps=params,
                    evaluator=evaluator)