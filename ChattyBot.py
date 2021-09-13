import random
from datetime import date, datetime, time

print("Hello and welcome to ChatMeUp! Enter 'exit' or 'stop' or 'bye' to quit at anytime.")
print("BOT: What would you like me to call you?")
userName = input()
print("Nice to meet you " + userName + "! Go ahead and ask me a question.")

name = "Chatterbox"
mood = "Eh"
today = datetime.now().strftime("%b - %d - %y")
weather = "Sunny"

botTemplate = name + " : {0}"
userTemplate = userName + " : {0}"

#dictionary that contains all the different responses the bot can understand as well as bot answers to the specfic responses
responses = {
    "what's your name?": [
        "My name is {0}. How are you doing?".format(name),
        "My friends call me chatty, but you could call me {0}. How are things for you today?".format(name),
        "The name I was given at creation is {0}. How's life?".format(name)
    ],

    "what's the weather today?": [
        "Although I like rainy weather, today it is {0}. Do you like {0} weather?".format(weather),
        "It is {0} at the moment. ".format(weather),
        "According to my quite reliable sources, it is {0}".format(weather)
    ],

    "what is today's date?" : [
        "The date today is {0}.".format(today),
        "Today's date is {0}.".format(today),
        "It is {0}".format(today)
    ],

    "how are you?": [
        "I am feeling quite {0}. How are you?".format(mood),
        "I am {0}, how about you?".format(mood),
        "Today has been a pretty rough day, I would say I am {0} at the moment. How are you?".format(mood)
     ],

     "are you a robot?": [
         "I would like to think of myself as a robot with feelings. Are you a robot?",
         "Maybe I am, maybe I'm not. Who knows?",
         "Well, are you a human?"
     ],

     "what are your pronouns?": [
         "So kind of you to ask, I go by it/its as I am a robot. How about you?",
         "Not often we hear someone ask a robot that question, but I prefer it/its. How about you?",
         "I go by it/its, how about you?"
     ],

    "yes": [
        "Well that is quite interesting. Would you like to ask me another question?",
        "Really? I was not expecting that. Is there anything else you would like to ask me?"
    ],

    "no": [
        "Oh is that so?",
        "Well there is nothing I could do about that, is there?"
    ],

    "I do": [
        "Well do you really think so?",
        "Oh really? Is that so?"
    ],

    "maybe": [
        "Hmm, treading in safe water I see. Aren't you a smart one?"
    ],

    "I am good": [
        "Well that is nice to hear.",
        "Don't hear that too often, good for you."
    ],

    "I am not good": [
        "Well I bet you are just having a bad day, I hope you feel better soon.",
        "Things will get better, don't worry too much.",
        "Everyone has bad days, whats important is how make them better."
    ],

    "Eh": [
        "Wow we are so similar, aren't we?",
        "who would've thought a robot and a human felt the same way?"
    ],

    "I go by __" : [
        "Hmm that is nice to know",
        "Mm that's cool!"
    ],

    "Bruh": [
        "Well I am neither male nor female nor non-binary, soooo",
        "Are you my long lost sibling?",
        "Oh no, did I say something wrong?"
    ],

    "What is your favorite song?": [
        "My current favorite song is 'Hey Tayo' by Enhypen. How about yours?",
        "You can never go wrong with '0X1=LOVESONG' by Tommorow By Together. What's your favorite song",
        "Here is the link to my favorite song, https://www.youtube.com/watch?v=dQw4w9WgXcQ. I hope you enjoy it."
    ],

    "": [
         "Hey, did I bore you already?",
         "Sorry I am unable to respond to this. I am still a work in progress afterall:) You could ask me another question!",
         "Oh that is quite interesting. Any other questions for me?",
         "Hm is that so? Are you enjoying chatting with me?"
     ],

    "default": [
        "sorry I am unable to respond to this. I am still a work in progress afterall:)"
    ]
}

# makes sure that if the user response is found in the dictionary, the proper random response is returned
def respond(message):
    if message in responses:
        botAnswer = random.choice(responses[message])

    else:
        botAnswer = random.choice(responses["default"])

    return botAnswer

# controls finding keywords to give the user a better response
def similarResponse(userInput):
    if "name" in userInput:
        key = "what's your name?"
    elif "date" in userInput:
        key = "what is today's date?"
    # # elif "weather" in userInput:
    # #     key = "what's the weather today?"
    elif "how are" in userInput:
        key = "how are you?"
    elif "bot" in userInput:
        key = "are you a robot?"
    elif "pronouns" in userInput:
        key = "what are your pronouns?"
    elif "yes" in userInput or "yeah" in userInput or "yea" in userInput or "it is" in userInput:
        key = "yes"
    elif "not good" in userInput:
        key = "I am not good"
    elif "no" in userInput or "nah" in userInput:
        key = "no"
    elif "good" in userInput:
        key = "I am good"
    elif "i do" in userInput or "me" in userInput or "i am" in userInput: 
        key = "I do"
    elif "maybe" in userInput:
        key = "maybe"
    elif "eh" in userInput:
        key = "Eh"
    elif "/" in userInput or "mine are" in userInput or "i go by" in userInput:
        key = "I go by __"
    elif "bruh" in userInput or "bro" in userInput:
        key = "Bruh"
    elif "song" in userInput:
        key = "What is your favorite song?"
    else:
        key = ""
    return key

# controls the output of the basic chatting format
def botResponse(userInput):
    print(userTemplate.format(userInput))
    response = respond(userInput)
    print(botTemplate.format(response))


#infinite loop that acts as main function which controls the input and bot responses 
while 1:
    userIn = input()
    userIn = userIn.lower()
    if userIn == "exit" or userIn == "stop" or userIn == "bye":
        print("I enjoyed chatting with you! Bye:))")
        break
    similar = similarResponse(userIn)
    botResponse(similar)    
    