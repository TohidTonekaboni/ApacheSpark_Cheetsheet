# Import the StopWordsRemover, HashingTF and IDF classes.
# Create a StopWordsRemover object (input column words, output column terms). Apply to sms.
# Create a HashingTF object (input results from previous step, output column hash). Apply to wrangled.
# Create an IDF object (input results from previous step, output column features). Apply to wrangled.


from pyspark.ml.feature import StopWordsRemover, HashingTF, IDF

# Remove stop words.
wrangled = StopWordsRemover(inputCol='words', outputCol='terms')\
      .transform(sms)

# Apply the hashing trick
wrangled = HashingTF(inputCol='terms', outputCol='hash', numFeatures=1024)\
      .transform(wrangled)

# Convert hashed symbols to TF-IDF
tf_idf = IDF(inputCol='hash', outputCol='features')\
      .fit(wrangled).transform(wrangled)
      
tf_idf.select('terms', 'features').show(4, truncate=False)