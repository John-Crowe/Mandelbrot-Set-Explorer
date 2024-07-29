#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk
import numpy as np
from PIL import Image

#Now let's declare the size of the canvas we want to make. We will start out with a square for simplicity
global L
L = 400

#Our variables X and Y will be the current values of the origin. With this and the magnification, we can figure out which values to check for the mandlebrot set
global X
X = 0
global Y
Y = 0
global imp
pstuff = np.ones((L,L,3), dtype='uint8')
plor = np.flipud(pstuff.transpose(1,0,2))
imp = Image.fromarray(plor, 'RGB')

#The num_click variable is used to determine the magnification
global num_clicks
num_clicks = 1

def is_mandelbrot(real,imag):
    result = []
    z_n = 0
    num = complex(real,imag)
    for i in range(50):
        z_n = z_n*z_n + num
        if (abs(z_n) > 4):
            result.append(False)
            result.append(i)
            return(result)
    result.append(True)
    return(result)

def make_mand():
    pvals = np.ones((L,L,3), dtype='uint8')
    #Now let's make an all white image
    pvals = pvals*255
    a = (L/8)*(2**num_clicks)
    b = (2/(2**(num_clicks-1)))
    for j in range(L):
        for i in range(L):
            #Modifying the x and y gives this program the 2x zoom characteristic
            x = X + i/a - b
            y = Y + j/a - b

            result = is_mandelbrot(x,y)
            if(result[0]==True):
                pvals[i,j,0] = 0
                pvals[i,j,1] = 0
                pvals[i,j,2] = 0
            else:
                pvals[i,j,0] = 2*result[1]
                pvals[i,j,1] = 5*result[1]
                pvals[i,j,2] = 10*result[1]
    
    plotarr = np.flipud(pvals.transpose(1,0,2))
    im = Image.fromarray(plotarr, 'RGB')
    global imp
    imp = im

master = Tk()
master.title('Mandelbrot Plot Explorer')

w = Canvas(master, width=L, height=L)
image = ImageTk.PhotoImage(imp)
w.create_image(10,10,image=image, anchor=NW)
w.pack()

def printcoords(event):
    global num_clicks
    #Now let's modify the origin. We reposition it around the point that was just clicked 
    global X,Y
    X = X + event.x/((L/8)*(2**num_clicks)) - (2/(2**(num_clicks-1)))
    Y = Y - event.y/((L/8)*(2**num_clicks)) + (2/(2**(num_clicks-1)))
    print("x = "+str(X),"y = "+str(Y))
    num_clicks = num_clicks + 1
    make_mand()
    new_image = ImageTk.PhotoImage(imp)
    w.create_image(10,10, image=new_image,anchor=NW)
    mainloop()

w.bind("<Button 1>", printcoords)
make_mand()
new_image = ImageTk.PhotoImage(imp)
w.create_image(10,10, image=new_image,anchor=NW)
mainloop()
