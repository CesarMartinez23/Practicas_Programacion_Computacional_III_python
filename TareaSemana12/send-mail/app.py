from dotenv import load_dotenv
from src.email import Email
from src.templates.mail_template import email_template
from tkinter import Button, Label, Entry, Text, Tk, messagebox

# Instance of Tkinter
root = Tk()

# Settings for the GUI form Tkinter
root.title('Email Sender')
root.geometry('500x500')
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)
root.configure(bg='#D9BBDF')

# Labels and entries for the GUI form Tkinter
labelEmailSend = Label(root, text='Send To:', bg='#82AAAC', font=16)
entryEmailSend = Entry(root, bg='#BBDDDF', font=16)

labelUsername = Label(root, text='Username:', bg='#82AAAC', font=16)
entryUsername = Entry(root, bg='#BBDDDF', font=16)

labelTitleEmail = Label(root, text='Title Email:', bg='#82AAAC', font=16)
entryTitleEmail = Entry(root, bg='#BBDDDF', font=16)

labelEmailBody = Label(root, text='Email Body', bg='#82AAAC', font=16)
textEmailBody = Text(root, bg='#BBDDDF', font=14)

# Load environment variables from .env file
load_dotenv()

# Create a function to empty the fields of the GUI form Tkinter
def emptyFields():
    entryEmailSend.delete(0, 'end')
    entryUsername.delete(0, 'end')
    entryTitleEmail.delete(0, 'end')
    textEmailBody.delete('1.0', 'end')

# Create a fuction with an instance of Email class and send email with the data from the GUI form Tkinter

def main():
    
    if(entryEmailSend.get() == '' or entryUsername.get() == '' or entryTitleEmail.get() == '' or textEmailBody.get('1.0', 'end-1c') == ''):
        messagebox.showerror('Error', 'Please fill all the fields.')
    else:
        email = Email()
        sendTo = entryEmailSend.get()
        emailTitle = entryTitleEmail.get()
        username = entryUsername.get()
        emailBody = textEmailBody.get('1.0', 'end-1c')
        email.sendEmail([sendTo], emailTitle, message_format=email_template.format(
        username, emailBody), format='html')
        
        messagebox.showinfo('Success', 'Email sent successfully.')
        emptyFields()

# Button to send email
buttonSendMail = Button(root, text='Send Email',
                        bg='#BEBBDF', font='Arial', command=main)

# Place the widgets
labelEmailSend.place(x=30, y=25)
entryEmailSend.place(x=135, y=25, width=300)

labelUsername.place(x=30, y=75)
entryUsername.place(x=135, y=75, width=300)

labelTitleEmail.place(x=10, y=150)
entryTitleEmail.place(x=115, y=150, width=320)

labelEmailBody.place(x=10, y=200)
textEmailBody.place(x=10, y=240, width=450, height=200)

buttonSendMail.place(x=345, y=450, width=115, height=40)

# Main loop of the app
root.mainloop()
