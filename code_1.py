import tkinter as tk 
from mysql.connector import connect, Error

#CONNECTING DATABASE
config = {
    'user': 'root',
    'password': 'Gubbi@2106',
    'host': 'localhost',
    'database': 'sys',
    'auth_plugin': 'mysql_native_password'
}
try:
    connection = connect(**config)
    print("Connection established")
except Error as e:
    print("An error occured in establishing connection :()", e) 
c = connection.cursor()
#-----------------------------------------------  

def management_interface_add_medicine():
    root = tk.Tk()
    root.title("Medicine")
    set_position_of_tkinter_window(root)
    def  Add_button_click_Medicine():
        m_id = medicine_id_entry.get()
        m_st = medicine_storage_temp_entry.get()
        m_c = medicine_concentration_entry.get()
        m_n = medicine_name_entry.get()
        m_p = medicine_price_entry.get()
        m_ed = medicine_expiry_date_entry.get()
        m_re = medicine_recommended_entry.get()
        m_q = medicine_quantity_entry.get()
        m_s = medicine_supplier_entry.get()
        m_e = medicine_employee_entry.get()
        try:
            query = f"insert into medicine (medicine_id, m_storage_temp, m_concentration, m_name, m_price, m_expiry_data, m_recommended_dosage, m_quantity, supplier_id, employee_id) values ({m_id},{m_st},{m_c},'{m_n}',{m_p},'{m_ed}',{m_re},{m_q},{m_s},{m_e})"            
            c.execute(query)
            connection.commit()
            print("Medicine Added")
            label_print = tk.Label(root, text="Medicine Added")
            label_print.pack(side = "bottom", padx=30, pady=30)
        except Error as e:
            print("An error occured in inserting data :()", e)
            label_print = tk.Label(root, text="An error occured in inserting data :()")
            label_print.pack(side = "bottom", padx=30, pady=30)

    canvas = tk.Canvas(root) 
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    #----------------------------------------------
    medicine_id_label = tk.Label(frame, text="Medicine ID")
    medicine_id_label.pack()
    medicine_id_entry = tk.Entry(frame)
    medicine_id_entry.pack()
    medicine_storage_temp_label = tk.Label(frame, text="Medicine Storage Temp")
    medicine_storage_temp_label.pack()
    medicine_storage_temp_entry = tk.Entry(frame)
    medicine_storage_temp_entry.pack()
    medicine_concentration_label = tk.Label(frame, text="Medicine Concentration")
    medicine_concentration_label.pack()
    medicine_concentration_entry = tk.Entry(frame)
    medicine_concentration_entry.pack()
    medicine_name_label = tk.Label(frame, text="Medicine Name")
    medicine_name_label.pack()
    medicine_name_entry = tk.Entry(frame)
    medicine_name_entry.pack()
    medicine_price_label = tk.Label(frame, text="Medicine Price")
    medicine_price_label.pack()
    medicine_price_entry = tk.Entry(frame)
    medicine_price_entry.pack()
    medicine_expiry_date_label = tk.Label(frame, text="Medicine Expiry Date")
    medicine_expiry_date_label.pack()
    medicine_expiry_date_entry = tk.Entry(frame)
    medicine_expiry_date_entry.pack()
    medicine_recommended_label = tk.Label(frame, text="Medicine Recommended Dosage")
    medicine_recommended_label.pack()
    medicine_recommended_entry = tk.Entry(frame)
    medicine_recommended_entry.pack()
    medicine_quantity_label = tk.Label(frame, text="Medicine Quantity")
    medicine_quantity_label.pack()
    medicine_quantity_entry = tk.Entry(frame)
    medicine_quantity_entry.pack()
    medicine_supplier_label = tk.Label(frame, text="Supplier ID")
    medicine_supplier_label.pack()
    medicine_supplier_entry = tk.Entry(frame)
    medicine_supplier_entry.pack()
    medicine_employee_label = tk.Label(frame, text="Employee ID")
    medicine_employee_label.pack()
    medicine_employee_entry = tk.Entry(frame)
    medicine_employee_entry.pack()
    add_button = tk.Button(root, text="Add", width=5, height=5, command=lambda: Add_button_click_Medicine())
    add_button.pack(side="bottom", padx=30, pady=30)  
    root.mainloop()


def management_interface_delete_medicine():
    root = tk.Tk()
    root.title("Medicine")
    set_position_of_tkinter_window(root)
    def  Add_button_click_Medicine():
        m_id = medicine_id_entry.get()
        try:
            query = f"DELETE FROM medicine WHERE medicine_id = {m_id}"            
            c.execute(query)
            connection.commit()
            label_print = tk.Label(root, text="Medicine DELETED")
            label_print.pack(side = "bottom", padx=30, pady=30)
        except Error as e:
            print("An error occured in inserting data :()", e)
            label_print = tk.Label(root, text="An error occured in inserting data :()")
            label_print.pack(side = "bottom", padx=30, pady=30)

    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    #----------------------------------------------

    medicine_id_label = tk.Label(frame, text="Medicine ID")
    medicine_id_label.pack()
    medicine_id_entry = tk.Entry(frame)
    medicine_id_entry.pack()
    add_button = tk.Button(root, text="DELETE", width=5, height=5, command=lambda: Add_button_click_Medicine())
    add_button.pack(side="bottom", padx=30, pady=30)  
    root.mainloop()


