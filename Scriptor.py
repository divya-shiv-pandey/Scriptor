from PIL import Image
import random
import re
from fpdf import FPDF

bgnum=random.randint(1,4)
img=Image.open("file\\bg%s.jpg"%bgnum)
sizeOfSheet=img.width

x,y=100,160
tilter=0
allowedchar='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm(),.?;1234567890'

def Write(char):
    global x,y
    global tilter
    tilter+=1
    y-=1
    if char=='\n':
        pass
    else:
        char.lower()
        cases=Image.open("file\\%s.png"%char)
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




if __name__=='__main__':

    try:
        with open("black.txt",'r') as file:
            #read the text file
            data=file.read()
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
                img1=Image.open("file\\bg%s.jpg"%bgnum)
                img=img1
                sizeOfSheet=img.width
                x,y=100,120
    except ValueError as E:
        print("{}\nTry again",format(E))
    imageList=[]
    for i in range(0,len(p)):
        imageList.append("%doutt.png"%i)

    cover=Image.open(imageList[0])
    width,height=cover.size
    pdf=FPDF(unit="pt",format=[width,height])
    for i in range(0,len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i],0,0)
    pdf.output("newwy2.pdf","F")
    print("Done")





