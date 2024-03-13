# Create map() transformation that cubes all of the numbers in numbRDD.
# Collect the results in a numbers_all variable.
# Print the output from numbers_all variable.


# Create map() transformation to cube numbers
cubedRDD = numbRDD.map(lambda x: x**3)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
	print(numb)