def management_interface_add_supplier():
    root = tk.Tk()
    root.title("Supplier")
    set_position_of_tkinter_window(root)
    def  Add_button_click_Medicine():
        supplier_id = supplier_id_entry.get()
        s_delivery_charge = s_delivery_charge_entry.get()
        s_delivery_time = s_delivery_time_entry.get()
        s_location = s_location_entry.get()
        s_price = s_price_entry.get()
        employee_id = employee_id_entry.get()

        try:
            query = f"insert into supplier (supplier_id, s_delivery_charge,s_delivery_time, s_location, s_prices, employee_id) values ({supplier_id}, {s_delivery_charge},{s_delivery_time}, {s_location}, {s_price}, {employee_id})"            
            c.execute(query)
            connection.commit()
            print("Supplier Added")
            label_print = tk.Label(root, text="Supplier Added")
            label_print.pack(side = "bottom", padx=30, pady=30)
        except Error as e:
            print("An error occured in inserting data :()", e)
            label_print = tk.Label(root, text="An error occured in inserting data :()")
            label_print.pack(side = "bottom", padx=30, pady=30)

    canvas = tk.Canvas(root) 
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    #----------------------------------------------
    supplier_id_label = tk.Label(frame, text="Supplier ID")
    supplier_id_label.pack()
    supplier_id_entry = tk.Entry(frame)
    supplier_id_entry.pack()

    s_delivery_charge_label = tk.Label(frame, text="Delivery Charge")
    s_delivery_charge_label.pack()
    s_delivery_charge_entry = tk.Entry(frame)
    s_delivery_charge_entry.pack()

    s_delivery_time_label = tk.Label(frame, text="Delivery Time")
    s_delivery_time_label.pack()
    s_delivery_time_entry = tk.Entry(frame)
    s_delivery_time_entry.pack()

    s_location_label = tk.Label(frame, text="Location")
    s_location_label.pack()
    s_location_entry = tk.Entry(frame)
    s_location_entry.pack()
    
    s_price_label = tk.Label(frame, text="Price")
    s_price_label.pack()
    s_price_entry = tk.Entry(frame)
    s_price_entry.pack()

    employee_id_label = tk.Label(frame, text="Employee ID")
    employee_id_label.pack()
    employee_id_entry = tk.Entry(frame)
    employee_id_entry.pack()

    add_button = tk.Button(root, text="Add", width=5, height=5, command=lambda: Add_button_click_Medicine())
    add_button.pack(side="bottom", padx=30, pady=30)  
    root.mainloop()
    
def management_interface_delete_supplier():
    return 0
    
def management_interface(user_id , password):
        root = tk.Tk()
        root.title("Management")
        set_position_of_tkinter_window(root)
        welcome_label = tk.Label(root, text="Welcome " + password)
        welcome_label.pack()
        query = "SELECT * FROM MANAGEMENT WHERE employee_id = %s AND employee_name = %s"
        c.execute(query, (user_id, password))
        result = c.fetchall()
        for i in result:
            employee_id_label = tk.Label(root, text="Employee ID : " + str(i[0]))
            employee_id_label.pack()
            employee_name_label = tk.Label(root, text="Employee Name : " + i[1])
            employee_name_label.pack()
            employee_shift_label = tk.Label(root, text="Employee Shift : " + i[2])
            employee_shift_label.pack()
            employee_phone_label = tk.Label(root, text="Employee Phone : " + str(i[3]))
            employee_phone_label.pack()
        def button_click(btn):
            if btn == "Logout":
                root.destroy()
                management_login()
            if btn == "Add Medicine":
                root.destroy()
                management_interface_add_medicine()
            if btn == "Delete Medicine":
                root.destroy()
                management_interface_delete_medicine()
            if btn == "Add Supplier":
                root.destroy()
                management_interface_add_supplier()
            if btn == "Delete Supplier":
                root.destroy()
                management_interface_delete_supplier()
        add_medicine_button = tk.Button(root , text="Add Medicine" , width=10 , height=5 , command=lambda: button_click("Add Medicine"))
        add_medicine_button.pack(side="top", padx=50, pady=30)
        delete_medicine_button = tk.Button(root , text="Delete Medicine" , width=10 , height=5 , command=lambda: button_click("Delete Medicine"))
        delete_medicine_button.pack(side="top", padx=50, pady=30)
        add_supplier_button = tk.Button(root , text="Add Supplier" , width=10 , height=5 , command=lambda: button_click("Add Supplier"))
        add_supplier_button.pack(side="top", padx=50, pady=30)
        logout_button = tk.Button(root , text="Logout" , width=10 , height=5 , command=lambda: button_click("Logout")) 
        logout_button.pack(side="top", padx=50, pady=30)
        root.mainloop()

# ------------------------------------------------------
# USER

from tkinter import ttk

def empty_doctor_cart(password,user_id):
    query = f"DELETE FROM doctor_cart WHERE user_id = {user_id};"
    c.execute(query)
    connection.commit()
def empty_medicine_cart(password,user_id):
    query = f"DELETE FROM medicine_id WHERE user_id = {user_id};"
    c.execute(query)
    connection.commit()
def empty_lab_cart(password,user_id):
    query = f"DELETE FROM lab_cart WHERE user_id = {user_id};"
    c.execute(query)
    connection.commit()

