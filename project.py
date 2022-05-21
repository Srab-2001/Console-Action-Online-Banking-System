# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:35:00 2022

@author: ncbyi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:13:36 2022

@author: intel

"""
"""
Database=billing_system
Tabe_name= Bill
Column name= Product_Name,Quantity,GST,Discount,Total

Database=billing_system
Table name= Customer
Column name= Customer_Name,Phone_Number,Product_Name,Quantity_Bought

"""

import mysql.connector
import sys
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="billing_system"
)

while(1):
    print("..................")
    print("1: Insertion")
    print("2: Billing")
    print("3: Updation")
    print("4: Deletion")
    print("5: Searching")
    print("6: EXIT")
    print("..................")

    n=int(input("Enter your choice"))

    if(n==1):
        print("1: Product Table")
        print("2: Customer Table")
        n1=int(input("Enter your choice to insert"))
        if(n1==1):
            mycursor=mydb.cursor()
            name=input("Enter Product Name")
            price=int(input("Enter Price"))
            qty=int(input("Enter product quantity"))
            gst=int(input("Enter product GST amount"))
            dis=int(input("Enter product discount"))
            tot=(price*qty)-dis
            tot=int(tot+(tot*gst)/100)

            sql="insert into Bill(Product_Name,price,Quantity,GST,Discount,Total) values(%s,%s,%s,%s,%s,%s)"
            val=(name,price,qty,gst,dis,tot)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data Inserted")
        if(n1==2):
            mycursor=mydb.cursor()
            Cust_name=input("Enter Customer Name")
            Ph_no=int(input("Enter Phone No."))
            Product_name=input("Enter Product Name")
            qty_bought=int(input("Enter Phone No."))

            sql="insert into Customer(Customer_Name,Phone_Number,Product_Name,Quantity_Bought) values(%s,%s,%s,%s)"
            val=(Cust_name,Ph_no,Product_name,qty_bought)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data Inserted")
            
            
    if(n==2):
            mycursor=mydb.cursor()
            name=input("Enter Customer Name")
            sql="select * from Customer where Customer_Name=%s"
            val=(name,)
            mycursor.execute(sql,val)
           # mydb.commit()
            res=mycursor.fetchall()
            Pr_name=res[0][3]
        
            sql="select * from Bill product where Product_Name=%s"
            val=(Pr_name,)
            mycursor.execute(sql,val)
           # mydb.commit()
            
            res1=mycursor.fetchall()
            print(res1[0][6])
            
            qty_Cust_bought=res[0][4]
            qty_in_stock=res1[0][3]
            Qty_remaining=qty_in_stock-qty_Cust_bought
            sql="insert into Bill(Quantity) values(%s)"
            val=(Qty_remaining,)
            mycursor.execute(sql,val)
            mydb.commit()
            
            
    if(n==3):
            name=input("Enter Product Name")

            if(name=='tv'):
                qty=int(input("Enter product quantity"))
                gst=int(input("Enter product GST amount"))
                dis=int(input("Enter product discount"))
                price=int(input("Enter product price"))
                tot=(price*qty)-dis
                tot=int(tot+(tot*gst)/100)
                mycursor=mydb.cursor()
                sql="update Bill set Quantity=%s,GST=%s,Discount=%s,Total=%s,price=%s where Product_Name=%s"
                val=(qty,gst,dis,tot,price,name)
                mycursor.execute(sql,val)
                mydb.commit()
                print("Table Updated")

            elif(name=='ac'):
                qty=int(input("Enter product quantity"))
                price=int(input("Enter product price"))
                gst=int(input("Enter product GST amount"))
                dis=int(input("Enter product discount"))
                tot=(price*qty)-dis
                tot=int(tot+(tot*gst)/100)
                mycursor=mydb.cursor()
                sql="update Bill set Quantity=%s,GST=%s,Discount=%s,Total=%s,price=%s where Product_Name=%s"
                val=(qty,gst,dis,tot,price,name)
                mycursor.execute(sql,val)
                mydb.commit()
                print("Table Updated")
            
            elif(name=='laptop'):
                qty=int(input("Enter product quantity"))
                price=int(input("Enter product price"))
                gst=int(input("Enter product GST amount"))
                dis=int(input("Enter product discount"))
                tot=(price*qty)-dis
                tot=int(tot+(tot*gst)/100)
                mycursor=mydb.cursor()
                sql="update Bill set Quantity=%s,GST=%s,Discount=%s,Total=%s,price=%s where Product_Name=%s"
                val=(qty,gst,dis,tot,price,name)
                mycursor.execute(sql,val)
                mydb.commit()
                print("Table Updated")
            
            elif(name=='computer'):
                qty=int(input("Enter product quantity"))
                price=int(input("Enter product price"))
                gst=int(input("Enter product GST amount"))
                dis=int(input("Enter product discount"))
                tot=(price*qty)-dis
                tot=int(tot+(tot*gst)/100)
                mycursor=mydb.cursor()
                sql="update Bill set Quantity=%s,GST=%s,Discount=%s,Total=%s,price=%s where Product_Name=%s"
                val=(qty,gst,dis,tot,price,name)
                mycursor.execute(sql,val)
                mydb.commit()
                print("Table Updated")
                
            
    if(n==4):
            name=input("Enter Product Name")
            mycursor=mydb.cursor()
            sql="delete from Bill where Product_name=%s"
            val=(name,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Row Deleted")
    if(n==5):
            name=input("Enter Product Name to be searched")
            mycursor=mydb.cursor()
            sql="select * from Bill where Product_Name=%s"
            val=(name,)
            mycursor.execute(sql,val)
            res=mycursor.fetchall()
            print(type(res))
            for i in res:
                print(i)
            
    if(n==6):
        sys.exit()
n=int(input("Enter your choice"))        


    

    
