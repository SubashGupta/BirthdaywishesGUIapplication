                                    #Birthday wishing GUI application BY K.SUBASH GUPTA

import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import os
import smtplib
from email.mime.text import MIMEText                        #mail including modules
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import pyscreenshot as ImageGrab

#initiating window
window=tk.Tk()
framemain=tk.Frame(window,relief=tk.FLAT,bg="khaki2")
framemain.pack()                                            #creation of frame

window.title("Birthday Wishes")
window.geometry("1500x1500")
window.configure(bg="khaki2")                               #background colour configuration

def pag1():
    global input
    input=dat1.get()
    windows=tk.Toplevel()                                   #use Toplevel for multiple windows display
    frame=tk.Frame(windows,relief=tk.FLAT,bg="khaki2",pady=10)
    windows.title("wishes page")
    windows.geometry("1450x1400")
    windows.configure(bg="khaki2")                          #background colour configuration

    if len(input)>21:                                       #input name length check
        sizes=("Monotype Corsiva",25,"bold")
    else:
        sizes=("Monotype Corsiva",30,"bold")
    wish="Many More Happy Returns of the Day "+input
    lbl3=tk.Label(windows,text=wish,font=sizes,bg="khaki2",fg="black",pady=8)
    lbl3.pack(anchor="center")
    imgw=Image.open("ROOT")  #root of the birthday.jpg image you saved in your desktop
    resizeu=imgw.resize((400,400),Image.ANTIALIAS)              #resizing the image into required dimensions
    picu=ImageTk.PhotoImage(resizeu)                            #selecting the image into the window
    uploade=Label(windows,image =picu,bg="khaki2")              #attaching the image to the window
    uploade.pack(anchor="center")
    l=tk.Label(windows,text="@Subash GUI Creations", font=("gothic",16,"bold"),bg="khaki2",fg="black",padx=65,pady=20)
    l.pack(anchor="se",padx=20)
    lbl4=tk.Label(frame,text="Enter e-mail id to send this greeting card",font=("gothic",16,"bold"),bg="khaki2",fg="black",pady=10)
    lbl4.pack(padx=20,side="left")
                                                        #Birthday wishing GUI application BY K.SUBASH GUPTA
    def mail():
        id=dat2.get()
        im = ImageGrab.grab(bbox=(100,30,1300,550))  # X1,Y1,X2,Y2          #grabbing the required part of the window
        # save image file
        x=input+".png"
        im.save(x)                                                  #saving image
        roots="ROOT"+x            #fetching the folder root where image is saved.
        img_data = open(roots, 'rb').read()
        frm='MAILID'                    #your mail id
        to=id
        msg = MIMEMultipart()                               #Linking mail with the image saved and sending mail.
        msg['Subject'] = 'Birthday wishes'
        msg['From'] = frm
        msg['To'] = id
        text = MIMEText("A Warm Birthday Wishes to you by K.SUBASH GUPTA.   PS: A mail sent by using \"Python\" Coding. ")
        msg.attach(text)
        image = MIMEImage(img_data)
        msg.attach(image)

        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('username','password')        #give your username and password in quotes
        s.sendmail(frm, to, msg.as_string())
        s.quit()
        lbl5=tk.Label(frame,text="Mail Sent Successfully ",font=("gothic",16,"bold"),bg="khaki2",fg="black",pady=10)
        lbl5.pack(padx=20,side="left")
                                                                    #Birthday wishing GUI application BY K.SUBASH GUPTA
    dat2=tk.Entry(frame,width=40)
    dat2.pack(padx=20,pady=10,side="left")
    btn2=tk.Button(frame,text="Send",padx=10,command=mail,fg="black",font=("gothic",12,"bold"))
    btn2.pack(padx=20,pady=10,side="left")
    frame.pack()

    windows.mainloop()

                                                    #Birthday wishing GUI application BY K.SUBASH GUPTA

lbl1=tk.Label(framemain,text="Welcome to Birthday Wishes App", font=("Monotype Corsiva",30,"bold"),bg="khaki2",fg="black",padx=10,pady=20)
lbl1.pack()
lbl2=tk.Label(framemain,text="Enter the person name here",font=("Monotype Corsiva",26),bg="khaki2",fg="red",padx=20,pady=15)
lbl2.pack(side="left")
dat1=tk.Entry(framemain,width=30)
dat1.pack(side="left")
btn1=tk.Button(framemain,text="Submit",padx=10,command=pag1,fg="black",font=("gothic",12,"bold"))
btn1.pack(side="left",padx=20,pady=20)
img=Image.open("ROOT2")            #opening image
resize=img.resize((420,380),Image.ANTIALIAS)  #resizing the image into required dimensions
pic=ImageTk.PhotoImage(resize)                #selecting the image into the window
upload=tk.Label(window,image = pic).pack()    #attaching the image to the window
l=tk.Label(text="@Subash GUI Creations", font=("gothic",16,"bold"),bg="khaki2",fg="black",padx=25,pady=10)
l.pack(side="right")
framemain.pack()
window.mainloop()                             #for running the loop infinite times

                    #Birthday wishing GUI application BY K.SUBASH GUPTA