def user_buy_medicine_page(password,user_id):
    print("REACHED")
    root = tk.Tk()
    root.title(f"MediMorph: Buy Medicine")
    set_position_of_tkinter_window(root)
    tree = ttk.Treeview(root)
    tree["columns"] = ("storage_temp", "concentration", "name", "price", "expiry_date", "recommended_dosage" , "quantity")
    tree.heading("#0", text="Medicine ID")
    tree.heading("storage_temp", text="Storage Temperature")
    tree.heading("concentration", text="Concentration")
    tree.heading("name", text="Name")
    tree.heading("price", text="Price")
    tree.heading("expiry_date", text="Expiry Date")
    tree.heading("recommended_dosage", text="Recommended Dosage")
    tree.heading("quantity", text="Quantity")
    tree.pack()
    query = "SELECT * FROM MEDICINE"
    c.execute(query)
    result = c.fetchall()
    for i in result:
        tree.insert("", "end", text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
    medicine_id_label = tk.Label(root, text="Medicine ID")
    medicine_id_label.pack()
    medicine_id_entry = tk.Entry(root)
    medicine_id_entry.pack()
    quantity_label = tk.Label(root, text="Quantity")
    quantity_label.pack()
    quantity_entry = tk.Entry(root)
    quantity_entry.pack()
    id = user_id
    def add_to_cart():
        user_id = id
        medicine__id = medicine_id_entry.get()
        quantity = quantity_entry.get()
        # c.execute(f"SELECT m_quantity FROM medicine WHERE medicine_id = '{medicine__id}'")
        # c.execute(f"SELECT * FROM medicine where medicine_id = '{medicine__id}' ;")
        # print("REACHED")
        result = c.fetchall()
        for i in result:
            if (int(i[-3])) < int(quantity):
                print(i)
                print(i[-3] , quantity)
                print("Not enough quantity")
                return
            else:
                print(i[-3] , quantity)
                print("Enough quantity")

        medicine__id = int(medicine__id)
        quantity = int(quantity)
        print(medicine__id)
        print(quantity)
        print(type(user_id))
        print(user_id)
        user_id_change = int(user_id)
        query = f"insert into medicine_id (medicine_id , user_id , quantity) values ({medicine__id} , {user_id_change} , {quantity})"
        c.execute(query)
        connection.commit()
        print("Added to cart")
        
    def back():
        root.destroy()
        user_homepage(password , user_id)
    def empty_medicine(name,id):
        empty_medicine_cart(password,id)

    add_to_cart_button = tk.Button(root, text="Add to Cart", width=10, height=5, command=lambda: add_to_cart())
    add_to_cart_button.pack(side="top", padx=50, pady=30)
    back_button = tk.Button(root, text="Back", width=10, height=5, command=lambda: back())
    med_button = tk.Button(root, text="Empty Medicine cart", width=10, height=5 , command=lambda: empty_medicine(password , user_id))
    med_button.pack(side="top", padx=50, pady=30)
    back_button.pack(side="top", padx=50, pady=30)
    root.mainloop()

def user_book_lab_test_page(password , user_id):
    print("REACHED")
    root = tk.Tk()
    root.title(f"MediMorph: Book Lab")
    set_position_of_tkinter_window(root)
    tree = ttk.Treeview(root)
    tree["columns"] = ("glt_time","glt_location","glt_type","glt_mode","glt_cost")
    tree.heading("#0", text="Lab Test ID")
    tree.heading("glt_time", text="Time")
    tree.heading("glt_location", text="Location")
    tree.heading("glt_type", text="Type")
    tree.heading("glt_mode", text="Mode")
    tree.heading("glt_cost", text="Cost")
    tree.pack()
    query = "SELECT * FROM `Get Lab Tests`"
    c.execute(query)
    result = c.fetchall()
    for i in result:
        tree.insert("", "end", text=i[0], values=(i[1], i[2], i[3], i[4],i[7]))
    lab_id_label = tk.Label(root, text="Lab ID")
    lab_id_label.pack()
    lab_id_entry = tk.Entry(root)
    lab_id_entry.pack()
    lab_label = tk.Label(root, text="Quantity")
    lab_label.pack()
    quantity_entry = tk.Entry(root)
    quantity_entry.pack()
    id = user_id
    def add_to_cart():
        user_id = id
        lab__id = lab_id_entry.get()
        quantity = quantity_entry.get()
        lab__id = int(lab__id)
        quantity = int(quantity)
        print(lab__id)
        print(quantity)
        print(type(user_id))
        print(user_id)
        user_id_change = int(user_id)
        query = f"insert into lab_cart (get_lab_test_id , user_id , l_quantity) values ({lab__id} , {user_id_change} , {quantity})"
        c.execute(query)
        connection.commit()
        print("Added to cart")

    def back():
        root.destroy()
        user_homepage(password , user_id)
    def empty_lab(name,id):
        empty_lab_cart(password,id)

    add_to_cart_button = tk.Button(root, text="Add to Cart", width=10, height=5, command=lambda: add_to_cart())
    add_to_cart_button.pack(side="top", padx=50, pady=30)
    back_button = tk.Button(root, text="Back", width=10, height=5, command=lambda: back())
    back_button.pack(side="top", padx=50, pady=30)
    lab_button = tk.Button(root, text="Empty Lab cart", width=10, height=5 , command=lambda: empty_lab(password , user_id))
    lab_button.pack(side="top", padx=50, pady=30)

    root.mainloop()
    

def user_book_doctor_page(password,user_id):
    root = tk.Tk()
    root.title(f"Book a doctor's appointment")
    set_position_of_tkinter_window(root)
    tree = ttk.Treeview(root)
    tree["columns"] = ("d_name", "d_fees", "d_qualification", "d_experience", "d_address" , "mode" , "timings")
    tree.heading("#0", text="Doctor ID")
    tree.heading("d_name", text="NAME")
    tree.heading("d_fees", text="FEES")
    tree.heading("d_qualification", text="QUALIFICATION")
    tree.heading("d_experience", text="EXPERIENCE")
    tree.heading("d_address", text="ADDRESS")
    tree.heading("mode", text="MODE")
    tree.heading("timings", text="TIMING")
    tree.pack()
    query = "SELECT * FROM DOCTOR"
    c.execute(query)
    result = c.fetchall()
    for i in result:
        tree.insert("", "end", text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7] ))

    doctor_id_label = tk.Label(root, text="Doctor ID")
    doctor_id_label.pack()
    doctor_id_entry = tk.Entry(root)
    doctor_id_entry.pack()
    def book():
        doctor_id = doctor_id_entry.get()
        query = f"insert into doctor_cart (user_id , doctor_id) values ({user_id} , {doctor_id} )"
        c.execute(query)
        connection.commit()
        print("Booked")
    def back():
        root.destroy()
        user_homepage(password , user_id)
    def empty_doctor(password,id):
        empty_doctor_cart(password,id)
    book_button = tk.Button(root, text="Book", width=10, height=5, command=lambda: book())
    book_button.pack(side="top", padx=50, pady=30)
    back_button = tk.Button(root, text="Back", width=10, height=5, command=lambda: back())
    back_button.pack(side="top", padx=50, pady=30)
    doc_button = tk.Button(root, text="Empty Doctor cart", width=10, height=5 , command=lambda: empty_doctor(password , user_id))
    doc_button.pack(side="top", padx=50, pady=30)
    root.mainloop()

