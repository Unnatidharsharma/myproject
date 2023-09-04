# class Employee:
#     increment = 1.5
#     def __init__(self, lname, fname, salary):
#         self.lname = lname
#         self.fname = fname
#         self.salary = salary
#         #self.increment = 1.4
#     def inc(self):
#         self.salary = int(self.salary * self.increment)
# harry = Employee("harry", "jackson", 440000)
# rohan = Employee("rohan", "das", 44000)
# print(harry.salary)
# #print(harry.__dict__)
# harry.inc()
# print(harry.salary)


# class Atm:
#     def __init__(self):
#         self.pin =input
#         self.balance = 0
#     def get_balance(self):
#         return self.balance
#     def set_balance(self,new_value):
#         if type(new_value==int):
#             self.balnce = new_value
#         else:
#             print(self)


# class A:
#     def fun(self):
#         print("Poblic method")
#     def __fun(self):
#         print("Private method")
#     def help(self):
#         self.fun()
#         self.__fun()
# obj=A()
# obj.fun()
# obj.help()
# obj._A__fun()

# class Emp:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def info(self):
#         print("Id is: ", self.id)
#         print("Name is: ", self.name)
#         print("Salary is: ", self.salary)
#
#     def inc(self, per):
#         self.salary = self.salary + (self.salary) * per / 100
# id = input("Ener your Id: ")
# if(id=='8873830829' or id=='12345678'):
#     pass
#     name = input("Enter the name: ")
#     salary = int(input("Enter the salary: "))
# else:
#     exit("Wrong ID..\nPlease enter right ID")
# a = Emp(id,name,salary)
# a.info()
# per = int(input("Enter the increase persentage: "))
# a.inc(per)
# a.info()

## Write a program illustrating class definition and accessing class member.
# class Myclass:
#     a=100
#     def myfun(self,box):
#         self.box = box
#     def display(self):
#         print("value =",self.box)
# myboj = Myclass()
# print("Using class name",Myclass.a)
# print("Using object name",myboj.a)
# Myclass.a = 200
# print("After updating using calss name",Myclass.a)
# print("After updating using object name",myboj.a)
# val = int(input("Enter some value"))
# myboj.myfun(val)
# myboj.display()
# Myclass.myfun(myboj,val+100)
# Myclass.display(myboj)

## Write a program to implement defult constructor, parametrized c-onstructor, and destructor.








# default constructoer

# class MyClass:
#     def __init__(self):
#         print("My name is Unnatidhar Sharma")
#     def uds(self):
#         b = int(input("Enter the number: "))
#         if(b%2==0):
#             print("Even number")
#         else:
#             print("Odd number")
# a = MyClass()
# a.uds()

# parameterized consturtor

# class Student:
#     def __init__(self,name,age,id):
#         self.name = name
#         self.age = age
#         self.id = id
#     def info(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)
#
# a = Student("unnatidhar Sharma",20,2064)
# a.info()


# destructor

# class MyClass:
#     def __init__(self):
#         print("I am Unnatidhar Sharma")
#     def __del__(self):
#         print("Why are you doing this")
# a = MyClass()




# class Rectangle:
#     def __init__(self):
#         self.length = int(input("Enter the length:- "))
#         self.width = int(input("Enter the width:- "))
#     def info(self):
#        print("The Rectangle area is",self.length*self.width)
# a = Rectangle()
# a.info()

# class Claculator:
#     def __init__(self):
#         self.n1 = n1 = int(input("Enter the n1:- "))
#         self.n2 = n2 = int(input("Enter the n2:- "))
#     def add(self):
#         return self.n1+self.n2
#     def sub(self):
#         return self.n1-self.n2
#     def mul(self):
#         return self.n1*self.n2
#     def div(self):
#          return self.n1/self.n2
# a = Claculator()
# print("Add= ",a.add())
# print("Sub= ",a.sub())
# print("Mul= ",a.mul())
# print("Div= ",a.div())


# class MyClass:
#     def __init__(self,rollno,name):
#         self.rollno = rollno
#         self.name = name
#         self.marks = marks
#         self.subject = [math,physics,python]
#     def info(self):
#         return self.rollno
#     def name(self):
#         return self.name
#     def mark(self):
#         return self.marks.append(self.subject)
#     def total(self):
#         return self.marks.math`


