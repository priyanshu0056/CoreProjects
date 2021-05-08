# pylint: disable=unused-wildcard-import,method-hidden,anomalous-backslash-in-string
# pylint: disable=assignment-from-no-return
#pylint: enable=too-many-lines
#pylint: disable=unused-variable
#pylint: disable=no-member
# ************************* IMPORTING MODULES ****************************
import tkinter.messagebox as msg
import tkinter.filedialog as fd
from PIL import ImageTk as ITk
from PIL import Image as MyImage
from tkinter import ttk, font
from pytube import YouTube
from tkinter import *
from multiprocessing import freeze_support
import PyPDF2 as pyp2
import math as m
import pyttsx3
from pyttsx3.drivers import sapi5
import webbrowser as wb
import pygame
import string
import random
import sys
import time
import os

# **************************** MAIN WINDOW ********************************
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
PyVault = Tk()
PyVault.geometry('620x650')
PyVault.resizable(False, False)
PyVault.title('PyVault')
PyVaulticonImg = MyImage.open(resource_path("PyVault logo.jpg"))
PyVaulticon = ITk.PhotoImage(PyVaulticonImg)
PyVault.iconphoto(False, PyVaulticon)




# ***************** Global Variable Deceleration *******************
passlenvalue = StringVar()
LowerC = StringVar()
UpperC = StringVar()
DigitC = StringVar()
SymbolC = StringVar()
enclenvalue = StringVar()
genlenvalue = StringVar()
passencvalue = StringVar()
scvalue = StringVar()
ytdEntryVar = StringVar()
playlist = StringVar()
simplesong = ""
ss = ""
singlesong = None
playlistsong = True
Folder_Name = ""
global TextArea

# ***************** 1.PyVault Password Generator/Encrypter************


def PyVault_Password():
    root = Toplevel(PyVault)
    root.geometry("450x600")
    root.resizable(False, False)
    root.title("Password")
    root.config(background="black")
    PyVault_Pass_iconImg = MyImage.open(resource_path("password logo.jpg"))
    PyVault_Pass_icon = ITk.PhotoImage(PyVault_Pass_iconImg)
    PyVault.iconphoto(True, PyVault_Pass_icon)

    def Generate():
        global passlenvalue
        global genlenvalue
        global LowerC, UpperC, DigitC, SymbolC
        passlen = passlenvalue.get()

        def is_integer(n):
            try:
                float(n)
            except ValueError:
                return False
            else:
                return float(n).is_integer()

        s1 = string.ascii_lowercase

        s2 = string.ascii_uppercase

        s3 = string.digits

        s4 = string.punctuation

        t = is_integer(passlen)
        if t == True:
            z = int(passlen)
            s = []

            lc = LowerC.get()
            if lc == "No":
                s.extend(list(s1))
            uc = UpperC.get()
            if uc == "No":
                s.extend(list(s2))
            dc = DigitC.get()
            if dc == "No":
                s.extend(list(s3))
            sc = SymbolC.get()
            if sc == "No":
                s.extend(list(s4))

            random.shuffle(s)
            a = ("".join(s[0:z]))

            genlenvalue.set(a)
            screen2.update()

        else:
            root.grab_set()
            msg.showerror("Invalid", "Enter a valid digit!!")
            root.grab_release()

    def Encrypt():
        SECURE = (('s', '$'), ('AND', '&'), ('a', '@'), ('o', '0'), ('k', '*'), ('i', '1'),
                  ('S', '^'), ('and', '&'), ('A',
                                             '%'), ('O', '0'), ('K', '/'), ('I', '|'),
                  ('Q', '('), ('H', '#'), ('h', '!'), ('N',
                                                       '<'), ('n', '>'), ('D', '}>'),
                  ('+', 'D'), ('-', 'Q'))

        def securePass(password):
            for a, b in SECURE:
                password = password.replace(a, b)
            return password

        global passencvalue
        global enclenvalue
        password = passencvalue.get()
        passwords = securePass(password)
        enclenvalue.set(passwords)
        encscreen2.update()

    # **********************PASSWORD GENERATOR******************

    mainframe = Frame(root, bg='grey', borderwidth=8, relief=SUNKEN)
    mainframe.pack(fill=X, padx=2, ipady=80, pady=8)

    passgenlabel = Label(mainframe, text="Password Generator",
                         font="Times 22 bold", fg="black", bg='grey').pack()
    passtextlabel = Label(mainframe, text="Password Length", font="Times 17 bold",
                          fg="black", bg="grey").pack(side=TOP, anchor="nw",
                                                      padx=5, pady=20)

    passlenvalue.set("4")
    screen1 = Entry(mainframe, textvar=passlenvalue, font="lucida 12",
                    bg="white", fg="black", relief=SUNKEN, borderwidth=8)
    screen1.place(x=220, y=60)

    genbutton = Button(mainframe, text="Generate", font="Times 15 bold italic",
                       fg="white", bg="black", relief=SUNKEN, borderwidth=8, command=Generate)
    genbutton.place(x=135, y=155)

    gentextlabel = Label(mainframe, text="Generated Password", font="Times 15 bold",
                         fg="green", bg="grey").place(x=3, y=220)

    genlenvalue.set("")
    screen2 = Entry(mainframe, textvar=genlenvalue, font="lucida 12",
                    bg="white", fg="black", relief=SUNKEN, borderwidth=8)
    screen2.place(x=220, y=220)

    LowerC.set("Yes")
    UpperC.set("Yes")
    DigitC.set("Yes")
    SymbolC.set("Yes")

    Lowercheck = Checkbutton(root, text="Lower", variable=LowerC,
                             onvalue='No', offvalue='Yes', font=8, bg="grey")
    Lowercheck.place(x=30, y=125)

    Uppercheck = Checkbutton(root, text="Upper", variable=UpperC,
                             onvalue='No', offvalue='Yes', font=8, bg="grey")
    Uppercheck.place(x=125, y=125)

    Digitcheck = Checkbutton(root, text="Digit", variable=DigitC,
                             onvalue='No', offvalue='Yes', font=8, bg="grey")
    Digitcheck.place(x=218, y=125)

    Symbolcheck = Checkbutton(root, text="Symbol", variable=SymbolC,
                              onvalue='No', offvalue='Yes', font=8, bg="grey")
    Symbolcheck.place(x=298, y=125)

    # **********************PASSWORD ENCRYPTER******************

    mainframe2 = Frame(root, bg='grey', borderwidth=8, relief=SUNKEN)
    mainframe2.pack(fill=X, padx=2, ipady=78, pady=5, anchor="sw")

    passenclabel = Label(mainframe2, text="Password Encrypter",
                         font="Times 22 bold", fg="black", bg='grey').pack()
    passtextlabel2 = Label(mainframe2, text="Original Password", font="Times 17 bold",
                           fg="black", bg="grey").pack(side=TOP, anchor="nw",
                                                       padx=5, pady=20)

    passencvalue.set("")
    encscreen1 = Entry(mainframe2, textvar=passencvalue, font="lucida 12",
                       bg="white", fg="black", relief=SUNKEN, borderwidth=8)
    encscreen1.place(x=220, y=60)

    encbutton = Button(mainframe2, text="Encrypt", font="Times 18 bold italic",
                       fg="white", bg="black", relief=SUNKEN, borderwidth=8, command=Encrypt)
    encbutton.place(x=135, y=115)

    enctextlabel = Label(mainframe2, text="Encrypted Password", font="Times 15 bold",
                         fg="green", bg="grey").place(x=3, y=190)

    enclenvalue.set("")
    encscreen2 = Entry(mainframe2, textvar=enclenvalue, font="lucida 12",
                       bg="white", fg="black", relief=SUNKEN, borderwidth=8)
    encscreen2.place(x=220, y=190)

    root.mainloop()

