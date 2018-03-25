import logging

logging.basicConfig(filename="CorporaToList.log", level=logging.DEBUG)


def convert_corpora_to_list(filePath):
    try:
        file = open(filePath, "r")
        words = file.read()
        words = words.split(",")
        return words
    except Exception as e:
        logging.debug(e.strerror)
