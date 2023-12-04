import cv2
import numpy as np
from cv2 import *

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter import filedialog
import random

def raise_proposed(f):
    f.tkraise()
def raise_frame(f):
    f.tkraise()
def finish():
    r.destroy()
def start1():
    raise_frame(f1)
def start2():
    raise_frame(f2)
def start3():
    raise_frame(f3)
def start4():
    raise_frame(f4)
def start5():
    raise_frame(f5)
def start6():
    raise_frame(f6)
def start7():
    raise_frame(f7)
def start8():
    raise_frame(f8)
def start9():
    raise_frame(f9)
def start10():
    raise_frame(f10)
def start11():
    raise_frame(f11)
def start12():
    raise_frame(f12)
def start13():
    raise_frame(f13)
def proposed():
    raise_proposed(f14)

#----------------------------------------------------------------------------------------------------------------------------
cc=0
filename=""
def upload_file():
    global img,filename,cc
    
    try:
        cc=1
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        print(filename)
        img = ImageTk.PhotoImage(file=filename)
        img11.configure(image=img,width=360,height=300)
    except:
        pass


def upload_file2():
    global img,filename,cc
    
    try:
        cc=1
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        print(filename)
        img = ImageTk.PhotoImage(file=filename)
        img1.configure(image=img,width=360,height=300)

      
    except:
        pass

def upload_file3():
    global img,filename,cc
    
    try:
        cc=1
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        print(filename)
        img = ImageTk.PhotoImage(file=filename)
        img2.configure(image=img,width=360,height=300)

      
    except:
        pass

def generateSecKey():
    key = np.load('data.npy') # load

    e3.insert(0,key)
def fun11():
    global arm
    try:
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(arm)
        f.close()
        messagebox.showinfo('Message Box','Armstrong values are saved')
    except:
        pass    

def fun12():
    global S
    try:
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(str(len(S)))
        f.close()
        messagebox.showinfo('Message Box','Save the Length')
    except:
        pass    
def fun13():
    global sig
    try:
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(sig)
        f.close()
        messagebox.showinfo('Message Box','All bits are saved')
    except:
        pass
