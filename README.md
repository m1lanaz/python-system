# Store Tracking System

A system in python I created to help with managing customers and orders along with staff. This was built as a part of my coursework for college.

# Video Walk-through
file:///home/milana/Downloads/COURSEWORK/walkthrough%20of%20system.mkv

# Functionality

The system has several unique features that set it apart. Upon loading, no login is needed, as it's meant solely for company staff. Yet, accessing the admin section does require a login.

## Staff
Staff members have the ability to view customer information and create new customer profiles. Additionally, they can access and manage orders, including updating order statuses and generating new orders.

> As this system is in third normal form,  it will **not** allow you to place an order if there is not an existing customer, as these are connected.

Staff members can also review tasks that have been assigned to them by the admin. They have the capability to update the status of these tasks once they are completed.
	

## Admin

The admin can also view customers and possesses additional functionality to delete customer records. 

They are able to create new staff accounts, update staff wages, and monitor staff hours. Additionally, a 'payroll' function is available to the admin, producing an output based on the staff member's worked hours multiplied by their wage.

Also, the admin can assign tasks to staff members, track task progress, and remove tasks that have been marked as completed.
