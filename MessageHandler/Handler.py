from fuzzywuzzy import fuzz
from MessageHandler import CorporaToLists as cpr
import random
from webchat import myWebchat

def substringReceivedMessage(str=None):
    return None


def process_the_message(msg):
    global matched
    matched = False
    while True:
        word_list = cpr.convert_corpora_to_list("/Users/ebrarsahin/GitHub/Graduation-Project/Corpora/WelcomeMessages")
        for i in word_list:
            print(str(fuzz.partial_ratio(i, msg)))
            if fuzz.partial_ratio(i, msg) >= 70:
                matched = True
                return "chatbot: " + (random.choice(cpr.convert_corpora_to_list("/Users/ebrarsahin/GitHub/Graduation-Project/Corpora/WelcomeMessagesAnswers"))).format(myWebchat.name)
                break
        if matched is False:
            return "chatbot: " + "ne dediğinizi anlayamadım."
