import logging
logging.basicConfig(filename="CorporaToList.log", level=logging.DEBUG)

def convert_corpora_to_list(str):
    try:
        file = open(str, "r")
        words = file.read()
        words = words.split(",")
        return words
    except Exception as e:
        logging.debug(e.strerror)

convert_corpora_to_list()