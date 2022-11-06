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
treev["columns"] = ("1", "2", "3")
 
# Defining heading
treev['show'] = 'headings'
 
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 150, anchor ='c')
treev.column("2", width = 150, anchor ='se')
treev.column("3", width = 150, anchor ='se')

 
# Assigning the heading names to the
# respective columns
treev.heading("1", text ="EMPID")
treev.heading("2", text ="NAME")
treev.heading("3", text ="Rating")


 
# Inserting the items and their features to the
# columns built
lst = []
with open('test2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(row)
a = len(lst)
print(a)
for i in range(1,a):
    treev.insert("", 'end', text ="L"+str(i),
             values =(lst[i][0], lst[i][1], lst[i][2]))
arr=lst[1:]
n=a-1
m=lst[1]
z=[]
k=[]
# for i in range(n):
#     z.append(int(arr[i][3]))
for i in range(n):
    k.append(int(arr[i][2]))


# def sort():
#     for item in treev.get_children():
#       treev.delete(item)
#     low_B = min(z)
#     upp_B = max(z)
#     b = [0 for i in range(n)]
# # initialize frequency
#     d = [0 for i in range(0, (upp_B - low_B + 1))]  # 0-n index
# # compute frequency of each item
#     for i in range(0, n):
#         j = int(arr[i][3]) - low_B
#         d[j] = d[j] + 1
# # compute sum of accumulated frequencies
#     for i in range(1, (upp_B - low_B + 1)):
#         d[i] = d[i] + d[i - 1]
# # access item and insert into sorted vector based onn distribution value
#     #st_time = time.time()
#     for i in range(n - 1, -1, -1):
#         j = int(arr[i][3])- low_B
#         d[j] = d[j] - 1
#         b[d[j]] = arr[i]
#     for i in range(0,n):
#         treev.insert("", 'end', text ="L"+str(i),
#              values =(b[i][0], b[i][1], b[i][2]))


def sort1():
    for item in treev.get_children():
      treev.delete(item)
    low_B = min(k)
    upp_B = max(k)
    b = [0 for i in range(n)]
# initialize frequency
    d = [0 for i in range(0, (upp_B - low_B + 1))]  # 0-n index
# compute frequency of each item
    for i in range(0, n):
        j = int(arr[i][2]) - low_B
        d[j] = d[j] + 1
# compute sum of accumulated frequencies
    for i in range(1, (upp_B - low_B + 1)):
        d[i] = d[i] + d[i - 1]
# access item and insert into sorted vector based onn distribution value
    #st_time = time.time()
    for i in range(n - 1, -1, -1):
        j = int(arr[i][2])- low_B
        d[j] = d[j] - 1
        b[d[j]] = arr[i]
    for i in range(0,n):
        treev.insert("", 'end', text ="L"+str(i),
             values =(b[i][0], b[i][1], b[i][2]))



B1 = Button( text ="Rating", command = sort1)
B1.place(x=500,y=450)
# B2 = Button( text ="Age", command = sort1)
# B2.place(x=300,y=450)

label1=Label(root,text="Sort the Discrect object  ",font=("Helvetica",15),fg="black",bg="white")
label1.place(x=120,y=100)

root.mainloop()