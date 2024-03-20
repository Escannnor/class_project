from tkinter import *
import random
import time
from tkinter import filedialog,messagebox
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import my_email
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fpdf import FPDF

conn=sqlite3.connect('Food Order.db')
cursor=conn.cursor()

# cursor.execute(
#     ''' 
#      CREATE A TABLE IF NOT EXISTS food transactions(
#         id iNTEGER PRIMARY KEY,
#         name TEXT,
#         price REAL
      
#   )  
    
#     '''
# )

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS drink_items (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         price REAL
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS snack_items (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         price REAL
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS transactions (
#         id INTEGER PRIMARY KEY,
#         item_name TEXT,
#         price REAL,
#         quantity INTEGER,
#         total_amount REAL
#     )
# ''')

# def insert_item(table_name, name, price):
#     cursor.execute(f'''
#         INSERT INTO {food_items} (name, price)
#         VALUES (?, ?)
#     ''', (name, price))
#     conn.commit()
    
    
    
# functions
def reset():
    text_receipt.delete(1.0,END)
    e_rice.set('0')
    e_beans.set('0')
    e_amala.set('0')
    e_rice.set('0')
    e_jollof_rice.set('0')
    e_fried_rice.set('0')
    e_coconut_rice.set('0')
    e_spaghetti.set('0')
    e_macaroni.set('0')
    e_peppersoup.set('0')
    e_pounded_yam.set('0')
    e_semo.set('0')
    e_yam.set('0')
    e_chinese_rice.set('0')
    
    e_alomo_bitters.set('0')
    e_henessey.set('0')
    e_fanta.set('0')
    e_pepsi.set('0')
    e_mirinda.set('0')
    e_nutri_milk.set('0')
    e_yoghurt.set('0')
    e_chivita.set('0')
    e_maltina.set('0')

    e_cake.set('0')
    e_sharwama.set('0')
    e_pizza.set('0')
    e_puff_puff.set('0')
    e_doughnurt.set('0')
    
    text_rice.config(state=DISABLED)
    text_beans.config(state=DISABLED)
    text_amala.config(state=DISABLED)
    text_rice.config(state=DISABLED)
    text_jollof_rice.config(state=DISABLED)
    text_fried_rice.config(state=DISABLED)
    text_coconut_rice.config(state=DISABLED)
    text_spaghetti.config(state=DISABLED)
    text_macaroni.config(state=DISABLED)
    text_peppersoup.config(state=DISABLED)
    text_pounded_yam.config(state=DISABLED)
    text_semo.config(state=DISABLED)
    text_yam.config(state=DISABLED)
    text_chinese_rice.config(state=DISABLED)
    
    text_alomo_bitters.config(state=DISABLED)
    text_henessey.config(state=DISABLED)
    text_red_wine.config(state=DISABLED)
    text_fanta.config(state=DISABLED)
    text_pepsi.config(state=DISABLED)
    text_mirinda.config(state=DISABLED)
    text_nutri_milk.config(state=DISABLED)
    text_maltina.config(state=DISABLED)
    text_yoghurt.config(state=DISABLED)
    text_chivita.config(state=DISABLED)
    text_zobo.config(state=DISABLED)
    
    text_doughnurt.config(state=DISABLED)
    text_cake.config(state=DISABLED)
    text_puff_puff.config(state=DISABLED)
    text_sharwama.config(state=DISABLED)
    text_pizza.config(state=DISABLED)
    text_red_wine.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    
    cost_of_drinksvar.set('')
    cost_of_foodvar.set('')
    cost_of_snacksvar.set('')
    sub_totalvar.set('')
    service_taxvar.set('')
    total_costvar.set('')
    
def send_email(to_email, subject, message, attachment_path=None):
    # Email server configuration
    smtp_server = 'smtp.gmail.com'  # Your SMTP server address
    smtp_port = 587  # Your SMTP port
    sender_email = my_email.email_address  # Your email address
    password = my_email.password  # Your email password
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body to the email
    msg.attach(MIMEText(_text= message, _subtype='plain'))

    # If attachment_path is provided, attach the file
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
        # Attach the attachment to the message
        msg.attach(part)

    # Create SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, password)  # Login with sender email and password
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)  # Send email
def text_to_pdf(text_content, pdf_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=text_content, ln=True, align='L')
    pdf.output(pdf_filename)


def send_email_with_pdf_attachment(to_email, subject, body, attachment_path):
    # Email server configuration
    smtp_server = 'smtp.gmail.com'  # Your SMTP server address
    smtp_port = 587  # Your SMTP port
    sender_email = my_email.email_address  # Your email address
    password = my_email.password # Your email password
    
#     # Create message container
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     # Attach body to the email
#     msg.attach(MIMEText(_text=body,_subtype= 'plain'))

#     # Attach the PDF file
#     with open(attachment_path, 'rb') as file:
#         attachment = MIMEBase('application', 'octet-stream')
#         attachment.set_payload(file.read())
#         encoders.encode_base64(attachment)
#         attachment.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
#         msg.attach(attachment)

#     # Create SMTP session
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Enable TLS encryption
#         server.login(sender_email, password)  # Login with sender email and password
#         server.sendmail(sender_email, to_email, msg.as_string())  # Send email




  
        
def send():
    if text_receipt.get(1.0,END)=='\n':
        pass
    else:
       def send_msg():
        message=text_area.get(1.0,END)
        email=email_field.get()
        # pdf_file = generate_pdf_bill('bill reciept', message)
        # send_email_with_pdf_attachment(email, 'bill details', '', pdf_file)
        send_email(email, 'Bill Details', message, None)
        
       root2=Toplevel()
    
       root2.title('SEND BILL')
       root2.config(bg='azure4')
       root2.geometry('500x620+50+50')
    
       logo_img=PhotoImage(file='Untitled.png')
       label=Label(root2,image=logo_img, bg='azure4')
       label.pack()
    
       email_label=Label(root2,text='Email Address', font=('arial',18,'bold underline'),bg='azure4',fg='white')
       email_label.pack(pady=3)
    
       email_field=Entry(root2,font=('helvetica',22, "bold"),bd=3,width=26)
       email_field.pack(pady=3)
    
       bill_label=Label(root2,text='Bill details', font=('arial',18,'bold underline'),bg='azure4',fg='white')
       bill_label.pack(pady=3)
    
       text_area=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=12)
       text_area.pack(pady=3)
    
       send_button=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='azure4',bd=7,relief=GROOVE, command=send_msg)
       send_button.pack(pady=3)
    
       text_area.insert(END, "Receipt Ref:\t\t" + bill_number + "\t\t" + date + "\n\n")

       if cost_of_foodvar.get()!= ('0 NGN'):
        text_area.insert(END,f'cost of food \t\t\t{priceoffood} NGN \n') 
        
       if cost_of_drinksvar.get()!= ('0 NGN'):
        text_area.insert(END,f'cost of drinks \t\t\t{priceofdrinks} NGN \n')
    
       if cost_of_snacksvar.get()!= ('0 NGN'):
        text_area.insert(END,f'cost of snacks \t\t\t{priceofsnacks} NGN \n')
        
       text_receipt.insert(END,f'sub total \t\t\t{subtotal_of_all_items} NGN \n')
       text_receipt.insert(END,f'service tax \t\t\t{20} NGN \n\n')
       text_receipt.insert(END,f'Total cost \t\t\t{subtotal_of_all_items+20} NGN \n')    

    
       
       
       root2.mainloop()
    
