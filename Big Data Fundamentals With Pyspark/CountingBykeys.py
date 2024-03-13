# countByKeyand assign the result to a variable total.
# What is the type of total?
# Iterate over the total and print the keys and their counts.


# Count the unique keys
total = Rdd.countByKey()

# What is the type of total?
print("The type of total is", type(total))

# Iterate over the total and print the output
for k, v in total.items(): 
  print("key", k, "has", v, "counts")