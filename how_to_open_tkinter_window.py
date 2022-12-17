# # import tkinter    #if import it without  from we have to call the tkinter everytime
# # window=tkinter.Tk()
# # #if we rename the title of the window
# # window.title("GUI")
# # #pack is to show the object in the window
# # label=tkinter.Label(window,text="Hello World").pack()
# # window.mainloop()
from tkinter import*
root=Tk()
root.title ("GUI")
root.geometry('300x200')
label=Label(root,text="hello world" font="Arial Bold",50).pack() #if we're using from there's no need to call tkinter
  # to resize our window
bt=Button(root,text="Enter",bg='sky blue').pack()
bt.grid(column=1,row=0)
root.mainloop()       #another way to import the tkinter module



# from tkinter import *
# import tkinter.font as font
# gui = Tk()
# gui.geometry("30x20")
# # set the font.
# f = font.Font(family='Times New Roman')
# # create button
# btn = Button(gui, text='Click here!', bg='red', fg='white')
# # apply font to the button label
# btn['font'] = f
# # add button to window
# btn.pack()
# gui.mainloop()