def save():
    if text_receipt.get(1.0,END)=='\n':
        pass
    else:
       url=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
       if url==None:
           pass
       else:
    
          bill_data=text_receipt.get(1.0,END)
          url.write(bill_data)
          url.close()
          messagebox.showinfo('Information','Your Bill Has Been Saved Succesfully')
    
def total_cost():
    global priceoffood,priceofdrinks,priceofsnacks,subtotal_of_all_items
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or\
        var10.get()!=0 or var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or\
        var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or var26.get()!=0 or\
        var27.get()!=0 or var28.get()!=0 or var29.get()!=0:
       item1=int(e_rice.get())
       item2=int(e_beans.get())
       item3=int(e_amala.get())
       item4=int(e_jollof_rice.get())
       item5=int(e_fried_rice.get())
       item6=int(e_coconut_rice.get())
       item7=int(e_spaghetti.get())
       item8=int(e_macaroni.get())
       item9=int(e_peppersoup.get())
       item10=int(e_pounded_yam.get())
       item11=int(e_semo.get())
       item12=int(e_yam.get())
       item13=int(e_chinese_rice.get())

       item14=int(e_alomo_bitters.get())
       item15=int(e_henessey.get())
       item16=int(e_fanta.get())
       item17=int(e_pepsi.get())
       item18=int(e_mirinda.get())
       item19=int(e_nutri_milk.get())
       item20=int(e_yoghurt.get())
       item21=int(e_chivita.get())
       item22=int(e_zobo.get())
       item23=int(e_maltina.get())

       item24=int(e_doughnurt.get())
       item25=int(e_cake.get())
       item26=int(e_puff_puff.get())
       item27=int(e_sharwama.get())
       item28=int(e_pizza.get())
       item29=int(e_red_wine.get())
    
       priceoffood=(item1*500)+(item2*300)+(item3*500)+(item4*1000)+(item5*1000)+(item6*1200)+(item7*500)+(item8*500)+(item9*2000)+(item10*500)+(item11*500)+(item12*800)+(item13*1500)
    
       priceofdrinks=(item14*4000)+(item15*20000)+(item16*500)+(item17*500)+(item18*500)+(item19*800)+(item20*3000)+(item21*2000)+(item22*1000)+(item23*1000)+(item29*10000)
        
       priceofsnacks=(item24*500)+(item25*8000)+(item26*500)+(item27*4000)+(item28*10000)
    
       cost_of_foodvar.set(str(priceoffood)+' NGN')
       cost_of_drinksvar.set(str(priceofdrinks)+' NGN')
       cost_of_snacksvar.set(str(priceofsnacks)+' NGN')

       subtotal_of_all_items=priceoffood + priceofdrinks + priceofsnacks
       sub_totalvar.set(str(subtotal_of_all_items)+ 'NGN')

       service_taxvar.set('20 NGN')

       totalcost = subtotal_of_all_items+ 20
       total_costvar.set(str(totalcost)+'NGN')
    else:
        messagebox.showerror('Error','No item selected')

    

