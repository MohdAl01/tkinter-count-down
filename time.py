# importing whole module
from tkinter import * 
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime
import datetime 

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to 
# display time on the label
def time():

	x =  datetime.datetime(2021, 11, 26) - datetime.datetime.now()
	hours = int(str(x)[0:3])*24
	hours += int(str(x)[0])
	x = str(x)[10:17]

	x_list = list(x)
	x_list[0] = str(hours) 
	"".join(x_list )
	x = x_list
	string = x 
	lbl.config(text = string)
	lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive ;) 
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()