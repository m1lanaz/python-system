#All my imported modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
from customers import *
from orders import *
from tasks import *
from tkinter import ttk
import csv
from staff import *



# This is the class that holds all my GUI related items, my GUI and my GUI functions
class mySystem():
        # This is my initialiser function, it declares all my key screens
        def __init__(self, window):
            # This is the overall window for my tkinter and it's got all the configuration that applies to all frames
            window.geometry("1100x700")
            window.configure(bg = "#EBE8E2", cursor="dot") 
            # Menu frame frame, pack propogate is so the width and height gets
            self.menu_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.menu_frame.pack_propagate(0)
            self.setMenuFrame()
            # Staff frame
            self.staff_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.staff_frame.pack_propagate(0)
            self.setStaffFrame()
            # Admin frame
            self.admin_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.admin_frame.pack_propagate(0)
            self.setAdminFrame()
            # Customer frame
            self.customerProfile_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.customerProfile_frame.pack_propagate(0)
            self.setCustomerProfileFrame()
            # Orders frame
            self.orders_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.orders_frame.pack_propagate(0)
            self.setOrders()
            # Tasks frame
            self.tasks_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.tasks_frame.pack_propagate(0)
            self.setTasksFrame()
            # Staff log in frame
            self.staffLogIn_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.staffLogIn_frame.pack_propagate(0)
            self.setAdminlogInSectionFrame()
            # Staff Admin frame 
            self.adminStaff_frame = Frame(window, bg="#EBE8E2", width="1100", height="700")
            self.adminStaff_frame.pack_propagate(0)
            self.setAdminStaffFrame()
            # Packging menu frame so it loads straight away
            self.menu_frame.pack()
            
        def setMenuFrame(self):
            #creates a label to display menu
            self.lbl_one = Label(self.menu_frame, text="Menu", font=("Open Sans", 80, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="40", x="410")
            
            #These buttons let me navigate to different frames using the commands attached
            self.buttonOne = Button(self.menu_frame, text="Admin Section", command =self.goAdminlogInSectionFrame, relief="ridge", bg ="#D5A6BD", height=8 , width=80, font=("Open Sans", 12, "bold"),activebackground="#e3c8d5", fg="white", activeforeground="white" )
            self.buttonOne.place(y="200", x="150")
            self.buttonTwo = Button(self.menu_frame, text="Staff Section", command =self.goStaffSectionFrame, relief="ridge", height=8 , width=80, font=("Open Sans", 12, "bold"),  bg ="#D5A6BD",activebackground="#e3c8d5",fg="white", activeforeground="white")
            self.buttonTwo.place(y="400", x="150")      

        def setAdminlogInSectionFrame(self):
            # Back to main menu button to take me back to main menu
            self.btn_toBFrame = Button(self.staffLogIn_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="50", x="70")
            # Label that tells the user this is the log in screen 
            self.lbl_one = Label(self.staffLogIn_frame, text="Log In", font=("Open Sans", 80, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="40", x="410")
            # Entry boxes that allow user to input their username and password, these are used with the .get function later in the program
            self.userName = Entry(self.staffLogIn_frame, font=("Open Sans", 10, "bold"), width= 20)
            self.userName.place(y="200", x="425")
            self.passWord = Entry(self.staffLogIn_frame, font=("Open Sans", 10, "bold"), width= 20, show="*")
            self.passWord.place(y="300", x="425")
            # Labels that display what entry box is for username and which for password
            self.lbl_one = Label(self.staffLogIn_frame, text="Username: " ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(x="225", y="180")
            self.lbl_one = Label(self.staffLogIn_frame, text="Password: " ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(x="225", y="280")
            # button to log in, funs logIntoAdmin command which uses .get on previous entries
            self.button = Button(self.staffLogIn_frame, text="Log in", command=self.logIntoAdmin,relief="ridge", height=4 , width=40, font=("Open Sans", 12, "bold"),  bg ="#D5A6BD",activebackground="#e3c8d5",fg="white", activeforeground="white")
            self.button.place(y="400", x="260")

        def setAdminStaffFrame(self):
            # creates a label to display that this is the admin section
            self.lbl_one = Label(self.adminStaff_frame, text="Staff List + Order prices", font=("Open Sans", 50, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="10", x="310")
            # Back to main menu button to take me back to main menu
            self.btn_toBFrame = Button(self.adminStaff_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="50", x="70")
            
            #Treeview display
            self.lbl_one = Label(self.adminStaff_frame, text="Staff" ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(y="157", x="741")
            # This is the columns list and its used for header columns
            columns = ("StaffID", "Staff name","Pay rate","Hours worked")
            self.tree4 = ttk.Treeview(self.adminStaff_frame, columns=columns ,height = 20)
            self.tree4.place(y="210", x="590")
            # Hides the 0 index column that treeview automatically creates
            self.tree4.heading("#0", text=" ")
            self.tree4.column('#0', anchor=CENTER, stretch=NO, width=0)
            #Creates columns for treeview
            for i in range(len(columns)):
                #Creates heading with the column index name and makes them a width of 100
                self.tree4.heading(columns[i], text = columns[i])
                self.tree4.column(columns[i], anchor=CENTER, stretch=NO, width=100)
            # Calls csvToTreeview from taks.csv into treeview
            self.csvToTreeview("staff.csv", "staff")
            
            #Update staff wage
            self.lbl_one = Label(self.adminStaff_frame, text="Update pay:",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="127", x="190")
            self.staffIdToUpdateWage = Entry(self.adminStaff_frame, font=("Open Sans", 10, "bold"))
            self.staffIdToUpdateWage.place(width=100, x="150", y="170")
            self.lbl_one = Label(self.adminStaff_frame, text="Staff ID", font=("Open Sans", 12, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="169", x="90")
            self.newPay = Entry(self.adminStaff_frame, font=("Open Sans", 10, "bold"))
            self.newPay.place(width=100, x="150", y="200")
            self.lbl_one = Label(self.adminStaff_frame, text="New wage", font=("Open Sans", 12, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="199", x="60")
            # Button when pressed calls command updatetask
            self.btn_toBFrame = Button(self.adminStaff_frame, text="Update Pay", command = lambda: self.updateWage(), relief="ridge", bg ="#D5A6BD", height=1 , width=20, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="200", x="260")
            
            #Update staff hours
            self.lbl_one = Label(self.adminStaff_frame, text="Add hours:",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="250", x="190")
            self.updateValueEntry = Entry(self.adminStaff_frame, font=("Open Sans", 10, "bold"))
            self.updateValueEntry.place(width=100, x="150", y="280")
            self.lbl_one = Label(self.adminStaff_frame, text="Staff ID", font=("Open Sans", 12, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="280", x="90")
            self.addHours = Entry(self.adminStaff_frame, font=("Open Sans", 10, "bold"))
            self.addHours.place(width=100, x="150", y="310")
            self.lbl_one = Label(self.adminStaff_frame, text="Hours worked", font=("Open Sans", 12, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="310", x="30")
            # Button when pressed calls command updatetask
            self.btn_toBFrame = Button(self.adminStaff_frame, text="Add hours", command = lambda: self.updateHours(), relief="ridge", bg ="#D5A6BD", height=1 , width=20, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="310", x="260")
            
            #See staff earnt
            self.lbl_one = Label(self.adminStaff_frame, text="Calculate pay:",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="350", x="190")
            self.staffIdToCalc = Entry(self.adminStaff_frame, font=("Open Sans", 10, "bold"))
            self.staffIdToCalc.place(width=100, x="150", y="390")
            self.lbl_one = Label(self.adminStaff_frame, text="StaffID:", font=("Open Sans", 12, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="390", x="60")
            # Button when pressed calls command updatetask
            self.btn_toBFrame = Button(self.adminStaff_frame, text="Calculate", command = lambda: self.calculatePay(), relief="ridge", bg ="#D5A6BD", height=1 , width=20, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="390", x="260")
            
        def setStaffFrame(self):
            # Back to main menu button to take me back to main menu
            self.btn_toBFrame = Button(self.staff_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="50", x="70")
            # Label to tell user this is the staff section
            self.lbl_one = Label(self.staff_frame, text="Staff Section", font=("Open Sans", 80, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="10", x="350")                        
            #button to take you to the order screen
            self.btn_toBFrame = Button(self.staff_frame, text="ORDER SECTION", command =self.goOrdersFrame, bg ="#D5A6BD", height=8 , width=80, font=("Open Sans", 12, "bold"),activebackground="#e3c8d5", fg="white", activeforeground="white" )
            self.btn_toBFrame.place(y="150",x="150")
            #button to take you to customer screen
            self.btn_toBFrame = Button(self.staff_frame, text="CUSTOMER SECTION", command =self.goCSFrame, bg ="#D5A6BD", height=8 , width=80, font=("Open Sans", 12, "bold"),activebackground="#e3c8d5", fg="white", activeforeground="white" )
            self.btn_toBFrame.place(y="320",x="150")
            #button to take you to task screen
            self.btn_toBFrame = Button(self.staff_frame, text="TASK SECTION", command =self.goTasksFrame, bg ="#D5A6BD", height=8 , width=80, font=("Open Sans", 12, "bold"),activebackground="#e3c8d5", fg="white", activeforeground="white" )
            self.btn_toBFrame.place(y="490",x="150")
            


        def setAdminFrame(self):
            # creates a label to display that this is the admin section
            self.lbl_one = Label(self.admin_frame, text="Admin Section", font=("Open Sans", 80, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="10", x="310")
            # Back to main menu button to take me back to main menu
            self.btn_toBFrame = Button(self.admin_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="50", x="70")

            
            #Treeview display
            self.lbl_one = Label(self.admin_frame, text="Tasks" ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(y="157", x="741")
            # This is the columns list and its used for header columns
            columns = ("TaskID", "Task Descrition","Task Status")
            self.tree3 = ttk.Treeview(self.admin_frame, columns=columns ,height = 20)
            self.tree3.place(y="210", x="550")
            # Hides the 0 index column that treeview automatically creates
            self.tree3.heading("#0", text=" ")
            self.tree3.column('#0', anchor=CENTER, stretch=NO, width=0)
            #Creates columns for treeview
            for i in range(len(columns)):
                #Task description is selected with an if statement as it needs a larger width
                if columns[i] == "Task Descrition":
                    self.tree3.heading(columns[i], text = columns[i])
                    self.tree3.column(columns[i], anchor=CENTER, stretch=NO, width=250)
                    continue
                #Creates heading with the column index name and makes them a width of 100
                self.tree3.heading(columns[i], text = columns[i])
                self.tree3.column(columns[i], anchor=CENTER, stretch=NO, width=100)
            # Calls csvToTreeview from taks.csv into treeview
            self.csvToTreeview("tasks.csv", "tasksAdmin")

            #Sets buttons for sorts
            self.lbl_one = Label(self.admin_frame, text="Sort List" ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(y="157", x="190")
            self.btn_toBFrame = Button(self.admin_frame, text="Sort by progress ⬇", command =lambda: self.sortTasksProgress("down"), relief="ridge", bg ="#D5A6BD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="210", x="30")
            self.btn_toBFrame = Button(self.admin_frame, text="Sort by progress ⬆", command =lambda: self.sortTasksProgress("up"), relief="ridge", bg ="#D5A6BD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="210", x="260")

            #The searches
            self.lbl_one = Label(self.admin_frame, text="Search",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="270", x="190")
            self.taskEntry = Entry(self.admin_frame, font=("Open Sans", 10, "bold"))
            self.taskEntry.place(width=100, x="150", y="315")
            # Button when pressed calls command searchInList
            self.btn_toBFrame = Button(self.admin_frame, text="🔍", command =lambda: self.searchInList(self.taskEntry, 1), relief="ridge", bg ="#D5A6BD", height=0 , width=0, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="310", x="260")

            #Add a task
            self.lbl_one = Label(self.admin_frame, text="Add Task",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="350", x="185")
            self.taskDesc = Entry(self.admin_frame, font=("Open Sans", 10, "bold"), )
            self.taskDesc.place(y="390", x="65")
            # Button when pressed calls command addTask
            self.btn_toBFrame = Button(self.admin_frame, text="Add Task", command =lambda: self.addTask(), relief="ridge", bg ="#D5A6BD", height=0 , width=0, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="385", x="260")

            #Delete a task
            self.lbl_one = Label(self.admin_frame, text="Delete Task",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="420", x="175")
            self.lbl_one = Label(self.admin_frame, text="Task Number:",font=("Open Sans", 10, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="460", x="115")
            self.toDeleteTask = Entry(self.admin_frame, font=("Open Sans", 10, "bold"))
            self.toDeleteTask.place(width=100, x="220", y="460")
            # Button when pressed calls command deleteTask to delete the task
            self.btn_toBFrame = Button(self.admin_frame, text="Delete task", command =lambda: self.deleteTask(), relief="ridge", bg ="#D5A6BD", height=0 , width=0, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="490", x="190")

            #Staff navigation
            self.btn_toBFrame = Button(self.admin_frame, text="Staff Profiles", command =lambda: self.goAdminStaffFrame() , relief="ridge", bg ="#D5A6BD", height=3 , width=30, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="540", x="100")

        def setCustomerProfileFrame(self):
            # Label so user knows this is the customer profiles section
            self.lbl_one = Label(self.customerProfile_frame, text="Customer Section", font=("Open Sans", 70, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="10", x="260")
            #button to go back to main menu
            self.btn_toBFrame = Button(self.customerProfile_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="40", x="30")
            
            # Create a new customer profile 
            self.lbl_one = Label(self.customerProfile_frame, text="Create Customer Profiles", font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="140", x="35")
            #Labels and entries for the values needed to create a customer profile
            self.lbl_one = Label(self.customerProfile_frame, text="First name:", font=("Open Sans", 15, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="180")
            self.cFirstName = Entry(self.customerProfile_frame, font=("Open Sans", 10, "bold"))
            self.cFirstName.place(width=100, x="160", y="186")
            self.lbl_one = Label(self.customerProfile_frame, text="Surname:", font=("Open Sans", 15, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="210")
            self.cLastName = Entry(self.customerProfile_frame, font=("Open Sans", 10, "bold"))
            self.cLastName.place(width=100, x="160", y="216")
            self.lbl_one = Label(self.customerProfile_frame, text="Phone number:", font=("Open Sans", 11, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="240")
            self.phoneNumber = Entry(self.customerProfile_frame, font=("Open Sans", 10, "bold"))
            self.phoneNumber.place(width=100, x="160", y="246")
            self.lbl_one = Label(self.customerProfile_frame, text="Date of birth:", font=("Open Sans", 11, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="270")
            self.DOB = Entry(self.customerProfile_frame, font=("Open Sans", 10, "bold"))
            self.DOB.place(width=100, x="160", y="276")
            self.lbl_one = Label(self.customerProfile_frame, text="Time of birth:", font=("Open Sans", 11, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="300")
            self.TOB = Entry(self.customerProfile_frame, font=("Open Sans", 10, "bold"))
            self.TOB.place(width=100, x="160", y="306")
            # Button to create a customer, this calls the command tocreate a customer which uses .get on the previous entries
            self.ButtonForCust = Button(self.customerProfile_frame, text="Create Customer", command =lambda:  self.addCustomer() ,relief="ridge", height=1 , width=10, font=("Open Sans", 8, "bold"),  bg ="#70AD47",activebackground="#70AD47",fg="white", activeforeground="white")            
            self.ButtonForCust.place(x="160", y="336",width=100)
            
            # Delete a customer profile
            self.lbl_one = Label(self.customerProfile_frame, text="Delete customer",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="360", x="40")
            # All entries needed to delete a customer (we only require the customer number)
            self.lbl_one = Label(self.customerProfile_frame, text = "enter customer # to delete:", font=("Open Sans", 10, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="390", x="40")
            self.userToDelete = Entry(self.customerProfile_frame, font=("Open Sans", 10, "bold"))
            self.userToDelete.place(width=100, x="218", y="396")
            # Button to delete a customer, calls delete customer command andthis will .get customer number to find a reference for what to delete
            self.ButtonToDelete = Button(self.customerProfile_frame, text="Delete", command=lambda: self.deleteCustomer() ,relief="ridge", height=1 , width=10, font=("Open Sans", 12, "bold"),  bg ="#F13B30",activebackground="#F13B30",fg="white", activeforeground="white")
            self.ButtonToDelete.place(x="160", y="420",width=100)
            
            #sort customer profiles
            self.lbl_one = Label(self.customerProfile_frame, text="Sort customers",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="460", x="40")
            self.ButtonTosort = Button(self.customerProfile_frame, text="Sort A - Z", command= lambda: self.sortCustomers() ,relief="ridge", height=1 , width=10, font=("Open Sans", 12, "bold"),  bg ="#D5A6BD",activebackground="#e3c8d5",fg="white", activeforeground="white")
            self.ButtonTosort.place(x="80", y="490",width=100)

            #Display customer profiles
            self.lbl_one = Label(self.customerProfile_frame, text="Customer Profiles", font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="139", x="580")
            #Treeview, column list used to set headers for columns
            columns = ("CustomerID","Name", "Surname", "Phone Number", "DOB", "TOB")
            self.tree2 = ttk.Treeview(self.customerProfile_frame, columns=columns ,height = 20)
            self.tree2.place(y="180", x="400")            
            # Sets the default treeview column to empty
            self.tree2.heading("#0", text=" ")
            self.tree2.column('#0', anchor=CENTER, stretch=NO, width=0)
            # Creates columns with headers from column list
            for i in range(len(columns)):
                self.tree2.heading(columns[i], text = columns[i])
                self.tree2.column(columns[i], anchor=CENTER, stretch=NO, width=100)
            # Calls csvToTreeview function, to copy the csv "customerProfiles" into the treeview
            self.csvToTreeview("CustomerProfiles.csv", "customers")
                
        def setOrders(self):
            #creates a label to display that this is the orders section
            self.lbl_one = Label(self.orders_frame, text="Order Section", font=("Open Sans", 80, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="10", x="310")
            
            #button to go back to main menu
            self.btn_toBFrame = Button(self.orders_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="50", x="70")
                
            #create orders section
            self.lbl_one = Label(self.orders_frame, text="Create orders:", font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="140", x="35")
            self.lbl_one = Label(self.orders_frame, text="Customer number:", font=("Open Sans", 10, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="180")
            self.customerNum = Entry(self.orders_frame, font=("Open Sans", 10, "bold"))
            self.customerNum.place(x="167", y="183")
            self.lbl_one = Label(self.orders_frame, text="Order type:",  font=("Open Sans", 10, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="210")
            self.type = Entry(self.orders_frame, font=("Open Sans", 10, "bold"))
            self.type.place(x="167", y="213")
            self.lbl_one = Label(self.orders_frame, text=" 1 - Full year career reading",  font=("Open Sans", 8, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="240")
            self.lbl_one = Label(self.orders_frame, text=" 2 - Half year career reading",  font=("Open Sans", 8, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="260")
            self.lbl_one = Label(self.orders_frame, text=" 3 - Full year life reading",  font=("Open Sans", 8, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="280")
            self.lbl_one = Label(self.orders_frame, text=" 4 - Half year life reading",  font=("Open Sans", 8, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="300")
            self.lbl_one = Label(self.orders_frame, text=" 5 - Full year love reading",  font=("Open Sans", 8, "bold"), bg="#EBE8E2")
            self.lbl_one.place(x="40", y="320")
            # Button to create order
            self.ButtonForOrder = Button(self.orders_frame, text="Create Order", command = self.addOrder,relief="ridge", height=1 , width=10, font=("Open Sans", 8, "bold"),  bg ="#70AD47",activebackground="#70AD47",fg="white", activeforeground="white")            
            self.ButtonForOrder.place(x="167", y="340",width=100)
            
            #Display orders section
            self.lbl_one = Label(self.orders_frame, text="Orders" ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(y="149", x="755")
            # Columns list for the headers to columns
            columns = ("OrderID","CustomerID", "order type", "price","staff" ,"Status")
            self.tree1 = ttk.Treeview(self.orders_frame, columns=columns ,height = 20)
            self.tree1.place(y="180", x="490")            
            # Sets the size to treeviews default 0 column to 0 so its not displayed
            self.tree1.heading("#0", text=" ")
            self.tree1.column('#0', anchor=CENTER, stretch=NO, width=0)
            # For loop to create a new header column
            for i in range(len(columns)):
                self.tree1.heading(columns[i], text = columns[i])
                self.tree1.column(columns[i], anchor=CENTER, stretch=NO, width=100)
            # Calls csvToTreeview from orders.csv into treeview
            self.csvToTreeview("orders.csv", "orders")
            
            #Search through orders
            self.lbl_one = Label(self.orders_frame, text="Search using Customer ID",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="370", x="100")
            self.searchValueEntry2 = Entry(self.orders_frame, font=("Open Sans", 10, "bold"))
            self.searchValueEntry2.place(width=100, x="150", y="410")
            # Button when pressed calls command searchInList
            self.btn_toBFrame = Button(self.orders_frame, text="🔍", command =lambda: self.binarySearchList(1,1), relief="ridge", bg ="#D5A6BD", height=0 , width=0, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="410", x="260")
            
            self.lbl_one = Label(self.orders_frame, text="Search using Order ID",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="465", x="100")
            self.searchValueEntry1 = Entry(self.orders_frame, font=("Open Sans", 10, "bold"))
            self.searchValueEntry1.place(width=100, x="150", y="510")
            # Button when pressed calls command searchInList
            self.btn_toBFrame = Button(self.orders_frame, text="🔍", command =lambda: self.binarySearchList(0,2), relief="ridge", bg ="#D5A6BD", height=0 , width=0, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="510", x="260")
            

        def setTasksFrame(self):
            #creates a label to display that this is the tasks section
            self.lbl_one = Label(self.tasks_frame, text="Task Section", font=("Open Sans", 80, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="10", x="350")
            
            #button to go back to main menu
            self.btn_toBFrame = Button(self.tasks_frame, text="BACK TO MAIN MENU", command =self.goMainMenuFrame, relief="ridge", bg ="#C7C2AD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="55", x="70")
            
            #Treeview display
            self.lbl_one = Label(self.tasks_frame, text="Tasks" ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(y="157", x="741")
            # This is the columns list and its used for header columns
            columns = ("TaskID", "Task Descrition","Task Status")
            self.tree = ttk.Treeview(self.tasks_frame, columns=columns ,height = 20)
            self.tree.place(y="210", x="550")
            # Hides the 0 index column that treeview automatically creates
            self.tree.heading("#0", text=" ")
            self.tree.column('#0', anchor=CENTER, stretch=NO, width=0)
            #Creates columns for treeview
            for i in range(len(columns)):
                #Task description is selected with an if statement as it needs a larger width
                if columns[i] == "Task Descrition":
                    self.tree.heading(columns[i], text = columns[i])
                    self.tree.column(columns[i], anchor=CENTER, stretch=NO, width=250)
                    continue
                #Creates heading with the column index name and makes them a width of 100
                self.tree.heading(columns[i], text = columns[i])
                self.tree.column(columns[i], anchor=CENTER, stretch=NO, width=100)
            # Calls csvToTreeview from taks.csv into treeview
            self.csvToTreeview("tasks.csv", "tasks")

            #Sets buttons for sorts
            self.lbl_one = Label(self.tasks_frame, text="Sort List" ,font=("Open Sans", 20, "bold"), bg="#EBE8E2" )
            self.lbl_one.place(y="157", x="190")
            self.btn_toBFrame = Button(self.tasks_frame, text="Sort by progress ⬇", command =lambda: self.sortTasksProgress("down"), relief="ridge", bg ="#D5A6BD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="210", x="30")
            self.btn_toBFrame = Button(self.tasks_frame, text="Sort by progress ⬆", command =lambda: self.sortTasksProgress("up"), relief="ridge", bg ="#D5A6BD", height=2 , width=20, font=("Open Sans", 12, "bold"),activebackground="#C7C2AD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="210", x="260")

            #The searches
            self.lbl_one = Label(self.tasks_frame, text="Search",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="280", x="190")
            self.searchValueEntry = Entry(self.tasks_frame, font=("Open Sans", 10, "bold"))
            self.searchValueEntry.place(width=100, x="150", y="340")
            # Button when pressed calls command searchInList
            self.btn_toBFrame = Button(self.tasks_frame, text="🔍", command =lambda: self.searchInList(self.searchValueEntry, 1), relief="ridge", bg ="#D5A6BD", height=0 , width=0, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="340", x="260")
            
            #Update Task
            self.lbl_one = Label(self.tasks_frame, text="Update:",font=("Open Sans", 20, "bold"), bg="#EBE8E2")
            self.lbl_one.place(y="400", x="190")
            self.updateValueEntry1 = Entry(self.tasks_frame, font=("Open Sans", 10, "bold"))
            self.updateValueEntry1.place(width=100, x="150", y="450")
            # Button when pressed calls command updatetask
            self.btn_toBFrame = Button(self.tasks_frame, text="Update Task", command = lambda: self.updateTask(), relief="ridge", bg ="#D5A6BD", height=1 , width=20, font=("Open Sans", 12, "bold"),activebackground="#D5A6BD", fg="white", activeforeground="white")
            self.btn_toBFrame.place(y="450", x="260")

        def forgetFrames(self):
            # Code to forget all the frames
            # Pack_forget is a default function to forget all the pack done
            self.menu_frame.pack_forget()
            self.staff_frame.pack_forget()
            self.admin_frame.pack_forget()
            self.customerProfile_frame.pack_forget()
            self.orders_frame.pack_forget()
            self.tasks_frame.pack_forget()
            self.staffLogIn_frame.pack_forget()
            self.adminStaff_frame.pack_forget()
            


        def goMainMenuFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs menu frame
            self.menu_frame.pack()



        def goAdminlogInSectionFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs staff log in frame
            self.staffLogIn_frame.pack()
        


        def goAdminSectionFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs admin screen frame 
            self.admin_frame.pack()
            


        def goStaffSectionFrame(self):
            # Calls forget frames function 
            self.forgetFrames()
            # Packs staff frame screen
            self.staff_frame.pack()
            


        def goCSFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs customer profile frame screen
            self.customerProfile_frame.pack()
            


        def goOrdersFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs order frame onto screen
            self.orders_frame.pack()
            


        def goTasksFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs task frame onto screen
            self.tasks_frame.pack()
            
            
            
        def goAdminStaffFrame(self):
            # Calls forget frames function
            self.forgetFrames()
            # Packs task frame onto screen
            self.adminStaff_frame.pack()
            


        def csvToTreeview(self, fileName, file):
        # This function takes 2 attributes, the fileName thats going into the treeview and the file, the file attribute helps identify how many values it needs to read
            # Opens the file into read mode          
            fileOpened = open(fileName, "r")
            # Opens the file using csv module so I can use additional csv functions, which are compatible with treeview
            csvreader = csv.reader(fileOpened)
            csvreader_list = list(csvreader)
            # Uses an if statement to check if the attribute file that was entered is equal to either 3
            if file == "customers":
                # For loops to loop through all the values in csv list
                for (a,b,c,d,e,f) in csvreader_list:
                    # Inserts the csv item into the treeview
                    self.tree2.insert('', 'end', values=(a,b,c,d,e,f))
            elif file == "orders":
                for (a,b,c,d,e,f) in csvreader_list:
                    self.tree1.insert('', 'end', values =(a,b,c,d,e,f))
            elif file == "tasks":
                for (a,b,c) in csvreader_list:
                    self.tree.insert('', 'end', values =(a,b,c))
            elif file == "tasksAdmin":
                for (a,b,c) in csvreader_list:
                    self.tree3.insert('', 'end', values =(a,b,c))
            elif file == 'staff':
                for (a,b,c,d) in csvreader_list:
                    self.tree4.insert('', 'end', values =(a,b,c,d))



        def sortTasksProgress(self, sortingOrder):
        # Function to sort tasks in order from assigned to completed
        # This function takes one attribute which is sortingOrder, I want this to be either up or down, it decides on the order the list is sorted
            # Calls class from tasks.py
            tasks = listTasks()
            tasks.readFromFile()
            # Sets sortingList variable to the output we got from .readFromFile which is saved in newlines
            sortingList = tasks.TestLines
            # Creating lists that will be added to
            frontOfList = []
            backOfList = []
            middleOfList = []
            sortedList = []
            # Calls clear_all function to clear the treeview 
            self.clear_allTasks()
            self.clear_allTasks2()
            # For loop for length of the sorting list
            for i in range(len(sortingList)):
                # Assigning the 2nd index in the list to be displayed as capital so it's easier to check with less errors
                checkData = sortingList[i][2].upper()
                # Moves the index of the list to the frontOfList list
                if checkData == "ASSIGNED":
                    frontOfList.append(sortingList[i])
                # Moves the index of the list to the middleOfList list
                elif checkData == "IN PROGRESS":
                    middleOfList.append(sortingList[i])
                # Moves every other option (completed) to the backOfList list
                else:
                    backOfList.append(sortingList[i])
            # Adds list into the sroted list so data is now sorted
                sortedList = frontOfList + middleOfList
                sortedList = sortedList + backOfList
            # If the sortingOrder attribute is equal to up then it reverses the list
                if sortingOrder == "up":
                    sortedList = backOfList + middleOfList
                    sortedList = sortedList + frontOfList
            # Overrides the file with new sorted data
            with open("tasks.csv","w+") as f:
                writer = csv.writer(f, delimiter=",", lineterminator='\n')
                writer.writerows(sortedList)
            # Calls csvToTreeview to read the tasks.csv file into the tasks treeview 
            self.csvToTreeview("tasks.csv", "tasks")
            self.csvToTreeview("tasks.csv", "tasksAdmin")
            
            
        def sortCustomers(self):
            sortedList = self.quickSortOnOrders()
            
            with open("customerProfiles.csv","w+") as f:
                writer = csv.writer(f, delimiter=",", lineterminator='\n')
                writer.writerows(sortedList)
                
            self.clear_allcustomers()
            self.csvToTreeview("customerProfiles.csv", "customers")


        def bubbleSortListTasks(listToSort):
        # This is the bubble sort I have created for sorting taks
        # The reason I only use this for sorting tasks is because I use 2D arrays
            # The passDone variable is set as 0 but later reassigned to the pass that needs to be held
            passDone = 0
            # This variable fetches the length of the list
            lengthOfList = len(listToSort)
            # For loop to loop the range of the list
            for i in range(0 ,lengthOfList):
                # As I use 2D arrays this loops the range of the list the second time
                for j in range(0, (lengthOfList - i - 1)):
                    # Checks if the selected index item is greater than the next index item
                    if (listToSort[j][1] > listToSort[j + 1][1]):
                        # pass
                        passDone = listToSort[j]
                        listToSort[j] = listToSort[j + 1]
                        listToSort[j + 1] = passDone

        #This function clears all the values in a treeview
        def clear_allTasks(self):
            # This collects all the children in the tree and for each child deletes the row
            for item in self.tree.get_children():
                self.tree.delete(item)
                
        #This function clears all the values in a treeview
        def clear_allTasks2(self):
            # This collects all the children in the tree and for each child deletes the row
            for item in self.tree3.get_children():
                self.tree3.delete(item)
                
        #This function clears all the values in a treeview
        def clear_allOrders(self):
            # This collects all the children in the tree and for each child deletes the row
            for item in self.tree1.get_children():
                self.tree1.delete(item)
                
        #This function clears all the values in a treeview
        def clear_allcustomers(self):
            # This collects all the children in the tree and for each child deletes the row
            for item in self.tree2.get_children():
                self.tree2.delete(item)
                
        #This function clears all the values in a treeview
        def clear_allStaff(self):
            # This collects all the children in the tree and for each child deletes the row
            for item in self.tree4.get_children():
                self.tree4.delete(item)

        def searchInList(self,entryForm,position):
            tasks = listTasks()
            tasks.readFromFile()
            searchingList = tasks.TestLines
            searchValue = entryForm.get()
            searchValue = searchValue.upper()
            foundIn = []
            for i in range(len(searchingList)):
                checkData = searchingList[i][position].upper()
                if searchValue in checkData:
                    foundIn.append(searchingList[i])
            self.foundItem = messagebox.showinfo("Match found" , "This has been found: "+str(foundIn))

        def addCustomer(self):
            customerProfileList = listCustomerProfile()
            customerProfileList.readFromFile()
            customerProfileList = customerProfileList.TestLines
            customerPhoneNumber = self.phoneNumber.get()
            try:
                int(customerPhoneNumber)
            except:
                self.foundItem = messagebox.showerror("Phone Number" , "Please re-enter your phone number using numbers")
                
            if len(customerPhoneNumber) == 11 or len(customerPhoneNumber) == 10:
                firstName = self.cFirstName.get()
                secondName = self.cLastName.get()
                customeNumber = customerModification()
                customeNumber = customeNumber.customerNum()
                customerDOB = self.DOB.get()
                customerTOB = self.TOB.get()
                
                newCustomer = [customeNumber, firstName, secondName, customerPhoneNumber, customerDOB, customerTOB]
                
                customerProfileList.append(newCustomer)
                
                self.clear_allcustomers()
                
                with open("customerProfiles.csv","w+") as f:
                    writer = csv.writer(f, delimiter=",", lineterminator='\n')
                    writer.writerows(customerProfileList)
                self.csvToTreeview("customerProfiles.csv", "customers")
                
            else:
               self.foundItem = messagebox.showerror("phone number" , "The phone number entered is invalid")
            
        def addTask(self):
            description = self.taskDesc.get()
            t = listTasks()
            t.readFromFile()
            existingList = t.TestLines
            num = t.taskNum()
            newTask = [num, description, "Assigned"]
            existingList.append(newTask)
            self.clear_allTasks2()
            self.clear_allTasks()
            with open("tasks.csv","w+") as f:
                writer = csv.writer(f, delimiter=",", lineterminator='\n')
                writer.writerows(existingList)
            self.csvToTreeview("tasks.csv", "tasksAdmin")
            self.csvToTreeview("tasks.csv", "tasks")

        def addOrder(self):
            orderInput = self.type.get()
            if orderType(orderInput) != False:
                customerNum = 'C' + self.customerNum.get()
                customers = listCustomerProfile()
                customers.readFromFile()
                searchList = customers.TestLines
                customerFound =False
                for i in range(len(searchList)):
                    if customerNum == searchList[i][0]:
                        customerFound = True
                if customerFound == True:
                    print(orderTypePrice(orderInput))
                    orderNumGen = orderModification()
                    orderNumGen = orderNumGen.orderNum()
                    o = listOrders()
                    o.readFromFile()
                    existingList = o.lines
                    
                    staffCurrent = listStaff()
                    staffCurrent.readFromFile() 
                    staffCurrent = staffCurrent.TestLines
                    staffLength = len(staffCurrent) - 1
                    randomStaff = random.randint(0,staffLength)
                    randomStaff = staffCurrent[randomStaff][0]
                    
                    newOrder = [orderNumGen, customerNum, orderType(orderInput), orderTypePrice(orderInput), randomStaff, "Just Ordered"]
                    existingList.append(newOrder)
                    self.clear_allOrders()
                    with open("orders.csv","w+") as f:
                        writer = csv.writer(f, delimiter=",", lineterminator='\n')
                        writer.writerows(existingList)
                    self.csvToTreeview('orders.csv',"orders")
                else: 
                    self.errorTaskNum = messagebox.showerror("Not Valid" , "Your customer ID doesn't exist")
                    
            else:
                self.errorTaskNum = messagebox.showerror("Not Valid" , "Your ordertype is not valid")
                
        def deleteCustomer(self):
            try:
                int(self.userToDelete.get())
            except:
                self.errorTaskNum = messagebox.showerror("Not Valid" , "Your customer number is not valid, please check that this is a number")
            else:
                itemToDelete = 'C' + self.userToDelete.get()
                listToFile = []
                customers = listCustomerProfile()
                customers.readFromFile()
                self.clear_allcustomers()
                searchList = customers.TestLines
                for i in range(len(searchList)):
                    if searchList[i][0] == itemToDelete:
                        continue
                    else:
                        listToFile.append(searchList[i])
                with open("customerProfiles.csv","w+") as f:
                    writer = csv.writer(f, delimiter=",", lineterminator='\n')
                    writer.writerows(listToFile)
                self.csvToTreeview("customerProfiles.csv", "customers")
                
                orders = listOrders()
                orders.readFromFile()
                searchListOrders = orders.lines
                newOrdersList = []
                for i in range(len(searchListOrders)):
                    if searchList[i][1] == itemToDelete:
                        continue
                    else:
                        newOrdersList.append(searchListOrders[i])
                with open("orders.csv","w+") as f:
                    writer = csv.writer(f, delimiter=",", lineterminator='\n')
                    writer.writerows(newOrdersList)
                self.csvToTreeview("orders.csv", "orders")
                      
                 
        def deleteTask(self):
            t = listTasks()
            t.readFromFile()
            updatedList = t.TestLines
            try:
                int(self.toDeleteTask.get())
            except:
                self.errorTaskNum = messagebox.showerror("Not Valid" , "Your task number is not valid, please check that this is a number")
            else:
                itemToDelete = "T"+self.toDeleteTask.get()
                listToFile = []
                self.clear_allTasks()
                self.clear_allTasks2()
                for i in range(len(updatedList)):
                    if updatedList[i][0] == itemToDelete:
                        continue
                    else:
                        listToFile.append(updatedList[i])
                with open("tasks.csv","w+") as f:
                    writer = csv.writer(f, delimiter=",", lineterminator='\n')
                    writer.writerows(listToFile)
                self.csvToTreeview("tasks.csv", "tasks")
                self.csvToTreeview("tasks.csv", "tasksAdmin")

        def logIntoAdmin(self):
            inputUS = self.userName.get()
            inputPS = self.passWord.get()
            if (inputUS == "Admin204") and (inputPS == "Password123"):
                self.goAdminSectionFrame()
            else:
                self.errorLogIn = messagebox.showerror("No match found" , "Your username and password dont match an account, please try again.")

        def quickSortOnOrders(self):

            def partition(array, low, high):
                pivot = array[high][1]

                i = low - 1
                for j in range(low, high):
                    if array[j][1] <= pivot:
                        i = i + 1
                        (array[i][1], array[j][1]) = (array[j][1], array[i][1])

                (array[i + 1][1], array[high][1]) = (array[high][1], array[i + 1][1])
                return i + 1


            def quickSort(array, low, high):
                if low < high:
                    pi = partition(array, low, high)
                    quickSort(array, low, pi - 1)
                    quickSort(array, pi + 1, high)

            customers = listCustomerProfile()
            customers.readFromFile()
            workingList = customers.TestLines
            listLength = len(workingList) -1
            quickSort(workingList, 0, listLength)
            return workingList
            
            
        def binarySearchList(self,indexPosition, searchValue):
            
            if searchValue == 1:
                searchValue =  self.searchValueEntry2.get()
            else:
                searchValue =  self.searchValueEntry1.get()
                
            try:
                int(searchValue)
            except:
                self.errorSearchValue = messagebox.showerror("Enter a number" , "Please enter a number")
                
            searchValue = int(searchValue)

            orders = listOrders()
            orders.readFromFile()
            searchList = orders.lines
            def binary_search(arr, low, high, x):
                # Check base case
                if high >= low:
                    mid = (high + low) // 2
                    # If element is present at the middle itself
                    if float(arr[mid][indexPosition][1:5]) == x:
                        return mid
                    # Moves to left if element is smaller
                    elif float(arr[mid][indexPosition][1:5]) > x:
                        return binary_search(searchList, low, mid - 1, searchValue)
                    # Else the element can only be present in right part
                    else:
                        return binary_search(searchList, mid + 1, high, searchValue)
                else:
                    # if element is not in array
                    return -1

            # Causes recursion
            result = binary_search(searchList, 0, len(searchList)-1, searchValue)

            if result != -1:
                print(searchList[result])
                self.foundItem = messagebox.showinfo("Match found" , "This has been found: "+str(searchList[result]))
            else:
                self.errorLogIn = messagebox.showerror("No match" , "This has not been found")
                
                
        def updateTask(self):
            tasks = listTasks()
            tasks.readFromFile()
            searchList = tasks.TestLines
            searchValue = self.updateValueEntry1.get()
            print(searchValue)
            self.clear_allTasks()
            for i in range(len(searchList)):
                if searchList[i][0] == searchValue:
                    print(searchList[i][0])
                    if searchList[i][2] == 'Assigned':
                        searchList[i][2] = 'In progress'
                    elif searchList[i][2] == 'In progress':
                        searchList[i][2] = 'Completed'
                    else:
                        self.errorLogIn = messagebox.showerror("Update error" , "This task cannot be updated.")
            with open("tasks.csv","w+") as f:
                writer = csv.writer(f, delimiter=",", lineterminator='\n')
                writer.writerows(searchList)
            # Calls csvToTreeview to read the tasks.csv file into the tasks treeview 
            self.csvToTreeview("tasks.csv", "tasks")
               
        def updateWage(self):
            staffIDToUpdate = "S" + self.staffIdToUpdateWage.get()
            newWage = self.newPay.get()
            try:
                int(self.staffIdToUpdateWage.get())
            except:
                self.errorStaffNum = messagebox.showerror("Not Valid" , "Your staff number is not valid, please check that this is a number")
            else:
                staffCurrent = listStaff()
                staffCurrent.readFromFile() 
                staffCurrent = staffCurrent.TestLines
                for i in range(len(staffCurrent)):
                    if staffCurrent[i][0] == staffIDToUpdate:
                        staffCurrent[i][2] = newWage
                self.clear_allStaff()
                with open("staff.csv","w+") as f:
                    writer = csv.writer(f, delimiter=",", lineterminator='\n')
                    writer.writerows(staffCurrent)
                # Calls csvToTreeview to read the tasks.csv file into the tasks treeview 
                self.csvToTreeview("staff.csv", "staff")
            
            
        def updateHours(self):
            staffID = "S" + self.updateValueEntry.get()
            addHours = self.addHours.get()
            try:
                int(self.updateValueEntry.get())
            except:
                self.errorStaffNum = messagebox.showerror("Not Valid" , "Your staff number is not valid, please check that this is a number")
            else:
                try:
                    int(self.addHours.get())
                except:
                    self.errorType = messagebox.showerror("Not Valid" , "Please enter time in number form")
                else:  
                    staffCurrent = listStaff()
                    staffCurrent.readFromFile() 
                    staffCurrent = staffCurrent.TestLines
                    for i in range(len(staffCurrent)):
                        if staffCurrent[i][0] == staffID:
                            print("Found")
                            staffCurrent[i][3] = int(staffCurrent[i][3])+ int(addHours)
                    self.clear_allStaff()
                    with open("staff.csv","w+") as f:
                        writer = csv.writer(f, delimiter=",", lineterminator='\n')
                        writer.writerows(staffCurrent)
                    # Calls csvToTreeview to read the tasks.csv file into the tasks treeview 
                    self.csvToTreeview("staff.csv", "staff")
            
        def calculatePay(self):
            staffId = "S" + self.staffIdToCalc.get()
            try:
                int(self.staffIdToCalc.get())
            except:
                self.errorStaffNum = messagebox.showerror("Not Valid" , "Your staff number is not valid, please check that this is a number")
            else:
                staffCurrent = listStaff()
                staffCurrent.readFromFile() 
                staffCurrent = staffCurrent.TestLines
                for i in range(len(staffCurrent)):
                    if staffCurrent[i][0] == staffId:
                        calculatedPay = int(staffCurrent[i][2]) * int(staffCurrent[i][3])
                        self.showCalculation = messagebox.showinfo("calculated pay" , "£" + str(calculatedPay))
                    else:
                        self.errorCalculation = messagebox.showerror("Invalid" , "Your staff number is not valid, couldn't locate")
def main():
        window = Tk()
        mySystem(window)
        window.mainloop()

if __name__ == '__main__':
    main()