def receipt():
    global bill_number,date
    if cost_of_drinksvar.get()!='' or cost_of_foodvar.get()!='' or cost_of_snacksvar.get()!='':
        
      text_receipt.delete(1.0,END)
      x=random.randint(100,10000)
      bill_number='BILL'+str(x)
      date=time.strftime('%d/%m/%Y')
      text_receipt.insert(END, 'Receipt Ref:\t\t' +bill_number+'\t\t'+date+'\n')
      text_receipt.insert(END,'**************************************************************************\n')
      text_receipt.insert(END,'Items:\t\t cost of items(NGN)\n')
      text_receipt.insert(END, '**************************************************************************\n')
      if e_rice.get()!='0':
        text_receipt.insert(END,f"Rice\t\t\t{int(e_rice.get())*500}\n\n")
        
      if e_beans.get()!='0':
        text_receipt.insert(END,f"Beans\t\t\t{int(e_rice.get())*300}\n\n")
    
      if e_amala.get()!='0':
        text_receipt.insert(END,f"Amala\t\t\t{int(e_amala.get())*500}\n\n")
        
      if e_jollof_rice.get()!='0':
    
       text_receipt.insert(END,f"Jollof Rice\t\t\t{int(e_jollof_rice.get())*1000}\n\n")
       
      if e_fried_rice.get()!='0':
        text_receipt.insert(END,f"Friend_Rice\t\t\t{int(e_fried_rice.get())*1000}\n\n")
        
      if e_coconut_rice.get()!='0':
        text_receipt.insert(END,f"Coconut Rice\t\t\t{int(e_coconut_rice.get())*1200}\n\n")
            
      if e_spaghetti.get()!='0':
        text_receipt.insert(END,f"spaghetti\t\t\t{int(e_spaghetti.get())*500}\n\n")
            
      if e_macaroni.get()!='0':
        text_receipt.insert(END,f"macaroni\t\t\t{int(e_macaroni.get())*500}\n\n")

      if e_peppersoup.get()!='0':
        text_receipt.insert(END,f"peppersoup\t\t\t{int(e_peppersoup.get())*2000}\n\n")
        
      if e_pounded_yam.get()!='0':
        text_receipt.insert(END,f"pounded yam\t\t\t{int(e_pounded_yam.get())*500}\n\n")
        
      if e_semo.get()!='0':
        text_receipt.insert(END,f"semo\t\t\t{int(e_semo.get())*500}\n\n")

      if e_yam.get()!='0':
        text_receipt.insert(END,f"yam\t\t\t{int(e_yam.get())*800}\n\n") 

      if e_chinese_rice.get()!='0':
        text_receipt.insert(END,f"Chinese Rice\t\t\t{int(e_chinese_rice.get())*1500}\n\n")
        
      if e_alomo_bitters.get()!='0':
        text_receipt.insert(END,f"alomo bitters\t\t\t{int(e_alomo_bitters.get())*4000}\n\n") 
        
      if e_henessey.get()!='0':
        text_receipt.insert(END,f"henessey\t\t\t{int(e_henessey.get())*20000}\n\n")
            
      if e_fanta.get()!='0':
         text_receipt.insert(END,f"fanta\t\t\t{int(e_fanta.get())*500}\n\n")
            
      if e_pepsi.get()!='0':
        text_receipt.insert(END,f"pepsi\t\t\t{int(e_pepsi.get())*500}\n\n")
        
      if e_mirinda.get()!='0':
        text_receipt.insert(END,f"mirinda\t\t\t{int(e_mirinda.get())*500}\n\n")
        
      if e_nutri_milk.get()!='0':
        text_receipt.insert(END,f"nutrimilk\t\t\t{int(e_nutri_milk.get())*800}\n\n")
        
      if e_yoghurt.get()!='0':
        text_receipt.insert(END,f"yoghurt\t\t\t{int(e_yoghurt.get())*3000}\n\n")
        
      if e_chivita.get()!='0':
        text_receipt.insert(END,f"chivita\t\t\t{int(e_chivita.get())*2000}\n\n")
        
      if e_zobo.get()!='0':
        text_receipt.insert(END,f"zobo\t\t\t{int(e_zobo.get())*1000}\n\n")
        
      if e_maltina.get()!='0':
        text_receipt.insert(END,f"maltina\t\t\t{int(e_maltina.get())*1000}\n\n")
        
      if e_doughnurt.get()!='0':
        text_receipt.insert(END,f"doughurt\t\t\t{int(e_doughnurt.get())*500}\n\n")
        
      if e_cake.get()!='0':
        text_receipt.insert(END,f"cake\t\t\t{int(e_cake.get())*8000}\n\n")
        
      if e_puff_puff.get()!='0':
        text_receipt.insert(END,f"puffpuff\t\t\t{int(e_puff_puff.get())*500}\n\n")
        
      if e_sharwama.get()!='0':
        text_receipt.insert(END,f"sharwama\t\t\t{int(e_sharwama.get())*4000}\n\n")
        
      if e_pizza.get()!='0':
        text_receipt.insert(END,f"pizza\t\t\t{int(e_pizza.get())*10000}\n\n")
        
      if e_red_wine.get()!='0':
        text_receipt.insert(END,f"red wine\t\t\t{int(e_red_wine.get())*10000}\n\n")
        
      text_receipt.insert(END,'**************************************************************************\n')
      if cost_of_foodvar.get()!= ('0 NGN'):
        text_receipt.insert(END,f'cost of food \t\t\t{priceoffood} NGN \n\n') 
        
      if cost_of_drinksvar.get()!= ('0 NGN'):
        text_receipt.insert(END,f'cost of drinks \t\t\t{priceofdrinks} NGN \n\n')
    
      if cost_of_snacksvar.get()!= ('0 NGN'):
        text_receipt.insert(END,f'cost of snacks \t\t\t{priceofsnacks} NGN \n\n')
        
      text_receipt.insert(END,f'sub total \t\t\t{subtotal_of_all_items} NGN \n\n')
      text_receipt.insert(END,f'service tax \t\t\t{20} NGN \n\n')
      text_receipt.insert(END,f'Total cost \t\t\t{subtotal_of_all_items+20} NGN \n\n')
      text_receipt.insert(END,'**************************************************************************\n')
    else:
        messagebox.showerror('Error','No item selected')
            
