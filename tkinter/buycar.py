import tkinter
from tkinter import *

window = Tk()
window.geometry('500x500')

window.title('ดาวน์-ผ่อน รถ')



label1 = Label(window,text='ราคารถที่จะซื้อ',font=400,bg='yellow').pack()

txt=IntVar()
Entry(window,textvariable=txt).pack()



label2 = Label(window,text='จำนวนเงินดาวน์',font=400,bg='yellow').pack()

txt2=IntVar()
Entry(window,textvariable=txt2).pack()




label2 = Label(window,text='เลือกจำนวนงวดที่ผ่อน',font=400,bg='yellow').pack()

l = IntVar()
l.set(1)
Radiobutton(text='12 งวด',variable=l,value=1).pack()
Radiobutton(text='24 งวด',variable=l,value=2).pack()
Radiobutton(text='36 งวด',variable=l,value=3).pack()
Radiobutton(text='48 งวด',variable=l,value=4).pack()







def cal():
    cal_txt = txt.get()
    cal_txt_2 = txt2.get()
    choice = l.get()
    cal_sum = int(cal_txt-cal_txt_2)
    
    
    result1 = int(cal_sum/12)
    result2 = int(cal_sum/24)
    result3 = int(cal_sum/36)
    result4 = int(cal_sum/48)
    
    
    
    if cal_txt_2 > cal_txt:
        print('โปรดใส่จำนวนเงินให้ถูกต้อง')
    else:
        if choice == 1:
            sum_label.config(text=f"ผ่อนเดือนละ {result1} บาท")
        elif choice == 2:
            sum_label.config(text=f"ผ่อนเดือนละ {result2} บาท")
        elif choice == 3:
            sum_label.config(text=f"ผ่อนเดือนละ {result3} บาท")
        elif choice == 4:
            sum_label.config(text=f"ผ่อนเดือนละ {result4} บาท")           
            
            
        
        
       


    
sum_label = Label(window, text=" ") 
sum_label.pack()    
    

Button(window,text='คำนวน',command= cal).pack()





window.mainloop()

