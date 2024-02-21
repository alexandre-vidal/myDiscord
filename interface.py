# importing modules
import socket
from tkinter import *
from tkinter import ttk

# client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client.connect(("localhost", 9999))

# done = False

# while not done:
#     client.send(input("Message: ").encode('utf-8'))
#     msg = client.recv(1024).decode('utf-8')
#     if msg == 'quit':
#         done = True
#     else:
#         print(msg)

# reference:

### Label: A widget used to display text in the screen
### Button: A button that can contain text and can perform an action when clicked
### Entry: A text entry widget that allows only a single line of text
### Text: A text entrey widget that allows multiline text entry
### Frame: A rectangular region used to group related widgets or provide padding between widgets

root = Tk()
root.title('Chat')
root.geometry("960x720")
root.iconbitmap("icon.ico")

my_menu = Menu(root)
root.config(menu = my_menu)

add_login_menu = Menu(my_menu)
my_menu.add_cascade(label = "Mon compte", menu = add_login_menu)
add_login_menu.add_command(label = "Se connecter")
add_login_menu.add_command(label = "Paramètres du compte")

add_contact_menu = Menu(my_menu)
my_menu.add_cascade(label = "Contacts", menu = add_contact_menu)
add_contact_menu.add_command(label = "David Hasselhoff")
add_contact_menu.add_command(label = "Arnold Schwarzenegger")
add_contact_menu.add_command(label = "Scarlett Johansson")
add_contact_menu.add_command(label = "Sean Bean")

chatbox = Listbox(root, bg = "black", fg = "green", width = 119, height = 39)
chatbox.place(x = 4, y = 4)

text = Text(root, height = 4)
text.place(x = 5, y = 636)

def message():
    messagetext = text
    message.insert(END, messagetext)

servertext = Label(text="========== Serveurs ==========")
servertext.place(x = 732, y = 0)
server0 = Button(root, text = "Serveur 0", height = 2, width = 13)
server0.place(x = 732, y = 25)
server1 = Button(root, text = "Serveur 1", height = 2, width = 13)
server1.place(x = 844, y = 25)
server2 = Button(root, text = "Serveur 2", height = 2, width = 13)
server2.place(x = 732, y = 75)
server3 = Button(root, text = "Serveur 3", height = 2, width = 13)
server3.place(x = 844, y = 75)
server4 = Button(root, text = "Serveur 4", height = 2, width = 13)
server4.place(x = 732, y = 125)
server5 = Button(root, text = "Serveur 5", height = 2, width = 13)
server5.place(x = 844, y = 125)
server6 = Button(root, text = "Serveur 6", height = 2, width = 13)
server6.place(x = 732, y = 175)
server7 = Button(root, text = "Serveur 7", height = 2, width = 13)
server7.place(x = 844, y = 175)

salontext = Label(text="=========== Salons ===========")
salontext.place(x = 729, y = 370)
salon0 = Button(root, text = "Salon 0", height = 2, width = 13)
salon0.place(x = 732, y = 395)
salon1 = Button(root, text = "Salon 1", height = 2, width = 13)
salon1.place(x = 844, y = 395)
salon2 = Button(root, text = "Salon 2", height = 2, width = 13)
salon2.place(x = 732, y = 445)
salon3 = Button(root, text = "Salon 3", height = 2, width = 13)
salon3.place(x = 844, y = 445)
salon4 = Button(root, text = "Salon 4", height = 2, width = 13)
salon4.place(x = 732, y = 495)
salon5 = Button(root, text = "Salon 5", height = 2, width = 13)
salon5.place(x = 844, y = 495)
salon6 = Button(root, text = "Salon 6", height = 2, width = 13)
salon6.place(x = 732, y = 545)
salon7 = Button(root, text = "Salon 7", height = 2, width = 13)
salon7.place(x = 844, y = 545)

sendphoto = PhotoImage(file = r"images/send.png")

send = Button(root, text = "button", image = sendphoto, command = message)
send.place(x = 658, y = 642)

root.mainloop()