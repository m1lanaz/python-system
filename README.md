# Store System

A system in python I created to help with managing customers and orders along with staff. This was built as a part of my coursework for college.

# Video Walk-through

> **Please Note:** You will be redirected to YouTube as this file exceeds GitHub's embedded video size

[<img src="https://img.youtube.com/vi/Aaft0Jc68eI/maxresdefault.jpg" width="100%">](https://youtu.be/Aaft0Jc68eI)

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

Certainly, here's a version with a bit more technical detail:

# System Development

### 1. Data Organization and Schema Design

I began by establishing a structured way of storing data. I adhered to the principles of database normalization to ensure efficient organization of data entities. This approach minimized redundancy and optimized data retrieval and manipulation. Adhering to the third normal form (3NF) ensured a robust data structure.

### 2. Graphical User Interface (GUI) Construction

After sorting out the data structure, I moved my focus to designing how users would interact with the system. I used the Tkinter framework to create a user-friendly and visually appealing interface. Utilizing Object-Oriented Programming (OOP) principles, I structured the GUI components modularly, enhancing code reusability and ease of maintenance by adding in comments.

### 3. Implementation of Access Control

Ensuring secure access to sensitive areas was a large focus of mine. I integrated a login for Admins. This safeguarded the system from unauthorized access that could potentially mess with the systems data.

### 4. Testing

After the system was created with minimal features, it was repeatedly tested. Allowing me to pinpoint any errors, both syntax and logical, this meant I could build up the system features with a solid foundation.

### 5. Data Management and Persistence Strategies

As this was a coursework project, I wasn't allowed to use any databases. I opted for text files as a solution, enabling me to store essential information like customer profiles and order records. This strategy maintained data integrity without relying on relational databases.

### 6. Optimization for Efficiency

Efficient data processing was a priority. I implemented the quicksort algorithm, known for its efficiency, as it would be able to sort through large amounts of data quicker than a linear or bubble sort. Additionally, I implemented the binary search algorithm.

### 7. Validation and Testing

I included validation for the inputs in the system, to ensure they matched what I was asking for. This also helped reduce errors as some calculations were relying on certain data types being entered in. Testing was also carried out, to ensure the system was working as intended.
