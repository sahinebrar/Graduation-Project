# !/usr/bin/env python3

name = ""
first_message_checker = 1


def handle_client(msg):
    global first_message_checker
    global name
    name = msg
    welcome = 'Merhaba %s! Eger cikmak istersen exit yaz' % msg
    first_message_checker = first_message_checker + 1
    return 4, welcome, msg
