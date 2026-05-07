from tkinter import *

root=Tk()
root.title("BMI")
root.geometry("600x700")
root.config(background="lightgreen")

def get_height():
    height=float(entry2.get())
    return height
def get_weight():
    weight=float(entry1.get())
    return weight
def get_wiek():
    wiek=int(entry3.get())
    return wiek

def bmi():
    bmi1=19
    bmi2=24
    try:
        height=get_height()
        weight=get_weight()
        height=height/100
        bmi=round(weight/(height**2),2)
        label4.config(text=bmi)
        wiek=get_wiek
    except ValueError:
        label4.config(text="Nic nie wpisaleś",fg="red")
    except ZeroDivisionError:
        label4.config(text="Nie można wpisac wzrostu 0")
    else:
        if bmi<16:
            info="BMI wynosi:"+ str(bmi)+ " -wygłodzenie"
            label4.config(text=info)
        elif bmi>=16 and bmi<=16.99:
            info1="BMI wynosi:"+ str(bmi)+ " -wychudzenie"
            label4.config(text=info1)
        elif bmi>=17 and bmi<=18.49:
            info2="BMI wynosi:"+ str(bmi)+ " -niedowaga"
            label4.config(text=info2)
        # elif bmi>=18.5 and bmi<=24.99:
        #     if wiek>35 and wiek <44:
               
        elif bmi>=25.0 and bmi<=29.99:
            info4="BMI wynosi:"+ str(bmi)+ " -nadwaga"
            label4.config(text=info4)
        elif bmi>=30 and bmi<=34.99:
            info5="BMI wynosi:"+ str(bmi)+ " -otyłośc I stopnia"
            label4.config(text=info5)
        elif bmi>=35 and bmi<=39.99:
            info6="BMI wynosi:"+ str(bmi)+ " -otyłosc II stopnia"
            label4.config(text=info6)
        elif bmi>=40:
            info7="BMI wynosi:"+ str(bmi)+ " -otyłosc III stopnia"
            label4.config(text=info7)
        # if wiek>=19 and wiek<=24:
        #     bmi

label1=Label(root, text="Kalkulator BMI ",bg="lightgreen",fg="black",font="TimesNewRoman 35",pady=15)
label1.pack()

label2=Label(root,text="Waga w kg",bg="lightgreen",fg="white",font="Arial, 20",pady="10")
label2.place(x=100,y=130)

entry1=Entry(root,width=6,font="Helvetica 25",justify="center",)
entry1.place(x=320,y=130)

label3=Label(root,text="wzrost w cm",bg="lightgreen",font="Arial 20")
label3.place(x=100,y=200)

entry2=Entry(root,width=6,font="Helvetica 25",justify="center")
entry2.place(x=320,y=200)

label4=Label(root,text="",width=55,font="Arial 17",bg="lightgreen")
label4.place(x=0,y=280)

label5=Label(root,text="Wiek",bg="lightgreen",font="Arial 20")
label5.place(x=200,y=500)

entry3=Entry(root,width=6,font="Helvetica 20",justify="center")
entry3.place(x=320,y=500)

button1=Button(text="Oblicz",bg="yellow",fg="red",font="TimesNewRoman 40",padx=20,pady=5,command=bmi)
button1.place(x=190,y=320)



root.mainloop()