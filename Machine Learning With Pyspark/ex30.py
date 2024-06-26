# Create a parameter grid builder.
# Add grids for with regression.regParam (values 0.01, 0.1, 1.0, and 10.0) and regression.elasticNetParam (values 0.0, 0.5, and 1.0).
# Build the grid.
# Create a cross validator, specifying five folds.

# Create parameter grid
params = ParamGridBuilder()

# Add grids for two parameters
params = params.addGrid(regression.regParam, [0.01, 0.1, 1.0, 10.0]) \
               .addGrid(regression.elasticNetParam, [0.0, 0.5, 1.0])

# Build the parameter grid
params = params.build()
print('Number of models to be tested: ', len(params))

# Create cross-validator
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)