import time
from plyer import notification
from tkinter import*
import sys
from tkinter import messagebox

# окно приложения

root = Tk()
root.title('Уведомелния')
root.geometry('250x250')
root.resizable(False,False)

#Ввод сообщения

msg_lbl = Label(text = "Введите сообщение:").grid(row = 1,column = 3)
msg_ent = Entry()
msg_ent.grid(row = 1,column = 5)

#Ввод вермени

time_lbl = Label(text = "Введите время(сек):").grid(row = 10,column = 3)
time_ent = Entry()
time_ent.grid(row = 10,column = 5)

#функция отправки уведомлений

def notify():

    local_time = time_ent.get()

    messagebox.showinfo("Уведомления","Таймер запущен, сработает через "+ local_time + " секунд")

    time.sleep(int(local_time))

    notification.notify(
    title = "Уведомления",
    message = msg_ent.get(),
    timeout = 10)
    
    root.destroy()
    

    

#Кнопка активации

act_btn = Button(text = 'Запуск',command = notify).grid(row = 12,column = 3)

#Кнопка отмены

del_button = Button(text = 'отменить',command = lambda:root.destroy()).grid(row = 12,column = 5)



root.mainloop()
