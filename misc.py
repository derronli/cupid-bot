import pandas as pd 

# 0 = negative, 2 = neutral, 4 = positive
# def cleanTrainingData():
#     df= pd.read_csv("../tweet-classification.csv", encoding="utf-8") 

#     df.columns = ['label', 'id', 'date', 'flag', 'user', 'text']
#     df = df.drop(columns=['id', 'date', 'flag', 'user'])

    
#     columns_titles = ["text","label"]
#     df=df.reindex(columns=columns_titles)

#     # Function to wrap each item with double quotations
#     def wrap_with_double_quotes(item):
#         return f'"{item}"'

#     # Apply the function to wrap items in the 'text' with double quotations
#     df["text"] = df["text"].apply(wrap_with_double_quotes)



#     # Write the DataFrame to a CSV file
#     output_file = "training-classify.csv"
#     df.to_csv(output_file, index=False)

        
#     # display 
#     print(df.head())



def cleanTrainingData():
    df= pd.read_csv("../Tweets.csv", encoding="utf-8") 

    df = df.drop(columns=['textID', 'selected_text'])

    # Function to wrap each item with double quotations
    def wrap_with_double_quotes(item):
        return f'"{item}"'

    # Apply the function to wrap items in the 'text' with double quotations
    df["text"] = df["text"].apply(wrap_with_double_quotes)



    # Write the DataFrame to a CSV file
    output_file = "training-twe-classify.csv"
    df.to_csv(output_file, index=False)

        
    # display 
    print(df.head())



''' ==========================FUNCTION CALLS (for testing)=========================== '''
cleanTrainingData()