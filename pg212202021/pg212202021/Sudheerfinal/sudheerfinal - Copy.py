import cv2
import numpy as np
from cv2 import *
from PIL import Image
from numpy import asarray

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
def clearText():
    ee1.delete(0, END)
    ee2.delete(0, END)
    ee3.delete(0, END)
    ee4.delete(0, END)
    e5.delete(0, END)
'''def clearTextE():
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)'''

key=0
y=0
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
def start14():
    raise_frame(f14)

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
        img11.configure(image=img,width=260,height=200)
        img11.image=img
        img = Image.open(filename)
        
        numpydata = asarray(img)
        print(numpydata)
        exe1.insert(0,numpydata)
    except:
        pass


def generateSecKey():
    global key
    key = np.load('data.npy') # load

    e3.insert(0,key)
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


def Secret_Key():
    key = np.load('data.npy') # load
    e3.insert(0,key)
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
    global key
    global y
    
    
    img = Image.open(filename)
    numpydata = asarray(img)
    print(numpydata)
    
    img = Image.open(filename)
    numpydata = asarray(img)
    image_input = cv2.imread(filename, 0)# 'C:/Users/aakas/Documents/flower.jpg'
    (x1, y) = image_input.shape
    image_input = image_input.astype(float) / 255.0
    # print(image_input)
    yval123=int(ee4.get())
    mu, sigma = 0, 0.1  # mean and standard deviation
    key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
    np.save('data.npy', key) # save
    
    print("key is ",key)
    
    # load the image and convert into
    # numpy array
    
    image_encrypted = image_input / key
    e5.insert(0,(image_encrypted))
    np.save('image.npy', image_encrypted) # save
    #fn='image_encrypted.jpg'
    fnn = asksaveasfile(mode='w', defaultextension=".jpg")
    if fnn is None:
        return
    print('Path ',fnn.name)
    cv2.imwrite(fnn.name, image_encrypted * 255)
    img = ImageTk.PhotoImage(file=fnn.name)
    img111.configure(image=img,width=260,height=200)
    img111.image=img
    
def decrypt_image():
    global filename
    global image_output
    file1 = open("datas.npy","r+", encoding="utf-8")
    key = np.load('data.npy') # load

    #e3.insert(0,key)
    
    dd=file1.read()
    dd1=dd.split('==')
    print("DD  ",dd1)
    #p=e1.get()
    pk=e2.get()
    if int(pk)==int(dd1[2]):
           
        image_encrypted = np.load('image.npy') # load
        #image_input = cv2.imread(filename, 0)
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
        window.geometry('200x200')
        img = tk.PhotoImage(file='image_output.png')  # has to be `file=`

        tk.Label(image=img).pack()

        window.after(5000, window.destroy)     # `destroy` without `()`

        window.mainloop()

    else:
        messagebox.showinfo('Message Box','Pls Check the keys')
def Y_value():
    global y
    global pkey
    p=ee1.get()
    a=ee2.get()
    pkey=ee3.get()
    if p=='' or a=='' or pkey=='':
        messagebox.showinfo('Message Box','Pls Enter the Values')
    else:
        p=int(p)
        a=int(a)
        ctr=0
        for i in range(1,p+1):
            if p%i==0:
                ctr=ctr+1
        if ctr!=2:
            messagebox.showinfo('Message Box','P Value Should be Primary')
        else:        
            pkey=int(pkey)
            y=(a**pkey)%p
            print("Y Value is ",y)
            
            print(p)
            print(a)
            print(pkey)
            data=str(p)+"=="+str(a)+"=="+str(pkey)
            with open('datas.npy', 'w', encoding="utf-8") as f:
                f.write(data)
            ee4.insert(0,str(y))
def K_value():
    global key
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
    e5.insert(0,key)
def Secret_KeyD():
     global key
     e3.insert(0,key)
def image_values():
    global image_output
    e4.insert(0,image_output)
def save_cipher():
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
        
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
f14.place(x = 0,y =0,height=825, width=1360)


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

from math import sqrt