def rice():
    if var1.get()==1:
        text_rice.config(state=NORMAL)
        text_rice.delete(0, END)
        text_rice.focus()
    else:
        text_rice.config(state=DISABLED)
        e_rice.set('0')
        
def beans():
    if var2.get()==1:
        text_beans.config(state=NORMAL)
        text_beans.delete(0, END)
        text_beans.focus()
    else:
        text_beans.config(state=DISABLED)
        e_beans.set('0')
        
def amala():
    if var3.get()==1:
        text_amala.config(state=NORMAL)
        text_amala.delete(0, END)
        text_amala.focus()
    else:
        text_amala.config(state=DISABLED)
        e_amala.set('0')

def jollof_rice():
    if var4.get()==1:
        text_jollof_rice.config(state=NORMAL)
        text_jollof_rice.delete(0, END)
        text_jollof_rice.focus()
    else:
        text_jollof_rice.config(state=DISABLED)
        e_jollof_rice.set('0')
def fried_rice():
    if var5.get()==1:
        text_fried_rice.config(state=NORMAL)
        text_fried_rice.delete(0, END)
        text_fried_rice.focus()
    else:
        text_fried_rice.config(state=DISABLED)
        e_fried_rice.set('0')
        
def coconut_rice():
    if var6.get()==1:
        text_coconut_rice.config(state=NORMAL)
        text_coconut_rice.delete(0, END)
        text_coconut_rice.focus()
    else:
        text_coconut_rice.config(state=DISABLED)
        e_coconut_rice.set('0')
        
def spaghetti():
    if var7.get()==1:
        text_spaghetti.config(state=NORMAL)
        text_spaghetti.delete(0, END)
        text_spaghetti.focus()
    else:
        text_spaghetti.config(state=DISABLED)
        e_spaghetti.set('0')

def macaroni():
    if var8.get()==1:
        text_macaroni.config(state=NORMAL)
        text_macaroni.delete(0, END)
        text_macaroni.focus()
    else:
        text_macaroni.config(state=DISABLED)
        e_macaroni.set('0')

def peppersoup():
    if var9.get()==1:
        text_peppersoup.config(state=NORMAL)
        text_peppersoup.delete(0, END)
        text_peppersoup.focus()
    else:
        text_peppersoup.config(state=DISABLED)
        e_peppersoup.set('0')

def pounded_yam():
    if var10.get()==1:
        text_pounded_yam.config(state=NORMAL)
        text_pounded_yam.delete(0, END)
        text_pounded_yam.focus()
    else:
        text_pounded_yam.config(state=DISABLED)
        e_pounded_yam.set('0')

def semo():
    if var11.get()==1:
        text_semo.config(state=NORMAL)
        text_semo.delete(0, END)
        text_semo.focus()
    else:
        text_semo.config(state=DISABLED)
        e_semo.set('0')

def yam():
    if var12.get()==1:
        text_yam.config(state=NORMAL)
        text_yam.delete(0, END)
        text_yam.focus()
    else:
        text_yam.config(state=DISABLED)
        e_yam.set('0')

def chinese_rice():
    if var13.get()==1:
        text_chinese_rice.config(state=NORMAL)
        text_chinese_rice.delete(0, END)
        text_chinese_rice.focus()
    else:
        text_chinese_rice.config(state=DISABLED)
        e_chinese_rice.set('0')

def alomo_bitters():
    if var14.get()==1:
        text_alomo_bitters.config(state=NORMAL)
        text_alomo_bitters.delete(0, END)
        text_alomo_bitters.focus()
    else:
        text_alomo_bitters.config(state=DISABLED)
        e_alomo_bitters.set('0')

def henessey():
    if var15.get()==1:
        text_henessey.config(state=NORMAL)
        text_henessey.delete(0, END)
        text_henessey.focus()
    else:
        text_henessey.config(state=DISABLED)
        e_henessey.set('0')

def red_wine():
    if var16.get()==1:
        text_red_wine.config(state=NORMAL)
        text_red_wine.delete(0, END)
        text_red_wine.focus()
    else:
        text_red_wine.config(state=DISABLED)
        e_red_wine.set('0')

def fanta():
    if var17.get()==1:
        text_fanta.config(state=NORMAL)
        text_fanta.delete(0, END)
        text_fanta.focus()
    else:
        text_fanta.config(state=DISABLED)
        e_fanta.set('0')