# ************************ 2.PyVault NotePad **************************


def PyVault_Notepad():
    root = Toplevel(PyVault)
    root.title('Notepad')
    root.minsize(600, 550)
    PyVault_NotePad_iconImg = MyImage.open(resource_path("notepad logo.jpg"))
    PyVault_NotePad_icon = ITk.PhotoImage(PyVault_NotePad_iconImg)
    PyVault.iconphoto(True, PyVault_NotePad_icon)

    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    def Algerian():
        global TextArea
        TextArea.config(font="Algerian")

    def Arial():
        global TextArea
        TextArea.config(font="Arial")

    def Courier():
        global TextArea
        TextArea.config(font="Courier")

    def Cambria():
        global TextArea
        TextArea.config(font="Cambria")

    def Times():
        global TextArea
        TextArea.config(font="Times")

    def Roman():
        global TextArea
        TextArea.config(font="Roman")

    def Lucida():
        global TextArea
        TextArea.config(font="lucida")

    def boldDoc():
        global TextArea
        TextArea.config(font="Arial 14 bold")

    def italicDoc():
        global TextArea
        TextArea.config(font="Arial 14 italic")

    def NewFile():
        global file
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0, END)

    def openFile():
        root.grab_set()
        global file
        file = fd.askopenfilename(defaultextension=".txt",
                                  filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            root.title(os.path.basename(file)+" - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()
        root.grab_release()

    def saveFile():
        root.grab_set()
        global file
        a = msg.askyesnocancel("Save ?", "Do you want to Save this File")
        if a == True:
            if file == None:
                file = fd.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

                if file == "":
                    file = None
                else:
                    f = open(file, "w")
                    f.write(TextArea.get(1.0, END))
                    f.close()

                    root.title(os.path.basename(file) + " - Notepad")

            else:
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()
        elif a == False:
            a = msg.askquestion("Work Unsaved", "Do you want to Continue ?")
            if a == "yes":
                root.destroy()
            else:
                return None
        else:
            return None
        root.grab_release()

    def quitApp():
        root.grab_set()
        a = msg.askquestion("Work Unsaved", "Do you want to Continue ?")
        if a == "yes":
            root.destroy()
        else:
            return None
        root.grab_release()

    def cut():
        TextArea.event_generate(("<<Cut>>"))

    def copy():
        TextArea.event_generate(("<<Copy>>"))

    def paste():
        TextArea.event_generate(("<<Paste>>"))

    def selectall():
        TextArea.event_generate(("<<SelectAll>>"))

    def About():
        root.grab_set()
        msg.showinfo("Notepad", "This NotePad is a Part of PyVault Software."
                     "It provides the user a space to Save,Format,Edit notes in txt format.\nThanks For Using")
        root.grab_release()
    global TextArea
    TextArea = Text(root, font="lucida 14")
    file = None
    TextArea.pack(padx=5, expand=True, fill=BOTH)
    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label="New", command=NewFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_command(label="Select All", command=selectall)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    Format = Menu(MenuBar, tearoff=0)
    FontMenu = Menu(Format, tearoff=0)
    FontMenu.add_command(label="Algerian", command=Algerian)
    FontMenu.add_command(label="Arial", command=Arial)
    FontMenu.add_command(label="Courier", command=Courier)
    FontMenu.add_command(label="Cambria", command=Cambria)
    FontMenu.add_command(label="Times", command=Times)
    FontMenu.add_command(label="Roman", command=Roman)
    FontMenu.add_command(label="Lucida", command=Lucida)
    Format.add_cascade(label="Fonts", menu=FontMenu)

    FontStyle = Menu(Format, tearoff=0)
    FontStyle.add_command(label="Bold", command=boldDoc)
    FontStyle.add_command(label="Italic", command=italicDoc)
    Format.add_cascade(label="Font Styles", menu=FontStyle)

    MenuBar.add_cascade(label="Format", menu=Format)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=About)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    VScroll = Scrollbar(TextArea, orient='vertical', cursor='arrow')
    VScroll.pack(side=RIGHT, fill=Y)
    VScroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=VScroll.set)

    HScroll = Scrollbar(TextArea, orient='horizontal', cursor='arrow')
    HScroll.pack(side=BOTTOM, fill=X)
    HScroll.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=HScroll.set)

    root.mainloop()

