from tkinter import *
from PIL import ImageTk, Image
import sqlite3

#1st window - main window
root = Tk()
root.title('tkbutton')
root.geometry('600x600')

#establishing connection to database
conn = sqlite3.connect('button.db')
c = conn.cursor()

#textboxes
song1 = Entry(root, width = 30)
song1.grid(row = 1, column = 1, padx = 20)
singer1 = Entry(root, width = 30)
singer1.grid(row = 2, column = 1, pady = 20)

#labels for the textboxes and their dimensions
song1_label = Label(root, text = "Song")
song1_label.grid(row = 1, column = 0)
singer1_label = Label(root, text = "Singer")
singer1_label.grid(row = 2, column = 0)


#class with all functions
class player():
    #intializing function - I think probelm is here - didn't intialize stuff - not sure how
    def __init__(self, newWindow):
        self.newWindow = newWindow


    #adding user input to database
    def submit():
        conn = sqlite3.connect('button.db')
        c = conn.cursor()
        c.execute("INSERT INTO buttontable VALUES(:song1, :singer1)", {'song1': song1.get(),'singer1': singer1.get()})

        conn.commit()
        conn.close()
        #clears textboxes
        # song1.delete(0, END)
        # singer1.delete(0, END)

    #query function - displays playlist in a listbox
    def query():
        conn = sqlite3.connect('button.db')
        c = conn.cursor()
        c.execute("SELECT *, oid  FROM buttontable")
        records = c.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\n"

        print(print_records)#need to change this to Listbox - not sure how

        # query_label = Label(root, text = print_records)
        # query_label.grid(row = 7, column = 2)

        # listbox = Listbox(root, height = 30, width = 30)
        # listbox.grid(row = 7, column = 2)
        # listbox.insert(END, print_records)

        conn.commit()
        conn.close()

    #delete function on main window - opens a new window asking user to enter which song to be deleted
    def delete1():
        conn = sqlite3.connect('button.db')
        c = conn.cursor()
        global newWindow

        global song2 #problem maybe here too - not sure how to use variables from one function in another function
        #think we need to intialize in __init__ function
        #need to use this variable in delete2 fuction
        newWindow = Toplevel(root)#new window - second window
        newWindow.title("Deleting a song")
        newWindow.geometry("300x300")
        Label(newWindow, text ="Which song do you want to delete?").pack()
        song2 = Entry(newWindow, width = 30)#takes user input
        song2.pack()
        song2_label = Label(newWindow, text ="Song: ").pack()

        print(song2.get()) #doesnt work gives empty space

        #write code for - inserting song 2 values in db
        #make connection to db
        #check if song1 == song2 and then delete if yes, move on if no

        Button(newWindow, text ="Delete2", command = player.delete2).pack()#second delete button defined here - again - dont know how to link this to delete2 function

        conn.commit()
        conn.close()

    def delete2():
        conn = sqlite3.connect('button.db')
        c = conn.cursor()
        # c.execute("DELETE from buttontable WHERE song == 'disco'")
        print("Song deleted.")#wrote somthing for time being

        conn.commit()
        conn.close()


    #buttons
    submit_btn = Button(root, text = "Add song to database", command = submit)
    submit_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80)

    query_btn = Button(root, text = "Show records", command = query)
    query_btn.grid(row = 4, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80)

    del1_btn = Button(root, text ="Delete1", command = delete1)
    del1_btn.grid(row = 6, column = 0, columnspan=2, pady = 10, padx = 10, ipadx = 80)

    # listbox = Listbox(root, height = 10, width = 15, bg = "grey", activestyle = 'dotbox', font = "Helvetica", fg = "yellow")

#object for the class
p = player(root)
#commiting changes to databse and closing connection
conn.commit()
conn.close()
#think this should be p.mainloop() - for now this statement runs the tkinter window
root.mainloop()
