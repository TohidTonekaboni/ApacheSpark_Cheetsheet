# Using df create a list of attribute and datatype tuples with dtypes called actual_dtypes_list.
# Iterate through actual_dtypes_list, checking if the column names exist in the dictionary of expected dtypes validation_dict.
# For the keys that exist in the dictionary, check their dtypes and print those that match.


# Create list of actual dtypes to check
actual_dtypes_list = df.dtypes
print(actual_dtypes_list)

# Iterate through the list of actual dtypes tuples
for attribute_tuple in actual_dtypes_list:
  
  # Check if column name is dictionary of expected dtypes
  col_name = attribute_tuple[0]
  if col_name in validation_dict:

    # Compare attribute names and types
    col_type = attribute_tuple[1]
    if col_type == validation_dict[col_name]:
      print(col_name + ' has expected dtype.')