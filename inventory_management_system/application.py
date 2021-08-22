# import all the modules
from tkinter import *
from tkinter import messagebox

import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import datetime
import math

date = datetime.datetime.now().date()
# temporary list like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []
r = []


class Application():
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.left = Frame(master, width=540, height=620, bg='#fefefe')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=620, bg='#ededed')
        self.right.pack(side=RIGHT)

        # components
        self.heading = Label(self.left, text="ONEMOUNT'S STORE", font=(
            'system-ui 40 bold'), fg='black', bg="#fefefe")
        self.heading.place(x=10, y=10)

        self.date_l = Label(self.right, text="Today's Date: " +
                            str(date), font=('system-ui 16 bold'), fg='black', bg="#ededed")
        self.date_l.place(x=10, y=18)

        # table invoice=======================================================
        self.tproduct = Label(self.right, text="Products", font=(
            'system-ui 18 bold'), bg='#ededed', fg='black')
        self.tproduct.place(x=10, y=80)

        self.tquantity = Label(self.right, text="Quantity", font=(
            'system-ui 18 bold'), bg='#ededed', fg='black')
        self.tquantity.place(x=300, y=80)

        self.tamount = Label(self.right, text="Amount", font=(
            'system-ui 18 bold'), bg='#ededed', fg='black')
        self.tamount.place(x=500, y=80)

        # enter stuff
        self.enterid = Label(self.left, text="Enter Product's ID", font=(
            'system-ui 18 bold'), fg='black', bg="#fefefe")
        self.enterid.place(x=10, y=88)

        self.enteride = Entry(self.left, font=(
            'system-ui 18 bold'), bg='lightblue')
        self.enteride.place(x=220, y=80, width=200, height=40)
        self.enteride.focus()

        # button
        self.search_btn = Button(
            self.left, text="Search", bg='orange', command=self.ajax)
        self.search_btn.place(x=430, y=80, width=100, height=40)

        # fill it later by the function ajax
        self.productname = Label(self.left, text="", font=(
            'system-ui 27 bold'), bg='#fefefe', fg='black')
        self.productname.place(x=10, y=250)

        self.pprice = Label(self.left, text="", font=(
            'system-ui 27 bold'), bg='#fefefe', fg='black')
        self.pprice.place(x=10, y=290)

        # total label
        self.total_l = Label(self.right, text="", font=(
            'system-ui 40 bold'))
        self.total_l.place(x=10, y=548)

    def ajax(self, *args, **kwargs):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='inventory_system',
                                            user='root',
                                            password='123456')
        self.get_id = self.enteride.get()
        # get the product info with that id and fill i the labels above
        self.mycursor = self.conn.cursor()
        self.mycursor.execute(
            "SELECT * FROM inventory WHERE id= %s", [self.get_id])
        self.pc = self.mycursor.fetchall()
        if self.pc:
            for self.r in self.pc:
                self.get_id = self.r[0]
                self.get_name = self.r[1]
                self.get_price = self.r[3]
                self.get_stock = self.r[2]
            self.productname.configure(
                text="Product's Name: " + str(self.get_name))
            self.pprice.configure(
                text="Price:RS. "+str(self.get_price))

        # craete the quantity and the discount label
            self.quantityl = Label(self.left, text="Enter Quantity", font=(
                'system-ui 18 bold'), bg="#fefefe")
            self.quantityl.place(x=10, y=370)

            self.quantity_e = Entry(self.left, font=(
                'system-ui 18 bold'), bg='lightblue')
            self.quantity_e.place(x=10, y=394, width=200, height=40)
            self.quantity_e.focus()

        # discount
            self.discount_l = Label(self.left, text="Enter Discount", font=(
                'system-ui 18 bold'), bg="#fefefe")
            self.discount_l.place(x=220, y=370)

            self.discount_e = Entry(self.left, width=25, font=(
                'system-ui 18 bold'), bg='lightblue')
            self.discount_e.place(x=220, y=394, width=200, height=40)
            self.discount_e.insert(END, 0)

        # add to cart button
            self.add_to_cart_btn = Button(
                self.left, text="Add to Cart", bg='orange', command=self.add_to_cart)
            self.add_to_cart_btn.place(x=430, y=394, width=100, height=40)

        # genrate bill and change
            self.change_l = Label(self.left, text="Given Amount", font=(
                'system-ui 18 bold'), fg='black', bg='#fefefe')
            self.change_l.place(x=10, y=464)

            self.change_e = Entry(self.left, font=(
                'system-ui 18 bold'), bg='lightblue')
            self.change_e.place(x=10, y=488, width=200, height=40)

            self.change_btn = Button(self.left, text="Calculate Change", bg='orange', command=self.change_func)
            self.change_btn.place(x=220, y=488, height=40)

        # geneerate bill button
            self.bill_btn = Button(self.left, text="Generate Bill", bg='orange', fg='black', command=self.generate_bill)
            self.bill_btn.place(x=10, y=558, width=520, height=40)
        else:
            messagebox.showinfo("success", "Done everything smoothly")

    def add_to_cart(self, *args, **kwargs):
        self.quantity_value = int(self.quantity_e.get())

        if self .quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo(
                "Error", "Not that any products in our stock.")
        else:
            # calculate the price first
            self.final_price = (float(self.quantity_value) *
                                float(self.get_price))-(float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index = 10
            self.y_index = 117
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=(
                    'system-ui 18'), bg='#ededed', fg='black')
                self.tempname.place(x=10, y=self.y_index)
                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=(
                    'system-ui 18'), bg='#ededed', fg='black')
                self.tempqt.place(x=300, y=self.y_index)
                self.tempprice = Label(self.right, text=str(
                    product_price[self.counter]), font=('system-ui 18'), bg='#ededed', fg='black')
                self.tempprice.place(x=500, y=self.y_index)

                self.y_index += 36
                self.counter += 1

                # total configure
                self.total_l.configure(
                    text="Total : VND "+str(sum(product_price)), bg='#ededed', fg='black')
                # delete
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.quantityl.configure(text="")
                self.add_to_cart_btn.destroy()
                # autofocus to the enter id
                self.enteride.focus()
                self.quantityl.focus()
                self.enteride.delete(0, END)

    def change_func(self, *args, **kwargs):
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given-self.our_total

        # label change
        self.c_amount = Label(self.left, text="Change: Rs. " +
                              str(self.to_give), font=('system-ui 18 bold'), fg='red', bg='#fefefe')
        self.c_amount.place(x=370, y=494)

    def generate_bill(self, *args, **kwargs):
        self.mycursor.execute(
            "SELECT * FROM inventory WHERE id=%s", [self.get_id])
        self.pc = self.mycursor.fetchall()
        for r in self.pc:
            self.old_stock = r[2]
        for i in products_list:
            for r in self.pc:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(self.quantity_value)
            # updating the stock
            self.mycursor.execute("UPDATE inventory SET stock=%s WHERE id=%s", [
                                  self.new_stock, self.get_id])
            self.conn.commit()

            # inster into transcation
            self.mycursor.execute("INSERT INTO transaction (product_name,quantity,amount,date) VALUES(%s,%s,%s,%s)", [
                                  self.get_name, self.quantity_value, self.get_price, date])
            self.conn.commit()
            print("Decreased")

        tkinter.messagebox.showinfo("success", "Done everything smoothly")


root = Tk()
root.resizable(False, False)
Application(root)
root.geometry("1206x620")
root.eval('tk::PlaceWindow . center')
root.title("Inventory Management System by Techmaster.vn")
root.mainloop()
