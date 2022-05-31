'''from tkinter import *

root=Tk()
root.title("Attendance System")
root.geometry("500x500")

#myButton= Button(root,text="Create")
#Button2= Button(root,text="Check")

font1=('Times',16,'normal')
k={'Create','Check'}
l=1
for j in k:
    e=Button(root,text=j,font=font1)
    e.grid(row=0,column=l,padx=2,pady=2)
    l=l+1
#myButton.place(relx=0.5,rely=0.5,anchor=CENTER)
#Button.place(relx=0.5,rely=0.5,anchor=CENTER)

#myButton.pack()
#Button2.pack()

#root.configure(width=200,height=500,background="yellow")

root.mainloop()

class CallPy(object):
   #
   def __init__(self,path='C:\\Users\\megha\Desktop\\Smart-Attendance-System\\1_datasetCreation.py'):
        self.path=path
        #print(path)
   def call_python_file(self):
        print(self.path)
        call(["Python3","{}".format(self.path)])

if __name__=="__main__":
     print("hello")

def onclick():
    c=CallPy()
    c.call_python_file()'''
from tkinter import * 
import datasetCreation as DC
import recognizingPersonwithCSVDatabase as rp
import trainingFaceML as TF

import preprocessingEmbeddings as PE



root= Tk()
root.geometry("600x400")  # Size of the window 
root.title("Attendance System")  # Adding a title
root["bg"]="#f7cac9"
font1=('Times',16,'normal')
'''
e1=Entry(root,width=20).place(x=150,y=180)
e1.pack()
e1.insert(0,"Name")

e2=Entry(root,width=20).place(x=200,y=180)
e2.pack()
     
     Name=e1.get()
     print(Name)
     rollno=e2.get() '''



e1=Entry(root,width=20)
e2=Entry(root,width=20)
label=Label(root,text="Enter Name")
label2=Label(root,text="Enter Pin Number")
label3=Label(root,text="NOTE:Please wait few minutes after submitting")

def Create():
     Name=e1.get()
     rollno=e2.get()

     bt.place(x=1800,y=1800)
     e1.place(x=1800,y=1800)
     e2.place(x=1800,y=1800)
     
     label2.place(x=1800,y=1800)
     label3.place(x=1800,y=1800)
     DC.createDataset(Name,rollno)
     label.place(x=1800,y=1800)
     
      
     PE.preprocessEmbeddings()
     TF.Training()
     mainButtons()

bt=Button(root,text="Submit",font=font1,background="yellow",relief=FLAT,
     cursor="hand2",activebackground="#FFEA00",command=Create)
def takeDetails():
    btn.place(x=1800,y=1800)
    btn2.place(x=1800,y=1800)
     
    
    label.place(x=160,y=100)   
    e1.place(x=160,y=130)


    label2.place(x=310,y=100)    
    e2.place(x=310,y=130) 
    label3.place(x=200,y=260)  
    bt.place(x=270,y=180)
    #label=Label(root,text="Please wait few minutes for processing")
    #label.place(x=200,y=100)
        



def Check():
     rp.final()

btn=Button(root,text="Create",font=font1,background="yellow",relief=FLAT,
     cursor="hand2",activebackground="#FFEA00",command=takeDetails)
btn2=Button(root,text="Check",font=font1,background="yellow",relief=FLAT,
     cursor="hand2",activebackground="#FFEA00",command=Check)


def mainButtons():     
     btn.place(x=200,y=140)
     btn2.place(x=350,y=140)


mainButtons()



root.mainloop()