def user_checkout_page(password , user_id ): 
    root = tk.Tk()
    root.title(f"Checkout")
    set_position_of_tkinter_window(root)
    total_price = 0 
    doctor_price = 0
    lab_price = 0
    medicine_price = 0
    query = f"select sum(d_fees) from doctor_cart , doctor where doctor.doctor_id = doctor_cart.doctor_id and user_id = {user_id} ; "
    c.execute(query)



    result = c.fetchall()                                                                                                                                                                                                                           
    for i in result:
        print(i[0])
        doctor_price = i[0]
    query = f"select sum(glt_cost*l_quantity) from lab_cart , `Get Lab Tests` as aa where aa.get_lab_test_id = lab_cart.get_lab_test_id and user_id = {user_id} ; "
    c.execute(query)



    result = c.fetchall()
    for i in result:
        print(i[0])
        lab_price = i[0]
    query = f"select sum(m_price*quantity) from medicine_id , medicine where medicine.medicine_id = medicine_id.medicine_id and user_id = {user_id} ; "
    c.execute(query)

    result = c.fetchall()
    for i in result:
        print(i[0])
        medicine_price = i[0]
    if(doctor_price == None):
        doctor_price = 0
    if(lab_price == None):
        lab_price = 0
    if(medicine_price == None):
        medicine_price = 0
    total_price = doctor_price + lab_price + medicine_price

    

    doctor_price_label = tk.Label(root, text=f"Doctor price = {doctor_price}" , font=("Arial Bold", 50))
    doctor_price_label.pack()
    lab_price_label = tk.Label(root, text=f"Lab price = {lab_price}" , font=("Arial Bold", 50))
    lab_price_label.pack()
    medicine_price_label = tk.Label(root, text=f"Medicine price = {medicine_price}" , font=("Arial Bold", 50))
    medicine_price_label.pack()
    print(total_price)
    total_price_label = tk.Label(root, text=f"Total price = {total_price}" , font=("Arial Bold", 50))
    total_price_label.pack()
    def checkout():
        c.execute(f"update medicine , medicine_id set medicine.m_quantity = medicine.m_quantity - medicine_id.quantity where medicine_id.medicine_id = medicine.medicine_id and user_id = {user_id} ;")
        connection.commit()
        c.execute(f"DELETE FROM doctor_cart WHERE user_id = {user_id};")
        connection.commit()
        c.execute(f"DELETE FROM lab_cart WHERE user_id = {user_id};")
        connection.commit()
        c.execute(f"DELETE FROM medicine_id WHERE user_id = {user_id};")
        connection.commit()
        query  = f"INSERT INTO order_summary (customer_id,medicine_price,doctor_price,lab_price) VALUES ({user_id},{medicine_price},{doctor_price},{lab_price})"
        c.execute(query)
        connection.commit()
        root.destroy()
        user_login()
    def back():
        root.destroy()
        user_login()
        
    confirm_label = tk.Label(root, text="Press checkout to proceed" , font=("Arial Bold", 50))
    confirm_label.pack()

    check_button = tk.Button(root, text="Checkout", width=10, height=5, command=lambda: checkout())
    check_button.pack(side="top", padx=50, pady=30)

    back_button = tk.Button(root, text="Back", width=10, height=5, command=lambda: back())
    back_button.pack(side="top", padx=50, pady=30)

    root.mainloop()

def user_homepage(name , id):
    root = tk.Tk()
    root.title("Welcome " + name)
    set_position_of_tkinter_window(root)
    def user_buy_medicine():
        root.destroy()
        user_buy_medicine_page(name , id)
    def user_book_doctor():
        root.destroy()
        user_book_doctor_page(name , id)
    def user_book_lab_test():
        root.destroy()
        user_book_lab_test_page(name , id)
    def back():
        root.destroy()
        user_login()

    buy_medicine_button = tk.Button(root, text="Buy Medicine", width=10, height=5, command=lambda: user_buy_medicine())
    buy_medicine_button.pack(side="top", padx=50, pady=30)
    book_doctor_button = tk.Button(root, text="Book Doctor", width=10, height=5 , command=lambda: user_book_doctor())
    book_doctor_button.pack(side="top", padx=50, pady=30)
    book_lab_test_button = tk.Button(root, text="Book Lab Test", width=10, height=5 , command=lambda: user_book_lab_test())
    book_lab_test_button.pack(side="top", padx=50, pady=30)
    checkout_button = tk.Button(root, text="Checkout", width=10, height=5 , command=lambda: user_checkout_page(name , id))
    checkout_button.pack(side="top", padx=50, pady=30)
    back_button = tk.Button(root, text="Back", width=10, height=5, command=lambda: back())
    back_button.pack(side="top", padx=50, pady=30)
    root.mainloop()
   

