#Add song button takes in user input for which song to add to the database from the file directory
#it takes in the input and adds to the db which displays its contents in the playlist
#Delete song deletes the selected song in the playlist
#Play song button plays the selected song in the playlist
#Pause song button pauses the selected song in the playlist


#use __init__ to initialise sqlite connection

import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import pygame

#1st window - main window
root = Tk()
root.title('Music player')
root.geometry('500x500')

pygame.init()
pygame.mixer.init()# initialise pygame

#establishing connection to database
conn = sqlite3.connect('mp3db.db')
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS mp3table (playlist text)""");

# my_frame = Frame(root)
# my_scrollbar = Scrollbar(my_frame, orient = VERTICAL)

# listbox = Listbox(my_frame, height = 20, width = 20, yscrollcommand = my_scrollbar.set)

listbox = Listbox(root, height = 20, width = 20)
listbox.grid(row = 1, column = 3, rowspan = 5)
# # listbox.grid(row = 1, column = 3, rowspan = 5, selectmode=root.SINGLE)

# my_scrollbar.config(command = listbox.yview)
# my_scrollbar.pack(side=RIGHT, fill=Y)
# my_frame.pack()


var = StringVar()
song_title = Label(root, font="Helvetica 12 bold", textvariable=var)
# song_title.pack()
song_title.grid(row = 3, column = 1)

#class with all functions
class player(str):

    def browseFiles():# browsefiles Function for opening the file explorer window
        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()

        filename = filedialog.askopenfilename(initialdir = r"C:\Users\srini\TanviPython", title = "Select a File", filetypes =  (("MP3 File", "*.mp3"),))
        c.execute("INSERT INTO mp3table VALUES(:playlist)", {'playlist': filename})

        listbox.insert(END, filename)
        conn.commit()
        conn.close()


    #query function - displays playlist in a listbox
    def query():
        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()
        c.execute("SELECT *, oid  FROM mp3table")
        records = c.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\n"
            listbox.insert(END, record)

        conn.commit()
        conn.close()



    def deleteSong():#deleteSong function deletes the selected song in the playlist
        # Delete from Listbox
        selection = listbox.curselection()
        listbox.delete(selection[0])

        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()

        # row_id=int(selection[0])
        # print(row_id)
        # c.execute("DELETE FROM mp3table WHERE playlist = ?",(row_id+1,))


        # c.execute("DELETE from mp3table WHERE playlist =?" , (playlist,))
        # print(str(id))
        conn.commit()
        conn.close()


    def playSong():#playSong function plays the selected song in the playlist
        # pygame.mixer.music.load(listbox.get(ACTIVE))
        # var.set(listbox.get(ACTIVE))
        # pygame.mixer.music.play()
        return

    def pauseSong():#pauseSong function pauses the selected song in the playlist
        return


    def deleteAll():
        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()

        c.execute("DELETE from mp3table")

        conn.commit()
        conn.close()


    #defining button properties
    del_btn = Button(root, text ="Delete song", command = deleteSong)
    del_btn.grid(row = 1, column = 2, pady = 5, padx = 5, ipadx = 50)

    add_btn = Button(root, text ="Add song", command = browseFiles)
    add_btn.grid(row = 1, column = 1, pady = 5, padx = 5, ipadx = 50)

    play_btn = Button(root, text ="Play song", command = playSong)
    play_btn.grid(row = 2, column = 1, pady = 5, padx = 5, ipadx = 50)

    pause_btn = Button(root, text ="Pause song", command = pauseSong)
    pause_btn.grid(row = 2, column = 2, pady = 5, padx = 5, ipadx = 50)

    deleteAll = Button(root, text ="Delete All", command = deleteAll)
    deleteAll.grid(row = 3, column = 2, pady = 5, padx = 5, ipadx = 50)

    show_records = Button(root, text ="Show Records", command = query)
    show_records.grid(row = 4, column = 1, pady = 5, padx = 5, ipadx = 50)


#object for the class
p = player(root)
#commiting changes to databse and closing connection
conn.commit()
conn.close()
root.mainloop()
