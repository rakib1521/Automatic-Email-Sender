from tkinter import *
import smtplib





def sendmail(username,password,reciver,message,count):

    session = smtplib.SMTP('smtp.gmail.com', 587)
    #server location ,port number

    # start TLS for security
    session.starttls()
    #TSL = Transport layer security

    # Authentication
    session.login(username,password)

    # message to be sent
    #message = message

    # sending the mail
    session.sendmail(username, reciver, message)
    #print("{} mail done".format(count))

    # terminating the session
    session.quit()







def show():


    username=s_email_input.get()
    password=s_password_input.get()
    reciver=r_email_input.get()
    message=text_input.get()
    count=int(no_email_input.get())

    for i in range(count):

        sendmail(username,password,reciver,message,i)
        print(i)






auto_mail = Tk()
auto_mail.geometry('500x500')
auto_mail.title("Email Info")

s_email_label = Label(auto_mail, text="Sender's Email",width=20,font=("bold", 10))
s_email_label.place(x=80,y=130)

s_email_input = Entry(auto_mail)
s_email_input.place(x=240,y=130)

s_password_label = Label(auto_mail, text="Sender's Password",width=20,font=("bold", 10))
s_password_label.place(x=80,y=180)


s_password_input = Entry(auto_mail,show="*")
s_password_input.place(x=240,y=180)

r_email_label = Label(auto_mail, text="Reciver's Email",width=20,font=("bold", 10))
r_email_label.place(x=80,y=230)

r_email_input = Entry(auto_mail)
r_email_input.place(x=240,y=230)

text = Label(auto_mail, text="Text",width=20,font=("bold", 10))
text.place(x=80,y=280)

text_input = Entry(auto_mail)
text_input.place(x=240,y=280)

no_email_label = Label(auto_mail, text="Number of Email",width=20,font=("bold", 10))
no_email_label.place(x=80,y=330)

no_email_input = Entry(auto_mail)
no_email_input.place(x=240,y=330)

Button(auto_mail, text='send',width=20,bg='red',fg='white',command=show).place(x=180,y=380)

auto_mail.mainloop()
