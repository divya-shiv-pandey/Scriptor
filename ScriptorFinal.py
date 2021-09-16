from PIL import ImageTk
import PIL.Image
import random
import re
from fpdf import FPDF
from tkinter import *
import tkinter as tk
import os
from tkinter.messagebox import *

bgnum=random.randint(1,4)
img=PIL.Image.open("file\\bg%s.jpg"%bgnum)
sizeOfSheet=img.width
x,y=100,160
tilter=0
allowedchar='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890'

def redefine():
    global bgnum
    global img
    global sizeOfSheet
    global x,y
    global tilter
    bgnum=random.randint(1,4)
    img=PIL.Image.open("file\\bg%s.jpg"%bgnum)
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
        cases=PIL.Image.open("file\\%s.png"%char)
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

def script(data):
    try:
        global img
        global bgnum
        global img
        global sizeOfSheet
        global x,y
        global tilter
        #read the text file
        #data=file.read()
        #calculate number of pages
        nn=len(data)//900
        #print(nn)
        # print(len(data))
        chunks,chunkysize=len(data),len(data)//nn+1
        p=[data[i:i+chunkysize] for i in range(0,chunks,chunkysize)]

        for i in range(0,len(p)): 
            Word(p[i])
            img.save("%doutt.png"%i)
            bgnum=random.randint(1,4)
            img1=PIL.Image.open("file\\bg%s.jpg"%bgnum)
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
    showinfo(title="Information", message="Completed")
    
    


def cheak(func):
	def inner():
		rule = str("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890 ")
		data = text_box.get('1.0', 'end')
		try:
			if len(data) >= 898:
				func()
				tk.messagebox.showinfo('Return','You will now return to the application screen')
				redefine()
				script(data)
			else:
				showerror(title="Failed", message="Please read INFO and PROCEED")
		except Exception as e:
			showerror("Error ", e)
	return inner

@cheak
def hand_write():
	print("hooray")

def info1():
	try:
		rule = str("Rules: \n\n I)Allowed charechters:\n'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890'\nAny charechters except these would be skipped\n\nII) Minimum 900 charachters to write.\n\nIII) Use it at your own risk. Do not use for illegal purpose or misconduct, authors will not be responsible.\n\nIV) After hitting 'WRITE' wait patiently, it takes around 1 to 10 seconds to execute depeending upon length of text.\n\n This is an Open-souce software. Do a visit to our Git-Hub for more information!!")
		showinfo(title="Information", message=rule)
	except Exception as e:
		showerror("Error", e)



f = ("Arial", 15, "bold")
root = Tk()
root.title('SCRIPTOR')
root.minsize(600,575)
root.geometry('600x575')

imgn = ImageTk.PhotoImage(PIL.Image.open("file\\img.ico"))
panel = tk.Label(root, image = imgn, height = 30)
panel.pack(side = "top", fill = "both", expand = "yes")

w = LabelFrame(root, text = "Convert your text to hand writtten with Scriptor", font=f)
w.pack(fill="both", expand = "yes")
text_box = Text(w, wrap = WORD)
text_box.insert(END, 'Type here..')


frame = Frame(root)

ww = LabelFrame(root)  
ww.pack(fill="both", expand = "yes") 
write = Button(ww, text = "Write", font = f, width = 20, command = hand_write)
info = Button(ww, text = "Info", font = f, width = 10, command = info1)
git = Button(ww, text = "GIT", font = f, width = 10)


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
