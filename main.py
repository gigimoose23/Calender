import tkinter,calendar,math
import sys

sys.set_int_max_str_digits(9999)
window = tkinter.Tk()
window.title("Calendar")

window.geometry("500x500")
window.resizable(False, False)
def onClickMeBtnPressed():
    yearDid = int(entry.get())
    calWin = tkinter.Tk()
    calWin.resizable(False,False)
    calWin.title("Main Calendar")
    calWin.geometry("600x400")
    winText = tkinter.Text(calWin)
    winText.insert("0.0", calendar.calendar(yearDid))
    winText.place(x=0,y=0)
    scrollbar = tkinter.Scrollbar(calWin,command=winText.yview)
    scrollbar.pack(side="right",fill="y")
    winText.config(yscrollcommand=scrollbar.set)
    
    print(calendar.calendar(yearDid))
label = tkinter.Label(window,text="CALENDAR: Enter Year",font=("Arial",25))
button = tkinter.Button(window,text="View Year",command=onClickMeBtnPressed,activebackground="red")
entry = tkinter.Entry(window,width=50)

label.place(x=0,y=0)
button.place(x=0,y=100)
entry.place(x=0,y=50)
window.mainloop()