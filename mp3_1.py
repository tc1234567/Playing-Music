from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('tkbutton1')
root.geometry('600x600')


conn = sqlite3.connect('button1.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS buttontable1 (song text, singer text)""");

#create delete function
def delete_song():
    conn = sqlite3.connect('button1.db')
    c = conn.cursor()
    s_delete = input(f"Do you want to delete {song_name.get()}? (y/n)")
    if s_delete == 'y':
        # delete record
        c.execute("DELETE from data WHERE song = song_name.get()")

    elif s_delete == 'n':
        pass
    else:
        print("Sorry Bad Input. \nPlease Verify Your Input")

    conn.commit()
    conn.close()


#create submit function
def submit():
    conn = sqlite3.connect('button1.db')
    c = conn.cursor()
    #insert into tables
    c.execute("INSERT INTO buttontable1 VALUES(:song_name, :singer_name)",
                {
                    'song_name': song_name.get(),
                    'singer_name': singer_name.get()
                }
                )

    conn.commit()
    conn.close()

    #clear the textboxes
    song_name.delete(0, END)
    singer_name.delete(0, END)



#create query function
def query():
    conn = sqlite3.connect('button1.db')
    c = conn.cursor()
    #query the databse
    c.execute("SELECT *, oid  FROM buttontable1")
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        print_records += str(record) +"\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row = 1, column = 6, columnspan = 2)

    conn.commit()
    conn.close()


#create text boxes
song_name = Entry(root, width = 30)
song_name.grid(row = 0, column = 1, padx = 20)
singer_name = Entry(root, width = 30)
song_name.grid(row = 1, column = 1, pady = 20)

#create text box labels
song_name_label = Label(root, text = "Song")
song_name_label.grid(row = 0, column = 0)
singer_name_label = Label(root, text = "Singer")
singer_name_label.grid(row = 1, column = 0)

#create a submit button
submit_btn = Button(root, text = "Add song to database", command = submit)
submit_btn.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80)

#create a query button
query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80)

#create a delete button
del_btn = Button(root, text="Delete a song", command = delete_song)
del_btn.grid(row=4, columnspan=2, pady = 10, padx = 10, ipadx = 80)


conn.commit()
conn.close()
root.mainloop()
