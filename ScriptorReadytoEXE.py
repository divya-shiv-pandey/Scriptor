'''
*
*
*
SCRIPTOR created by Divya Shiv Pandey & Sawan Raj on 16/Sept/2021
Text to Handwriting converter. Enter text and generate hand written PDF document in seconds.
*
*
*
'''

from tkinter import filedialog
from PIL import ImageTk
import PIL.Image
import webbrowser
import random
import re
from fpdf import FPDF
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from tkinter.messagebox import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

bgnum=random.randint(1,4)
img=PIL.Image.open(resource_path("res\\bg%s.jpg")%bgnum)
sizeOfSheet=img.width
x,y=100,160
count = 0
total = 0
tilter=0
allowedchar='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890'



def darkstyle(root):
    ''' Return a dark style to the window'''
    style = ttk.Style(root)
    root.tk.call('source', resource_path('azure dark/azure dark.tcl'))
    style.theme_use('azure')
    style.configure("Accentbutton", foreground='white')
    style.configure("Togglebutton", foreground='white')
    return style

def redefine():
    global bgnum
    global img
    global sizeOfSheet
    global x,y
    global tilter
    global count
    count = 0
    bgnum=random.randint(1,4)
    img=PIL.Image.open(resource_path("res\\bg%s.jpg")%bgnum)
    sizeOfSheet=img.width
    x,y=100,160
    tilter=0
    
def Write(char):
    global x,y
    global tilter
    global img
    
    tilter+=1
    y-=1
    if char=='\n':
        pass
    else:
        char.lower()
        cases=PIL.Image.open(resource_path("res\\%s.png")%char)
        cases.thumbnail(size=(int(cases.width/1.65),int(cases.height/1.65)))
        img.paste(cases,(x,y))
        size=cases.width
        #print(size)
        x+=size
        del cases

def Letters(word):
    global x,y
    
    untune = random.randint(0,20)
    y+=untune
    #print(word) 
    if x > sizeOfSheet-50*(len(word))or "\n" in word:
        #change line and put random spacing infront of each line
        global tilter
        y+=tilter
        tilter=0
        x=random.randint(130, 160)
        y+=random.randint(65,75)
    for letter in word:
        if letter in allowedchar:
            if letter.islower():
                pass
            elif letter.strip().isupper():
                letter.lower()
                letter+="upper"
            elif letter=='.':
                letter="fullstop"
            elif letter==',':
                letter="comma"
            elif letter==':':
                letter="colon"
            elif letter=='!':
                letter="exclamation"
            elif letter=='?':
                letter="question"
            elif letter=='(':
                letter="bracketopen"
            elif letter==')':
                letter="bracketclose"
            Write(letter)
    y-=untune

def Word(Input):
    wordlist=Input.split(' ')
    global x,y
    for i in wordlist:
        if "\n" in i:
        #split the first and second word
            words=i.split('\n')
            for word in words:
                Letters(word)
                if(word != words[-1]):
                    x=random.randint(120, 150)
                    y+=random.randint(120,130)
        else:
            Letters(i)
        Write('space')

def cheak(func):
	def inner():
		rule = str("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890 ")
		data = text_box.get('1.0', 'end')
		w.config(text ="Working on it...")
		try:
			if len(data) >= 898:
				func()
				redefine()
				
			else:
				showerror(title="Failed", message="Please follow rules!")
		except Exception as e:
			showerror("Error ", e)
		
	return inner


@cheak
def script():
    data = text_box.get('1.0', 'end')
    w.config(text ="Working on it...")
    try:
        global img
        global bgnum
        global img
        global sizeOfSheet
        global x,y
        global count
        global tilter
        global total
        #read the text file
        #data=file.read()
        #calculate number of pages
        nn=len(data)//900
        #print(nn)
        # print(len(data))
        chunks,chunkysize=len(data),len(data)//nn+1
        p=[data[i:i+chunkysize] for i in range(0,chunks,chunkysize)]
        total = len(p)
        for i in range(0,len(p)):
            count= count+1
            Word(p[i])
            img.save("%doutt.png"%i)
            bgnum=random.randint(1,4)
            img1=PIL.Image.open(resource_path("res\\bg%s.jpg")%bgnum)
            img=img1
            sizeOfSheet=img.width
            x,y=100,120
    except ValueError as E:
        print("{}\nTry again",format(E))
    imageList=[]
    for i in range(0,len(p)):
        imageList.append("%doutt.png"%i)

    cover=PIL.Image.open(imageList[0])
    width,height=cover.size
    pdf=FPDF(unit="pt",format=[width,height])
    for i in range(0,len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i],0,0)
    pdf.output("newwy2.pdf","F")
    print("Done")
    '''res = askquestion('Sucess', 'Open destination folder?')
    if res == 'yes':
        modstring = sys.path[0]
        modstring = modstring[:-16]
        os.system('start '+modstring+'\ ')
    else:'''
    showinfo(title="Success", message="Text converted! You can find them in same folder as Scriptor.")
    w.config(text ="Text to Handwriting")
    


def info1():
	try:
		rule = str("Rules: \n\n I)Allowed characters:\n'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890'\n\nAny characters except these will be skipped\n\nII) Minimum of 900 charachters.\n\nIII) Use it at your own risk. Do not use for illegal purpose or misconduct, authors will not be responsible.\n\nIV) After clicking 'WRITE' wait patiently, it takes around 1 to 10 seconds to execute depeending upon length of text.\n\n This is an Open-souce software. Do a visit to our Git-Hub for more information!!")
		showinfo(title="Information", message=rule)
	except Exception as e:
		showerror("Error", e)

def callback():
    webbrowser.open_new("https://github.com/divya-shiv-pandey/Scriptor")



f = ("Arial", 15, "bold")
f1 = ("Arial", 12, "bold")
root = Tk()
root.title('SCRIPTOR')
root.minsize(600,575)
root.geometry('600x575')
root.iconbitmap(resource_path('res\\img.ico'))

style = darkstyle(root)

imgn = ImageTk.PhotoImage(PIL.Image.open(resource_path("res\\img.ico")))
panel = tk.Label(root, image = imgn, height = 30)
panel.pack(side = "top", fill = "both", expand = "yes")

w = LabelFrame(root, text = "Text to Handwriting", font=f)
w.pack(fill="both", expand = "yes")
text_box = Text(w, wrap = WORD)
text_box.insert(END, 'Type here..')


frame = Frame(root)
ww = LabelFrame(root)  
ww.pack(fill="both", expand = "yes") 
write = ttk.Button(ww, text = "Write", width = 20, style="Accentbutton", command = script)
info = ttk.Button(ww, text = "Rules", width = 10, style="Accentbutton", command = info1)
git = ttk.Button(ww, text = "Git", width = 10, style="Accentbutton", command = callback)


vbar = Scrollbar(w,orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=text_box.yview)

hbar = Scrollbar(w, orient=HORIZONTAL)
hbar.pack(side=BOTTOM, fill=X)
hbar.config(command=text_box.xview)

text_box.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

text_box.pack(fill="both", expand="yes")
frame.pack()
#write.grid(row = 0, column = 2, pady = margin_size_height, columnspan = 2)
write.place(relx=0.5, rely=0.5, anchor=CENTER)
info.place(relx=0.0, rely=0.5, anchor=W)
git.place(relx=1.0, rely=.5, anchor=E)

root.mainloop()


if __name__=='__main__':
    #ui()
    print("EXITING")