def pepsi():
    if var18.get()==1:
        text_pepsi.config(state=NORMAL)
        text_pepsi.delete(0, END)
        text_pepsi.focus()
    else:
        text_pepsi.config(state=DISABLED)
        e_pepsi.set('0')

def mirinda():
    if var19.get()==1:
        text_mirinda.config(state=NORMAL)
        text_mirinda.delete(0, END)
        text_mirinda.focus()
    else:
        text_mirinda.config(state=DISABLED)
        e_mirinda.set('0')
        
def nutri_milk():
    if var20.get()==1:
        text_nutri_milk.config(state=NORMAL)
        text_nutri_milk.delete(0, END)
        text_nutri_milk.focus()
    else:
        text_nutri_milk.config(state=DISABLED)
        e_nutri_milk.set('0')

def yoghurt():
    if var21.get()==1:
        text_yoghurt.config(state=NORMAL)
        text_yoghurt.delete(0, END)
        text_yoghurt.focus()
    else:
        text_yoghurt.config(state=DISABLED)
        e_yoghurt.set('0')
        
def chivita():
    if var22.get()==1:
        text_chivita.config(state=NORMAL)
        text_chivita.delete(0, END)
        text_chivita.focus()
    else:
        text_chivita.config(state=DISABLED)
        e_chivita.set('0')
        
def zobo():
        if var23.get()==1:
         text_zobo.config(state=NORMAL)
         text_zobo.delete(0, END)
         text_zobo.focus()
        else:
            text_zobo.config(state=DISABLED)
            e_zobo.set('0')
            
def maltina():
    if var24.get()==1:
        text_maltina.config(state=NORMAL)
        text_maltina.delete(0, END)
        text_maltina.focus()
    else:
        text_maltina.config(state=DISABLED)
        e_maltina.set('0')

def sharwama():
    if var25.get()==1:
        text_sharwama.config(state=NORMAL)
        text_sharwama.delete(0, END)
        text_sharwama.focus()
    else:
        text_sharwama.config(state=DISABLED)
        e_sharwama.set('0')

def pizza():
    if var26.get()==1:
        text_pizza.config(state=NORMAL)
        text_pizza.delete(0, END)
        text_pizza.focus()
    else:
        text_pizza.config(state=DISABLED)
        e_pizza.set('0')

def puff_puff():
    if var27.get()==1:
        text_puff_puff.config(state=NORMAL)
        text_puff_puff.delete(0, END)
        text_puff_puff.focus()
    else:
        text_puff_puff.config(state=DISABLED)
        e_puff_puff.set('0')

def doughnurt():
    if var28.get()==1:
        text_doughnurt.config(state=NORMAL)
        text_doughnurt.delete(0, END)
        text_doughnurt.focus()
    else:
        text_doughnurt.config(state=DISABLED)
        e_doughnurt.set('0')

def cake():
    if var29.get()==1:
        text_cake.config(state=NORMAL)
        text_cake.delete(0, END)
        text_cake.focus()
    else:
        text_cake.config(state=DISABLED)
        e_cake.set('0')

root = Tk()

root.geometry("1600x900+0+0")



root.title("ESANCONR'S food ordeing system")
root.config(bg="azure4")

top_frame = Frame(root, bd=10, relief=RIDGE, bg="antiquewhite")
top_frame.pack(side="top")

label_Tille = Label(top_frame, text="Food Ordering System", font=('arial', 30, 'bold'),fg="red4", width=61, bd=8, bg='azure4')
label_Tille.grid(row=0, column=0)

menu_frame = Frame(root, bd=10, relief=RIDGE, bg='azure4')
menu_frame.pack(side=LEFT)

cost_frame = Frame(menu_frame, bd=4, relief=RIDGE, bg='azure4')
cost_frame.pack(side=BOTTOM)

food_frame = LabelFrame(menu_frame, text="Food", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="red4", bg='azure4')
food_frame.pack(side=LEFT)

drink_frame = LabelFrame(menu_frame, text="Drink", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="red4", bg='azure4')
drink_frame.pack(side=LEFT)

snacks_frame = LabelFrame(menu_frame, text="Snacks", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="red4", bg='azure4')
snacks_frame.pack(side=LEFT)

right_frame = Frame(root, bd=15, relief=RIDGE,bg='azure4')
right_frame.pack(side=RIGHT)

calcualtor_frame = Frame(right_frame, bd=1, relief=RIDGE, bg='azure4')
calcualtor_frame.pack()

receipt_frame = Frame(right_frame, bd=4, relief=RIDGE, bg='azure4')
receipt_frame.pack()

button_frame = Frame(right_frame, bd=3, relief=RIDGE, bg='azure4')
button_frame.pack()


# variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()

e_rice = StringVar()
e_beans = StringVar()
e_amala = StringVar()
e_jollof_rice = StringVar()
e_fried_rice = StringVar()
e_coconut_rice = StringVar()
e_spaghetti = StringVar()
e_macaroni = StringVar()
e_peppersoup = StringVar()
e_pounded_yam = StringVar()
e_semo = StringVar()
e_yam = StringVar()
e_chinese_rice = StringVar()

e_alomo_bitters = StringVar()
e_henessey = StringVar()
e_red_wine = StringVar()
e_fanta = StringVar()
e_pepsi = StringVar()
e_mirinda = StringVar()
e_nutri_milk = StringVar()
e_yoghurt = StringVar()
e_chivita = StringVar()
e_zobo = StringVar()
e_maltina = StringVar()