# class Grendfather:
#     def __init__(self,grandfathername):
#         self.grandfathername=grandfathername
# class Father(Grendfather):
#     def __init__(self,fathername,grandfathername):
#         self.fathername=fathername
#         Grendfather.__init__(self,grandfathername)
# class Son(Father):
#     def __init__(self,sonname,fathername,grandfathername):
#         self.sonname=sonname
#         Father.__init__(self,fathername,grandfathername)
#     def print_name(self):
#         print("Grand Father name: ",self.grandfathername)
#         print("Father name: ",self.fathername)
#         print("son name: ",self.sonname)
# a=Son("Unnatibdhar Sharma","Dhanushdhar Sharma","Dharnidhar Sharma")
# print(a.grandfathername)
# a.print_name()




# class Uds:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def info(self):
#         print("PRESS 1:\nFill the details")
#         print("PRESS 2:\nAlready Filled")
#         self.a = int(input(":-- "))
#     def info2(self):
#         if(self.a==1):
#                 print("Ok! Fill The form")
#                 self.b=int(input("Enter the Physics no.:-- "))
#                 self.c=int(input("Enter the Python no.:-- "))
#                 self.d=int(input("Enter the Maths no:-- "))
#                 print("ThankYou for fill the details")
#                 self.total = self.b+self.c+self.d
#                 self.avg=self.total/3
#         elif(self.a==2):
#             print("Lol!")
#
#
#     def info3(self):
#         print("Name: ",self.name)
#         print("Roll No.: ",self.rollno)
#         print(self.b)
#         print(self.c)
#         print(self.d)
#         print("Total No is: ",self.total)
#         print("Average: ",self.avg)
# str=Uds((input("Enter the name:- ")),int(input("Enter the Roll number:-")))
# str.info()
# str.info2()
# str.info3()

# class Emp:
#     def __init__(self,name,salary,id):
#         self.name=name
#         self.salary=salary
#         self.id=id
#     def info(self,per):
#         self.per=per
#         self.inc = self.salary+self.salary*per/100
#     def info1(self):
#         print("Employee name: ",self.name)
#         print("Employee salary: ",self.salary)
#         print("Employee id: ",self.id)
#         print(" Employee Salary: ",self.salary)
#         print("Employee increment salary: ",self.inc)
# a = Emp(input("Enter the Employee name: "),int(input("Enter the Salary: ")),int(input("Enter the Employee id: ")))
# a.info(int(input("Enter the increment Persentage: ")))
# a.info1()






# class Atm:
#     def __init__(self,id,password,balance):
#         self.id=id
#         self.password=password
#         self.balance=balance
#     def info(self):
#         print("1. Press 1 to Check balance")
#         print("2. Press 2 to create pin")
#         print("3. Press 3 to change pin")
#         print("4. Press 4 to whithdraw")
#         print("5. Press 5 to exit")
#         self.a = int(input(":--"))
#     def check_bal(self):
#         if(self.a==1):
#
#             pin=int(input("Enter your pin: "))
#             if(pin==self.password):
#                 print("Your balance is: ",self.balance)
#             else:
#                 print("Wrong Pin")
#         else:
#             pass
#     def create_pin(self):
#         if(self.a==2):
#             pin1=int(input("Enter the pin: "))
#             if(pin1==self.password):
#                 self.psaaword=pin1
#                 print("Pin created Successfully")
#             else:
#                 print("Wrong Pin")
#         else:
#             pass
#     def change_pin(self):
#         if(self.a==3):
#             pin2 = int(input("Enter the pin: "))
#             if(pin2==self.password):
#                 print("OK")
#                 new_pin=int(input("Enter the new pin: "))
#                 pin2=new_pin
#                 print("Pin changed Successfully")
#             else:
#                 print("Wrong Pin")
#         else:
#             pass
#     def withdraw(self):
#         if(self.a==4):
#             pin3 = int(input("Enter the pin: "))
#             if (pin3 == self.password):
#                 print("OK")
#                 b = int(input("Enter the Withdraw Amount: "))
#                 c=self.balance-b
#                 self.balance=c
#                 print("Your remaining balance is: ",self.balance)
#             else:
#                 print("Wrong Pin")
#         else:
#             pass
#     def exit1(self):
#         if(self.a==5):
#             exit()
# p=Atm(int(input("Enter your id: ")),int(input("Enter your password: ")),int(input("Enter your balance: ")))
# p.info()
# p.check_bal()
# p.change_pin()
# p.create_pin()
# p.withdraw()


# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return self.length+2*self.width
# class squre(Rectangle):
#     def __init__(self,length):
#         super().__init__(length,length)
# a = squre(int(input("Enter the number:--")))
# print(a.area())
# print(a.perimeter())

# class Ai:
#     def question1(self):
#         self.a=input("Hello! how can i help you..\n:-")
#
#     def question2(self):
#         print("1. play game\n2. math\n3. any question")
#         self.c=input(":-")
#     def question3(self):
#         if(self.c=="1"):
#             print("ok\na. rock paper\n2.ludo ")
#             self.d = input(":-")
#     def info(self):
#         if(self.d==a):
#             print("ok")
#
#
#
# a=Ai()
# a.question1()
# a.question2()
# a.question3()


# class A:
#     def method(self):
#         print("A. method will be called")
# class B:
#     def method(self):
#         print("B. method will be called")
# class C(A,B):
#     pass
# class D(C,B):
#     pass
# d=D()
# d.method()
# for i in D.mro():
#     print(i)


# class Father:
#     def __init__(self):
#         super().__init__()
#         print("Father class will be run")
# class Mother:
#     def __init__(self):
#         super().__init__()
#         print("Mother class will be run")
# class Son(Mother,Father):
#     def __init__(self):
#         super().__init__()
#         Father().__init__()
#         print("Son class will be called")
# a=Son()


# class Student:
#      def __init__(self,name,age):
#          self.name = name
#          self.age = age
#      def display(self):
#          print("Name :",self.name)
#          print("Age :",self.age)
# S = Student("Kapil",18)
# print(isinstance(S,Student))
# S.display()

# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def info(self):
#         print("Name is: ",self.name)
#         print("ID is: ",self.id)
# a = Student(input("Enter the name: "),int(input("Enter the id: ")))
# a.info()
# print(isinstance(a,Student))


# class Student:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#     def info(self):
#         return self.n1*self.n2
# a = Student(5,7)
# print(a.info())
# class Child(Student):
#     def info1(self):
#         return self.n1/self.n2
# b=Child(10,2)
# print(b.info1())
# print(isinstance(a,Child))
# print(isinstance(b,Student))


# class Student:
#  def __init__(self,name,age):
#      self.name = name
#      self.age = age
#  def display(self):
#      print("Name :",self.name)
#      print("Age :",self.age)
# class Marks(Student):
#  def __init__(self,name,age,marks):
#      super().__init__(name,age)
#      self.marks = marks
#  def display(self):.
#      super().display()
#      print("Marks :",self.marks)
# S = Marks("Kapil",18,[78,88,91])
# print(issubclass(Marks,Student))

# a = []
# for i in range(10):
#     if i%2==0:
#         a.append(i)
# print(a)


# def my_decorator(func):
#     def wrapper():
#         print("*************")
#         func()
#         print("*************")
#     return wrapper()
# def hello():
#     print("hello")
# a=my_decorator(hello)


# import time
# def timer(func):
#     def info(*args):
#         a=time.time()
#         func(*args)
#         print("time taken by",func.__name__,time.time()-a,"sec")
#     return info
# @timer
# def hello():
#     print("hello world!")
#     time.sleep(2)
# @timer
# def power(num):
#     print(num**2)
#     time.sleep(1)
# @timer
# def square(a,b):
#     print(a**b)
#     time.sleep(4)
# hello()
# square(2)
# power(2,3)



# import tkinter
# m=tkinter.Tk()
# #m.mainloop()
#
# w=tkinter.Button(m,text="Hello",command=m.destroy)
# w.pack()
# m.mainloop()

# import tkinter
# def info():
#     print("Welcome to GUI")
# m=tkinter.Tk()
# w=tkinter.Button(m,text="Hello",command=info,width=30,bg="Green",activebackground="blue",activeforeground="red",font="black")
# w.pack()
# x=tkinter.Button(m,text="END",command=m.destroy,width=25,bg="white",activebackground="blue",activeforeground="red",font="black")
# x.pack()
# m.mainloop()

