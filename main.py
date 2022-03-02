import requests
from urllib import request
import webbrowser
import metadata_parser

def callback(url):
   webbrowser.open_new_tab(url)

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

root = Tk()
root.title("StackOverflow Query")
root.geometry("700x700")

styles = ttk.Style(root)
styles.theme_use('clam')

fonts = tkFont.Font(family="Helvetica",size=36,weight="bold")
font1 = tkFont.Font(family="Helvetica",size=20)
font2 = tkFont.Font(family="Helvetica",size=15)
font3 = tkFont.Font(family="Helvetica",size=10)

canvas = Canvas(root, width=200, height=200)
canvas.pack(side=TOP)
img = PhotoImage(file = "stck.png")
canvas.create_image(20,20,anchor=NW, image=img)

w = Label(root, text='StackOverflow Query', font=fonts, fg="blue")
w.pack()
q = Label(root, text='By Kartik Tiwari', font=font1, pady=10)
q.pack()

e = Entry(root, bd= 6, selectborderwidth=3, font=font2)
e.pack(fill=X)
e.focus_set()
   
frame = Frame(root)
frame.pack()

def printtext():
    for child in frame.winfo_children():
        child.destroy()
    global e
    strings = e.get() 
    responses = requests.get("https://api.stackexchange.com/2.3/similar?order=desc&sort=relevance&title={}&site=stackoverflow".format(strings))    
    data = responses.json()
    for i in range(3):
        title = data['items'][i]['title']
        titlelabel = Label(frame, text=title, font=font2)
        titlelabel.pack()
        links = data['items'][i]['link']
        linklabel = Label(frame, text=links,font=('Helveticabold', 15), fg="blue", cursor="hand2")
        linklabel.pack()
        linklabel.bind("<Button-1>", lambda e:
        callback(links))
        page = metadata_parser.MetadataParser(url=links, search_head_only = True) 
        metas=page.metadata['twitter']['description'] 
        descriptions = Label(frame, text=metas, font=font3, fg="grey")
        descriptions.pack()

b = Button(root,text='SEARCH!',command=printtext, background="green", height=4, width=8, fg="white")
b.pack(side='bottom')

root.mainloop()
