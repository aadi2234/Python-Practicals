from tkinter import *
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1280, height=750)
        self.root.minsize(width=1280, height=750)
        self.root.title("Panchkrushna Kirana")

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
        bg_color = "#FFF86D"
        fg_color = "black"
        lbl_color = 'black'
        # Title of App
        title = Label(self.root, text="Panchkrushna Kirana Store", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

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
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bath Soap")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bath_soap)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        #*********************Tea Powder*********************#
        face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tea Powder")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.tea_powder)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # *********************Coffee*********************#
        wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coffee")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Coffee)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # *********************Dry Coconut*********************#
        hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Dry Coconut")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.dry_coconut)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        #*********************Mango Pickle*********************#
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Mango Pickle")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.mango_pickle)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # *********************Grocery Frame*********************#
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        # *********************Frame Content
        rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
        rice_lbl.grid(row=0, column=0, padx=10, pady=20)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

      # *********************Food Oil
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.food_oil)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # *********************Daal
        daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.daal)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        #*********************Wheat
        wheat_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============Sugar
        sugar_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sugar")
        sugar_lbl.grid(row=4, column=0, padx=10, pady=20)
        sugar_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sugar)
        sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        # ===========Frame Content
        Milk_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Milk")
        Milk_lbl.grid(row=0, column=0, padx=10, pady=20)
        Milk_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Milk)
        Milk_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======Salt
        cock_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Salt")
        cock_lbl.grid(row=1, column=0, padx=10, pady=20)
        cock_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.Salt)
        cock_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======Coconut Oil
        CoconutOil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coconut Oil")
        CoconutOil_lbl.grid(row=2, column=0, padx=10, pady=20)
        CoconutOil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.CoconutOil)
        CoconutOil_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========Groundnuts
        cold_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Groundnuts ")
        cold_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.groundnuts)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============Biscuits
        bis_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Biscuits")
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

    # Function to get total prices
    def total(self):
        # =================Total  Prices
        self.total__prices = (
                (self.bath_soap.get() * 20) +
                (self.tea_powder.get() * 100) +
                (self.Coffee.get() * 140) +
                (self.dry_coconut.get() * 240) +
                (self.mango_pickle.get() * 260)+
                (self.wheat.get() * 100)+
                (self.food_oil.get() * 180) +
                (self.daal.get() * 80) +
                (self.rice.get() * 35) +
                (self.sugar.get() * 45) +
                (self.Milk.get() * 70) +
                (self.CoconutOil.get() * 50) +
                (self.Salt.get() * 10) +
                (self.groundnuts.get() * 50) +
                (self.biscuits.get() * 20)
        )
        self.total_.set("Rs. " + str(self.total__prices))
        self.tax_cos.set("Rs. " + str(float(self.total__prices * 0.05)))

    # Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "     Panchkrushna Kirana Store\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")


    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.bath_soap.get() != 0:
            self.txt.insert(END, f"\nBath Soap         {self.bath_soap.get()}           {self.bath_soap.get() * 20}")
        if self.tea_powder.get() != 0:
            self.txt.insert(END, f"\nTea Powder        {self.tea_powder.get()}           {self.tea_powder.get() * 100}")
        if self.Coffee.get() != 0:
            self.txt.insert(END, f"\nCoffee            {self.Coffee.get()}           {self.Coffee.get() * 140}")
        if self.dry_coconut.get() != 0:
            self.txt.insert(END, f"\nDry Coconut       {self.dry_coconut.get()}           {self.dry_coconut.get() * 240}")
        if self.mango_pickle.get() != 0:
            self.txt.insert(END ,f"\nMango Pickle      {self.mango_pickle.get()}           {self.mango_pickle.get() * 260}")
        if self.wheat.get() != 0:
            self.txt.insert(END, f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END, f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END, f"\nDaal              {self.daal.get()}           {self.daal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END, f"\nRice              {self.rice.get()}           {self.rice.get() * 35}")
        if self.sugar.get() != 0:
            self.txt.insert(END, f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 45}")
        if self.Milk.get() != 0:
            self.txt.insert(END, f"\nMilk              {self.Milk.get()}           {self.Milk.get() * 70}")
        if self.CoconutOil.get() != 0:
            self.txt.insert(END, f"\nCoconut Oil       {self.CoconutOil.get()}           {self.CoconutOil.get() * 50}")
        if self.Salt.get() != 0:
            self.txt.insert(END, f"\nSalt              {self.Salt.get()}           {self.Salt.get() * 10}")
        if self.groundnuts.get() != 0:
            self.txt.insert(END, f"\nGroundnuts        {self.groundnuts.get()}           {self.groundnuts.get() * 50}")
        if self.biscuits.get() != 0:
            self.txt.insert(END, f"\nBiscuits          {self.biscuits.get()}           {self.biscuits.get() * 20}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, f"\nTotal : {self.total__prices + self.total__prices * 0.05}")
        self.txt.insert(END, "\nThank You...! Visit Again")
        self.config(state=DISABLED)
        self.print()



    # Function to exit
    def exit(self):
        self.root.destroy()

    # Function To Clear All Fields


root = Tk()
object = Bill_App(root)
root.mainloop()
