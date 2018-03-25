from fuzzywuzzy import fuzz
from MessageHandler import CorporaToLists as cpr
import random


def substringReceivedMessage(str=None):
    return None


def process_the_message(msg):
    global matched
    matched = False
    word_list = cpr.convert_corpora_to_list()
    for i in word_list:
        print(str(fuzz.partial_ratio(i, msg)))
        if fuzz.partial_ratio(i, msg) >= 70:
            matched = True
            return "chatbot: " + random.choice(word_list)
    if matched is False:
        return "chatbot: " + "ne dediğinizi anlayamadım."