# from tkinter import *
# def info1():
#     text = entry.get()
#     print("Entered text: ",text)
# root = Tk()
# entry=Entry(root)
# entry.pack()
# button=Button(root,text="Submit",command=info1,width=15)
# button.pack()
# root.mainloop()

# from tkinter import *
# def info():
#     if var1.get():
#         print("Option 1 selected.")
#     if var2.get():
#         print("Option 2 selected.")
# root = Tk()
# var1=IntVar()
# var2=IntVar()
# checkbutton1=Checkbutton(root,text="Option 1",variable=var1)
# checkbutton2=Checkbutton(root,text="Option 2",variable=var2)
# button=Button(root,text="Submit",command=info,width=15)
# checkbutton1.pack()
# checkbutton2.pack()
# button.pack()
# root.mainloop()
#

# from tkinter import *
# def info():
#     if var.get()==1:
#         print("Operation 1 selected")
#     elif var.get()==2:
#         print("Operation 2 selected")
# root=Tk()
# var=IntVar()
# radiobutton1=Radiobutton(root,text="Option 1",variable=var,value=1)
# radiobutton2=Radiobutton(root,text="Option 2",variable=var,value=2)
# button=Button(root,text="Submit",command=info,width=15)
# button.pack()
# radiobutton1.pack()
# radiobutton2.pack()
# root.mainloop()

# from tkinter import *
# def display1():
#     a=[listbox.get(i) for i in listbox.curselection()]
#     print("Selected items: ",a)
# root=Tk()
# listbox=Listbox(root,selectmode=MULTIPLE)
# listbox.pack()
# listbox.insert(END,"Item 1")
# listbox.insert(END,"Item 2")
# listbox.insert(END,"Item 3")
# listbox.insert(END,"Item 4")
# button=Button(root,text="Submit",command=display1)
# button.pack()
# root.mainloop()

# from tkinter import *
# def display():
#     text = text_area.get("1.0",END)
#     print("Entered text: ",text)
# root=Tk()
# text_area=Text(root)
# text_area.pack()
# button=Button(root,text="Submit",command=display)
# button.pack()
# root.mainloop()

# from tkinter import *
# def info(value):
#     print("Selected value",value)
# root=Tk()
# scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=info)
# scale.pack()
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import Progressbar
# import time
# def info():
#     for i in range(101):
#         progress["value"]=i
#         root.update_idletasks()
#         time.sleep(0.1)
# root=Tk()
# progress=Progressbar(root,orient=HORIZONTAL,length=200,mode="determinate")
# progress.pack()
# button=Button(root,text="Start",command=info)
# button.pack()
# root.mainloop()


# from tkinter import *
# #def menu_action():
#     #print("menu operation selected.")
# def menu_time():
#     if var.get=="New":
#         from tkinter import Button
#         button=Button(root,text="Buy",command=menu_time)
#         #radiobutton1 = Radiobutton(root, text="Option 1",variable=var, value="New")
#         button.pack()
#         #radiobutton1.pack()
#         root.mainloop()
#
# root=Tk()
# var=StringVar
# menu1=Menu(root)
# root.config(menu=menu1)
# file_menu=Menu(menu1,tearoff=0)
# menu1.add_cascade(label="file",menu=file_menu)
# file_menu.add_command(label="New",command=menu_time)
# file_menu.add_command(label="Open",command=menu_time)
# file_menu.add_command(label="Exit",command=menu_time)
# root.mainloop()



# from tkinter import *
# def info():
#     def menu_time():
#         print("menu operation selected.")
#     def info2():
#         e = Tk()
#         button1 = Button(e, text="rock", command=menu_time)
#         button2 = Button(e, text="paper", command=info1)
#         button3 = Button(e, text="cuter", command=e.destroy)
#
#
#         button1.pack()
#         button2.pack()
#         button3.pack()
#         e.mainloop()
#
#     def info1():
#         b=Tk()
#         button=Button(b,text="Game",command=info2)
#         button.pack()
#         b.mainloop()
#
#     root=Tk()
#     menu1=Menu(root)
#     root.config(menu=menu1)
#     file_menu=Menu(menu1,tearoff=0)
#     menu1.add_cascade(label="file",menu=file_menu)
#     file_menu.add_command(label="New",command=info1)
#     file_menu.add_command(label="Open",command=info2)
#     file_menu.add_command(label="Exit",command=menu_time)
#     root.mainloop()
#
#
# root=Tk()
# var=StringVar()
# button=Button(root,text="Open",command=info,width=25)
# button.pack()
# root.mainloop()