# Returns True if n is prime
def isPrime( n):

	# Corner cases
	if (n <= 1):
		return False
	if (n <= 3):
		return True

	# This is checked so that we can skip
	# middle five numbers in below loop
	if (n % 2 == 0 or n % 3 == 0):
		return False
	i = 5
	while(i * i <= n):
		if (n % i == 0 or n % (i + 2) == 0) :
			return False
		i = i + 6

	return True

""" Iterative Function to calculate (x^n)%p
	in O(logy) */"""
def power( x, y, p):

	res = 1 # Initialize result

	x = x % p # Update x if it is more
			# than or equal to p

	while (y > 0):

		# If y is odd, multiply x with result
		if (y & 1):
			res = (res * x) % p

		# y must be even now
		y = y >> 1 # y = y/2
		x = (x * x) % p

	return res

# Utility function to store prime
# factors of a number
def findPrimefactors(s, n) :

	# Print the number of 2s that divide n
	while (n % 2 == 0) :
		s.add(2)
		n = n // 2

	# n must be odd at this point. So we can
	# skip one element (Note i = i +2)
	for i in range(3, int(sqrt(n)), 2):
		
		# While i divides n, print i and divide n
		while (n % i == 0) :

			s.add(i)
			n = n // i
		
	# This condition is to handle the case
	# when n is a prime number greater than 2
	if (n > 2) :
		s.add(n)

