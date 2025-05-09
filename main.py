import tkinter
from tkinter import ttk

#### window creation start ####
window = tkinter.Tk()
window.title("TmEsg")
window.resizable(0, 0)
window.geometry("950x700")
#### window creation end ####

class Playerparams():

    def __init__(self, health, damage, weapon):
        self.health = health
        self.damage = damage
        self.weapon = weapon
    
    def __str__(self):
        return f'{self.weapon}'

class Enemparams():

    def __init__(self, health, damage, rng, weapon):
        self.health= health
        self.damage = damage
        self.rng = rng
        self.weapon = weapon

player = Playerparams(100, 5, 'None')

#### UI buttons handling ####
def exitpressed():
    window.destroy()



def settingspressed():
    global player

    settingwindow = tkinter.Tk()
    settingwindow.title("Settings")
    settingwindow.resizable(0, 0)
    settingwindow.geometry("650x650")
    
    def exitsett():
        settingwindow.destroy()

    exitbut = tkinter.Button(settingwindow, text="Back", background='grey', height=2, width=21, command=exitsett)
    exitbut.place(x=4, y=20)
    settingslabel = tkinter.Label(settingwindow, text="Settings", font=('Arial', 25))
    settingslabel.place(x=245, y=40)

    #### health setting handler ####
    health_label = tkinter.Label(settingwindow, text="Player Health:")
    health_label.place(x=50, y=150)
    health_entry = tkinter.Entry(settingwindow)
    health_entry.place(x=160, y=150)
    playerlabel = tkinter.Label(settingwindow, text="Player", font=('Arial', 25))
    playerlabel.place(x=160, y= 100)
    def update_health():
        try:
            new_health = int(health_entry.get())
            player.health = new_health
            # confirmlabel = tkinter.Label()
        except ValueError:
            pass # needs label
    updatehealthb = tkinter.Button(settingwindow, text="Set Health", command=update_health)
    updatehealthb.place(x=300, y=150)
   
    #### geeks4geeks ####
    
    def show():
        selected_weapon = cb.get()
        player.weapon = selected_weapon  # Update the weapon attribute
        lbl.config(text=f"Weapon set to: {selected_weapon}")  # Update the label
        print(player.weapon)

    a = ["None", "Sword", "Gun"]


    cb = ttk.Combobox(settingwindow, values=a)
    cb.set("None")
    cb.place(x=151, y=250)
    confirmweap = tkinter.Button(settingwindow, text="Set Weapon", command=show)
    confirmweap.place(x=300, y=250)
# Label to show selected value  
    lbl = tkinter.Label(settingwindow, text="")
    lbl.place(x=150, y=285)
    
    
    #### geeks4geeks ####


    #### health setting handler ####

    #### damage setting handler ####

    damagelabel = tkinter.Label(settingwindow, text = "Player Damage:")
    damagelabel.place(x=50, y= 200)
    damage_entry = tkinter.Entry(settingwindow)
    damage_entry.place(x=160, y=200)
    
    def updatedamage():
        try:
            new_damage = int(health_entry.get())
            player.damage = new_damage
            # confirmlabel = tkinter.Label()
        except ValueError:
            pass # needs label
    updatedamageb = tkinter.Button(settingwindow, text="Set Damage", command= updatedamage)
    updatedamageb.place(x=300,y= 200)
        
#### UI buttons handling ####




#### main menu UI ####
logo = tkinter.PhotoImage(file="Media/logo.png")  
logolabel = tkinter.Label(window, image=logo)
logolabel.place(x=0, y=0)  # initial creation, will be overidden later 
playbutton = tkinter.Button(window, text= "Play", background='grey', height= 2, width= 21)
settingsbutton = tkinter.Button(window, text= "Settings", background='grey', height= 2, width= 21, command = settingspressed)
exitbutton = tkinter.Button(window, text='Exit', background='grey', height= 2, width= 21, command= exitpressed)


def center_logo(item, window_width, y_position):
    item.update_idletasks() 
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
