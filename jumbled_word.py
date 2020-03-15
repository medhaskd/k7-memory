import tkinter
from tkinter import *
from tkinter import messagebox
import random
import sqlite3 as lite
import sys

conn = lite.connect('User12.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS User12(JumbleWords TEXT)")
    cur.execute("INSERT INTO User12 VALUES ('Kushagra')")

conn = lite.connect('User12.db')
# Fetching Data from the Database
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM User12 ")
    db = cur.fetchall()

print(db)


def save():
    global words

    # Adding Data to the Database
    s1 = str(a1.get())
    print(s1)
    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO User12 VALUES(?)', (s1,))
    a1.delete(0, END)

    # Fetching Data from the Database

    # for i in words:
    #     print(i)


# list of word
ords = ['rainbow', 'computer', 'science', 'programming',
        'mathematics', 'player', 'condition', 'reverse',
        'water', 'board', 'geeks']


# function for choosing random word.
def choose():
    global pick, words, rows
    global db1
    # choice() method randomly choose
    # any word from the list.
    with conn:
        cur.execute("SELECT * FROM User12 ")
        db1 = cur.fetchall()
    pick = random.choice(db1)
    print(pick)
    print(db1)

    return pick


# Function for shuffling the
# characters of the chosen word.
def jumble(word):
    global random_word, jumbled, pick, words
    global db1
    # sample() method shuffling the characters of the word

    random_word = random.sample(word, len(word))
    print(random_word)

    # join() method join the elements
    # of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)

    return jumbled


def default():
    global words, pick, picked_word, picked_word1, pick1, num, temp
    # choose() function calling to call for the word that has been picked at random
    pick2 = str(choose())
    pick1 = pick2.strip('(')
    pick1 = pick2.strip(')')
    pick1 = pick2.strip("'")
    # print(pick)

    # jumble() function calling to jumble the picked word
    num = len(pick1) - 3
    qn = jumble(pick1[2:num])
    temp = pick1[2:num]
    # print(jumbled)
    xy = str(qn)
    lbl.config(text=xy)


def reset():
    global words, pick, jumbled, picked_word, temp
    # choose() function calling to call for the word that has been picked at random
    # picked_word = str(choose())
    picked_word2 = str(choose())
    pick1_word1 = picked_word2.strip('(')
    pick1_word1 = picked_word2.strip(')')
    pick1_word1 = picked_word2.strip("'")
    print(pick1_word1)
    # jumble() function calling to jumble the picked word
    num2 = len(pick1_word1) - 3
    temp = pick1_word1[2:num2]
    qn = jumble(pick1_word1[2:num2])
    print("temp" + qn)
    xy = str(qn)
    lbl.config(text=xy)
    e1.delete(0, END)
    pass


def checkans():
    global words, answers, num, pick1, jumbled, pick, temp
    var = e1.get()
    if var == temp:
        messagebox.showinfo("Success", "This is the correct Answer. ")
        reset()
    else:
        messagebox.showerror("Error", "This is not the correct Answer.")


root = tkinter.Tk()
root.geometry("550x600+400+300")
root.title("JumbledWords")
root.configure(background="#000000")

lbl = Label(
    root,
    text="You're here",
    font=("Verdana", 28),
    bg="#000000",
    fg="#ffffff",
)
lbl.pack(pady=30, ipady=10, ipadx=10)

ans1 = StringVar()
e1 = Entry(
    root,
    font=("Verdana", 16),
    textvariable=ans1,
)
e1.pack(ipady=5, ipadx=5)

btncheck = Button(
    root,
    text="Check",
    font=("Verdana", 24),
    width=16,
    # bg = "#4c4b4b",
    bg="black",
    fg="green",
    relief=GROOVE,
    command=checkans,

)
btncheck.pack(pady=40)

btnreset = Button(
    root,
    text="Reset",
    font=("Verdana", 24),
    width=16,
    bg="black",
    fg="red",
    relief=GROOVE,
    command=reset,

)
btnreset.pack()

# root = tkinter.Tk()
# root.geometry("550x600+400+300")
# root.title("JumbledWords")
# root.configure(background = "#000000")

# Add To the Database
#
#
#
#


lbl2 = Label(
    root,
    text="Add New Words",
    font=("Verdana", 28),
    bg="#000000",
    fg="#ffffff",
)
lbl2.pack(pady=30, ipady=10, ipadx=10)

ans1 = StringVar()

a1 = Entry(
    root,
    font=("Verdana", 16),
    textvariable=ans1,
)

a1.pack(ipady=5, ipadx=5)

save1 = Button(
    root,
    text="Add",
    font=("Verdana", 24),
    width=16,
    # bg = "#4c4b4b",
    bg="black",
    fg="green",
    relief=GROOVE,
    command=save,

)
save1.pack(pady=40)

default()

root.mainloop()