from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os

#Select the save folder
def save_folder():
    folderSelected1 = filedialog.askdirectory()
    os.chdir(folderSelected1)

#Select the file with the links
def links_file():
    global fileSelected1
    fileSelected1 = filedialog.askopenfilename()

#Download as music function
def download_music(links_file):
    #Running this command on CLI
    os.system(f"clear\
		&& youtube-dl --geo-bypass --yes-playlist \
		      -x --audio-format mp3 -o '%(title)s.%(ext)s' \
	    -a {links_file}")
    messagebox.showinfo('Downloaded','Check your save folder. The process is finished')

#Download as video function
def download_video(links_file):
    os.system(f"clear\
		&& youtube-dl --geo-bypass --yes-playlist \
		-o '%(title)s.%(ext)s' -f best -a {links_file}")
    messagebox.showinfo('Downloaded','Check your save folder. The process is finished')

#Menu function
def menu():

    #Destroys the main window and creates the menu window
    main_window.destroy()
    #lock maximize button
    menu_window = tk.Tk()
    menu_window.resizable(0,0)
    menu_window.title('˖ ˖ ˖   MENU   ˖ ˖ ˖')
    menu_window.geometry('340x250')

    #Version label
    version_window = tk.Label(text = 'Version 1.0',
                              font = 'arial 8',
                              fg = 'grey')
    version_window.place(x = 140,
                         y = 230)

    #Menu buttons with icons
    music_photo = PhotoImage(file = "icons/music_icon.png")
    music_icon = music_photo.subsample(10, 10)
    music_button = tk.Button(text = 'Download as music',
           image = music_icon,
           font='arial 9 bold',
           bd = 1,
           compound = TOP,
           command = lambda:[download_music(fileSelected1)])
    music_button.place(x = 20,
                       y = 20)

    video_photo = PhotoImage(file = "icons/video_icon.png")
    video_icon = video_photo.subsample(10, 11)
    video_button = tk.Button(text = 'Download as video',
           image = video_icon,
           font='arial 9 bold',
           bd = 1,
           compound = TOP,
           command = lambda:[download_video(fileSelected1)])
    video_button.place(x = 180,
                       y = 20)

    links_photo = PhotoImage(file = "icons/file_icon.png")
    links_icon = links_photo.subsample(10, 11)
    links_button = tk.Button(text = 'File with links',
           image = links_icon,
           font='arial 9 bold',
           bd = 1,
           height = 70,
           width = 110,
           compound = TOP,
           command = links_file)
    links_button.place(x = 20,
                       y = 120)

    folder_photo = PhotoImage(file = "icons/folder_icon.png")
    folder_icon = folder_photo.subsample(10, 11)
    folder_button = tk.Button(text = 'Save folder',
           image = folder_icon,
           font='arial 9 bold',
           bd = 1,
           height = 70,
           width = 107,
           compound = TOP,
           command = save_folder)
    folder_button.place(x = 180,
                        y = 120)

    #The mainloop is listining the user events
    menu_window.mainloop()

#Initializing the main window
main_window = tk.Tk()
main_window.resizable(0,0)
main_window.title('˖ ˖ ˖   WELCOME   ˖ ˖ ˖')
main_window.geometry('350x100')

#Version label in the main window
version_window = tk.Label(text = 'Version 1.0',
                          font = 'arial 8',
                          fg = 'grey')
version_window.place(x = 150,
                     y = 85)

#Welcome text in the main window
main_label = tk.Label(text = 'Welcome to the Music and Video Downloader',
                      font='arial 11')
main_label.place(x = 30,
                 y = 15)

#Single button in the main window
main_button = Button(text = "Go to the Menu",
                        font='arial 9 bold',
                        command = menu)
main_button.place(x = 120,
                  y = 45)

#The mainloop is listining the user events
main_window.mainloop()
