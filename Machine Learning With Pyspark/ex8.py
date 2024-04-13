# Split into training and testing sets in a 80:20 ratio
flights_train, flights_test = flights.randomSplit([0.8,0.2], seed=43)

# Check that training set has around 80% of records
training_ratio = flights_train.count() / flights.count()
print(training_ratio)