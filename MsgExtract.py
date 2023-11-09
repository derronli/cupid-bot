import pandas as pd
from credentials import TARGET_SENDER, OTHER_SENDER

def extractMsgs():
    # Define the sender's name you want to extract messages from
    target_sender = TARGET_SENDER
    other_sender = OTHER_SENDER
    MSG_FILE = "../punyRec.txt"

    # Initialize a list to store the messages sent by the target sender
    target_sender_messages = []
    other_sender_messages = []

    with open(MSG_FILE, "r", encoding="utf8") as file:
        lines = file.readlines()

    current_message = ""
    other_message = ""

    # Ensure first message processed is from target sender -> this is to get desired form
    for i in range(0, len(lines)):
        if lines[i].strip().endswith(target_sender):
            start = i
            break


    # For loop extracts messages from both users in the format:
    # Other sender Message  |  Target user's response to the message
    # saves results into CSV

    # Format is always -> user followed by message on next line
    for i in range(start, len(lines), 2):
        line = lines[i].strip()

        if line == "":
            continue

        # We want to continuously add to the current message -> this is to take care of the cases where
        # Users type semantic sentences in more than one message -> so we merge the lines as such
        if line.endswith(target_sender):

            # Process target user message
            current_message += lines[i + 1].strip() + " "
        # As soon as we see a line not from target user
        elif line.endswith(other_sender):

            ''' We will make the assumption that messages < 3 words long are semantically irrelevant -> just added noise'''
            number_words = current_message.split()
            if len(number_words) >= 3:
                # We only SAVE the other user message when we save target user (so that they come 1:1)
                
                other_sender_messages.append(other_message)
                other_message = ""
                # Save target user
                target_sender_messages.append(current_message)
            current_message = ""

            # Processesing other user messaages => we'll process it every time we come across it
            other_message += lines[i + 1].strip() + " "

    # For last message
    if current_message and other_message:
        number_words = current_message.split()
        if len(number_words) >= 3:
            other_sender_messages.append(other_message)
            #other_message = ""
            # Save target user
            target_sender_messages.append(current_message)


    for message in target_sender_messages:
        print(message)
    print("=================")
    for message in other_sender_messages:
        print(message)

    
    try:
        df = pd.DataFrame({'Prompt':target_sender_messages[:-1], 'Message': other_sender_messages[1:], 'Response': target_sender_messages[1:]})
    except:
        print(len(target_sender_messages))
        print(len(other_sender_messages))
    # Write the DataFrame to a CSV file
    output_file = "conversation.csv"
    df.to_csv(output_file, index=False)
    
    return df


''' ==========================FUNCTION CALLS (for testing)=========================== '''