# *********************** 3.PyVault Calculator *************************


def PyVault_Calculator():
    root = Toplevel(PyVault)
    root.title('Calculator')
    root.maxsize(400, 500)
    root.minsize(300, 425)
    root.configure(background="dark grey")
    PyVault_Calc_iconImg = MyImage.open(resource_path("calculator logo.jpg"))
    PyVault_Calc_icon = ITk.PhotoImage(PyVault_Calc_iconImg)
    PyVault.iconphoto(True, PyVault_Calc_icon)

    def Simple(event):
        global scvalue
        text = event.widget.cget("text")
        if text == "=":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                try:
                    value = eval(screen.get())
                except Exception:
                    value = "Error"

            scvalue.set(value)
            screen.update()
        else:
            scvalue.set(scvalue.get()+text)

    def Scientific(event):
        key = event.widget
        text = key['text']
        no = scvalue.get()
        no = no.replace('(', '')
        no = no.replace(')', '')
        result = ''
        if text == 'deg':
            result = str(m.degrees(float(no)))
        if text == 'mod':
            result = str(m.modf(float(no)))
        if text == 'sin':
            result = str(m.sin(float(no)))
        if text == 'cos':
            result = str(m.cos(float(no)))
        if text == 'tan':
            result = str(m.tan(float(no)))
        if text == 'lg':
            try:
                result = str(m.log10(float(no)))
            except:
                result = "Error"
                scvalue.set(result)
                screen.update()
                raise ValueError(result)

        if text == 'ln':
            try:
                result = str(m.log(float(no)))
            except:
                result = "Error"
                scvalue.set(result)
                screen.update()
                raise ValueError(result)

        if text == 'Sqrt':
            try:
                result = str(m.sqrt(float(no)))
            except:
                result = "Error"
                scvalue.set(result)
                screen.update()
                raise ValueError(result)

        if text == '1/x':
            result = str(1/(float(no)))
        if text == 'pi':
            if no == "":
                result = str(m.pi)
            else:
                result = str(float(no)*m.pi)
        if text == 'e':
            if no == "":
                result = str(m.e)
            else:
                result = str(m.e**float(no))
        if text == 'x^2':
            result = str(m.pow(float(no), 2))
        screen.delete(0, END)
        screen.insert(0, result)

    def Clear(event):
        screen.delete(0, END)
        return

    def Bksp(event):
        current = screen.get()
        length = len(current)-1
        screen.delete(length, END)

    scvalue.set("")
    screen = Entry(root, textvar=scvalue, font="lucida 22",
                   bg="black", fg="white", relief=SUNKEN, borderwidth=10)
    screen.pack(fill=X, ipadx=15, ipady=3, padx=10, pady=10)
    f = Frame(root, bg="grey")
    SimpleKeys = ['7', '8', '9', '4', '5', '6',
                  '1', '2', '3', '+', '0', '-', '/', '*', '%']
    SimpleCount = 0
    ScientficCount = 0
    for r in range(5):
        for c in range(3):
            b = Button(f, width=3, height=1, text=str(
                SimpleKeys[SimpleCount]), font="Times 15 bold italic", relief=RAISED, borderwidth=5)
            b.grid(row=r, column=c, padx=2, pady=2)
            b.bind("<Button-1>", Simple)
            SimpleCount += 1
        f.pack()

    ScientificKeys = ['tan', 'sin', 'cos', 'mod', 'deg', 'ln',
                      'Sqrt', 'pi', '1/x', '(', ')', '.', 'x^2', 'lg', 'e']
    for r in range(5):
        for c in range(4, 7):
            b = Button(f, width=3, height=1, text=str(
                ScientificKeys[ScientficCount]), font="Times 15 bold italic", relief=RAISED, borderwidth=5)
            b.grid(row=r, column=c, padx=2, pady=2)
            if ScientificKeys[ScientficCount] == '(':
                b.bind("<Button-1>", Simple)
            elif ScientificKeys[ScientficCount] == ')':
                b.bind("<Button-1>", Simple)
            elif ScientificKeys[ScientficCount] == '.':
                b.bind("<Button-1>", Simple)
            else:
                b.bind("<Button-1>", Scientific)
            ScientficCount += 1
        f.pack()

    b = Button(f, width=3, height=1, text='Bksp',
               font="Times 15 bold italic", relief=RAISED, borderwidth=5)
    b.grid(columnspan=2, row=6, column=0, ipadx=30, pady=2)
    b.bind("<Button-1>", Bksp)
    f.pack()

    b = Button(f, width=3, height=1, text='AC',
               font="Times 15 bold italic", relief=RAISED, borderwidth=5)
    b.grid(columnspan=3, row=6, column=2, ipadx=30, pady=2)
    b.bind("<Button-1>", Clear)
    f.pack()

    b = Button(f, width=3, height=1, text='=',
               font="Times 15 bold italic", relief=RAISED, borderwidth=5)
    b.grid(columnspan=3, row=6, column=5, ipadx=30, pady=2)
    b.bind("<Button-1>", Simple)
    f.pack()

    root.mainloop()