def user_signup():
    root = tk.Tk()
    root.title("User Signup")
    set_position_of_tkinter_window(root)
    def button_click(btn):
        if btn == "Signup":
            user_id = user_id_entry.get()
            query = f"SELECT * FROM patient WHERE user_id = {user_id}"
            c.execute(query)
            result = c.fetchall()
            if len(result)>0:
                print("User id already exists")
                return user_login_signup_page()
            else:
                print("User id does not exist")
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            p_phone_number = phone_number_entry.get()
            city = city_entry.get()
            state = state_entry.get()
            middle_name = middle_name_entry.get()
            gender  = p_gender.get()
            age = p_age_entry.get()
            date_joined = date_joined_entry.get()
            email = p_email_entry.get()
            query = f"insert into patient (user_id, first_name, middle_name, last_name, city, state, p_gender, p_age, p_phone_number, p_date_joined, p_email) values ({user_id}  ,'{first_name}' , '{middle_name}' , '{last_name}' ,'{city}' , '{state}' , '{gender}', {age} , '{p_phone_number}' , '{date_joined}' , '{email}');"
            print("successfully registered")
            c.execute(query)
            connection.commit()
            root.destroy()
            user_login_signup_page()
        elif btn == "Back":
            root.destroy()
            user_login_signup_page()

    user_id_label = tk.Label(root, text="User ID")
    user_id_label.pack()
    user_id_entry = tk.Entry(root)
    user_id_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    date_joined_label = tk.Label(root, text="Date Joined")
    date_joined_label.pack()
    date_joined_entry = tk.Entry(root)
    date_joined_entry.pack()

    phone_number_label = tk.Label(root, text="Phone Number")
    phone_number_label.pack()
    phone_number_entry = tk.Entry(root)
    phone_number_entry.pack()

    first_name_label = tk.Label(root, text="First Name")
    first_name_label.pack()
    first_name_entry = tk.Entry(root)
    first_name_entry.pack()

    last_name_label = tk.Label(root, text="Last Name")
    last_name_label.pack()
    last_name_entry = tk.Entry(root)
    last_name_entry.pack()

    city_label = tk.Label(root, text="City")
    city_label.pack()
    city_entry = tk.Entry(root)
    city_entry.pack()

    middle_name_label = tk.Label(root, text="Middle Name")
    middle_name_label.pack()
    middle_name_entry = tk.Entry(root)
    middle_name_entry.pack()

    state_label = tk.Label(root, text="State")
    state_label.pack()
    state_entry = tk.Entry(root)
    state_entry.pack()

    p_gender_label = tk.Label(root , text = "Gender")
    p_gender_label.pack()
    p_gender = tk.Entry(root)
    p_gender.pack()

    p_age_label = tk.Label(root, text="Age")
    p_age_label.pack()
    p_age_entry = tk.Entry(root)
    p_age_entry.pack()

    p_email_label = tk.Label(root, text="Email")
    p_email_label.pack()
    p_email_entry = tk.Entry(root)
    p_email_entry.pack()

    login_button = tk.Button(root, text="Signup", width=5, height=5, command=lambda: button_click("Signup"))
    login_button.pack(side="top", padx=30, pady=30)
    back_button = tk.Button(root, text="Back", width=5, height=5, command=lambda: button_click("Back"))
    back_button.pack(side="bottom", padx=30, pady=30)    
    root.mainloop()
    
def user_login():
    root = tk.Tk()
    root.title("User Login")
    set_position_of_tkinter_window(root)
    def button_click(btn):
        if btn == "Login":
            user_id = user_id_entry.get()
            password = password_entry.get()
            query = "SELECT * FROM patient WHERE user_id = %s AND first_name = %s"
            c.execute(query, (user_id, password))
            result = c.fetchall()
            if len(result)>0:
                print("Login successful")
                root.destroy()
                user_homepage(password , user_id) 
            else:
                print("Login failed")
                root.destroy()
                user_login_signup_page()
        elif btn == "Back":
            root.destroy()
            user_login_signup_page()
    user_id_label = tk.Label(root, text="User ID")
    user_id_label.pack()
    user_id_entry = tk.Entry(root)
    user_id_entry.pack()
    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    login_button = tk.Button(root, text="Login", width=5, height=5, command=lambda: button_click("Login"))
    login_button.pack(side="top", padx=30, pady=30)
    back_button = tk.Button(root, text="Back", width=5, height=5, command=lambda: button_click("Back"))
    back_button.pack(side="bottom", padx=30, pady=30)
    root.mainloop()
    return

def user_login_signup_page():
    root = tk.Tk()
    root.title("User Login")
    set_position_of_tkinter_window(root)
    def button_click(btn):
        if btn == "Login":
            root.destroy()
            user_login()
        elif btn == "Signup":
            root.destroy()
            user_signup()
    button_frame = tk.Frame(root, bg="black")
    button_frame.pack(side="top")
    login_button = tk.Button(button_frame, text="Login", width=10, height=5, command=lambda: button_click("Login"))
    login_button.pack(side="left", padx=30, pady=30)
    signup_button = tk.Button(button_frame, text="Signup", width=10, height=5, command=lambda: button_click("Signup"))
    signup_button.pack(side="left", padx=30, pady=30)
    root.mainloop()
