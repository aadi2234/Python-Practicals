from tkinter import *
import random
import tempfile
import os
import tkinter.messagebox as mb

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1280, height=750)
        self.root.minsize(width=1280, height=750)
        self.root.title("Bhagavti Kirana")

        # *********************Variables***********************#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        # For Generating Random Bill Numbers
        x = random.randint(1, 9999)
        self.c_bill_no = StringVar()
        # Seting Value to variable
        self.c_bill_no.set(str(x))

        self.bath_soap = IntVar()
        self.tea_powder = IntVar()
        self.Coffee = IntVar()
        self.dry_coconut = IntVar()
        self.mango_pickle = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.Milk = IntVar()
        self.Salt = IntVar()
        self.CoconutOil = IntVar()
        self.groundnuts = IntVar()
        self.biscuits = IntVar()
        self.total_ = StringVar()
        self.tax_cos = StringVar()

        # *********************Header of Application*********************#
        bg_color = "#ADD8E6"
        fg_color = "black"
        lbl_color = 'black'
        # Title of App
        title = Label(self.root, text="Bhagavti Kirana Store", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        # *********************Customers Frame*********************#
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="red", bg=bg_color,relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # *********************Customer Name*********************#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        #*********************Customer Phone*********************#
        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # *********************Customer Bill No*********************#
        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ********************* Frame*********************#
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        # *********************Frame Content*********************#
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bath Soap (qty)")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bath_soap)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        #*********************Tea Powder*********************#
        face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tea Powder (qty)")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.tea_powder)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # *********************Coffee*********************#
        wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coffee (qty)")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Coffee)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # *********************Dry Coconut*********************#
        hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Dry Coconut (kg)")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.dry_coconut)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        #*********************Mango Pickle*********************#
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Mango Pickle (qty)")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.mango_pickle)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # *********************Grocery Frame*********************#
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        # *********************Frame Content
        rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice (kg)")
        rice_lbl.grid(row=0, column=0, padx=10, pady=20)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

      # *********************Food Oil
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil (ltr)")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.food_oil)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # *********************Daal
        daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal (kg)")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.daal)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        #*********************Wheat
        wheat_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat (kg)")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============Sugar
        sugar_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sugar (kg)")
        sugar_lbl.grid(row=4, column=0, padx=10, pady=20)
        sugar_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sugar)
        sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        # ===========Frame Content
        Milk_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Milk (ltr)")
        Milk_lbl.grid(row=0, column=0, padx=10, pady=20)
        Milk_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Milk)
        Milk_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======Salt
        cock_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Salt (kg)")
        cock_lbl.grid(row=1, column=0, padx=10, pady=20)
        cock_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Salt)
        cock_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======Coconut Oil
        CoconutOil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coconut Oil (ltr)")
        CoconutOil_lbl.grid(row=2, column=0, padx=10, pady=20)
        CoconutOil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.CoconutOil)
        CoconutOil_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========Groundnuts
        cold_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Groundnuts (kg)")
        cold_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.groundnuts)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============Biscuits
        bis_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Biscuits (qty)")
        bis_lbl.grid(row=4, column=0, padx=10, pady=20)
        bis_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.biscuits)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=960, y=180, width=325, height=380)
        # ===========
        bill_title = Label(F3, text="Bill Area", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="red",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=100)

        # ===================
        lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total ")
        lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ================Tax
        cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text=" GST")
        cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
        cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_cos)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)
        # ====================
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,command=self.total)
        total_btn.grid(row=0, column=4, ipadx=20, padx=30)

        # ========================
        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=0, column=5, ipadx=20)

        # ====================
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=0, column=6, ipadx=20, padx=30)

        # ======================
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=0, column=7, ipadx=20)
        
        # ======================
        print_btn = Button(F4, text="Print", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.confirm_print)
        print_btn.grid(row=0, column=8, ipadx=20)

    # Function to get total prices
    def total(self):
        # =================Total  Prices
        self.total__prices = (
                (self.bath_soap.get() * 20) +
                (self.tea_powder.get() * 100) +
                (self.Coffee.get() * 140) +
                (self.dry_coconut.get() * 240) +
                (self.mango_pickle.get() * 260) +
                (self.rice.get() * 60) +
                (self.daal.get() * 80) +
                (self.food_oil.get() * 110) +
                (self.wheat.get() * 50) +
                (self.sugar.get() * 45) +
                (self.Milk.get() * 55) +
                (self.Salt.get() * 20) +
                (self.CoconutOil.get() * 200) +
                (self.groundnuts.get() * 150) +
                (self.biscuits.get() * 30)
        )

        self.total_.set(str(self.total__prices))

        # ==================Tax
        self.tax = ((self.total__prices * 2.5) / 100)
        self.tax_cos.set(str(round(self.tax, 2)))

    # ==================Bill Generation
    def bill_area(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "Panchkrushna Kirana Store\n")
        self.txt.insert(END, "Phone: 1234567890\n")
        self.txt.insert(END, "Add: Near Gandhi Circle, Xyz City\n")
        self.txt.insert(END, "********************************\n")
        self.txt.insert(END, f"Bill No: {self.c_bill_no.get()}\n")
        self.txt.insert(END, f"Customer Name: {self.cus_name.get()}\n")
        self.txt.insert(END, f"Phone No: {self.c_phone.get()}\n")
        self.txt.insert(END, "********************************\n")
        self.txt.insert(END, "Products\t\tQty\tPrice\n")
        self.txt.insert(END, "********************************\n")
        self.txt.insert(END, f"Bath Soap\t\t{self.bath_soap.get()}\t{self.bath_soap.get()*20}\n")
        self.txt.insert(END, f"Tea Powder\t\t{self.tea_powder.get()}\t{self.tea_powder.get()*100}\n")
        self.txt.insert(END, f"Coffee\t\t{self.Coffee.get()}\t{self.Coffee.get()*140}\n")
        self.txt.insert(END, f"Dry Coconut\t\t{self.dry_coconut.get()}kg\t{self.dry_coconut.get()*240}\n")
        self.txt.insert(END, f"Mango Pickle\t\t{self.mango_pickle.get()}\t{self.mango_pickle.get()*260}\n")
        self.txt.insert(END, f"Rice\t\t{self.rice.get()}kg\t{self.rice.get()*60}\n")
        self.txt.insert(END, f"Daal\t\t{self.daal.get()}kg\t{self.daal.get()*80}\n")
        self.txt.insert(END, f"Food Oil\t\t{self.food_oil.get()}ltr\t{self.food_oil.get()*110}\n")
        self.txt.insert(END, f"Wheat\t\t{self.wheat.get()}kg\t{self.wheat.get()*50}\n")
        self.txt.insert(END, f"Sugar\t\t{self.sugar.get()}kg\t{self.sugar.get()*45}\n")
        self.txt.insert(END, f"Milk\t\t{self.Milk.get()}ltr\t{self.Milk.get()*55}\n")
        self.txt.insert(END, f"Salt\t\t{self.Salt.get()}kg\t{self.Salt.get()*20}\n")
        self.txt.insert(END, f"Coconut Oil\t\t{self.CoconutOil.get()}ltr\t{self.CoconutOil.get()*200}\n")
        self.txt.insert(END, f"Groundnuts\t\t{self.groundnuts.get()}kg\t{self.groundnuts.get()*150}\n")
        self.txt.insert(END, f"Biscuits\t\t{self.biscuits.get()}\t{self.biscuits.get()*30}\n")
        self.txt.insert(END, "********************************\n")
        self.txt.insert(END, f"Total Amount:\t\t{self.total_.get()}\n")
        self.txt.insert(END, f"GST:\t\t{self.tax_cos.get()}\n")
        self.txt.insert(END, "********************************\n")
        self.txt.insert(END, "Thank You for Visiting\n")
        self.txt.insert(END, "********************************\n")

    # ==================Clear Functions
    def clear(self):
        self.bath_soap.set(0)
        self.tea_powder.set(0)
        self.Coffee.set(0)
        self.dry_coconut.set(0)
        self.mango_pickle.set(0)
        self.rice.set(0)
        self.daal.set(0)
        self.food_oil.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.Milk.set(0)
        self.Salt.set(0)
        self.CoconutOil.set(0)
        self.groundnuts.set(0)
        self.biscuits.set(0)
        self.total_.set("")
        self.tax_cos.set("")
        self.cus_name.set("")
        self.c_phone.set("")
        self.c_bill_no.set(random.randint(1, 9999))
        self.txt.delete('1.0', END)

    # ===================Exit Function
    def exit(self):
        op = mb.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

    # ===================Confirmation Prompt for Print
    def confirm_print(self):
        confirmation = mb.askyesno("Print Bill", "Do you want to print the bill?")
        if confirmation:
            self.print_bill()

    # ===================Print Function
    def print_bill(self):
        # Generate temporary file path
        file_path = os.path.join(tempfile.gettempdir(), "bill.txt")
        with open(file_path, "w") as file:
            file.write(self.txt.get("1.0", "end-1c"))
        # Print the file
        os.startfile(file_path, "print")

# =====================Root Method===================#
if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
