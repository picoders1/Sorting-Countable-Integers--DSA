import csv
from tkinter import *

import tkinter as tk
from tkinter import ttk 


root=Tk()
root.title("DSA ")
root.geometry("900x550+300+200")
root.resizable(False,False)
root.configure(bg="White")

Si1=PhotoImage(file="rv.png")
myimage1=Label(image=Si1,bg="white")
myimage1.place(x=700,y=0)
label1=Label(root,text=" DSA ASSIGNEMENT  ",font=("Helvetica",15),fg="black",bg="white")
label1.place(x=80,y=20)

treev = ttk.Treeview(root, selectmode ='browse')
treev.place(x=180,y=180)
#treev.pack(side ='right')
 
# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(root,
                           orient ="vertical",
                           command = treev.yview)
 
# Calling pack method w.r.to vertical
# scrollbar
verscrlbar.pack(side ='right', fill ='x')
 
# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)
 
# Defining number of columns
treev["columns"] = ("1", "2", "3","4")
 
# Defining heading
treev['show'] = 'headings'
 
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 150, anchor ='c')
treev.column("2", width = 150, anchor ='se')
treev.column("3", width = 150, anchor ='se')
treev.column("4",width=150,anchor='se')
 
# Assigning the heading names to the
# respective columns
treev.heading("1", text ="EMPID")
treev.heading("2", text ="NAME")
treev.heading("3", text ="Age")
treev.heading("4",text="Salary")

 
# Inserting the items and their features to the
# columns built
lst = []
with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(row)
a = len(lst)
print(a)
for i in range(1,a):
    treev.insert("", 'end', text ="L"+str(i),
             values =(lst[i][0], lst[i][1], lst[i][2],lst[i][3]))
arr=lst[1:]
n=a-1
m=lst[1]
z=[]
k=[]
for i in range(n):
    z.append(int(arr[i][3]))
for i in range(n):
    k.append(int(arr[i][2]))


def sort():
    for item in treev.get_children():
      treev.delete(item)
    b = [0 for i in range(n)]
    c = [0 for i in range(n)]
    #st_time = time.time()
    for i in range(0, n - 1):  # (element 1 till (n) th)
        for j in range((i + 1), n):  # (element 2 till n th)
            if int(arr[i][3]) < int(arr[j][3]):
                c[j] = c[j] + 1
            else:
                c[i] = c[i] + 1
    for i in range(n):
        b[c[i]] = arr[i]
    for i in range(0,n):
        treev.insert("", 'end', text ="L"+str(i),
             values =(b[i][0], b[i][1], b[i][2],b[i][3]))

def sort1():
     for item in treev.get_children():
      treev.delete(item)
     b = [0 for i in range(n)]
     c = [0 for i in range(n)]
    #st_time = time.time()
     for i in range(0, n - 1):  # (element 1 till (n) th)
        for j in range((i + 1), n):  # (element 2 till n th)
            if int(arr[i][2]) < int(arr[j][2]):
                c[j] = c[j] + 1
            else:
                c[i] = c[i] + 1
     for i in range(n):
        b[c[i]] = arr[i]
     for i in range(0,n):
        treev.insert("", 'end', text ="L"+str(i),
             values =(b[i][0], b[i][1], b[i][2],b[i][3]))


B1 = Button( text ="Salary", command = sort)
B1.place(x=500,y=450)
B2 = Button( text ="Age", command = sort1)
B2.place(x=300,y=450)

label1=Label(root,text="Sort the Discrect object  ",font=("Helvetica",15),fg="black",bg="white")
label1.place(x=120,y=100)

root.mainloop()