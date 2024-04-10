# Pivot the values of ex_garage_list by grouping by the record id NO with groupBy() use the provided code to aggregate constant_val to ignore nulls and take the first value.
# Left join piv_df to df using NO as the join condition.
# Create the list of columns, zfill_cols, to zero fill by using the columns attribute on piv_df
# Zero fill the pivoted dataframes columns, zfill_cols, by using fillna() with a subset.

from pyspark.sql.functions import coalesce, first

# Pivot 
piv_df = ex_df.groupBy('NO').pivot('ex_garage_list').agg(coalesce(first('constant_val')))

# Join the dataframes together and fill null
joined_df = df.join(piv_df, on='NO', how='left')

# Columns to zero fill
zfill_cols = piv_df.columns

# Zero fill the pivoted values
zfilled_df = joined_df.fillna(0, subset=zfill_cols)