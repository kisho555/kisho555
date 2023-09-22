from tkinter import *
from tkinter import messagebox

#address book -initalize window
root = Tk()
root.geometry('700x550')
root.config(bg = '#d3f3f5')
root.title('PythonGeeks Contact Book')
root.resizable(0,0)
contactlist=[['Emily Davis','45747448'],['Theodore Dinh','76969696969'],['Luna Sanders','679767697'],['Joshua Gupta','5090747775'],
             ['Madeline Walker','6467460460'],['Camila Rogers','088088008'],['Bella Powell','6548367453'],['Madeline Walker','0909090909'],
             ['Camila Rogers','3456789009876'],['Daniel Richardson','09876556789'],['Jameson Alvarado','0757645638'],['Skylar Watson','0980798676857']   
]

Name = StringVar()
Number = StringVar()


frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame,orient=VERTICAL)
select = Listbox(frame,yscrollcommand=scroll.set ,font=('times new roman',16),
         bg="#f0fffc", width=20, height=20,borderwidth=3, relief="groove")

scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT ,fill=BOTH, expand=1)
def selected():
    print ("hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error","Please Select the Name")
    else:
        return int(select.curselection()[0])
    
def AddContact():
    if Name.get()!=""and Number.get()!="":
           contactlist.append([Name.get(),Number.get()])
           print(contactlist)
           select_set()
           EntryReset()
           messagebox.showinfo("Conformation","Successfully Add New Contact")
           
    else:
        messagebox.showerror("Error","Please Fill the information")
        
def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[selected()]=[Name.get(), Number.get()] 
        messagebox.showinfo("Confirmation","Successfully Update Contact")  
        EntryReset()
        Select_set()
        
    elif not(Name.get()) and not (Number.get()) and not (len(select.curselection())==0):
        messagebox.showerror("Error","Please fill the information")
    
    else:
        if len (select.columnconfigure())==0:
            messagebox.showerror("Error","Please Selecet the Name and \n press Load bitton")
        else:
            Message1 = """ To Load All information of \n seleted row press load button \n
            """ 
            messagebox.showerror("Error",Message1)                                                 
                                                    
    