#--------------------------------------Decryption-1 -------------------------------------------------------------------------------
ck=1
def upload_file1():
    global img,filename,ck
    if(ck==1):
        try:
            ck=1
            f_types = [('Jpg Files', '*.png')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = ImageTk.PhotoImage(file=filename)
            img2D.configure(image=img,width=360,height=300)
        except:
            pass    
    else:
        messagebox.showinfo('Message Box','Click the previous button')    
def fun14():
    global vj,dec,bi,bi1,sig,val,ck
    if(ck==1):
        path= 'Images\img7.jpg'
        try:
            ck=2
            fin = open(path, 'rb')	
            image = fin.read()
            fin.close()	
            image = bytearray(image)
            val=''
            for i, values in enumerate(image):
                image[i] = values
                if(i<300):
                    val=val+str(D8B(values))+' '
                    if(i%22==0):
                        val=val+'\n'
                                    
            fin = open(path, 'wb')
            fin.write(image)
            fin.close()
            #print('Encryption Done...')
            x16.set(val)
            
        except Exception:
            print('Error caught : ', Exception.__name__)
    else:
        messagebox.showinfo('Message Box','Click the previous button')

def fun15():
    global length,ck
    if(ck==2):
        try:
            ck=3
            file=askopenfile(mode='r',filetypes=[('All files','*.txt')])
            if file is not None:
                length=file.read()
                x17.set(str(length))
        except:
            pass
    else:
        messagebox.showinfo('Message Box','Click the previous button')    
#----------------------------------------------------------------------------------------------------------------------------




def encrypt_image():
    global filename
    from PIL import Image
    from numpy import asarray

    p=int(ee1.get())
    a=int(ee2.get())
    pkey=int(ee3.get())
    
    y=(a**pkey)%p
    print("Y Value is ",y)
    ee4.insert(0,str(y))
    print(p)
    print(a)
    print(pkey)
    img = Image.open(filename)
    numpydata = asarray(img)
    print(numpydata)
    
    
    data=str(p)+"=="+str(a)+"=="+str(pkey)
    with open('datas.npy', 'w', encoding="utf-8") as f:
        f.write(data)
    # load the image and convert into
    # numpy array
    img = Image.open(filename)
    numpydata = asarray(img)
    image_input = cv2.imread('test.jpg', 0)# 'C:/Users/aakas/Documents/flower.jpg'
    (x1, y) = image_input.shape
    image_input = image_input.astype(float) / 255.0
    # print(image_input)

    mu, sigma = 0, 0.1  # mean and standard deviation
    key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
    np.save('data.npy', key) # save
    
    print("key is ",key)
    image_encrypted = image_input / key
    np.save('image.npy', image_encrypted) # save
    e5.insert(0,key)
    cv2.imwrite('image_encrypted.jpg', image_encrypted * 255)
    
def decrypt_image():


    file1 = open("datas.npy","r+", encoding="utf-8")
    key = np.load('data.npy') # load

    #e3.insert(0,key)
    
    dd=file1.read()
    dd1=dd.split('==')
    p=e1.get()
    pk=e2.get()
    if int(p)==int(dd1[0]) and int(pk)==int(dd1[2]):
            
        image_encrypted = np.load('image.npy') # load
        #image_input = cv2.imread('image_encrypted.jpg', 0)
        #(x1, y) = image_input.shape
        #image_encrypted = image_input.astype(float)
        key = np.load('data.npy') # load
        
        image_output = image_encrypted * key
        image_output *= 255.0
        cv2.imwrite('image_output.jpg', image_output)
        cv2.imwrite('image_output.png', image_output)
        print('done')
        e4.insert(0,image_output)
        #fname='C:/Users/sudheer/Desktop/Sudheerfinal/image_output.jpg'
        #img = ImageTk.PhotoImage(file='image_output.png')
        #img2.configure(image=img,width=360,height=300)
        #upload_file3()
        import tkinter as tk

        window = tk.Tk()

        img = tk.PhotoImage(file='image_output.png')  # has to be `file=`

        tk.Label(image=img).pack()

        window.after(5000, window.destroy)     # `destroy` without `()`

        window.mainloop()

    else:
        print("Pls Check the keys")
def save_cipher():
    print("Cons")
r = Tk()
f1 = Frame(r)
f2 = Frame(r)
f3 = Frame(r)
f4 = Frame(r)
f5 = Frame(r)
f6 = Frame(r)
f7 = Frame(r)
f8 = Frame(r)
f9 = Frame(r)
f10 = Frame(r)
f11 = Frame(r)
f12 = Frame(r)
f13 = Frame(r)
f14 = Frame(r)


f1.place(x = 0,y = 0,height=825, width=1360)
f2.place(x = 0,y = 0,height=825, width=1360)
f3.place(x = 0,y = 0,height=825, width=1360)
f4.place(x = 0,y = 0,height=825, width=1360)
f5.place(x = 0,y = 0,height=825, width=1360)
f6.place(x = 0,y = 0,height=825, width=1360)
f7.place(x = 0,y = 0,height=825, width=1360)
f8.place(x = 0,y = 0,height=825, width=1360)
f9.place(x = 0,y = 0,height=825, width=1360)
f10.place(x = 0,y =0,height=825, width=1360)
f11.place(x = 0,y =0,height=825, width=1360)
f12.place(x = 0,y =0,height=825, width=1360)
f13.place(x = 0,y =0,height=825, width=1360)


lab1001 = Label(f5)
lab1001.place(x=350,y=420)

rgbc=StringVar()
trk=StringVar()
x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()
x7=StringVar()
x8=StringVar()
x9=StringVar()
x10=StringVar()
x11=StringVar()
x12=StringVar()
x13=StringVar()
x14=StringVar()
x15=StringVar()
x16=StringVar()
x17=StringVar()
x18=StringVar()
x19=StringVar()
x20=StringVar()
x21=StringVar()
x22=StringVar()
x23=StringVar()
x24=StringVar()
x25=StringVar()
x26=StringVar()
x27=StringVar()
x28=StringVar()
x29=StringVar()


#-----------------------abstract------frame-2--------------------

ph33=ImageTk.PhotoImage(Image.open("Images\myabs.jpg"))
lab1 = Label(f2,image=ph33).place(x = 0, y = 0)

b7 = Button(f2, text = "Prev",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start1).place(x = 100, y = 60)
b8 = Button(f2, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start10).place(x = 1100, y = 60)


#-----------------------Proposed------frame-2--------------------
ph3=ImageTk.PhotoImage(Image.open("Images\slide4.jpg"))
lab1 = Label(f14,image=ph3).place(x = 0, y = 0)

b7 = Button(f14, text = "Prev",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start1).place(x = 100, y = 60)
b8 = Button(f14, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start10).place(x = 1100, y = 60)


#------------------StartPage-----------frame 1----------------------------------------------------------------
ph1=ImageTk.PhotoImage(Image.open("Images\Slide1.jpg"))
lab1 = Label(f1,image=ph1).place(x = -10, y = -10)

but1 = Button(f1, text = "Proceed",fg="black",bg="#FFFACD", font = "Helvetica 18 bold",height=1,width=10, command = start10).place(x = 500, y = 550)
but2 = Button(f1, text = "Close",fg="black",bg="#FFFACD", font = "Helvetica 18 bold",height=1,width=10,command=finish).place(x = 720, y = 550)

#------------------------Menu-----frame-2--------------------
ph7=ImageTk.PhotoImage(Image.open("Images\empty.jpg"))
lab1 = Label(f10,image=ph7).place(x = 0, y = 0)

#ph70=ImageTk.PhotoImage(Image.open("Images\ED.jpg"))
#lab1 = Label(f10,image=ph70).place(x = 300, y = 340)

b7 = Button(f10, text = "Home",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start1).place(x = 650, y = 255)
b8 = Button(f10, text = "Abstract",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start2).place(x = 650, y = 325)
b9 = Button(f10, text = "Proposed",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = proposed).place(x = 650, y = 395)
b10 = Button(f10, text = "Encryption",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start3).place(x = 650, y = 465)
b11 = Button(f10, text = "Decryption",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start6).place(x = 650, y = 535)

#-----------------------abstract------frame-2--------------------
#ph3=ImageTk.PhotoImage(Image.open("Images\Slide3.jpg"))
#lab1 = Label(f2,image=ph3).place(x = 0, y = 0)

b7 = Button(f2, text = "Prev",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start1).place(x = 100, y = 760)
b8 = Button(f2, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start10).place(x = 1100, y = 760)

#-----------------------------frame-3--------------------
lab1 = Label(f3,image=ph7).place(x = 0, y = 0)
lab1 = Label(f3,text="Encryption", font = "Helvetica 24 bold").place(x = 100, y = 250)



b1 = Button(f3,text='Browse Image',font = "Helvetica 12 bold",command = upload_file).place(x = 500, y = 300)
img11 =Label(f3) 
img11.place(x=700,y=270)


l1 = Label(f3,text='Enter P Value',font = "Helvetica 12 bold").place(x = 200, y = 350)
ee1 = Entry(f3,font = "Helvetica 12 bold")
ee1.place(x = 350, y = 350)

l2 = Label(f3,text='Enter a Value',font = "Helvetica 12 bold").place(x = 200, y = 400)
ee2 = Entry(f3,font = "Helvetica 12 bold")
ee2.place(x = 350, y = 400)

l3 = Label(f3,text='Enter Private Key',font = "Helvetica 12 bold").place(x = 200, y = 450)
ee3 = Entry(f3,font = "Helvetica 12 bold")
ee3.place(x = 350, y = 450)

ll4 = Label(f3,text='Y Value',font = "Helvetica 12 bold").place(x = 200, y = 500)
ee4 = Entry(f3,font = "Helvetica 12 bold")
ee4.place(x = 350, y = 500)

l5 = Label(f3,text='K Value',font = "Helvetica 12 bold").place(x = 200, y = 550)
e5 = Entry(f3,font = "Helvetica 12 bold")
e5.place(x = 350, y = 550)

#l6 = Label(f3,text='Secrete Key',font = "Helvetica 12 bold").place(x = 200, y = 600)
#e6 = Entry(f3,font = "Helvetica 12 bold")
#e6.place(x = 350, y = 600)


Button(f3,text='Encrypt',font = "Helvetica 12 bold",command=encrypt_image).place(x = 860, y = 550)
tr = Label(f3,textvariable=trk,font = "Helvetica 12 bold")
tr.place(x = 700, y = 650)


Button(f3,text='Save',font = "Helvetica 12 bold",command=save_cipher).place(x = 860, y = 600)

b7 = Button(f3, text = "Home",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start10).place(x = 1000, y = 550)
#b8 = Button(f3, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start4).place(x = 1100, y = 760)
#-----------------------------frame-4--------------------
ph17=ImageTk.PhotoImage(Image.open("Images\empty1.jpg"))
lab1 = Label(f4,image=ph17).place(x = 0, y = 0)
#lab1 = Label(f4,text="Encryption-2", font = "Helvetica 24 bold").place(x = 100, y = 200)

#Button(f4,text='Create ASCII values for message is to be sent.',font = "Helvetica 12 bold",command=fun2).place(x = 150, y = 150)
L1 = Label(f4,textvariable=x2,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 200)
L1 = Label(f4,textvariable=x3,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 250)

#Button(f4,text='Now adds this digits with Armstrong number',font = "Helvetica 12 bold",command=fun3).place(x = 150, y = 300)
L1 = Label(f4,textvariable=x4,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 350)
L1 = Label(f4,textvariable=x5,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 400)
L1 = Label(f4,textvariable=x6,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 450)

#Button(f4,text='Now adds this digits with Password',font = "Helvetica 12 bold",command=fun4).place(x = 150, y = 500)
L1 = Label(f4,textvariable=x7,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 550)
L1 = Label(f4,textvariable=x8,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 600)
L1 = Label(f4,textvariable=x9,anchor='w',font = "Helvetica 12 bold",width=90).place(x = 150, y = 650)

b7 = Button(f4, text = "Prev",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start3).place(x = 100, y = 760)
b8 = Button(f4, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start5).place(x = 1100, y = 760)
#Button(f4,text='Reset Button',font = "Helvetica 12 bold",command=funR).place(x = 1190, y = 500)

#-----------------------------frame-5--------------------

#-----------------------------frame-6--------------------
lab1 = Label(f6,image=ph17).place(x = 0, y = 0)

lab1 = Label(f6,text="Decryption", font = "Helvetica 12 bold").place(x = 50, y = 50)


b1 = Button(f6,text='Browse Cipher Image',font = "Helvetica 12 bold",command = upload_file2).place(x = 200, y = 100)
img1 =Label(f6) 
img1.place(x=700,y=100)

'''
l1 = Label(f6,text='Enter P Value',font = "Helvetica 12 bold").place(x = 200, y = 150)
e1 = Entry(f6,font = "Helvetica 12 bold")
e1.place(x = 350, y = 150)
'''
l2 = Label(f6,text='Enter Private Key',font = "Helvetica 12 bold").place(x = 200, y = 200)
e2 = Entry(f6,font = "Helvetica 12 bold")
e2.place(x = 350, y = 200)

l3 = Button(f6,text='Secert Key',font = "Helvetica 12 bold",command=generateSecKey).place(x = 200, y = 250)
e3 = Entry(f6,font = "Helvetica 12 bold")
e3.place(x = 350, y = 250)

l4 = Label(f6,text='image values',font = "Helvetica 12 bold").place(x = 200, y = 300)
e4 = Entry(f6,font = "Helvetica 12 bold")
e4.place(x = 350, y = 300)


Button(f6,text='Decrypt',font = "Helvetica 12 bold",command=decrypt_image).place(x = 200, y = 350)
img2 =Label(f6) 
img2.place(x=200,y=360)



b7 = Button(f6, text = "Home",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start10).place(x = 700, y = 600)

#-----------------------------frame-7--------------------
#-----------------------------frame-8--------------------
ph12=ImageTk.PhotoImage(Image.open("Images\Slide1.jpg"))
lab1 = Label(f8,image=ph12).place(x = 0, y = 0)


b7 = Button(f8, text = "Prev",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start7).place(x = 100, y = 760)
b8 = Button(f8, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start9).place(x = 1100, y = 760)

#-----------------------------frame-9--------------------
#ph13=ImageTk.PhotoImage(Image.open("Images\Slide12.jpg"))
#lab1 = Label(f9,image=ph13).place(x = 0, y = 0)

b7 = Button(f9, text = "Prev",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start8).place(x = 100, y = 760)
b8 = Button(f9, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start1).place(x = 1100, y = 760)
#-----------------------------End--------------------
raise_frame(f1)
r.geometry("1360x825+100+0")
r.title("el gamal image encryption AND DECRYPTION")
r.mainloop()


raise_proposed(f1)
r.geometry("1360x825+100+0")
r.title("IMAGE BASED STEGANOGRAPHY USING CRYPTOGRAPHY")
r.mainloop()
