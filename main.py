import pandas as pd
from MsgExtract import extractMsgs
from ClassifyFilter import classifyFilter
from MsgGeneration import cleanGenerateTrainingData

''' THESE ARE MAINLY ALL FOR DATA SETUP AND CLEANING'''
# Extract messages and format from discord logs
df = extractMsgs()
# Classify each message as positive/negative -> filter out all negatives
'''df = classifyFilter(df)'''
# Use this filtered dataset as the training data for generate model
# Outputs the training data which can be fed into Cohere 
cleanGenerateTrainingData(df)

# The rest is just using the Cohere generate endpoint function (with our model) to generate responses to user input
