import pandas as pd

# Takes the filtered dataframe from ClassifyFilter -> structures the data into CSV format for training
# Format: Prompt , generation pairs 
def cleanGenerateTrainingData(df):
    # Current dataframe has [Prompt, Message, Response, Response Semantic]
    # Only positive labels are left after ClassifyFilter
    '''prompt_message_df = df = df.drop(columns=['Response', 'Response Semantic'])'''
    prompt_message_df = df = df.drop(columns=['Response'])

    # Function to wrap each item with double quotations
    def wrap_with_double_quotes(item):
        return f'"{item}"'

    # Wrap with double quotes so commas don't mess up model training
    prompt_message_df["Prompt"] = prompt_message_df["Prompt"].apply(wrap_with_double_quotes)
    prompt_message_df["Message"] = prompt_message_df["Message"].apply(wrap_with_double_quotes)


    output_file = "training-generate.csv"
    prompt_message_df.to_csv(output_file, index=False)