e_doughnurt = StringVar()
e_cake = StringVar()
e_puff_puff = StringVar()
e_sharwama = StringVar()
e_pizza = StringVar()

cost_of_foodvar=StringVar()
cost_of_drinksvar=StringVar()
cost_of_snacksvar=StringVar()

e_rice.set('0')
e_beans.set('0')
e_amala.set('0')
e_jollof_rice.set('0')
e_fried_rice.set('0')
e_coconut_rice.set('0')
e_spaghetti.set('0')
e_macaroni.set('0')
e_peppersoup.set('0')
e_pounded_yam.set('0')
e_semo.set('0')
e_yam.set('0')
e_chinese_rice.set('0')


e_alomo_bitters.set('0')
e_henessey.set('0')
e_red_wine.set('0')
e_fanta.set('0')
e_pepsi.set('0')
e_mirinda.set('0')
e_nutri_milk.set('0')
e_maltina.set('0')
e_yoghurt.set('0')
e_chivita.set('0')
e_zobo.set('0')

e_cake.set('0')
e_sharwama.set('0')
e_pizza.set('0')
e_puff_puff.set('0')
e_doughnurt.set('0')

# cost_of_foodvar.set('0 NGN')
# cost_of_drinksvar.set('0 NGN')
# cost_of_snacksvar.set('0 NGN')

sub_totalvar=StringVar()
service_taxvar=StringVar()
total_costvar=StringVar()
# food
rice = Checkbutton(food_frame, text="Rice", font=("Bradley Hand ITC", 15, "bold",),  onvalue=1, offvalue=0, variable=var1, fg='gold', bg='azure4', command=rice)
rice.grid(row=0, column=0, sticky=W)

beans = Checkbutton(food_frame, text="Beans", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var2, fg='gold', bg='azure4', command=beans)
beans.grid(row=1, column=0, sticky=W)

amala = Checkbutton(food_frame, text="Amala", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var3, fg='gold', bg='azure4', command=amala)
amala.grid(row=2, column=0, sticky=W)

jollof_rice = Checkbutton(food_frame, text="Jollof Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var4, fg='gold', bg='azure4', command=jollof_rice)
jollof_rice.grid(row=3, column=0, sticky=W)

fried_rice = Checkbutton(food_frame, text="Fried Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var5, fg='gold', bg='azure4',command=fried_rice)
fried_rice.grid(row=4, column=0, sticky=W)

coconut_rice = Checkbutton(food_frame, text="Cononut Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var6, fg='gold', bg='azure4',command=coconut_rice)
coconut_rice.grid(row=5, column=0, sticky=W)

spaghetti = Checkbutton(food_frame, text="spaghetti", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var7,fg='gold', bg='azure4',command=spaghetti)
spaghetti.grid(row=6, column=0, sticky=W)

macaroni = Checkbutton(food_frame, text="Macaroni", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var8, fg='gold', bg='azure4',command=macaroni)
macaroni.grid(row=7, column=0, sticky=W)

peppersoup = Checkbutton(food_frame, text="Peppersoup", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var9, fg='gold', bg='azure4',command=peppersoup)
peppersoup.grid(row=8, column=0, sticky=W)

pounded_yam = Checkbutton(food_frame, text="PoundedYam", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var10, fg='gold', bg='azure4',command=pounded_yam)
pounded_yam.grid(row=9, column=0, sticky=W)

semo = Checkbutton(food_frame, text="Semo", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var11, fg='gold', bg='azure4',command=semo)
semo.grid(row=10, column=0, sticky=W)

yam = Checkbutton(food_frame, text="Yam", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var12, fg='gold', bg='azure4',command=yam)
yam.grid(row=11, column=0, sticky=W)

chinese_rice = Checkbutton(food_frame, text="Chinese Rice", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var13, fg='gold', bg='azure4',command=chinese_rice)
chinese_rice.grid(row=12, column=0, sticky=W)

# food entry

text_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5,state=DISABLED,textvariable=e_rice)
text_rice.grid(row=0, column=1,)

text_beans = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_beans)
text_beans.grid(row=1, column=1,)

text_amala = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_amala)
text_amala.grid(row=2, column=1,)

text_jollof_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_jollof_rice)
text_jollof_rice.grid(row=3, column=1,)

text_fried_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_fried_rice)
text_fried_rice.grid(row=4, column=1,)

text_coconut_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_coconut_rice)
text_coconut_rice.grid(row=5, column=1,)

text_spaghetti = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_spaghetti)
text_spaghetti.grid(row=6, column=1,)

text_macaroni = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_macaroni)
text_macaroni.grid(row=7, column=1,)

text_peppersoup = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_peppersoup)
text_peppersoup.grid(row=8, column=1,)

text_pounded_yam = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_pounded_yam)
text_pounded_yam.grid(row=9, column=1,)

text_semo = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_semo)
text_semo.grid(row=10, column=1,)

text_yam = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_yam)
text_yam.grid(row=11, column=1,)

text_chinese_rice = Entry(food_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_chinese_rice)
text_chinese_rice.grid(row=12, column=1,)

# drinks