# **************************** 4.PyVault PDF ******************************


def PyVault_PDF():
    root = Toplevel(PyVault)
    root.geometry('600x500')
    root.resizable(False, False)
    root.title('PDF EXTRACTOR')
    PyVault_PDF_iconImg = MyImage.open(resource_path("pdf logo.jpg"))
    PyVault_PDF_icon = ITk.PhotoImage(PyVault_PDF_iconImg)
    PyVault.iconphoto(True, PyVault_PDF_icon)
    File_Name = ""
    pfile = ""

    def openpdf():
        root.grab_set()
        global File_Name
        File_Name = fd.askopenfilename(initialdir="C:/gui/",
                                       defaultextension=".pdf",
                                       filetypes=[("All Files", "*.*"), ("PDF Files", "*.pdf")])

        if File_Name:
            pfile = os.path.basename(File_Name)
            pdfLabel.config(text=pfile)

        else:
            File_Name = None
            pdfLabel.config(text="Please Select a File", fg="green",
                            font="Times 15 italic bold")
        root.grab_release()

    def extract_text():
        global File_Name
        if File_Name:
            mainfile = pyp2.PdfFileReader(File_Name)
            page = mainfile.getPage(0)
            pagetext = page.extractText()
            pdftext.delete(1.0, END)
            pdftext.insert(1.0, pagetext)
        else:
            return None

    def extract_audio():
        global File_Name
        if File_Name:
            mainfile = pyp2.PdfFileReader(File_Name)
            pages = mainfile.numPages
            engine = pyttsx3.init()
            for num in range(0, pages):
                page = mainfile.getPage(num)
                pagetext = page.extractText()
                engine.say(pagetext)
                engine.runAndWait()
            engine.stop()

        else:
            engine = pyttsx3.init()
            engine.say("PDF Error")
            engine.runAndWait()
    
    def PDF_quit():
        root.destroy()
    
    def cut():
        pdftext.event_generate(("<<Cut>>"))

    def copy():
        pdftext.event_generate(("<<Copy>>"))

    def paste():
        pdftext.event_generate(("<<Paste>>"))

    def selectall():
        pdftext.event_generate(("<<SelectAll>>"))

    def About():
        root.grab_set()
        msg.showinfo("PDF Reader", "This PDF Extractor is a Part of PyVault Software."
                     "It allows the user to extract pdf in Text and Audio Output Format and gives Editing Features.\nThanks For Using")
        root.grab_release()

    pdfl = Label(root, text="PDF EXTRACTOR", font="Times 25")
    pdfl.pack()

    pdfbutton = Button(root, text="Upload File", font="Times 12 bold",
                       relief=RIDGE, borderwidth=5, command=openpdf)
    pdfbutton.pack(pady=3)
    pdfLabel = Label(root, text="", fg="green", font="jost 13 bold italic")
    pdfLabel.pack()

    extract_text_button = Button(root, text="Text", font="Times 12 bold",
                                 relief=GROOVE, borderwidth=5, command=extract_text)
    extract_text_button.pack()

    extract_audio_button = Button(root, text="Audio", font="Times 12 bold",
                                  relief=GROOVE, borderwidth=5, command=extract_audio)
    extract_audio_button.pack()

    pdftext = Text(root, fg="black", font="lucida 12",
                   relief=SUNKEN, borderwidth=5)
    pdftext.pack(padx=10, pady=10, expand=True, fill=BOTH)

    MenuBar = Menu(root)
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_command(label="Select All", command=selectall)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    root.config(menu=MenuBar)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=About)
    HelpMenu.add_command(label="Exit", command=PDF_quit)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    VScroll = Scrollbar(pdftext, orient='vertical', cursor='arrow')
    VScroll.pack(side=RIGHT, fill=Y)
    VScroll.config(command=pdftext.yview)
    pdftext.config(yscrollcommand=VScroll.set)
    root.mainloop()

