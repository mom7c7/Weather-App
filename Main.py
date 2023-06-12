# Modules
from tkinter import *
import requests
from datetime import *

# Datetime
now_times = datetime.now()

now_hours = now_times.hour

# Reaquests
URL = "https://api.open-meteo.com/v1/forecast?latitude=35.83&longitude=50.99&hourly=temperature_2m&forecast_days=1&timezone=Europe%2FMoscow"
location = "delhi technological university"
PARAMS = {'address':location}
info = requests.get(url=URL,params=PARAMS)
data = info.json()
temps = data["hourly"]["temperature_2m"]

# Tkinter
root = Tk()
root.geometry('300x320')
root.title('Live Weather')
root.resizable(False,False)
root.config(bg='#CC99FF')
# Frame
frm1 = Frame(root,width=300,height=40,bg='#CC99FF')
frm1.pack(side=TOP)
frm2 = Frame(root,width=300,height=40,bg='#CC99FF')
frm2.pack(side=TOP)
frm3 = Frame(root,width=300,height=40,bg='#CC99FF')
frm3.pack(side=TOP)
frm4 = Frame(root,width=300,height=40,bg='#CC99FF')
frm4.pack(side=TOP)
frm5 = Frame(root,width=300,height=40,bg='#CC99FF')
frm5.pack(side=TOP)
frm6 = Frame(root,width=300,height=40,bg='#CC99FF')
frm6.pack(side=TOP)
frm7 = Frame(root,width=300,height=40,bg='#CC99FF')
frm7.pack(side=TOP)
frm8 = Frame(root,width=300,height=40,bg='#CC99FF')
frm8.pack(side=TOP)
# Label
lbl1 = Label(frm6,text='For Get Temp Click On Any Hours',bg='#CC99FF',fg='black')
lbl1.pack()

lbl2 = Label(frm7,text='Temp is : C',bg='#CC99FF',fg='black')
lbl2.pack()

lbl3 = Label(frm5,text=' ',bg='#CC99FF',fg='black')
lbl3.pack()
# Variable

enh = None
lih = None
# Functions

def h00():
    enh = temps[0]
    lbl2.config(text=f'Temp is : {enh} C')
def h01():
    enh = temps[1]
    lbl2.config(text=f'Temp is : {enh} C')
def h02():
    enh = temps[2]
    lbl2.config(text=f'Temp is : {enh} C')
def h03():
    enh = temps[3]
    lbl2.config(text=f'Temp is : {enh} C')
def h04():
    enh = temps[4]
    lbl2.config(text=f'Temp is : {enh} C')
def h05():
    enh = temps[5]
    lbl2.config(text=f'Temp is : {enh} C')
def h06():
    enh = temps[6]
    lbl2.config(text=f'Temp is : {enh} C')
def h07():
    enh = temps[7]
    lbl2.config(text=f'Temp is : {enh} C')
def h08():
    enh = temps[8]
    lbl2.config(text=f'Temp is : {enh} C')
def h09():
    enh = temps[9]
    lbl2.config(text=f'Temp is : {enh} C')
def h10():
    enh = temps[10]
    lbl2.config(text=f'Temp is : {enh} C')
def h11():
    enh = temps[11]
    lbl2.config(text=f'Temp is : {enh} C')
def h12():
    enh = temps[12]
    lbl2.config(text=f'Temp is : {enh} C')
def h13():
    enh = temps[13]
    lbl2.config(text=f'Temp is : {enh} C')
def h14():
    enh = temps[14]
    lbl2.config(text=f'Temp is : {enh} C')
def h15():
    enh = temps[15]
    lbl2.config(text=f'Temp is : {enh} C')
def h16():
    enh = temps[16]
    lbl2.config(text=f'Temp is : {enh} C')
def h17():
    enh = temps[17]
    lbl2.config(text=f'Temp is : {enh} C')
def h18():
    enh = temps[18]
    lbl2.config(text=f'Temp is : {enh} C')
def h19():
    enh = temps[19]
    lbl2.config(text=f'Temp is : {enh} C')
def h20():
    enh = temps[20]
    lbl2.config(text=f'Temp is : {enh} C')
def h21():
    enh = temps[21]
    lbl2.config(text=f'Temp is : {enh} C')
def h22():
    enh = temps[22]
    lbl2.config(text=f'Temp is : {enh} C')
def h23():
    enh = temps[23]
    lbl2.config(text=f'Temp is : {enh} C')
def lih_T():
    lih = temps[now_hours]
    lbl3.config(text=f'Hour is : {now_hours} , And Temp Is : {lih} C')

# Button
btn1 = Button(frm1,text='00',command=h00)
btn1.pack(side=LEFT,padx=10,pady=10)
btn2 = Button(frm1,text='01',command=h01)
btn2.pack(side=LEFT,padx=10,pady=10)
btn3 = Button(frm1,text='02',command=h02)
btn3.pack(side=LEFT,padx=10,pady=10)
btn4 = Button(frm1,text='03',command=h03)
btn4.pack(side=LEFT,padx=10,pady=10)
btn5 = Button(frm1,text='04',command=h04)
btn5.pack(side=LEFT,padx=10,pady=10)
btn6 = Button(frm1,text='05',command=h05)
btn6.pack(side=LEFT,padx=10,pady=10)
# --------------------------------------
btn7 = Button(frm2,text='06',command=h06)
btn7.pack(side=LEFT,padx=10,pady=10)
btn8 = Button(frm2,text='07',command=h07)
btn8.pack(side=LEFT,padx=10,pady=10)
btn9 = Button(frm2,text='08',command=h08)
btn9.pack(side=LEFT,padx=10,pady=10)
btn10 = Button(frm2,text='09',command=h09)
btn10.pack(side=LEFT,padx=10,pady=10)
btn11 = Button(frm2,text='10',command=h10)
btn11.pack(side=LEFT,padx=10,pady=10)
btn12 = Button(frm2,text='11',command=h11)
btn12.pack(side=LEFT,padx=10,pady=10)
# --------------------------------------
btn13 = Button(frm3,text='12',command=h12)
btn13.pack(side=LEFT,padx=10,pady=10)
btn14 = Button(frm3,text='13',command=h13)
btn14.pack(side=LEFT,padx=10,pady=10)
btn15 = Button(frm3,text='14',command=h14)
btn15.pack(side=LEFT,padx=10,pady=10)
btn16 = Button(frm3,text='15',command=h15)
btn16.pack(side=LEFT,padx=10,pady=10)
btn17 = Button(frm3,text='16',command=h16)
btn17.pack(side=LEFT,padx=10,pady=10)
btn18 = Button(frm3,text='17',command=h17)
btn18.pack(side=LEFT,padx=10,pady=10)
# --------------------------------------
btn19 = Button(frm4,text='18',command=h18)
btn19.pack(side=LEFT,padx=10,pady=10)
btn20 = Button(frm4,text='19',command=h19)
btn20.pack(side=LEFT,padx=10,pady=10)
btn21 = Button(frm4,text='20',command=h20)
btn21.pack(side=LEFT,padx=10,pady=10)
btn22 = Button(frm4,text='21',command=h21)
btn22.pack(side=LEFT,padx=10,pady=10)
btn23 = Button(frm4,text='22',command=h22)
btn23.pack(side=LEFT,padx=10,pady=10)
btn24 = Button(frm4,text='23',command=h23)
btn24.pack(side=LEFT,padx=10,pady=10)
# --------------------------------------

livebtn = Button(frm8,text='Get Live Temp',command=lih_T)
livebtn.pack(pady=10)


root.mainloop()