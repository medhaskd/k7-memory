import tkinter
from tkinter import *
from tkinter import messagebox
import random
import sqlite3 as lite
import sys
import cv2
from PIL import ImageTk, Image
def j():
    conn = lite.connect('User1233.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS User123(JumbleWords TEXT)")
        cur.execute("INSERT INTO User123 VALUES ('Computer')")
        cur.execute("INSERT INTO User123 VALUES ('Education')")
        cur.execute("INSERT INTO User123 VALUES ('Programming')")
        cur.execute("INSERT INTO User123 VALUES ('Electricity')")
        cur.execute("INSERT INTO User123 VALUES ('Creativity')")

    conn = lite.connect('User1233.db')
    # Fetching Data from the Database
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM User123 ")
        db = cur.fetchall()

    print(db)


    def save():
        global words

        # Adding Data to the Database
        s1 = str(a1.get())
        print(s1)
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO User123 VALUES(?)', (s1,))
        a1.delete(0, END)
        messagebox.showinfo("Success", "New Word Successfully Added..!!")

    # function for choosing random word.
    def choose():
        global pick, words, rows
        global db1
        # choice() method randomly choose
        # any word from the list.
        with conn:
            cur.execute("SELECT * FROM User123 ")
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
            messagebox.showinfo("Congralutions", "This is the correct Answer. ")
            reset()
        else:
            messagebox.showerror("Oops", "This is not the correct Answer.")


    root = tkinter.Tk()
    root.geometry("1300x1000")
    root.title("JumbledWords")
    root.configure(background="#444444")

    lbl = Label(
        root,
        text="You're here",
        font=("courier", 28),
        bg="#444444",
        fg="#E5B700",
    )
    lbl.pack(pady=30, ipady=10, ipadx=10)

    ans1 = StringVar()
    e1 = Entry(
        root,
        font=("courier", 16),
        textvariable=ans1,
    )
    e1.pack(ipady=5, ipadx=5)

    btncheck = Button(
        root,
        text="Check",
        font=("courier", 24),
        width=16,
        bg="black",
        fg="green",
        relief=GROOVE,
        command=checkans,

    )
    btncheck.pack(pady=40)

    btnreset = Button(
        root,
        text="Reset",
        font=("courier", 24),
        width=16,
        bg="black",
        fg="red",
        relief=GROOVE,
        command=reset,

    )
    btnreset.pack()

    lbl2 = Label(
        root,
        text="Add New Words",
        font=("courier", 28),
        bg="#444444",
        fg="#00E590",
    )
    lbl2.pack(pady=30, ipady=10, ipadx=10)

    ans1 = StringVar()

    a1 = Entry(
        root,
        font=("courier", 16),
        textvariable=ans1,
    )

    a1.pack(ipady=5, ipadx=5)

    save1 = Button(
        root,
        text="Add",
        font=("courier", 24),
        width=6,
        bg="black",
        fg="green",
        relief=GROOVE,
        command=save,

    )
    save1.pack(pady=40)


    default()

    root.mainloop()
def fun_window():
        def cam_1():
            import cv2

            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")

            img_counter = 0

            while True:
                ret, frame = cam.read()
                cv2.imshow("test", frame)
                if not ret:
                    break
                k = cv2.waitKey(1)

                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()

            cv2.destroyAllWindows()

        def cam_2():
            import cv2
            import numpy as np
            cap = cv2.VideoCapture(0)
            if (cap.isOpened()):
                print("WebCam Opened")
                while (cv2.waitKey(3) != ord('q')):
                    ret, frame = cap.read()
                    # canny method fro edges detection
                    # arguments: image_array, MinVal, maxVal
                    # above maxVal: sure:edges, belowminVal : non-edges
                    # between maxVal and mimnVal : depends on the connectivity to sure-edges
                    edges = cv2.Canny(frame, 100, 200)
                    cv2.imshow("edges", edges)
            else:
                print("Opening webCam failed")
            cap.release()
            cv2.destroyAllWindows()

        window = tkinter.Tk()
        window.geometry("1000x800")
        window.title("More Activites")
        window.configure(background ="#444444")


        lbl_1 = Label(
            window,
            text="Click the Below Button To TAKE A SELFIE",
            font=("courier", 24),
            bg="#444444",
            fg="#93ED7B",
        )
        lbl_1.pack(pady=40, ipady=10, ipadx=10)
        lbl_2 = Label(
            window,
            text="Hit SPACEBAR to a take photo and ESC to close the camera",
            font=("courier", 20),
            bg="#444444",
            fg="#93ED7B",
        )
        lbl_2.pack(pady=40, ipady=5, ipadx=5)
        btn_cam = Button(
            window,
            text="Open Webcam",
            font=("courier", 24),
            width=20,
            bg="black",
            fg="#27B9E5",
            relief=GROOVE,
            command=cam_1,

        )
        btn_cam.pack(pady=40)

        lbl_4 = Label(
            window,
            text="Click the Below Button To Open a Filter Webcam",
            font=("courier", 24),
            bg="#444444",
            fg="#93ED7B",
        )
        lbl_4.pack(pady=10, ipady=10, ipadx=10)
        lbl_3 = Label(
            window,
            text="Hit 'Q' to close the camera",
            font=("courier", 20),
            bg="#444444",
            fg="#93ED7B",
        )
        lbl_3.pack(pady=40, ipady=5, ipadx=5)

        btn_cam_2 = Button(
            window,
            text="Open Filter Webcam",
            font=("courier", 24),
            width=20,
            bg="black",
            fg="#27B9E5",
            relief=GROOVE,
            command=cam_2,

        )
        btn_cam_2.pack(pady=10)



        window.mainloop()



main_window = tkinter.Tk()
main_window.geometry("1000x800")
main_window.title("More Activites")
main_window.configure(background="#444444")
img = Image.open("G:/PyCharm/Jumbled_Word_Project/FINAL_PROJECT/brain.jpg")
img = img.resize((225, 160), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(main_window, image=img)
panel.image = img
panel.pack()

l_1 = Label(
    main_window,
    text="FOR JUMBLE WORDS GAME",
    font=("courier", 28),
    bg="#444444",
    fg="#E5A927",
)
l_1.pack(pady=30, ipady=10, ipadx=10)
btn_j = Button(
    main_window,
    text="Click Here..!!",
    font=("courier", 24),
    width=25,
    # bg = "#4c4b4b",
    bg="black",
    fg="green",
    relief=GROOVE,
    command=j,

)
btn_j.pack(pady=15)
l_1 = Label(
    main_window,
    text="FOR WEBCAM ",
    font=("courier", 28),
    bg="#444444",
    fg="#E5A927",
)
l_1.pack(pady=30, ipady=10, ipadx=10)
btn_c = Button(
        main_window,
        text="Click Here..!!",
        font=("courier", 24),
        width=25,
        # bg = "#4c4b4b",
        bg="black",
        fg="green",
        relief=GROOVE,
        command=fun_window,

    )
btn_c.pack(pady=15)



main_window.mainloop()