# ************************ 5.PyVault YouTube ************************


def PyVault_YouTube():
    root = Toplevel(PyVault)
    root.title("YouTube Downloader")
    root.geometry('350x400')
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)
    PyVault_YouTube_iconImg = MyImage.open(resource_path("youtube logo.jpg"))
    PyVault_YouTube_icon = ITk.PhotoImage(PyVault_YouTube_iconImg)
    PyVault.iconphoto(True, PyVault_YouTube_icon)

    def openlc():
        root.grab_set()
        global Folder_Name
        Folder_Name = fd.askdirectory()
        if(len(Folder_Name) > 1):
            locationError.config(text=Folder_Name, fg="green")
            return True
        else:
            msg.showerror("Location", "Please Choose a Folder !")
            locationError.config(text="Please Choose a Folder !", fg="red")
            return False
        root.grab_release()

    def download():
        choice = ytdchoices.get()
        url = ytdEntry.get()
        try:
            if(len(url) > 1):
                yt = YouTube(url)
                ytdError.config(text="")
                if(choice == choices[0]):
                    select = yt.streams.filter(
                        progressive=True, resolution="720p").first()
                elif(choice == choices[1]):
                    select = yt.streams.filter(progressive=True).first()
                elif(choice == choices[2]):
                    select = yt.streams.filter(only_audio=True).first()
                else:
                    msg.showwarning("Quality", "Please Choose Quality !")
                    ytdError.config(text="Please Choose Quality !", fg="red")
            vtitle = yt.title
            vlength = yt.length
            vviews = yt.views
            vrating = yt.rating
            root.grab_set()
            a = msg.askquestion(
                "Confirm", f"Do You Want To Download This Video With Info!\nTitle={vtitle}\nLength(seconds)={vlength}\nViews={vviews}\nRating={vrating}")
            if a == "yes":
                select.download(Folder_Name)
                msg.showinfo("Success", "Download Completed")
                ytdError.config(text="Download Completed", fg="blue")
            else:
                return None
            root.grab_release()
        except Exception:
            root.grab_set()
            msg.showerror("Error", "Please Enter Correct URL")
            ytdError.config(text="Please Enter Correct URL", fg="red")
            root.grab_release()

    ytdLabel = Label(root, text="Enter URL Of The Video", font="Times 18 bold")
    ytdLabel.grid()

    ytdEntry = Entry(root, width=45, textvariable=ytdEntryVar)
    ytdEntry.grid()

    ytdError = Label(root, text="", fg="red", font="Times 15 bold italic")
    ytdError.grid()

    saveLabel = Label(root, text="File Location", font="Times 15 bold italic")
    saveLabel.grid()

    saveEntry = Button(root, width=12, bg="dark grey", fg="black", text="Choose Path", font="Roman 15 bold italic",
                       command=openlc)
    saveEntry.grid()

    locationError = Label(root, text="", fg="red", font="jost 15 bold italic")
    locationError.grid()

    ytdQuality = Label(root, text="Select Quality",
                       font="ComicSansMs 15 bold italic")
    ytdQuality.grid()

    choices = ["720p", "360p", "only_audio"]
    ytdchoices = ttk.Combobox(root, values=choices)
    ytdchoices.grid()

    downloadbtn = Button(root, text="Download", width=15, height=2, borderwidth=5, bg="black", fg="cyan",
                         font="lucida 13 bold italic", command=download)
    downloadbtn.place(x=85, y=255)

    InfoLabel = Label(
        root, text="Note:-Stay Connected To Internet\n\tWhile Downloading", font="jost 10 bold")
    InfoLabel.place(x=40, y=355)

    root.mainloop()

# ************************ 6.PyVault Music *****************************