# ------------------------------------------------------

def set_position_of_tkinter_window(root):
    root.geometry("1200x1000")
    root.configure(bg="black")
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2-500)
    positionDown = int(root.winfo_screenheight()/2-200 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

def supplier_homepage(password , id):
    root = tk.Tk()
    root.title(f"Welcome Supplier from: {password} , supplier_id: {id}")
    set_position_of_tkinter_window(root)

    tree = ttk.Treeview(root)
    tree["columns"] = ("storage_temp", "concentration", "name", "price", "expiry_date", "recommended_dosage")
    tree.heading("#0", text="Medicine ID")
    tree.heading("storage_temp", text="Storage Temperature")
    tree.heading("concentration", text="Concentration")
    tree.heading("name", text="Name")
    tree.heading("price", text="Price")
    tree.heading("expiry_date", text="Expiry Date")
    tree.heading("recommended_dosage", text="Recommended Dosage")
    tree.pack()
    query = "SELECT * FROM MEDICINE"
    c.execute(query)
    result = c.fetchall()
    for i in result:
        tree.insert("", "end", text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6]))

    def button_click(btn):
        if btn == "Update":
            medicine_id = medicine_id_entry.get()
            quantity = quantity_entry.get()
            c.execute(f"UPDATE medicine SET m_quantity = m_quantity + {quantity} WHERE medicine_id = {medicine_id}")
            connection.commit()
            root.destroy()
            supplier_homepage(password , id)
        elif btn == "Logout":
            root.destroy()
            supplier_login()

    medicine_id_label = tk.Label(root, text="Medicine ID")
    medicine_id_label.pack()
    medicine_id_entry = tk.Entry(root)
    medicine_id_entry.pack()
    quantity_label = tk.Label(root, text="Add Quantity")
    quantity_label.pack()
    quantity_entry = tk.Entry(root)
    quantity_entry.pack()
    update_button = tk.Button(root, text="Update", width=5, height=5, command=lambda: button_click("Update"))
    update_button.pack(side="top", padx=30, pady=30)
    logout_button = tk.Button(root, text="Logout", width=5, height=5, command=lambda: button_click("Logout"))
    logout_button.pack(side="bottom", padx=30, pady=30)   
    root.mainloop()

def supplier_login():
    root = tk.Tk()
    root.title("Supplier Login")
    set_position_of_tkinter_window(root)

    def button_click(btn):
        if btn == "Login":
            supplier_id = supplier_id_entry.get()
            password = password_entry.get()
            query = "SELECT * FROM supplier WHERE supplier_id = %s AND s_location = %s"
            c.execute(query, (supplier_id, password))
            result = c.fetchall()
            if len(result)>0:
                print("Login successful")
                root.destroy()
                supplier_homepage(password , supplier_id)
            else:
                login_failed_label = tk.Label(root, text="Login failed")
                login_failed_label.pack()
        elif btn == "Back":
            root.destroy()
            main_page()
    supplier_id_label = tk.Label(root, text="Supplier ID")
    supplier_id_label.pack()
    supplier_id_entry = tk.Entry(root)
    supplier_id_entry.pack()
    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    login_button = tk.Button(root, text="Login", width=5, height=5, command=lambda: button_click("Login"))
    login_button.pack(side="top", padx=30, pady=30)
    back_button = tk.Button(root, text="Back", width=5, height=5, command=lambda: button_click("Back"))
    back_button.pack(side="bottom", padx=30, pady=30)
    root.mainloop()
 

def main_page():
    root = tk.Tk()
    root.title("My Application")
    set_position_of_tkinter_window(root)
    def button_click(btn):
        if btn == "User":
            root.destroy()
            user_login_signup_page()
        elif btn == "Management":
            root.destroy()
            management_login()
        elif btn == "Supplier":
            root.destroy()
            supplier_login()
    button_frame = tk.Frame(root, bg="black")
    button_frame.pack(expand=True, padx=50, pady=20)
    welcome_label = tk.Label(button_frame, text="Welcome to MediMorph!", font=("Georgia", 50), bg="white")
    # bring it more to the top 
    welcome_label.pack(side="top", fill="x", padx=50, pady=20)
    button_row_frame = tk.Frame(button_frame, bg="black")
    button_row_frame.pack(side="top", pady=50)
    user_button = tk.Button(button_row_frame, text="User", width=20, height=10, bd=2, fg="black", bg="white", font=("Arial", 16), command=lambda: button_click("User"))
    user_button.pack(side="left", padx=50)
    management_button = tk.Button(button_row_frame, text="Management", width=20, height=10, bd=2, fg="black", bg="white", font=("Arial", 16), command=lambda: button_click("Management"))
    management_button.pack(side="left", padx=50)
    supplier_button = tk.Button(button_row_frame, text="Supplier", width=20, height=10, bd=2, fg="black", bg="white", font=("Arial", 16), command=lambda: button_click("Supplier"))
    supplier_button.pack(side="left", padx=50)
    button_frame.pack(anchor="center")
    root.mainloop()


