#codsoft intern 1 project calculator using arithmetic operators
from tkinter import*
calculation = ""
def click(symbol):
    global passvalue
    text= symbol.widget.cget("text")
    print("text")
    if text == "=":
       if passvalue.get().isdigit():
          value = int(passvalue.get())
       else:
          value =eval(screen.get())
       
       passvalue.set(value)
       screen.update()
    elif text == "c":
       passvalue.set("")
       screen.update()
    else:
       passvalue.set(passvalue.get() + text)
       screen.update()
root =Tk()
root.geometry("330x350")
root.title("Aman's calculator")
passvalue = StringVar()
passvalue.set("")
screen = Entry(root, textvar=passvalue, font= "Arial 35 bold")
screen.pack(fill=X, ipadx= 10, pady = 12, padx = 12)
f = Frame(root, bg = "grey")
button1 = Button(f, text ="c", width = 5,fg = "red", font= ("Arial 15 bold "))
button1.pack(side= "left",anchor= "ne")
button1.bind("<Button-1>", click)
button2 = Button(f, text ="()", width = 5,fg = "green" ,font= ("Arial 15 bold "))
button2.pack(side="left",anchor= "ne")
button2.bind("<Button-1>", click)
button3 = Button(f, text ="%", width = 5,fg = "green" ,font= ("Arial 15 bold"))
button3.pack(side= "left" , anchor= "ne")
button3.bind("<Button-1>", click)
button4 = Button(f, text ="/", width = 5,fg = "green" ,font= ("Arial 15 bold"))
button4.pack(side="left" , anchor = "ne")
f.pack()

button4.bind("<Button-1>", click)
f = Frame(root, bg = "grey")
button5 = Button(f, text ="7", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button5.pack(side= "left", anchor= "ne")
button5.bind("<Button-1>", click)
button6 = Button(f, text ="8", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button6.pack(side= "left", anchor= "ne")
button6.bind("<Button-1>", click)
button7 = Button(f, text ="9", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button7.pack(side= "left",anchor= "ne")
button7.bind("<Button-1>", click)
button8 = Button(f, text ="*", width = 5,fg = "green" ,font= ("Arial 15 bold"))
button8.pack(side= "left",anchor= "ne")
button8.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg = "grey")
button9 = Button(f, text ="4", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button9.pack(side= "left",anchor= "ne")
button9.bind("<Button-1>", click)
button10 = Button(f, text ="5", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button10.pack(side= "left",anchor= "ne")
button10.bind("<Button-1>", click)
button11 = Button(f, text ="6", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button11.pack(side= "left",anchor= "ne")
button11.bind("<Button-1>", click)
button12 = Button(f, text ="-", width = 5,fg = "green" ,font= ("Arial 15 bold"))
button12.pack(side= "left",anchor= "ne")
button12.bind("<Button-1>", click)
f.pack()
f = Frame(root,bg = "grey")
button13 = Button(f, text ="1", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button13.pack(side= "left",anchor= "ne")
button13.bind("<Button-1>", click)
button14 = Button(f, text ="2", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button14.pack(side= "left",anchor= "ne")
button14.bind("<Button-1>", click)
button15 = Button(f, text ="3", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button15.pack(side= "left",anchor= "ne")
button15.bind("<Button-1>", click)
button16 = Button(f, text ="+", width = 5,fg = "green" ,font= ("Arial 15 bold"))
button16.pack(side= "left",anchor= "ne")
button16.bind("<Button-1>", click)
f.pack()
f= Frame(root, bg="grey")
button17 = Button(f, text ="//", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button17.pack(side= "left",anchor= "ne")
button17.bind("<Button-1>", click)
button18 =Button(f,text="0" , width = 5, fg = "black" , font= ("Arial 15 bold"))
button18.pack(side= "left",anchor= "ne")
button18.bind("<Button-1>", click)
button10 = Button(f, text= "**", width = 5,fg = "black" ,font= ("Arial 15 bold"))
button10.pack(side= "left",anchor= "ne")
button10.bind("<Button-1>", click)
button11 = Button(f, text= "=", width = 5,fg = "white" ,bg = "green",font= ("Arial 15 bold"))
button11.pack(side= "left",anchor= "ne")
button11.bind("<Button-1>", click)
f.pack()
root.mainloop()