def PyVault_Music():
    root = Toplevel(PyVault)
    root.geometry('680x430')
    root.resizable(False, False)
    root.title('Music Player')
    PyVault_Music_iconImg = MyImage.open(resource_path("music_player logo.jpg"))
    PyVault_Music_icon = ITk.PhotoImage(PyVault_Music_iconImg)
    PyVault.iconphoto(True, PyVault_Music_icon)

    def add_song():
        root.grab_set()
        global simplesong
        global singlesong
        simplesong = fd.askopenfilename(initialdir='audio/', title='Choose A Song',
                                        filetypes=(("mp3 Files", "*.mp3"),))
        song = os.path.basename(simplesong)
        songbox.insert(END, song)
        singlesong = True
        root.grab_release()

    def add_more_song():
        global simplesong
        global playlist
        global playlistsong
        global ss
        try:
            ss = playlistEnter.get()
            s = os.listdir(ss)
            mp3files = list(filter(lambda f: f.endswith('.mp3'), s))
            for simplesong in mp3files:
                song = os.path.basename(simplesong)
                songbox.insert(END, song)
            playlistsong = None
        except Exception:
            msg.showinfo("Path", "Please Enter Correct Path to Playlist")

    def play():
        global simplesong
        global singlesong
        global playlistsong
        if (playlistsong == None):
            song = songbox.get(ACTIVE)
            global ss
            is_song = f'{ss}\{song}'
            pygame.mixer.music.load(is_song)
            pygame.mixer.music.play(loops=0)
        elif(singlesong == True):
            song = songbox.get(ACTIVE)
            songd = f'{simplesong}'
            pygame.mixer.music.load(songd)
            pygame.mixer.music.play(loops=0)
        else:
            return None

    def stop():
        pygame.mixer.music.stop()
        songbox.selection_clear(ACTIVE)

    global paused
    paused = False

    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    def next_song():
        next_one = songbox.curselection()
        next_one = next_one[0]+1
        if (playlistsong == None):
            song = songbox.get(next_one)
            global ss
            is_song = f"{ss}\{song}"
            pygame.mixer.music.load(is_song)
            pygame.mixer.music.play(loops=0)

        elif(singlesong == True):
            song = songbox.get(next_one)
            song = f'{simplesong}'
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
        else:
            return None
        songbox.selection_clear(0, END)
        songbox.activate(next_one)
        songbox.selection_set(next_one, last=None)

    def previous_song():
        next_one = songbox.curselection()
        next_one = next_one[0]-1
        if (playlistsong == None):
            song = songbox.get(next_one)
            global ss
            is_song = f"{ss}\{song}"
            pygame.mixer.music.load(is_song)
            pygame.mixer.music.play(loops=0)
        elif(singlesong == True):
            song = songbox.get(next_one)
            song = f'{simplesong}'
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
        else:
            return None
        songbox.selection_clear(0, END)
        songbox.activate(next_one)
        songbox.selection_set(next_one, last=None)

    def delete_song():
        songbox.delete(ANCHOR)
        pygame.mixer.music.stop()

    def delete_all_songs():
        songbox.delete(0, END)
        pygame.mixer.music.stop()

    def volume(x):
        pygame.mixer.music.set_volume(volume_slider.get())

    pygame.mixer.init()

    playlist_label = Label(root, text="Playlist Path", font="Times 12")
    playlist_label.place(x=12, y=10)
    playlistEnter = Entry(root, textvariable=playlist,
                          width=40, borderwidth=8, relief=RIDGE)
    playlistEnter.place(x=165, y=10)

    songbox = Listbox(root, bg="grey", fg="black", width=60, borderwidth=12,
                      relief=SUNKEN, font="Times 12 bold italic", selectbackground="green")
    songbox.pack(anchor="nw", padx=10, pady=50)

    Playerframe = Frame(root)
    Playerframe.pack()
    MyImage1 = MyImage.open(resource_path("backward.jpg"))
    MyImage2 = MyImage.open(resource_path("forward.jpg"))
    MyImage3 = MyImage.open(resource_path("play_button.jpg"))
    MyImage4 = MyImage.open(resource_path("pause_button.jpg"))
    MyImage5 = MyImage.open(resource_path("stop.jpg"))

    backbtnimg = ITk.PhotoImage(MyImage1)
    fwdbtnimg = ITk.PhotoImage(MyImage2)
    playbtnimg = ITk.PhotoImage(MyImage3)
    pausebtnimg = ITk.PhotoImage(MyImage4)
    stopbtnimg = ITk.PhotoImage(MyImage5)

    back_button = Button(Playerframe, image=backbtnimg,
                         borderwidth=0, command=previous_song)
    fwd_button = Button(Playerframe, image=fwdbtnimg,
                        borderwidth=0, command=next_song)
    play_button = Button(Playerframe, image=playbtnimg,
                         borderwidth=0, command=play)
    pause_button = Button(Playerframe, image=pausebtnimg,
                          borderwidth=0, command=lambda: pause(paused))
    stop_button = Button(Playerframe, image=stopbtnimg,
                         borderwidth=0, command=stop)

    back_button.grid(row=0, column=0, padx=10)
    pause_button.grid(row=0, column=1, padx=10)
    play_button.grid(row=0, column=2, padx=10)
    stop_button.grid(row=0, column=3, padx=10)
    fwd_button.grid(row=0, column=4, padx=10)

    menubar = Menu(root)
    root.config(menu=menubar)

    add_song_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Add Songs", menu=add_song_menu)
    add_song_menu.add_command(label="Add Song", command=add_song)
    add_song_menu.add_command(label="Add Playlist", command=add_more_song)

    remove_song_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Remove Songs", menu=remove_song_menu)
    remove_song_menu.add_command(label="Delete A Song", command=delete_song)
    remove_song_menu.add_command(
        label="Delete All Song", command=delete_all_songs)

    volume_frame = LabelFrame(root, text="Volume", font="Times 13 bold")
    volume_frame.place(x=585, y=38)

    volume_slider = ttk.Scale(volume_frame, from_=1, to=0,
                              orient=VERTICAL, value=1, command=volume, length=125)
    volume_slider.pack(ipady=15, pady=35)

    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)

    root.mainloop()

