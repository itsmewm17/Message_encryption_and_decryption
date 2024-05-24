from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if  password=="1234":
            screen2=Toplevel(screen)
            screen2.title("decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            message=text1.get(1.0,END)
            decode_message=message.encode("utf-8")
            base64_byte=base64.b64encode(decode_message)
            decrypt=base64_byte.decode("utf-8")
    
            Label(screen2,text="ENCRYPT",font="Microsoft YaHei UI",fg="white",bg="#ed3833").place(x=10,y=0)
            text2=Text(screen2,font="Rpbote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
            text2.place(x=10,y=40,width=300,height=150)
    
            text2.insert(END,decrypt)
    
    elif password=="":
         messagebox.showerror("encryption","Input Password")

    elif password!="1234":
         messagebox.showerror("encryption","Invalid Password")


def encrypt():
    password=code.get()

    if password=="1234":
            screen1=Toplevel(screen)
            screen1.title("encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#ed3833")

            message=text1.get(1,END)
            encode_message=message.encode("utf-8") 
            base64_byte=base64.b64decode(encode_message)
            encrypt=base64_byte.decode("utf-8")
            #是基於拉丁字母的一套電腦字元編碼標準。它主要用於顯示現代英語，
            #而其擴展版本延伸美國標準資訊交換碼則可以部分支援其他西歐語言，
            #並等同於國際標準ISO/IEC 646

            Label(screen1,text="DECRYPT",font="Microsoft YaHei UI",fg="white",bg="#00bd56").place(x=10,y=0)
            text2=Text(screen1,font="Rpbote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
            text2.place(x=10,y=40,width=300,height=150)
    
            text2.insert(END,encrypt)
    
    elif password=="":
         messagebox.showerror("encryption","Input Password")

    elif password !="1234":
         messagebox.showerror("encryption","Invalid Password")
 

def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("575x400")
    screen.title("Encryption Program")

    Label(text="Enter text for encryption and decryption",fg="black",font=("Microsoft YaHei UI",14)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0) #wrap=WORD怕字太長可以自行切換到下一行
    text1.place(x=10,y=50,width=355,height=100)

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter secrect key for encryption and decryption",fg="black",font=("Microsoft YaHei UI",14) ).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=24,bd=0,font=("Microsoft YaHei UI",25),show="'").place(x=10,y=200)


    Button(text="ENCRYPT",height=2,width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRIPT",height=2,width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=240,y=250)
    Button(text="RESET",height=2,width=46,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=310)


    screen.mainloop()

main_screen()