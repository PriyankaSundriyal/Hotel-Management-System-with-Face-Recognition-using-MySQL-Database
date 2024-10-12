import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import face_recognition
import mysql.connector
import random
import datetime

# Function to create a database connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='SAUMAYOJHA'
        database='hotel_managemen'
    )

# Function to add a customer to the database
def add_customer():
    name = entry_name.get()
    phone = entry_phone.get()
    address = text_address.get("1.0", tk.END).strip()
    check_in = entry_check_in.get()
    check_out = entry_check_out.get()
    room_type = room_type_var.get()

    if not name or not phone or not address or not check_in or not check_out or not room_type:
        messagebox.showerror("Input Error", "All fields are required")
        return

    conn = create_connection()
    cursor = conn.cursor()

    room_no = random.randrange(40) + 300
    cust_id = random.randrange(40) + 10

    cursor.execute("INSERT INTO bookings (name, phone, checkin, checkout, room_type, address, room_no, cust_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (name, phone, check_in, check_out, room_type, address, room_no, cust_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer added successfully")
    clear_fields()
    display_customers()

# Function to display all customers in the treeview
def display_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    conn.close()

    for row in tree.get_children():
        tree.delete(row)
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# Function to clear input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_check_in.delete(0, tk.END)
    entry_check_out.delete(0, tk.END)
    room_type_var.set("")
    text_address.delete("1.0", tk.END)

# Function to book a room (calls add_customer)
def book_room():
    add_customer()

# Function to show room information
def show_rooms_info():
    messagebox.showinfo("Rooms Info", "1. Standard Non-AC\n2. Standard AC\n3. 3-Bed Non-AC\n4. 3-Bed AC")

# Function to display restaurant menu
def restaurant_service():
    messagebox.showinfo("Menu Card", "1. Regular Tea - Rs. 20\n2. Masala Tea - Rs. 25\n3. Coffee - Rs. 25\n...")

# Function to handle payment
def make_payment():
    phone = entry_phone.get()
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings WHERE phone=%s", (phone,))
    row = cursor.fetchone()

    if row:
        total_amount = calculate_total_amount(row)
        messagebox.showinfo("Payment", f"Total Amount: {total_amount}\nPayment Successful!")
    else:
        messagebox.showerror("Error", "Customer not found")
    
    conn.close()
    clear_fields()

# Function to calculate total amount for stay
def calculate_total_amount(customer):
    check_in = datetime.datetime.strptime(customer[3], "%d/%m/%Y")
    check_out = datetime.datetime.strptime(customer[4], "%d/%m/%Y")
    days = (check_out - check_in).days
    room_charges = {"Standard Non-AC": 3500, "Standard AC": 4000, "3-Bed Non-AC": 4500, "3-Bed AC": 5000}
    return days * room_charges[customer[5]]

# Function to show records (calls display_customers)
def show_records():
    display_customers()

# Function to start face recognition and initialize hotel management system if face matches
def start_recognition():
    known_image = face_recognition.load_image_file("C:\\Users\\sauma\\Pictures\\Saved Pictures\\Screenshots\\Screenshot 2024-05-22 001551.png")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    known_face_encodings = [known_face_encoding]

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            if True in matches:
                video_capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Face Recognition", "Welcome!")
                display_hotel_management_system(frame)
                return
            else:
                messagebox.showinfo("Face Recognition", "Face not recognized. Try again!")
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

# Function to display the hotel management system GUI
def display_hotel_management_system(recognized_image):
    global entry_name, entry_phone, entry_check_in, entry_check_out, text_address, room_type_var, tree, background_photo

    root = tk.Tk()
    root.title("Green Valley Hotel")

    background_image = Image.open("C:\\Users\\sauma\\Downloads\\greenvalley.png")
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame_details = ttk.Frame(root, padding="05")
    frame_details.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    ttk.Label(frame_details, text="Name:").grid(row=0, column=0, sticky="e")
    entry_name = ttk.Entry(frame_details, width=30)
    entry_name.grid(row=0, column=1)

    ttk.Label(frame_details, text="Phone:").grid(row=1, column=0, sticky="e")
    entry_phone = ttk.Entry(frame_details, width=30)
    entry_phone.grid(row=1, column=1)

    ttk.Label(frame_details, text="Check-In (DD/MM/YYYY):").grid(row=3, column=0, sticky="e")
    entry_check_in = ttk.Entry(frame_details, width=30)
    entry_check_in.grid(row=3, column=1)

    ttk.Label(frame_details, text="Check-Out (DD/MM/YYYY):").grid(row=4, column=0, sticky="e")
    entry_check_out = ttk.Entry(frame_details, width=30)
    entry_check_out.grid(row=4, column=1)

    ttk.Label(frame_details, text="Address:").grid(row=2, column=0, sticky="ne")
    text_address = tk.Text(frame_details, width=23, height=5)
    text_address.grid(row=2, column=1, pady=5)

    ttk.Label(frame_details, text="Room Type:").grid(row=5, column=0, sticky="e")
    room_type_var = tk.StringVar()
    room_type_combo = ttk.Combobox(frame_details, textvariable=room_type_var, values=("Standard Non-AC", "Standard AC", "3-Bed Non-AC", "3-Bed AC"), state="readonly", width=28)
    room_type_combo.grid(row=5, column=1)

    frame_buttons = ttk.Frame(root, padding="10")
    frame_buttons.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    ttk.Button(frame_buttons, text="Book Room", command=book_room).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(frame_buttons, text="Rooms Info", command=show_rooms_info).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(frame_buttons, text="Restaurant", command=restaurant_service).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(frame_buttons, text="Make Payment", command=make_payment).grid(row=0, column=3, padx=5, pady=5)
    ttk.Button(frame_buttons, text="Show Records", command=show_records).grid(row=0, column=4, padx=5, pady=5)

    frame_treeview = ttk.Frame(root, padding="10")
    frame_treeview.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    columns = ("id", "name", "phone", "check_in", "check_out", "room_type", "address", "room_no", "cust_id")
    tree =ttk.Treeview(frame_treeview, columns=columns, show="headings")
    tree.heading("id", text="ID")
    tree.heading("name", text="Name")
    tree.heading("phone", text="Phone")
    tree.heading("check_in", text="Check-In")
    tree.heading("check_out", text="Check-Out")
    tree.heading("room_type", text="Room Type")
    tree.heading("address", text="Address")
    tree.heading("room_no", text="Room No")
    tree.heading("cust_id", text="Customer ID")

    tree.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(frame_treeview, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    display_customers()

    # Display recognized image on the left side
    recognized_image = cv2.cvtColor(recognized_image, cv2.COLOR_BGR2RGB)
    recognized_image = Image.fromarray(recognized_image)
    recognized_photo = ImageTk.PhotoImage(recognized_image)
    recognized_label = tk.Label(root, image=recognized_photo)
    recognized_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

    root.mainloop()

# Start face recognition and hotel management system
start_recognition()