def management_login():
    root = tk.Tk()
    root.title("Management Page")
    set_position_of_tkinter_window(root)
    def button_click(btn):
        if btn == "Login":
            user_id = user_id_entry.get()
            password = password_entry.get()
            query = "SELECT * FROM MANAGEMENT WHERE employee_id = %s AND employee_name = %s" 
            c.execute(query, (user_id, password))
            result = c.fetchall()
            if len(result) == 0:
                invalid_label = tk.Label(root, text="Invalid user id or password")
                invalid_label.pack(side = "bottom", padx=30, pady=30)
            else:
                management_interface(user_id , password) 
        elif btn == "Back":
            root.destroy()
            main_page()

    user_id_label = tk.Label(root, text="User ID")
    user_id_label.pack()
    user_id_entry = tk.Entry(root)
    user_id_entry.pack()

    password_label = tk.Label(root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Login", width=5, height=5, command=lambda: button_click("Login"))
    login_button.pack(side="top", padx=30, pady=30)
    back_button = tk.Button(root, text="Back", width=5, height=5, command=lambda: button_click("Back"))
    back_button.pack(side="bottom", padx=30, pady=30)    

    
    root.mainloop()

def test_olap_query():
    x = int(input("Enter the OLAP query number to execute the query: "))
    if x == 1:
        query = "SELECT IF(GROUPING(employee_shift), 'ALL SHIFTS',employee_shift) AS EMPLOYEE_SHIFT, IF(GROUPING(s_delivery_time), 'ALL TIME',s_delivery_time) AS DELIVERY_TIME, COUNT(*) AS NUMBER_OF_EMPLOYEES FROM management,supplier WHERE management.employee_id = supplier.employee_id GROUP BY employee_shift,s_delivery_time WITH ROLLUP;"
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns) 
        for i in result:
            for j in i:
                print(j, end="   ")
            print()
    elif x == 2:
        query = "SELECT IF(GROUPING(m_name), 'ALL MEDICINES WITH THE NAME',m_name) AS MEDICINE_NAME, IF(GROUPING(m_expiry_data),'ALL EXPIRY MEDICINES',m_expiry_data) AS EXPIRY_DATE, SUM(m_quantity*m_price) AS TOTAL_PRICE FROM medicine GROUP BY m_name, m_expiry_data WITH ROLLUP;"
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns) 
        for i in result:
            for j in i:
                print(j, end="   ")
            print()
    elif x == 3:
        query = "SELECT IF(GROUPING(state), 'ALL STATES',state) AS STATE_OF_PEOPLE, IF(GROUPING(p_date_joined),'ALL DATES',p_date_joined) AS DATE_JOINED, COUNT(*) AS TOTAL_COUNTING FROM patient GROUP BY state, p_date_joined WITH ROLLUP;"   
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns) 
        for i in result:
            for j in i:
                print(j, end="  ")
            print()
    elif x == 4:
        query = "SELECT IF(GROUPING(user_id), 'ALL USERS',user_id) AS USER_ID, IF(GROUPING(type), 'ALL TYPES',type) AS TYPE_OF_SERVICE, SUM(quantity) AS TOTAL_QUANTITY FROM order_history GROUP BY user_id,type WITH ROLLUP;"
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns) 
        for i in result:
            for j in i:
                print(j, end="  ")
            print()
    elif x == 5:
        query = "SELECT IF(GROUPING(employee_shift), 'ALL SHIFTS',employee_shift) AS SHIFT, COUNT(*) AS COUNTING FROM management GROUP BY employee_shift WITH ROLLUP;"
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns)
        for i in result:
            for j in i:
                print(j, end="  ")
            print()