alomo_bitters = Checkbutton(drink_frame, text="Alomo Bitters", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var14,fg='gold', bg='azure4', command=alomo_bitters)
alomo_bitters.grid(row=0, column=0, sticky=W)

henessey = Checkbutton(drink_frame, text="Henessey", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var15, fg='gold', bg='azure4', command=henessey)
henessey.grid(row=1, column=0, sticky=W)

red_wine = Checkbutton(drink_frame, text="Red wine", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var16, fg='gold', bg='azure4', command=red_wine)
red_wine.grid(row=2, column=0, sticky=W)

fanta = Checkbutton(drink_frame, text="Fanta", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var17, fg='gold', bg='azure4',command= fanta)
fanta.grid(row=3, column=0, sticky=W)

pepsi = Checkbutton(drink_frame, text="Pepsi", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var18, fg='gold', bg='azure4', command=pepsi)
pepsi.grid(row=4, column=0, sticky=W)

mirinda = Checkbutton(drink_frame, text="Mirinda", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var19, fg='gold', bg='azure4', command=mirinda)
mirinda.grid(row=5, column=0, sticky=W)

nutri_milk = Checkbutton(drink_frame, text="Nutri Milk", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var20, fg='gold', bg='azure4', command=nutri_milk)
nutri_milk.grid(row=6, column=0, sticky=W)

yoghurt = Checkbutton(drink_frame, text="Yoghurt", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var21, fg='gold', bg='azure4', command=yoghurt)
yoghurt.grid(row=7, column=0, sticky=W)

chivita = Checkbutton(drink_frame, text="Chivita", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var22, fg='gold', bg='azure4',command=chivita)
chivita.grid(row=8, column=0, sticky=W)

zobo = Checkbutton(drink_frame, text="Zobo", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var23, fg='gold', bg='azure4', command=zobo)
zobo.grid(row=9, column=0, sticky=W)

maltina = Checkbutton(drink_frame, text="Maltina", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var24, fg='gold', bg='azure4', command=maltina)
maltina.grid(row=10, column=0, sticky=W)

# drink_entry
text_alomo_bitters = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_alomo_bitters)
text_alomo_bitters.grid(row=0, column=1,)

text_henessey = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_henessey)
text_henessey.grid(row=1, column=1,)

text_red_wine = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_red_wine)
text_red_wine.grid(row=2, column=1,)

text_fanta = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_fanta)
text_fanta.grid(row=3, column=1,)

text_pepsi = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_pepsi)
text_pepsi.grid(row=4, column=1,)

text_mirinda = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_mirinda)
text_mirinda.grid(row=5, column=1,)

text_nutri_milk = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_nutri_milk)
text_nutri_milk.grid(row=6, column=1,)

text_yoghurt = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_yoghurt)
text_yoghurt.grid(row=7, column=1,)

text_chivita = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_chivita)
text_chivita.grid(row=8, column=1,)

text_zobo = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_zobo)
text_zobo.grid(row=9, column=1,)

text_maltina = Entry(drink_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_maltina)
text_maltina.grid(row=10, column=1,)

# snacks

sharwama = Checkbutton(snacks_frame, text="sharwama", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var25,fg='gold', bg='azure4', command=sharwama)
sharwama.grid(row=0, column=0, sticky=W)

pizza = Checkbutton(snacks_frame, text="pizza", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var26, fg='gold', bg='azure4', command=pizza)
pizza.grid(row=1, column=0, sticky=W)

puff_puff = Checkbutton(snacks_frame, text="PuffPuff", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var27, fg='gold', bg='azure4', command=puff_puff)
puff_puff.grid(row=2, column=0, sticky=W)

doughnurt = Checkbutton(snacks_frame, text="doughnurt", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var28, fg='gold', bg='azure4', command=doughnurt)
doughnurt.grid(row=3, column=0, sticky=W)

cake = Checkbutton(snacks_frame, text="Caket", font=("Bradley Hand ITC", 15, "bold"), onvalue=1, offvalue=0, variable=var29, fg='gold', bg='azure4', command=cake)
cake.grid(row=4, column=0, sticky=W)

# snacks_entry

text_sharwama = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_sharwama)
text_sharwama.grid(row=0, column=1,)

text_pizza = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_pizza)
text_pizza.grid(row=1, column=1,)

text_puff_puff = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_puff_puff)
text_puff_puff.grid(row=2, column=1,)

text_doughnurt = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_doughnurt)
text_doughnurt.grid(row=3, column=1,)

text_cake = Entry(snacks_frame, font=("arial", 15, "bold"),bd=5, width=5, state=DISABLED, textvariable=e_cake)
text_cake.grid(row=4, column=1,)

# costlabels and entry fields

label_cost_food = Label(cost_frame, text="cost of foods",font=('arial', 16, 'bold'),fg='red4', bg='azure4')
label_cost_food.grid(row=0, column=0, sticky=W)

text_cost_food = Entry(cost_frame, font=('arial', 16, 'bold'), state="readonly", bd=6, width=14,textvariable=cost_of_foodvar)
text_cost_food.grid(row=0, column=1, padx=10)

label_cost_drinks = Label(cost_frame, text="cost of drinks",font=('arial', 16, 'bold'),fg='red4', bg='azure4')
label_cost_drinks.grid(row=1, column=0, sticky=W)

