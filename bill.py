from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("My Textiles")
        title=Label(self.root,text="Cloth Billing",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.slip=IntVar()
        self.panties=IntVar()
        self.brasier=IntVar()
        self.chudi=IntVar()
        self.saree=IntVar()
        self.towel=IntVar()
        self.shawl=IntVar()
        self.tops=IntVar()
        self.linning=IntVar()
        self.legginngs=IntVar()
        self.plazo=IntVar()
        self.skimmer=IntVar()
        self.shirt=IntVar()
        self.dhoti=IntVar()
        self.trunks=IntVar()
        self.vest=IntVar()
        self.kerchiefs=IntVar()
        self.jetty=IntVar()	
        self.lungi=IntVar()
        self.tshirt=IntVar()
        self.jeans=IntVar()
        self.total_inners=StringVar()
        self.total_men=StringVar()
        self.total_women=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)
        
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)
        
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)
        
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #======================================= label frame=================================================================
        inners=LabelFrame(self.root,text="Inners",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        inners.place(x=5,y=180,height=380,width=325)
        
        item1=Label(inners,text="slip",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(inners,borderwidth=2,width=15,textvariable= self.slip).grid(row=0,column=1,padx=10)

        item2=Label(inners,text="panties",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(inners,borderwidth=2,width=15,textvariable=self.panties).grid(row=1,column=1,padx=10)

        item3=Label(inners,text="brasier",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(inners,borderwidth=2,width=15,textvariable=self.brasier).grid(row=2,column=1,padx=10)

        item4=Label(inners,text="trunks",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(inners,borderwidth=2,width=15,textvariable=self.trunks).grid(row=3,column=1,padx=10)

        item5=Label(inners,text="vest",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(inners,borderwidth=2,width=15,textvariable=self.vest).grid(row=4,column=1,padx=10)

        item6=Label(inners,text="jetty",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(inners,borderwidth=2,width=15,textvariable=self.jetty).grid(row=5,column=1,padx=10)

        item7=Label(inners,text="Linning",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(inners,borderwidth=2,width=15,textvariable=self.linning).grid(row=6,column=1,padx=10)
        #===================================GROCERY=====================================================================================
        mens=LabelFrame(self.root,text="Mens",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        mens.place(x=340,y=180,height=380,width=325)

        item8=Label(mens,text="kerchief",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.kerchiefs).grid(row=0,column=1,padx=10)

        item9=Label(mens,text="shirt",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.shirt).grid(row=1,column=1,padx=10)

        item10=Label(mens,text="dhoti",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.dhoti).grid(row=2,column=1,padx=10)

        item11=Label(mens,text="lungi",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.lungi).grid(row=3,column=1,padx=10)

        item12=Label(mens,text="towel",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.towel).grid(row=4,column=1,padx=10)

        item13=Label(mens,text="tshirt",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.tshirt).grid(row=5,column=1,padx=10)

        item14=Label(mens,text="jeans",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(mens,borderwidth=2,width=15,textvariable=self.jeans).grid(row=6,column=1,padx=10)
        #========================================beauty and hygine===============================================================================
        girls=LabelFrame(self.root,text="Girls",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        girls.place(x=677,y=180,height=380,width=325)

        item15=Label(girls,text="saree",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.saree).grid(row=0,column=1,padx=10)

        item16=Label(girls,text="chudi",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.chudi).grid(row=1,column=1,padx=10)

        item17=Label(girls,text="tops",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.tops).grid(row=2,column=1,padx=10)

        item18=Label(girls,text="leggings",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.legginngs).grid(row=3,column=1,padx=10)

        item19=Label(girls,text="plazo",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.plazo).grid(row=4,column=1,padx=10)

        item20=Label(girls,text="skimmer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.skimmer).grid(row=5,column=1,padx=10)

        item21=Label(girls,text="shawl",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(girls,borderwidth=2,width=15,textvariable=self.shawl).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_inners=Label(billing_menu,text="Total Inners Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_inners_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_inners).grid(row=0,column=1,padx=10,pady=7)
        
        total_mens=Label(billing_menu,text="Total Mens Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_mens_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_men).grid(row=1,column=1,padx=10,pady=7)

        
        total_womens=Label(billing_menu,text="Total Women Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_womens_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_women).grid(row=2,column=1,padx=10,pady=7)

        tax_inners=Label(billing_menu,text="inners Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_inners_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
        
        tax_mens=Label(billing_menu,text="men Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_mens_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)

        
        tax_womens=Label(billing_menu,text="women Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_womens_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)
        
        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.sl= self.slip.get()*80
    self.pa=self.panties.get()*40
    self.br=self.brasier.get()*30
    self.tr=self.trunks.get()*120
    self.ve=self.vest.get()*90
    self.je=self.jetty.get()*70
    self.li=self.linning.get()*40
    total_inners_price=(
                self.sl+
                self.pa+
                self.br+
                self.tr+
                self.ve+
                self.je+
                self.li)          
    self.total_inners.set(str(total_inners_price)+" Rs")
    self.a.set(str(round(total_inners_price*0.05,3))+" Rs")

    self.ke=self.kerchief.get()*20
    self.sh=self.shirt.get()*250
    self.dh=self.dhoti.get()*150
    self.lu=self.lungi.get()*120
    self.to=self.towel.get()*40
    self.ts=self.tshirt.get()*200
    self.jea=self.jeans.get()*750
    total_mens_price=(
        self.ke+
        self.sh+
        self.dh+
        self.lu+
        self.to+
        self.ts+
        self.jea)
        
    self.total_men.set(str(total_mens_price)+" Rs")
    self.b.set(str(round(total_mens_price*0.01,3))+" Rs")

    self.sa=self.saree.get()*800
    self.ch=self.chudi.get()*250
    self.top=self.tops.get()*150
    self.leg=self.leggings.get()*300
    self.pl=self.plazo.get()*850
    self.ski=self.skimmer.get()*400
    self.sha=self.shawl.get()*120
    
    total_women_price=(
        self.sa+
        self.ch+
        self.top+
        self.leg+
        self.pl+
        self.ski+
        self.sha)
        
    self.total_women.set(str(total_women_price)+" Rs")
    self.c.set(str(round(total_women_price*0.10,3))+" Rs")
    self.total_all_bill=(total_inners_price+
                total_mens_price+
                total_women_price+
                (round(total_mens_price*0.01,3))+
                (round(total_women_price*0.10,3))+
                (round(total_inners_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO K.R.TEX\n\tPhone-No.9876543210")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.slip.get()!=0:
        self.txtarea.insert(END,f"slip\t\t {self.slip.get()}\t{self.nu}\n")
    if self.panties.get()!=0:
        self.txtarea.insert(END,f"panties\t\t {self.panties.get()}\t{self.no}\n")
    if self.brasiers.get()!=0:
        self.txtarea.insert(END,f"brasiers\t\t {self.brasiers.get()}\t{self.la}\n")
    if self.trunks.get()!=0:
        self.txtarea.insert(END,f"trunks\t\t {self.trunks.get()}\t{self.ore}\n")
    if self.vest.get()!=0:
        self.txtarea.insert(END,f"vests\t\t {self.vest.get()}\t{self.mu}\n")
    if self.jetty.get()!=0:
        self.txtarea.insert(END,f"jetty\t\t {self.jetty.get()}\t{self.si}\n")
    if self.linning.get()!=0:
        self.txtarea.insert(END,f"linning\t\t {self.linning.get()}\t{self.na}\n")
    if self.kerchief.get()!=0:
        self.txtarea.insert(END,f"kerchief\t\t {self.kerchief.get()}\t{self.at}\n")
    if self.shirt.get()!=0:
        self.txtarea.insert(END,f"shirt\t\t {self.shirt.get()}\t{self.pa}\n")
    if self.dhoti.get()!=0:
        self.txtarea.insert(END,f"dhoti\t\t {self.dhoti.get()}\t{self.ri}\n")
    if self.lungi.get()!=0:
        self.txtarea.insert(END,f"lungi\t\t {self.lungi.get()}\t{self.oi}\n")
    if self.towel.get()!=0:
        self.txtarea.insert(END,f"towel\t\t {self.towel.get()}\t{self.su}\n")
    if self.tshirt.get()!=0:
        self.txtarea.insert(END,f"tshirt\t\t {self.tshirt.get()}\t{self.da}\n")
    if self.jeans.get()!=0:
        self.txtarea.insert(END,f"jeans\t\t {self.jeans.get()}\t{self.te}\n")
    if self.saree.get()!=0:
        self.txtarea.insert(END,f"saree\t\t {self.saree.get()}\t{self.so}\n")
    if self.chudi.get()!=0:
        self.txtarea.insert(END,f"chudi\t\t {self.chudi.get()}\t{self.sh}\n")
    if self.tops.get()!=0:
        self.txtarea.insert(END,f"tops\t\t {self.tops.get()}\t{self.lo}\n")
    if self.leggings.get()!=0:
        self.txtarea.insert(END,f"leggings\t\t {self.leggings.get()}\t{self.cr}\n")
    if self.plazo.get()!=0:
        self.txtarea.insert(END,f"plazo\t\t {self.plazo.get()}\t{self.fo}\n")
    if self.skimmer.get()!=0:
        self.txtarea.insert(END,f"skimmer\t\t {self.skimmer.get()}\t{self.ma}\n")
    if self.shawl.get()!=0:
        self.txtarea.insert(END,f"shawl\t\t {self.shawl.get()}\t{self.sa}\n")
        
    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Inners Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Mens Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Women Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.slip.set(0)
        self.panties.set(0)
        self.brasiers.set(0)
        self.trunks.set(0)
        self.vest.set(0)
        self.jetty.set(0)
        self.linning.set(0)
        self.kerchief.set(0)
        self.shirt.set(0)
        self.dhoti.set(0)
        self.lungi.set(0)
        self.towel.set(0)
        self.tshirt.set(0)
        self.jeans.set(0)
        self.saree.set(0)
        self.chudi.set(0)
        self.tops.set(0)
        self.leggings.set(0)
        self.plazo.set(0)
        self.skimmer.set(0)
        self.shawl.set(0)
        self.total_inners.set(0)
        self.total_men.set(0)
        self.total_women.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()
            
root=Tk()
obj=Bill_App(root)
root.mainloop()
    
