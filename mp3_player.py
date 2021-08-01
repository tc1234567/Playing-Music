#Add song button takes in user input for which song to add to the database from the file directory
#it takes in the input and adds to the db which displays its contents in the playlist
#Delete song deletes the selected song in the playlist
#Play song button plays the selected song in the playlist
#Pause song button pauses the selected song in the playlist


import os
from tkinter import *
from tkinter import filedialog
import sqlite3
import pygame

#1st window - main window
root = Tk()
root.title('Music player')
root.geometry('500x400')

pygame.init()
pygame.mixer.init()#initialise pygame

#establishing connection to database
conn = sqlite3.connect('mp3db.db')
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS mp3table (playlist text)""");

listbox = Listbox(root, height = 20, width = 80)
listbox.grid(row = 1, column = 5, rowspan = 5)

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
        # print(filename)
        conn.commit()
        conn.close()

    def query():#query function - displays playlist in a listbox

        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()
        c.execute("SELECT playlist FROM mp3table")
        records = c.fetchall()

        print_records = ""
        for record in records:
            print_records += record[0] + "\n"
            listbox.insert(END, record[0])

        conn.commit()
        conn.close()

        newWindow = Toplevel(root)
        newWindow.title("Deleting a song")
        newWindow.geometry("300x100")
        Label(newWindow, text ="Select in the playlist which song you want to \n delete and click on the Delete button.").pack()

    def deleteSong():#deleteSong function deletes the selected song in the playlist
        #Delete from Listbox
        selection1 = str(listbox.curselection())
        select = selection1.split(',')[0]
        select1 = select.split('(')[1]
        select2 = int(select1)+1

        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()

        selected_line = listbox.curselection()
        listbox.delete(selected_line)

        c.execute("DELETE FROM mp3table where rowid = ?", (select2,))

        conn.commit()
        conn.close()

    def playSong():#playSong function plays the selected song in the playlist
        pygame.mixer.music.load(listbox.get(ACTIVE))
        var.set(listbox.get(ACTIVE))
        pygame.mixer.music.play()

    def pauseSong():#pauseSong function pauses the selected song in the playlist
        pygame.mixer.music.stop()
        return

    def deleteAll():#deletes all songs in the playlist
        listbox.delete(0,END)
        conn = sqlite3.connect('mp3db.db')
        c = conn.cursor()

        c.execute("DELETE from mp3table")

        conn.commit()
        conn.close()

    #defining button properties
    del_btn = Button(root, text ="Delete song", command = deleteSong)
    del_btn.grid(row = 1, column = 2, pady = 5, padx = 20, ipadx = 20)

    add_btn = Button(root, text ="Add song", command = browseFiles)
    add_btn.grid(row = 1, column = 1, pady = 5, padx = 20, ipadx = 20)

    play_btn = Button(root, text ="Play song", command = playSong)
    play_btn.grid(row = 2, column = 1, pady = 5, padx = 20, ipadx = 20)

    pause_btn = Button(root, text ="Pause song", command = pauseSong)
    pause_btn.grid(row = 2, column = 2, pady = 5, padx = 20, ipadx = 20)

    deleteAll = Button(root, text ="Delete All", command = deleteAll)
    deleteAll.grid(row = 3, column = 2, pady = 5, padx = 20, ipadx = 20)

    show_records = Button(root, text ="Show Records", command = query)
    show_records.grid(row = 3, column = 1, pady = 5, padx = 20, ipadx = 20)


#object for the class
p = player(root)
#commiting changes to databse and closing connection
conn.commit()
conn.close()
root.mainloop()