# ************************ PyVault Window ***********************


def AboutPyVault():
    PyVault.grab_set()
    msg.showinfo("About", "PyVault is a Python based Application that allows the user "
                 "to intereact with different Applications at a same place to save "
                 "users precious Time.All Copyrights are Reserved and Maintain by Developer - Priyanshu Sharma\nThanks for Using .\nDeveloper Info = https://bit.ly/3h2zaX0")
    PyVault.grab_release()

def PyVault_exit():
    PyVault.destroy()

def github():
    url = "https://bit.ly/335KlpI"
    wb.open(url)


def linkedin():
    url = "https://bit.ly/3h2zaX0"
    wb.open(url)


def gmail():
    PyVault.grab_set()
    msg.showinfo("Contact", "Email us at priyanshu.sha56@gmail.com")
    PyVault.grab_release()


def donate():
    PyVault.grab_set()
    msg.showinfo("Donate", "For Donation mail us at priyanshu.sha56@gmail.com")
    PyVault.grab_release()

if __name__ == '__main__':
    freeze_support()
    topbar = Menu(PyVault)
    baritems1 = Menu(topbar, tearoff=0)
    baritems1.add_command(label="Github", command=github)
    baritems1.add_separator()
    baritems1.add_command(label="Gmail", command=gmail)
    topbar.add_cascade(label="Report Bug", menu=baritems1)
    baritems2 = Menu(topbar, tearoff=0)
    baritems2.add_command(label="Mail Us", command=gmail)
    baritems2.add_separator()
    baritems2.add_command(label="Linkedin", command=linkedin)
    topbar.add_cascade(label="Contact", menu=baritems2)
    baritems3 = Menu(topbar, tearoff=0)
    baritems3.add_command(label="About", command=AboutPyVault)
    baritems3.add_command(label="Exit", command=PyVault_exit)
    topbar.add_cascade(label="Help", menu=baritems3)
    baritems4 = Menu(topbar, tearoff=0)
    topbar.add_cascade(label="Donate", command=donate)
    PyVault.config(menu=topbar)
    canvas_width = 640
    canvas_height = 600
    canavs_img = MyImage.open(resource_path("pyvaultbgimg.jpg"))
    canvas_resized = canavs_img.resize((650, 650), MyImage.ANTIALIAS)
    canimg = ITk.PhotoImage(canvas_resized)
    my_canvas = Canvas(PyVault, width=canvas_width, height=canvas_height)
    my_canvas.pack(expand=True, fill=BOTH)
    my_canvas.create_image(0, 0, image=canimg, anchor="nw")
    # ********************* Simple Button ********************************
    password_button = Button(PyVault, text="Password\nGenerator-Encrypter", height=2, width=18, bg='DarkOliveGreen3',
                             font="Times 12", relief=RAISED, borderwidth=8, command=PyVault_Password)
    notepad_button = Button(PyVault, text="NotePad", height=2, width=18, bg='DarkOliveGreen3',
                            font="Times 12", relief=RAISED, borderwidth=8, command=PyVault_Notepad)
    SciCalc_button = Button(PyVault, text="Scientific\nCalculator", height=2, width=18, bg='DarkOliveGreen3',
                            font="Times 12", relief=RAISED, borderwidth=8, command=PyVault_Calculator)
    ytdownloader_button = Button(PyVault, text="YouTube Video\nDownloader", height=2, width=18, bg='DarkOliveGreen3',
                                 font="Times 12", relief=RAISED, borderwidth=8, command=PyVault_YouTube)
    pdf_button = Button(PyVault, text="PDF\nExtractor", height=2, width=18, bg='DarkOliveGreen3',
                        font="Times 12", relief=RAISED, borderwidth=8, command=PyVault_PDF)
    music_button = Button(PyVault, text="Music\nPlayer", height=2, width=18, bg='DarkOliveGreen3',
                          font="Times 12", relief=RAISED, borderwidth=8, command=PyVault_Music)
    # *********************** Image Button ********************************
    PasswordImg = MyImage.open(resource_path("password logo.jpg"))
    passresized = PasswordImg.resize((150, 150), MyImage.ANTIALIAS)
    passimg = ITk.PhotoImage(passresized)
    pass_img_btn = Button(PyVault, image=passimg, borderwidth=5,
                          relief=SUNKEN, bg='DarkOliveGreen3', command=PyVault_Password)
    NotepadImg = MyImage.open(resource_path("notepad logo.jpg"))
    noteresized = NotepadImg.resize((150, 150), MyImage.ANTIALIAS)
    noteimg = ITk.PhotoImage(noteresized)
    note_img_btn = Button(PyVault, image=noteimg, borderwidth=5,
                          relief=SUNKEN, bg='DarkOliveGreen3', command=PyVault_Notepad)
    SciCalcImg = MyImage.open(resource_path("calculator logo.jpg"))
    calcresized = SciCalcImg.resize((150, 150), MyImage.ANTIALIAS)
    calcimg = ITk.PhotoImage(calcresized)
    calc_img_btn = Button(PyVault, image=calcimg, borderwidth=5,
                          relief=SUNKEN, bg='DarkOliveGreen3', command=PyVault_Calculator)
    YoutubeImg = MyImage.open(resource_path("youtube logo.jpg"))
    ytresized = YoutubeImg.resize((150, 150), MyImage.ANTIALIAS)
    ytimg = ITk.PhotoImage(ytresized)
    yt_img_btn = Button(PyVault, image=ytimg, borderwidth=5,
                        relief=SUNKEN, bg='DarkOliveGreen3', command=PyVault_YouTube)
    pdfImg = MyImage.open(resource_path("pdf logo.jpg"))
    pdfresized = pdfImg.resize((150, 150), MyImage.ANTIALIAS)
    pdfimg = ITk.PhotoImage(pdfresized)
    pdf_img_btn = Button(PyVault, image=pdfimg, borderwidth=5,
                         relief=SUNKEN, bg='DarkOliveGreen3', command=PyVault_PDF)
    musicImg = MyImage.open(resource_path("music_player logo.jpg"))
    musicresized = musicImg.resize((150, 150), MyImage.ANTIALIAS)
    musicimg = ITk.PhotoImage(musicresized)
    music_img_btn = Button(PyVault, image=musicimg, borderwidth=5,
                           relief=SUNKEN, bg='DarkOliveGreen3', command=PyVault_Music)
    # ********************* Button Placing **************************
    pass_btn_canvas = my_canvas.create_window(
        10, 310, anchor="nw", window=password_button)
    notepad_btn_canvas = my_canvas.create_window(
        220, 310, anchor="nw", window=notepad_button)
    sciCalc_btn_canvas = my_canvas.create_window(
        430, 310, anchor="nw", window=SciCalc_button)
    yt_btn_canvas = my_canvas.create_window(
        10, 560, anchor="nw", window=ytdownloader_button)
    pdf_btn_canvas = my_canvas.create_window(
        220, 560, anchor="nw", window=pdf_button)
    music_btn_canvas = my_canvas.create_window(
        430, 560, anchor="nw", window=music_button)
    pass_img_btn_canvas = my_canvas.create_window(
        20, 150, anchor="nw", window=pass_img_btn)
    note_img_btn_canvas = my_canvas.create_window(
        230, 150, anchor="nw", window=note_img_btn)
    calc_img_btn_canvas = my_canvas.create_window(
        440, 150, anchor="nw", window=calc_img_btn)
    yt_img_btn_canvas = my_canvas.create_window(
        20, 400, anchor="nw", window=yt_img_btn)
    pdf_img_btn_canvas = my_canvas.create_window(
        230, 400, anchor="nw", window=pdf_img_btn)
    music_img_btn_canvas = my_canvas.create_window(
        440, 400, anchor="nw", window=music_img_btn)
    # ********************** Other Applications ***********************
    time1 = ''
    def tick():
        global time1
        time2 = time.strftime('%I:%M:%S %p')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)
    def todaydate():
        date = time.strftime('%D,%a')
        dailydate.config(text=date)
    clock = Label(PyVault, font=('Roman', 18, 'bold'),
                  bg='grey22', fg='green2')
    clock.pack(fill=BOTH, expand=1)
    dailydate = Label(PyVault, font=('Newmanns', 20, 'bold'),
                      bg='firebrick3', fg='goldenrod1')
    dailydate.pack(fill=BOTH, expand=1)
    clock_canvas = my_canvas.create_window(480, 10, anchor="nw", window=clock)
    dailydate_canvas = my_canvas.create_window(
        10, 10, anchor="nw", window=dailydate)
    tick()
    todaydate()
    PyVaultImg = MyImage.open(resource_path("PyVault logo.jpg"))
    PyVaultresized = PyVaultImg.resize((100, 120), MyImage.ANTIALIAS)
    PyVaultimg = ITk.PhotoImage(PyVaultresized)
    PyVault_img_btn = Label(PyVault, image=PyVaultimg,
                            borderwidth=5, bg='magenta4')
    PyVault_img_canvas = my_canvas.create_window(
        260, 10, anchor="nw", window=PyVault_img_btn)
    PyVault.mainloop()
# ************************ --x--END--x-- *********************