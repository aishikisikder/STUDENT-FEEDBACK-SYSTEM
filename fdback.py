from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk() #create object
root.title('MINI PROJECT')

img = PhotoImage(file = '/home/aishiki/Downloads/logo.png')
label = Label(image = img)
label.pack()


frame_header = ttk.Frame(root)
frame_header.pack()

headerlabel = ttk.Label(frame_header,text='STUDENT FEEDBACK SYSTEM',foreground='dark green',font=('Times New Roman',24,'bold'))
headerlabel.grid(row=0, column=1)

messagelabel = ttk.Label(frame_header,text='This is the Feedback Window for the Workshop that held on 12th July,2022',foreground='blue',font=('Times New Roman', 12))
messagelabel.grid(row=1, column=1)


frame_content = ttk.Frame(root)
frame_content.pack()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

namelabel = ttk.Label(frame_content, text='Name',foreground='red')
namelabel.grid(row=0, column=0,pady=5,sticky='sw')
entry_name = ttk.Entry(frame_content,width=18,foreground='blue', font=('Arial', 12,), textvariable=var1)
entry_name.grid(row=0, column=1)

rollabel = ttk.Label(frame_content, text='Roll No',foreground='red')
rollabel.grid(row=0, column=2, pady=5,sticky='sw')
entry_roll = ttk.Entry(frame_content, width=14,foreground='blue',font=('Arial', 12,), textvariable=var2)
entry_roll.grid(row=0, column=3)

idlabel = ttk.Label(frame_content, text='Student ID',foreground='red')
idlabel.grid(row=1, column=0,pady=5,sticky='sw')
entry_id = ttk.Entry(frame_content, width=18,foreground='blue',font=('Arial', 12,), textvariable=var3)
entry_id.grid(row=1, column=1)


seclabel = ttk.Label(frame_content, text='Section',foreground='red')
seclabel.grid(row=1, column=2,pady=5, sticky='sw')
var4.set("Select Section")
entry_sec = OptionMenu(frame_content, var4,'A','B','C','D','E','F','G','H','I','J','K','L','M','N')
entry_sec.grid(row=1, column=3)


commentlabel = ttk.Label(frame_content, text='Workshop Feedback',font=('Arial',12),foreground='red')
commentlabel.grid(row=4, column=0,pady=5, sticky='sw')
textcomment = Text(frame_content, width=75,height=15)
textcomment.grid(row=5, column=0, columnspan=4)

textcomment.config(wrap ='word')
def clear():
    global entry_name
    global entry_roll
    global entry_id
    global entry_sec
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_roll.delete(0, END)
    entry_id.delete(0, END)
    var4.set("Select Section")
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_roll
    global entry_sec
    global entry_id
    global textcomment
    '''print('Name:{}'.format(var1.get()))
    print('Roll No:{}'.format(var2.get()))
    print('Student ID:{}'.format(var3.get()))
    print('Section:{}'.format(var4.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))'''
    Name = var1.get()
    RollNo = var2.get()
    StudentID = var3.get()
    Section = var4.get()
    Comment = textcomment.get(1.0, END)
    file = open('/home/aishiki/Documents/AISHI/feedback.txt','a')
    file.write("NAME: "+Name+'\n')
    file.write("ROLL NO.: "+RollNo+'\n')
    file.write("STUDENT ID: "+StudentID+'\n')
    file.write("SECTION: "+Section+'\n')
    file.write("FEEDBACK: "+Comment+'\n'+'\n')
    file.close()

    messagebox.showinfo(title='Submit', message='Thank you for your valuable feedback')
    entry_name.delete(0, END)
    entry_roll.delete(0, END)
    entry_id.delete(0, END)
    var4.set("Select Section")
    textcomment.delete(1.0, END)

    
submitbutton = ttk.Button(frame_content, text='Submit',command=submit).grid(row=6, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=6, column=3, sticky='w')

mainloop()