text_cost_drinks = Entry(cost_frame, font=('arial', 16, 'bold'), state="readonly",bd=6, width=14,textvariable=cost_of_drinksvar)
text_cost_drinks.grid(row=1, column=1, pady=15)

label_cost_snacks = Label(cost_frame, text="cost of snacks",font=('arial', 16, 'bold'), fg='red4', bg='azure4')
label_cost_snacks.grid(row=2, column=0, sticky=W)

text_cost_snacks = Entry(cost_frame, font=('arial', 16, 'bold'), state="readonly",bd=6, width=14, textvariable=cost_of_snacksvar)
text_cost_snacks.grid(row=2, column=1, padx=15)

sub_total = Label(cost_frame, text="SubTotal",font=('arial', 16, 'bold'), fg='red4', bg='azure4')
sub_total.grid(row=0, column=2)

text_sub_total = Entry(cost_frame, font=('arial', 16, 'bold'), state="readonly",bd=6, width=14, textvariable=sub_totalvar)
text_sub_total.grid(row=0, column=3)

service_tax = Label(cost_frame, text="Service Tax",font=('arial', 16, 'bold'), fg='red4', bg='azure4')
service_tax.grid(row=1, column=2)

text_service_tax = Entry(cost_frame, font=('arial', 16, 'bold'), state="readonly",bd=6, width=14, textvariable=service_taxvar)
text_service_tax.grid(row=1, column=3)

labeltotal_cost = Label(cost_frame, text="Total Cost",font=('arial', 16, 'bold'), fg='red4', bg='azure4')
labeltotal_cost.grid(row=2, column=2)

text_total_cost = Entry(cost_frame, font=('arial', 16, 'bold'), state="readonly",bd=6, width=14, textvariable=total_costvar)
text_total_cost.grid(row=2, column=3)

# right buttons

button_total =Button(button_frame, text='Total', font=('arial', 15, 'bold'),fg='white',bd=3, bg='azure4',padx=15, command=total_cost)
button_total.grid(row=0, column=0)

button_receipt =Button(button_frame, text='Receipt', font=('arial', 15, 'bold'),fg='white',bd=3, bg='azure4',padx=15, command=receipt)
button_receipt.grid(row=0, column=1)

button_save =Button(button_frame, text='Save', font=('arial', 15, 'bold'),fg='white',bd=3, bg='azure4',padx=15, command=save)
button_save.grid(row=0, column=2)

button_send =Button(button_frame, text='Send', font=('arial', 15, 'bold'),fg='white',bd=3, bg='azure4',padx=15, command=send)
button_send.grid(row=0, column=3)

button_reset =Button(button_frame, text='Reset', font=('arial', 15, 'bold'),fg='white',bd=3, bg='azure4',padx=15,command=reset)
button_reset.grid(row=0, column=4)

# text_receipt

text_receipt= Text(receipt_frame, font=('arial',12 ,'bold'),bd=3, width=55,height=18)
text_receipt.grid(row=0, column=0)

# calculator
operator=''
def button_click(numbers):
    global operator
    operator = operator + numbers
    calculator_field.delete(0, END)
    calculator_field.insert(END,operator)
    
def clear():
    global operator
    operator = ''
    calculator_field.delete(0, END)
    
def answer():
    global operator
    result=str(eval(operator))
    calculator_field.delete(0, END)
    calculator_field.insert(0,result)
    operator=''
    
calculator_field= Entry(calcualtor_frame, font=('arial',16, 'bold'), width=40 ,bd=5)
calculator_field.grid(row=0, column=0, columnspan=4)

# buttons

button7= Button(calcualtor_frame, text='7', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('7'))
button7.grid(row=1,column=0)

button8= Button(calcualtor_frame, text='8', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('8'))
button8.grid(row=1,column=1)

button9= Button(calcualtor_frame, text='9', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('9'))
button9.grid(row=1,column=2)

button_plus= Button(calcualtor_frame, text='+', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('+'))
button_plus.grid(row=1,column=3)

button4= Button(calcualtor_frame, text='4', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('4'))
button4.grid(row=2,column=0)

button5= Button(calcualtor_frame, text='5', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('5'))
button5.grid(row=2,column=1)

button6= Button(calcualtor_frame, text='6', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('6'))
button6.grid(row=2,column=2)

button_minus= Button(calcualtor_frame, text='-', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('-'))
button_minus.grid(row=2,column=3)

button1= Button(calcualtor_frame, text='1', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('1'))
button1.grid(row=3,column=0)

button2= Button(calcualtor_frame, text='2', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('2'))
button2.grid(row=3,column=1)

button3= Button(calcualtor_frame, text='3', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('3'))
button3.grid(row=3,column=2)

button_multi= Button(calcualtor_frame, text='x', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('*'))
button_multi.grid(row=3,column=3)

button_equal= Button(calcualtor_frame, text='=', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=answer)
button_equal.grid(row=4,column=0)

button_clr= Button(calcualtor_frame, text='CLR', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=clear)
button_clr.grid(row=4,column=1)

button_div= Button(calcualtor_frame, text='/', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('/'))
button_div.grid(row=4,column=3)

button_0= Button(calcualtor_frame, text='0', font=('arial', 16,'bold'),fg='white', bg='azure4', width='7',bd=6, command=lambda:button_click('0'))
button_0.grid(row=4,column=2)

root.mainloop()
