# Create a new variable ASSESSED_TO_LIST by dividing ASSESSEDVALUATION by LISTPRICE to help us understand if the having a high or low assessment value impacts our price.
# Create another new variable TAX_TO_LIST to help us understand the approximate tax rate by dividing TAXES by LISTPRICE.
# Lastly create another variable BED_TO_BATHS to help us know how crowded our bathrooms might be by dividing BEDROOMS by BATHSTOTAL.


# ASSESSED_TO_LIST
df = df.withColumn('ASSESSED_TO_LIST', df['ASSESSEDVALUATION'] / df['LISTPRICE'])
df[['ASSESSED_TO_LIST', 'ASSESSEDVALUATION', 'LISTPRICE']].show(5)
# TAX_TO_LIST
df = df.withColumn('TAX_TO_LIST', df['TAXES'] / df['LISTPRICE'])
df[['TAX_TO_LIST', 'TAXES', 'LISTPRICE']].show(5)
# BED_TO_BATHS
df = df.withColumn('BED_TO_BATHS', df['BEDROOMS'] / df['BATHSTOTAL'])
df[['BED_TO_BATHS', 'BEDROOMS', 'BATHSTOTAL']].show(5)