# from tkinter import *
# def display_text():
#     text=entry.get()
#     print("Entered text: ",text)
# root=Tk()
# entry=Entry(root)
# entry.pack()
# button=Button(root,text="Submit",command=display_text)
# button.pack()
# root.mainloop()
#
#
# from tkinter import *
# from tkinter.ttk import Progressbar
# import time
# def update_progress():
#  for i in range(101):
#  progress['value'] = i
#  root.update_idletasks()
#  time.sleep(0.1)
# root = Tk()
# progress = Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
# progress.pack()
# button = Button(root, text="Start", command=update_progress)
# button.pack()
# root.mainloop()
#
#

# from tkinter import *
# def draw_shape():
#     canvas.create_rectangle(50,50,150,150,fill="blue")
#     canvas.create_oval(200,50,300,150,fill="red")
#     canvas.create_line(350,50,450,150,fill="green")
# root=Tk()
# canvas=Canvas(root,width=500,height=200)
# canvas.pack()
# button=Button(root,text="Draw",command=draw_shape)
# button.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# button=Button(root,text="Welcome",command=root.destroy,activebackground="Green",activeforeground="red",bd=10,bg="blue",
#               fg="yellow",font="Dark",height=10,highlightcolor="Orange",justify=RIGHT,pady=10,padx=40,relief=SUNKEN,
#               state=NORMAL,width=10,wraplength=100)
#
# button.pack()
# button.place(x=0,y=0)
# button.flash()
# root.mainloop()


#3. Entry: Create a text entry field and display the entered text.
# from tkinter import *
# def display_text():
#     text = entry.get()
#     print("Entered text:", text)
# root = Tk()
# entry = Entry(root,width=30)
# entry.pack()
# button = Button(root, text="Submit", command=display_text,height=0)
# button.pack()
# button.place(x=862,y=0)
# root.mainloop()



#4. Check button: Create a checkbox and display the selected options.
# from tkinter import *
# def display_options():
#     if var1.get():
#         print("Option 1 selected.")
#     if var2.get():
#         print("Option 2 selected.")
# root = Tk()
# var1 = IntVar()
# var2 = IntVar()
# checkbutton1 = Checkbutton(root, text="Option 1", variable=var1)
# checkbutton1.pack()
# checkbutton2 = Checkbutton(root, text="Option 2", variable=var2)
# checkbutton2.pack()
# button = Button(root, text="Submit", command=display_options)
# button.pack()
# root.mainloop()
#
# from tkinter import *
# root=Tk()
# entry=Entry(root,width=20)
# entry.pack()
# entry.place(x=400,y=0)
# entry=Entry(root,width=20)
# entry.pack()
# entry.place()
# entry=Entry(root,width=20)
# entry.pack()
# entry.place(x=1000,y=0)
# root.mainloop()



# a = [1,2,3,4,6,8]
# final_list = map(lambda x:2*x,a)
# print(list(final_list))

#
# import numpy as np
# from scipy.sparse.csgraph import connected_components
# from scipy.sparse import csr_matrix
# a = np.array([[0,1,2],[1,0,0],[2,0,0]])
# b= csr_matrix(a)
# print(connected_components(b))

# from matplotlib import pyplot
# a = [1,2,3,4,5,6,7,8,9]
# b = [55,75,96,75,36,45,87,99,100]
# pyplot.plot(a,b)
# pyplot.show()


# import ipywidgets as widgets
# from IPython.display import display
# name_text = widgets.Text(description='Name:')
# email_text = widgets.Text(description='Email:')
# submit_button = widgets.Button(description='Submit')
# validation_label = widgets.Label(value='')
# def handle_submission(b):
#     if not name_text.value or not email_text.value:
#         validation_label.value = 'Please fill in all fields.'
#     else:
#         validation_label.value = 'Form submitted successfully.'
# submit_button.on_click(handle_submission)
# display(name_text, email_text, submit_button, validation_label)
#
#
#

# def info(func):
#     def inner():
#         print("I got decorated")
#         func()
#
#     return inner
#
#
# def info1():
#     print("I am ordinary")