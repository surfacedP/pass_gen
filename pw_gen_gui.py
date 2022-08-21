import pyperclip
import random
from random import randint
from tkinter import *
from tkinter import ttk


# Globals
word = ""
word_list = []
symbol_list = ["!", "&", "*", "@", "#", "?", "="]
word_length = 8


def create_word_list():
    word_list_file = open("pass_gen_word_list.txt", "r")
    
    for line in word_list_file:
        word_list.append(line)
        
    word_list_file.close()
        
        
def create_password():
    global word
    global word_length
    
    word = random.choice(word_list)
    strip_word = word.rstrip('\n')
    num1 = randint(0, 9)
    num2 = randint(0, 9)
    num3 = randint(0, 9)
    symbol = random.choice(symbol_list)
    password = f"{strip_word}{num1}{num2}{num3}{symbol}"
    
    print(word_length) #debug
    
    return password
    
    
def change_password():
    current_password.set(create_password())
    
    
def copy_password():
    current_password_copy = current_password.get()
    pyperclip.copy(current_password_copy)
    
    
def delete_word():
    global word_list
    
    word_list.remove(word)
    word_list_file = open("pass_gen_word_list.txt", "w")
    word_list_file.write("".join(word_list))
    word_list_file.close()
    
    print(word + "deleted")
    
    
def create_menu(gui):
    global current_password
    global word_length
    

    current_password = StringVar()
    current_password.set(create_password())
    
    current_password_label = Label(gui, textvariable=current_password, font="none 16")
    word_length_scale = Scale(gui, from_=1, to=8, orient=HORIZONTAL)
    change_password_button = Button(gui, text="Change", command=change_password, font="none 12")
    copy_password_button = Button(gui, text="Copy", command=copy_password, font="none 12")
    delete_word_button = Button(gui, text="Delete", command=delete_word, font="none 12")

    #word_length_scale.set(word_length)
    word_length = word_length_scale.get()

    current_password_label.grid(row=0, column=1, pady=11)
    word_length_scale.grid(row=3, column=1, pady=11)
    change_password_button.grid(row=1, column=0, padx=11, pady=11)
    copy_password_button.grid(row=1, column=1, padx=11, pady=11)
    delete_word_button.grid(row=1, column=2, padx=11, pady=11)
    
    root.mainloop()
    
    
    
def create_menubar(gui):
    menubar = Menu(gui)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=print("new"))
    filemenu.add_command(label="Open", command=print("open"))
    filemenu.add_command(label="Save", command=print("save"))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    gui.config(menu=menubar)
    

if __name__ == "__main__":
    root = Tk()
    root.title("PassGen")
    
    create_word_list()
    create_menu(root)
    