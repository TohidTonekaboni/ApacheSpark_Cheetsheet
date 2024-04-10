# Create a pandas dataframe using the values of importances and name the column importance by setting the parameter columns.
# Using the imported list of features names, feature_cols, create a new pandas.Series by wrapping it in the pd.Series() function. Set it to the column fi_df['feature'].
# Sort the dataframe using sort_values(), setting the by parameter to our importance column and sort it descending by setting ascending to False. Inspect the results.

# Convert feature importances to a pandas column
fi_df = pd.DataFrame(importances, columns=['importance'])

# Convert list of feature names to pandas column
fi_df['feature'] = pd.Series(feature_cols)

# Sort the data based on feature importance
fi_df.sort_values(by=['importance'], ascending=False, inplace=True)

# Inspect Results
fi_df.head(10)