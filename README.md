# Cupid Bot
A discord bot that can adapt to the user's speech patterns to answer the hard questions and provide personalized relationship help - using generative AI and NLP\
\
Built with Python and Cohere API

**Disclaimer:** Cupid bot is purely for entertainment purposes and is not indicative of my opinions on human relationships😅 
## Motivation
The dreaded trap relationship questions where it seems like there is no right answer. *Would you still love me if I was a worm?*, *If you had to kiss my best friend to save my life, would you do it?*, *Aren't they pretty? They are so pretty right??* A real hair-puller right.
> Cupid bot aims to solve this problem by using previous conversation data and AI to construct the perfect, most optimal answer. Based on your personal speech patterns AND your significant other's ideal communication style

## Demo
Note that for this demo, Cupid bot was trained to mimic a very affectionate boyfriend whose replying to a girlfriend that responds well to sweet messages and compliments.\
\
**Invoking the \cupid_gen command in discord will prompt the bot to read in the previous message sent in the chat, and reply to it**

![image](https://github.com/derronli/cupid-bot/assets/104483680/1a0279ec-28e4-4e1c-bfa4-10144d501d09)

**Cupid Bot has basic emotional intelligence**  

![image](https://github.com/derronli/cupid-bot/assets/104483680/70dd753c-d821-4842-94c3-2c1ab29b6eba)

**Cupid bot knows to use the User's commonly used emojis and words. It's almost creepy...**

![image](https://github.com/derronli/cupid-bot/assets/104483680/73510af4-e871-4679-a573-c653a33d15cb)


**Notice the short forms and texting style**

![asdasd](https://github.com/derronli/cupid-bot/assets/104483680/c4c13ab5-1da2-49bc-b1f3-03e6e0edc31f)

**Sometimes it has some funny mistakes**

![image](https://github.com/derronli/cupid-bot/assets/104483680/e0c9c4cd-4fcd-41b9-add7-3c676bfc3d2a)
![image](https://github.com/derronli/cupid-bot/assets/104483680/3cea2b1c-392f-4fb3-87fa-819dde29a9da)



Note that these bot messages are normally only visible to the user (as a discord Ephemeral message) but were exposed for demo sake

## Customization Demo
To effectively show Cupid bot's ability to match speech patterns and adapt to the target who it's responding to, I trained Cupid Bot on my friend and my chat logs

**Very different style**

![image](https://github.com/derronli/cupid-bot/assets/104483680/ef031264-7c36-4bcc-bb78-fcbb2124a9c2)

**Context: we normally ask each other to play League**

![image](https://github.com/derronli/cupid-bot/assets/104483680/27e6bb8d-485f-4955-86fd-495b9042778e)

## Summarization Demo
Prompt generated courtesy of ChatGPT\
In case you're in the middle of a game/video/project and need to quickly reply to your significant other

![image](https://github.com/derronli/cupid-bot/assets/104483680/11975ca4-c577-4739-996d-51129e3d8a87)

## How does it Work

![image](https://github.com/derronli/cupid-bot/assets/104483680/fdb07a27-94af-4c20-832e-4f80fbdb89d0)

*Above is the general flow which I followed, starting from the top left.*
### I believe the most crucial step was the classification
Text messages were extracted into the following format:
1. Prompt (target) - "How do you like my new hairstyle?"
2. Message (user) - "Wow it looks great on you!"
3. Response (target) - "Aw, thanks!!!"

Then each **Response** was tagged with a Response Semantic using the Cohere Classify Endpoint. (Positive/Negative/Neutral)\
\
From here, all rows in the table tagged with a non-Positive response were removed, along with the Response column - leaving us with only the Prompt-Message pairs which we know the **target responds well to**\
\
These Prompt-Message pairs were then used to train the Generative AI Model. Allowing for the bot to pick up on the optimal responses to the target's "Prompts".

## Using Cupid Bot
**Disclaimer:** Cupid Bot is not liable if it were to damage your relationships.\
Setup is quite complex right now, a future goal would be to simplify it.

`clone the repo`

Install dependencies
```
pip install cohere
pip install pandas
```

Use [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) to extract messages from you and your significant other (or friend)\
**Export as a .txt file**\
The period of time you choose to extract is up to you\
\
Place the .txt into the project's root directory\
Run the `main.py` file, either with your editor's code runner or `python main.py`\
This will output the *training-generate.csv* file\
Create a customized Generate model with Cohere and input the *training-generate.csv* file\
Fill in the MODEL_ID field in `CohereLayer.py` with the customized model ID produced\
Fill in the `examples.py` file with desired prompt (Keep in mind, mine examples.py is hidden for privacy sake, but I will provide a template for this)\
Run the bot!

### If you made it this far: Thanks for reading! I hope you had as much fun reading about/playing with Cupid Bot as I did making it
