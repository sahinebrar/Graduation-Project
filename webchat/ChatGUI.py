#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""

import tkinter
from webchat import myWebchat
from MessageHandler import Handler

index = 2


def send(received_message = ""):
    global index
    index = index + 1
    print(my_msg.get())

    if myWebchat.first_message_checker == 1:
        yerelIndex, tempMessage, real_message = myWebchat.handle_client(my_msg.get())
        msg_list.insert(index, real_message)
        msg_list.insert(yerelIndex, tempMessage)
        index = index + 1
    else:
        msg_list.insert(index, my_msg.get())
        index = index + 1
        msg_list.insert(index, Handler.process_the_message(my_msg.get()))

    my_msg.set("")


top = tkinter.Tk()
top.title("Chatbot")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Mesajınızı buraya yazın.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
msg_list.insert(index, "Lutfen isminizi yazin ve konusmaya baslayin")
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

tkinter.mainloop()  # Starts GUI execution.