# Function to find smallest primitive
# root of n
def findPrimitive( n) :
	s = set()

	# Check if n is prime or not
	if (isPrime(n) == False):
		return -1

	# Find value of Euler Totient function
	# of n. Since n is a prime number, the
	# value of Euler Totient function is n-1
	# as there are n-1 relatively prime numbers.
	phi = n - 1

	# Find prime factors of phi and store in a set
	findPrimefactors(s, phi)

	# Check for every number from 2 to phi
	for r in range(2, phi + 1):

		# Iterate through all prime factors of phi.
		# and check if we found a power with value 1
		flag = False
		for it in s:

			# Check if r^((phi)/primefactors)
			# mod n is 1 or not
			if (power(r, phi // it, n) == 1):

				flag = True
				break
			
		# If there was no power with value 1.
		if (flag == False):
			return r

	# If no primitive root found
	return -1


def GenAValue():
    p=ee1.get()
    if p=='':
        messagebox.showinfo('Message Box','Pls Enter the P Value')
    else:
        p=int(p)
        proot=findPrimitive(p)
        ee2.insert(0,str(proot))
#-----------------------abstract------frame-2--------------------

ph33=ImageTk.PhotoImage(Image.open("Images\myabs.jpg"))
lab1 = Label(f2,image=ph33).place(x = 0, y = 0)

b7 = Button(f2, text = "Back",fg="black",bg="#FFFACD",font = "Helvetica 12 bold",height=1,width=10,command=start10).place(x = 550, y = 570)
#b8 = Button(f2, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start10).place(x = 1100, y = 60)


#-----------------------Proposed------frame-2--------------------
ph3=ImageTk.PhotoImage(Image.open("Images\slide4.jpg"))
lab1 = Label(f14,image=ph3).place(x = 0, y = 0)

b7 = Button(f14, text = "Back",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start1).place(x = 800, y = 580)
b8 = Button(f14, text = "Proceed",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start10).place(x = 600, y = 580)


#------------------StartPage-----------frame 1----------------------------------------------------------------
ph1=ImageTk.PhotoImage(Image.open("Images\Slide1.jpg"))
lab1 = Label(f1,image=ph1).place(x = -10, y = -10)
#b9 = Button(f10, text = "Proceed",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start14).place(x = 00, y = 450)
#but1 = Button(f1, text = "Contents",fg="black",bg="#FFFACD", font = "Helvetica 18 bold",height=1,width=10, command = start10).place(x = 500, y = 550)
but2 = Button(f1, text = "Close",fg="black",bg="#FFFACD", font = "Helvetica 18 bold",height=1,width=10,command=finish).place(x = 800, y = 550)
but3 = Button(f1, text = "Proceed",fg="black",bg="#FFFACD", font = "Helvetica 18 bold",height=1,width=10,command=start10).place(x = 600, y = 550)

#------------------------Menu-----frame-2--------------------
ph7=ImageTk.PhotoImage(Image.open("Images\empty.jpg"))
lab1 = Label(f10,image=ph7).place(x = 0, y = 0)

#ph70=ImageTk.PhotoImage(Image.open("Images\ED.jpg"))
#lab1 = Label(f10,image=ph70).place(x = 300, y = 340)
lab1 = Label(f10,text="El Gamal CRYPTOSYSTEM FOR IMAGE ENCRYPTION AND DECRYPTION", font = "Helvetica 24 bold").place(x = 100, y = 200)


b7 = Button(f10, text = "Home",fg="black",bg="#FFFACD", font = "Helvetica 20 bold",height=1,width=13,command=start1).place(x = 550, y = 350)
b8 = Button(f10, text = "Abstract",fg="black",bg="#FFFACD", font = "Helvetica 20 bold",height=1,width=13,command = start2).place(x = 550, y = 420)
#b9 = Button(f10, text = "Proposed",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = proposed).place(x = 550, y = 280)
b10 = Button(f10, text = "Encryption",fg="black",bg="#FFFACD", font = "Helvetica 20 bold",height=1,width=13,command=start3).place(x = 550, y = 490)
b11 = Button(f10, text = "Decryption",fg="black",bg="#FFFACD", font = "Helvetica 20 bold",height=1,width=13,command = start6).place(x = 550, y = 560)

#-----------------------abstract------frame-2--------------------
#ph3=ImageTk.PhotoImage(Image.open("Images\Slide3.jpg"))
#lab1 = Label(f2,image=ph3).place(x = 0, y = 0)

b7 = Button(f2, text = "Back",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start1).place(x = 100, y = 760)
b8 = Button(f2, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start3).place(x = 1100, y = 760)

#-----------------------------frame-3--------------------
lab1 = Label(f3,image=ph7).place(x = 0, y = 0)
lab1 = Label(f3,text="Encryption", font = "Helvetica 34 bold").place(x = 100, y = 200)



b1 = Button(f3,text='Browse Image',font = "Helvetica 12 bold",command = upload_file).place(x = 100, y = 300)
img11 =Label(f3) 
img11.place(x=450,y=300)

#l1123 = Label(f3,text='Enter P Value',font = "Helvetica 12 bold").place(x = 200, y = 350)
exe1 = Entry(f3,font = "Helvetica 12 bold")
exe1.place(x = 250, y = 300)

l1 = Label(f3,text='Enter P Value',font = "Helvetica 12 bold").place(x = 100, y = 350)
ee1 = Entry(f3,font = "Helvetica 12 bold")
ee1.place(x = 250, y = 350)

l2 = Button(f3,text='Enter a Value',font = "Helvetica 12 bold",command=GenAValue).place(x = 100, y = 400)
ee2 = Entry(f3,font = "Helvetica 12 bold")
ee2.place(x = 250, y = 400)

l3 = Label(f3,text='Enter Private Key',font = "Helvetica 12 bold").place(x = 100, y = 450)
ee3 = Entry(f3,font = "Helvetica 12 bold")
ee3.place(x = 250, y = 450)

ll4 = Button(f3,text='Y Value',font = "Helvetica 12 bold",command =Y_value ).place(x = 100, y = 500)
ee4 = Entry(f3,font = "Helvetica 12 bold")
ee4.place(x = 250, y = 500)

l5 = Button(f3,text='Cipher Values',font = "Helvetica 12 bold",command = K_value).place(x = 100, y = 550)
e5 = Entry(f3,font = "Helvetica 12 bold")
e5.place(x = 250, y = 550)

#l6 = Label(f3,text='Secrete Key',font = "Helvetica 12 bold").place(x = 200, y = 600)
#e6 = Entry(f3,font = "Helvetica 12 bold")
#e6.place(x = 350, y = 600)


Button(f3,text='Encrypt&Save',fg="black",bg="#FFFACD",font = "Helvetica 12 bold",command=encrypt_image).place(x = 660, y = 550)
img111 =Label(f3) 
img111.place(x=900,y=320)

#tr = Label(f3,textvariable=trk,font = "Helvetica 12 bold")
#tr.place(x = 700, y = 650)


#Button(f3,text='Save',font = "Helvetica 12 bold",command=save_cipher).place(x = 760, y = 550)

b7 = Button(f3, text = "Back",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start10).place(x = 860, y = 550)
#b8 = Button(f3, text = "Next",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command = start4).place(x = 1100, y = 760)
bb7 = Button(f3, text = "Clear",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=clearText).place(x = 600, y = 600)
#-----------------------------frame-4--------------------
ph17=ImageTk.PhotoImage(Image.open("Images\empty.jpg"))
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

lab1 = Label(f6,text="Decryption", font = "Helvetica 12 bold").place(x = 50, y = 250)


b1 = Button(f6,text='Browse Cipher Image',font = "Helvetica 12 bold",command = upload_file2).place(x = 200, y = 300)
img1 =Label(f6) 
img1.place(x=700,y=300)

'''
l1 = Label(f6,text='Enter P Value',font = "Helvetica 12 bold").place(x = 200, y = 150)
e1 = Entry(f6,font = "Helvetica 12 bold")
e1.place(x = 350, y = 150)
'''
l2 = Label(f6,text='Enter Private Key',font = "Helvetica 12 bold").place(x = 200, y = 350)
e2 = Entry(f6,font = "Helvetica 12 bold")
e2.place(x = 350, y = 350)

l3 = Button(f6,text='Secert Key',font = "Helvetica 12 bold",command =Secret_Key).place(x = 200, y = 400)
e3 = Entry(f6,font = "Helvetica 12 bold")
e3.place(x = 350, y = 400)

l4 = Button(f6,text='image values',font = "Helvetica 12 bold",command =image_values).place(x = 200, y = 450)
e4 = Entry(f6,font = "Helvetica 12 bold")
e4.place(x = 350, y = 450)


Button(f6,text='Decrypt',font = "Helvetica 12 bold",command=decrypt_image).place(x = 200, y = 500)
img2 =Label(f6) 
img2.place(x=200,y=500)



b7 = Button(f6, text = "Back",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start10).place(x = 700, y = 600)

'''lab1 = Label(f6,image=ph17).place(x = 0, y = 0)

lab1 = Label(f6,text="Decryption", font = "Helvetica 12 bold").place(x = 50, y = 250)


b1 = Button(f6,text='Browse Cipher Image',font = "Helvetica 12 bold",command = upload_file2).place(x = 200, y = 300)
img1 =Label(f6) 
img1.place(x=700,y=300)


l1 = Label(f6,text='Enter P Value',font = "Helvetica 12 bold").place(x = 200, y = 150)
e1 = Entry(f6,font = "Helvetica 12 bold")
e1.place(x = 350, y = 150)

l2 = Label(f6,text='Enter Private Key',font = "Helvetica 12 bold").place(x = 200, y = 330)
e2 = Entry(f6,font = "Helvetica 12 bold")
e2.place(x = 350, y = 330)

l3 = Button(f6,text='Secert Key',font = "Helvetica 12 bold",command =Secret_Key).place(x = 200, y = 550)
e3 = Entry(f6,font = "Helvetica 12 bold")
e3.place(x = 350, y = 550)

l4 = Button(f6,text='image values',font = "Helvetica 12 bold",command =image_values).place(x = 200, y = 650)
e4 = Entry(f6,font = "Helvetica 12 bold")
e4.place(x = 350, y = 650)


Button(f6,text='Decrypt',font = "Helvetica 12 bold",command=decrypt_image).place(x = 200, y = 750)
img2 =Label(f6) 
img2.place(x=200,y=750)



b7 = Button(f6, text = "Home",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=start10).place(x = 350, y = 850)
#bb7 = Button(f6, text = "Clear",fg="black",bg="#FFFACD", font = "Helvetica 12 bold",height=1,width=10,command=clearText).place(x = 600, y = 600)'''


#-----------------------------frame-7--------------------
#-----------------------------frame-8--------------------
ph12=ImageTk.PhotoImage(Image.open("Images\empty.jpg"))
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
