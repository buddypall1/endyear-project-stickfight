import tkinter


#### window creation start ####
window = tkinter.Tk()
window.title("TmEsg")
window.resizable(0, 0)
window.geometry("950x700")
#### window creation end ####


#### UI buttons handling ####
def exitpressed():
    window.destroy()

def settingspressed():
    settingwindow = tkinter.Tk()
    settingwindow.title("Settings")
    settingwindow.resizable(0, 0)
    settingwindow.geometry("650x650", anchor= 'center')
        
#### UI buttons handling ####




#### main menu UI ####
logo = tkinter.PhotoImage(file="Media/testlogo.png")  
logolabel = tkinter.Label(window, image=logo)
logolabel.place(x=0, y=0)  # initial creation, will be overidden later 





playbutton = tkinter.Button(window, text= "Play", background='grey', height= 2, width= 21)
settingsbutton = tkinter.Button(window, text= "Settings", background='grey', height= 2, width= 21, command = settingspressed)
exitbutton = tkinter.Button(window, text='Exit', background='grey', height= 2, width= 21, command= exitpressed)


def center_logo(item, window_width, y_position):
    item.update_idletasks()  # AI 
    item_width = item.winfo_width()
    x_position = (window_width - item_width) // 2
    item.place(x=x_position, y=y_position)
    


def center_item(item, window_width, y_position):
    item.update_idletasks()  # AI 
    item_width = item.winfo_width()
    x_position = (window_width - item_width) // 2
    item.place(x=x_position, y=y_position, anchor= 'center')
    






#### handling of centering ####

center_logo(logolabel, 950, 70) 
center_item(playbutton, 950, 340)
center_item(settingsbutton, 950, 440)
center_item(exitbutton, 950, 540)

#### handling of centering ####
window.mainloop()
