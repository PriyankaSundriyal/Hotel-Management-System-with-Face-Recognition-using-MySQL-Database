# Hotel-Management-System-with-Face-Recognition-using-MySQL-Database
This Hotel Management System is an advanced solution built using Python's Tkinter for the GUI, MySQL for data management, and OpenCV with face recognition for security and authentication. It is designed to streamline the process of managing hotel bookings, customer records, and payments. By incorporating face recognition
Hotel Management System with Face Recognition
Overview
This Hotel Management System is an advanced solution built using Python's Tkinter for the GUI, MySQL for data management, and OpenCV with face recognition for security and authentication. It is designed to streamline the process of managing hotel bookings, customer records, and payments. By incorporating face recognition, it adds a layer of security, ensuring that only authorized personnel can access the system.
Features
•	Face Recognition for Security: Utilizes real-time face recognition using the OpenCV and face_recognition libraries. This ensures that only authorized personnel can access and operate the system, enhancing security.
•	Room Booking System: Customers can book rooms by providing their details such as name, phone number, check-in and check-out dates, and room type. The system automatically assigns a room and generates a customer ID.
•	Restaurant Service Information: Displays the restaurant menu with pricing, making it easier for customers to order food from the hotel.
•	Payment System: Calculates total charges based on the customer's stay and processes payments.
•	Customer Records: Displays all customer bookings in a searchable treeview format, providing easy access to information.
•	Room Information: Displays available room types and their corresponding prices, helping customers make informed choices.
•	Advanced GUI: The system is built using the Tkinter library, offering an intuitive, easy-to-use interface.
Key Differentiators
•	Face Recognition Integration: Unlike traditional hotel management systems, this solution integrates face recognition, offering an added layer of security.
•	Real-Time Access Control: Only authorized personnel can access the system, reducing unauthorized access.
•	Automated Customer ID & Room Assignment: The system automatically assigns room numbers and generates unique customer IDs, simplifying hotel operations.
•	Custom Payment System: Automatically calculates the total amount for the stay based on room type and the number of days.
•	Seamless Database Connectivity: The system integrates with MySQL to store and manage customer bookings, providing a robust and scalable solution for real-world use.
Technologies Used
•	Python: Core logic and functionality.
•	Tkinter: For the graphical user interface (GUI).
•	OpenCV & Face_Recognition: For real-time face recognition.
•	MySQL: Database management for storing customer and booking details.
•	Pillow: Image handling for background and customer photo display.
Setup Instructions
1.	Install Required Libraries:
Use the following commands to install the necessary libraries:
bash
Copy code
pip install opencv-python face-recognition mysql-connector-python Pillow
2.	Database Configuration:
Ensure you have MySQL installed and create a database named hotel_management with the following table structure:
sql
Copy code
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20),
    checkin DATE,
    checkout DATE,
    room_type VARCHAR(50),
    address TEXT,
    room_no INT,
    cust_id INT
);
3.	Run the Application:
Execute the script to start the hotel management system. The face recognition feature will initialize automatically.
How to Use
1.	Face Recognition Login: The system will first verify your identity through face recognition. Once recognized, you can proceed with managing bookings.
2.	Book a Room: Fill in the customer's details and click "Book Room" to confirm the booking.
3.	View and Manage Records: View all the customer records using the treeview and manage bookings accordingly.
4.	Make Payment: Enter the phone number to retrieve the booking and process payment.
Future Enhancements
•	Online Booking Integration: Add online booking functionality to allow customers to book rooms remotely.
•	Advanced Reporting: Include more detailed reporting and analytics on hotel performance and customer trends.
•	Multi-user Authentication: Allow multiple users with varying levels of access to use the system.
