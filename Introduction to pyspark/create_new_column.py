# Create the column plane_age using the .withColumn() method and 
# subtracting the year of manufacture (column plane_year) from the year 
# (column year) of the flight.

# Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)