def transaction():
    x = int(input("Enter the transaction number to execute: "))

    #1a
    if x == 1: 
        '''
        use mydb ;  
        SET autocommit = 1;
        start transaction ;  
        update doctor 
        set d_fees = d_fees + 1000 
        where doctor_id = 50;
        commit ; 
        '''
        c.execute("use mydb")
        c.execute("SET autocommit = 1")
        c.execute("start transaction")
        c.execute("update doctor set d_fees = d_fees + 1000 where doctor_id = 50")
        c.execute("commit")
        connection.commit()
         
    #1b
    elif x == 2: 
        '''
        use mydb ;  
        SET autocommit = 1;
        start transaction ;  
        update doctor 
        set d_fees = d_fees + 5000 
        where doctor_id = 50;
        commit ; 
        '''
        c.execute("use mydb")
        c.execute("SET autocommit = 1")
        c.execute("start transaction")
        c.execute("update doctor set d_fees = d_fees + 5000 where doctor_id = 50")
        c.execute("commit")
        connection.commit()

    #2a
    elif x == 3:
        '''
        use mydb ; 
        SET autocommit = 1;

        start transaction ; 
        update medicine 
        set m_quantity = m_quantity - 5
        where medicine_id = 2;

        update `Get Lab Tests`
        set `Get Lab Tests`.glt_fasting_time  = `Get Lab Tests`.glt_fasting_time - 40 
        where `Get Lab Tests`.get_lab_test_id = 1 ;
        commit ; 
        '''
        c.execute("use mydb")
        c.execute("SET autocommit = 1")
        c.execute("start transaction")
        c.execute("update medicine set m_quantity = m_quantity - 5 where medicine_id = 2")
        c.execute("update `Get Lab Tests` set `Get Lab Tests`.glt_fasting_time  = `Get Lab Tests`.glt_fasting_time - 40 where `Get Lab Tests`.get_lab_test_id = 1")
        c.execute("commit;")
        connection.commit()

    #2b
    elif x == 4:
        '''
        use mydb ; 
        SET autocommit = 1;

        start transaction ; 
        update medicine 
        set m_quantity = m_quantity + 10
        where medicine_id = 2;

        update `Get Lab Tests`
        set `Get Lab Tests`.glt_fasting_time  = `Get Lab Tests`.glt_fasting_time + 10 
        where `Get Lab Tests`.get_lab_test_id = 1 ; 

        update Doctor 
        set d_fees = d_fees + 1000
        where doctor_id = 50 ;

        commit ; 

        ''' 
        c.execute("use mydb")
        c.execute("SET autocommit = 1")
        c.execute("start transaction")
        c.execute("update medicine set m_quantity = m_quantity + 10 where medicine_id = 2")
        c.execute("update `Get Lab Tests` set `Get Lab Tests`.glt_fasting_time  = `Get Lab Tests`.glt_fasting_time + 10 where `Get Lab Tests`.get_lab_test_id = 1")
        c.execute("update Doctor set d_fees = d_fees + 1000 where doctor_id = 50")
        c.execute("commit;")
        connection.commit()

    elif x==5:
        '''
        use mydb ;
        start transaction ;
        insert into management (employee_id, employee_name, employee_shift, employee_phone) 
        values (
            111, 'Vasan', 'morning', '+12345'
        );
        savepoint one ; 

        select * from management
        where employee_name = 'Vasan'; 
        commit ; 
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("insert into management (employee_id, employee_name, employee_shift, employee_phone) values (111, 'Vasan', 'morning', '+12345')")
        c.execute("savepoint one")
        c.execute("select * from management where employee_name = 'Vasan'")
        results = c.fetchall()
        c.execute("commit;")
        connection.commit()

    elif x==6:
        '''
        use mydb ;

        start transaction ;

        select * from medicine 
        where medicine_id = 1;

        commit ; 
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("select * from medicine where medicine_id = 1")
        results = c.fetchall()
        c.execute("commit")
        connection.commit()
    
    elif x==7:
        '''
        use mydb ;
        start transaction ;

        select * from medicine 
        where medicine_id = 5;

        commit ;
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("select * from medicine where medicine_id = 5")
        results = c.fetchall()
        c.execute("commit")
        connection.commit()

    elif x==8:
        '''
        use mydb ;

        start transaction ;

        savepoint one ;
        update medicine 
        set m_concentration = 1
        where medicine_id = 50; 

        savepoint two ;
        update medicine 
        set m_concentration = 1
        where medicine_id = 51; 

        savepoint three ;
        update medicine 
        set m_concentration = 1
        where medicine_id = 52; 
        rollback to savepoint three ; 
        commit ; 
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("savepoint one")
        c.execute("update medicine set m_concentration = 1 where medicine_id = 50")
        c.execute("savepoint two")
        c.execute("update medicine set m_concentration = 1 where medicine_id = 51")
        c.execute("savepoint three")
        c.execute("update medicine set m_concentration = 1 where medicine_id = 52")
        c.execute("rollback to savepoint three")
        c.execute("commit")
        connection.commit()
    
    elif x==9:
        '''
        use mydb ;

        start transaction ;

        savepoint one ;
        update doctor 
        set d_fees = 1000
        where doctor_id = 50; 

        savepoint two ;
        update doctor 
        set d_fees = 1000
        where doctor_id = 51; 

        savepoint three ;
        update doctor 
        set d_fees = 1000
        where doctor_id = 52; 

        commit ; 
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("savepoint one")
        c.execute("update doctor set d_fees = 1000 where doctor_id = 50")
        c.execute("savepoint two")
        c.execute("update doctor set d_fees = 1000 where doctor_id = 51")
        c.execute("savepoint three")
        c.execute("update doctor set d_fees = 1000 where doctor_id = 52")
        c.execute("commit")
        connection.commit()

    elif x==10:
        '''
        use mydb ;
        start transaction ;
        update doctor 
        set d_name = "Dari"
        where doctor_id = 6;

        update doctor 
        set d_name = "Raman"
        where doctor_id = 8;
        commit ;
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("update doctor set d_name = \"Dari\" where doctor_id = 6")
        c.execute("update doctor set d_name = \"Raman\" where doctor_id = 8")
        c.execute("commit")
        connection.commit()

    elif x==11:
        '''
        use mydb ;
        start transaction ;
        update doctor 
        set d_name = "Pankaj"
        where doctor_id = 7;
        commit ; 
        '''
        c.execute("use mydb")
        c.execute("start transaction")
        c.execute("update doctor set d_name = \"Pankaj\" where doctor_id = 7")
        c.execute("commit")
        connection.commit()



while(True):
    print("Welcome to the Pharmacy Management System")
    print("Please select an option:")
    print("1. OLAP")
    print("2. Front End")
    print("3. Shiftwise doctor earning report")
    print("4. Run transactions")
    print("5. View order history")
    
    x = int(input("Enter your choice: "))
    if x == 1:
        test_olap_query()
    elif x == 2:  
        main_page()
    elif x == 3:
        m = input("Enter the shift: ")
        query = f"SELECT  identifying_id AS doctor_id , d_experience AS experience , SUM(quantity) AS number_of_consultations, d_fees , d_fees*SUM(quantity) AS earning FROM order_history JOIN doctor ON doctor_id = identifying_id WHERE type IN ('doctor') and identifying_id IN ( SELECT doctor_id FROM doctor WHERE timings = '{m}' ) GROUP BY doctor_id ORDER BY earning DESC , experience;"
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns)
        for i in result:
            for j in i:
                print(j, end="  ")
            print()
    elif x == 4:
        transaction()
    elif x == 5:
        query = "select * from order_summary"
        c.execute(query)
        result = c.fetchall()
        columns = [i[0] for i in c.description]
        print(columns)
        for i in result:
            for j in i:
                print(j, end="  ")
            print()
    else:
        print("Invalid choice")
        break ; 

#-----------------------------------------------  
#CLOSE DATABASE
c.close()












