
from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("241x258")
#to disabled all buttons:
def disabled_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
#x starts so true             
clicked=True
count=0
#check if someone won 
def check_if_someone_won():
    global Winner
    Winner=False
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons() 
    ### check for O's win:
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        Winner =True
        messagebox.showinfo("Tic Tac Toe","Congratulations!  X Wins!!")
        disabled_all_buttons()
        
#button clicked function
def b_click(b):
    global count,clicked
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        check_if_someone_won()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked =True
        count+=1
        check_if_someone_won()
    else:
        messagebox.showinfo("Tic Tac Toe","Invalid Move")
b1=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b1))
b2=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b2))
b3=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b3))
b4=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b4))
b5=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b5))
b6=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b6))
b7=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b7))
b8=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b8))
b9=Button(window,height=5,width=10,text=" ",command=lambda:b_click(b9))
#Grid our Buttons to the screen
b1.grid(column=0,row=0)
b2.grid(column=1,row=0)
b3.grid(column=2,row=0)
b4.grid(column=0,row=1)
b5.grid(column=1,row=1)
b6.grid(column=2,row=1)
b7.grid(column=0,row=2)
b8.grid(column=1,row=2)
b9.grid(column=2,row=2)
# 

 

window.mainloop()
