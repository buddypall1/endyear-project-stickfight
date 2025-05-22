import tkinter
from tkinter import ttk
import tkinter.messagebox
import pickle
from PIL import Image, ImageTk
saveloc = "Data/game_data.dat"
def loadData():
    try:
        with open(saveloc, 'rb') as file:
            data = pickle.load(file)
        return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError, ImportError, MemoryError):
        tkinter.messagebox.showerror("Data Error", "Couldn't load save data, reverting to defaults.")
        return {
        "Playerhealth" : 100,
        "Playerdmg" : 5,
        "Playerweap" : "None",
        "Enemhealth" : 100,
        "Enemdmg" : 5,
        "Enemweap" : "None",
        "Enemrng" : 50
        }


gamedata = loadData()

# ENEMY RNG TABLE DEFAULTS: 50
# For attack: This will be default when nothing is needed
# When below half health: it will heal if RNG rolls below selected RNG value, will attack if above, which means higher RNG = harder fight. (100 would mean 100% chance, 0 would mean 0%)


#### window creation start ####
window = tkinter.Tk()
def disable_event():
   pass
window.protocol("WM_DELETE_WINDOW", disable_event)
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
        return f'{self.weapon} {self.damage} {self.weapon}'

class Enemparams():

    def __init__(self, health, damage, rng, weapon):
        self.health= health
        self.damage = damage
        self.rng = rng
        self.weapon = weapon


#### player and enemy obj creation #### 

player = Playerparams(gamedata['Playerhealth'], gamedata['Playerdmg'], gamedata['Playerweap'])
enemy = Enemparams(gamedata['Enemhealth'], gamedata['Enemdmg'], gamedata['Enemrng'], gamedata['Enemweap'])



#### UI buttons handling ####
def exitpressed():
    window.destroy()
    savedata()


def playpressed():
    global player, enemy
    playwindow = tkinter.Toplevel(window)
    playwindow.resizable(0,0)
    def disable_event():
        pass
    playwindow.protocol("WM_DELETE_WINDOW", disable_event)
    playwindow.title('TmEsg')
    playwindow.geometry('950x700')

    playersprite = tkinter.PhotoImage(file = "Media\playerplaceholder.png")
    playersprlabel = tkinter.Label(playwindow, image=playersprite)
    playersprlabel.place(x=200, y= 150)
    playersprlabel.image = playersprite

def settingspressed():
    global player, enemy

    settingwindow = tkinter.Toplevel(window)
    settingwindow.title("Settings")
    settingwindow.resizable(0, 0)
    settingwindow.geometry("650x650")
    playersprite = tkinter.PhotoImage(file = "Media\playersprite.png")
    playersprlabel = tkinter.Label(settingwindow, image=playersprite)
    playersprlabel.place(x=440, y= 100)
    playersprlabel.image = playersprite


    Enemsprite = tkinter.PhotoImage(file = "Media\enemysprite.png")
    Enemsprlabel = tkinter.Label(settingwindow, image=Enemsprite)
    Enemsprlabel.place(x=440, y= 370)
    Enemsprlabel.image = Enemsprite

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
    health_entry.insert(0, str(player.health))

    def update_health():
        try:
            new_health = int(health_entry.get())
            if new_health <= 0 or new_health > 100:
                tkinter.messagebox.showerror('Out of range', 'You inputted a out of range number! Range: 1-100')
            else:
                player.health = new_health
                tkinter.messagebox.showinfo('Success!', 'Health Changed Successfully!')
        except ValueError:
            tkinter.messagebox.showerror('Non number value!', 'ERROR! You have entered a non number value.')
    updatehealthb = tkinter.Button(settingwindow, text="Set Health", command=update_health)
    updatehealthb.place(x=300, y=150)
    
    #### geeks4geeks ####
    
    def show():
        selected_weapon = cb.get()
        player.weapon = selected_weapon 
        lbl.config(text=f"Weapon set to: {selected_weapon}")  
        print(player.weapon)
    
    WeaponSelectPlayer = ["None", "Sword", "Gun"]


    cb = ttk.Combobox(settingwindow, values=WeaponSelectPlayer)
    cb.set(f"{player.weapon}")
    cb.place(x=151, y=250)
    confirmweap = tkinter.Button(settingwindow, text="Set Weapon", command=show)
    confirmweap.place(x=300, y=250)
    lbl = tkinter.Label(settingwindow, text="")
    lbl.place(x=151, y=280)
    weaponlabl = tkinter.Label(settingwindow, text= "Player Weapon:")
    weaponlabl.place(x=50, y = 250)
    
    #### geeks4geeks ####


    #### health setting handler ####

    #### damage setting handler ####

    damagelabel = tkinter.Label(settingwindow, text = "Player Damage:")
    damagelabel.place(x=50, y= 200)
    damage_entry = tkinter.Entry(settingwindow)
    damage_entry.place(x=160, y=200)
    damage_entry.insert(0, str(player.damage))

    def updatedamage():
        try:
            new_damage = int(damage_entry.get())
            if new_damage <= 0 or new_damage > 10:
                tkinter.messagebox.showerror('Out of range', 'You inputted an out of range number! range: 1-10')
            else:
                player.damage = new_damage
                tkinter.messagebox.showinfo('Success!', 'Damage Changed Successfully!')
        except ValueError:
            tkinter.messagebox.showerror('Non number value!', 'ERROR! You have entered a non number value.')
    updatedamageb = tkinter.Button(settingwindow, text="Set Damage", command= updatedamage)
    updatedamageb.place(x=300,y= 200)

        #### ENEMY SETTINGS ####
        
    enemylabel = tkinter.Label(settingwindow, text="Enemy", font=('Arial', 25))
    enemylabel.place(x=160, y= 340) #40

    #### health setting handler ####

    healthEnemy_label = tkinter.Label(settingwindow, text="Enemy Health:")
    healthEnemy_label.place(x=50, y=390)
    healthEnemy_entry = tkinter.Entry(settingwindow)
    healthEnemy_entry.place(x=160, y=390)
    healthEnemy_entry.insert(0, str(enemy.health))
    def updateEnem_health():
        try:
            new_healthEnemy = int(healthEnemy_entry.get())
            if new_healthEnemy <= 0 or new_healthEnemy > 100:
                tkinter.messagebox.showerror('Out of range', 'You inputted an out of range number! Range: 1-100')
            else:
                enemy.health = new_healthEnemy
                tkinter.messagebox.showinfo('Success!', 'Health Changed Successfully!')
        except ValueError:
            tkinter.messagebox.showerror('Non number value!', 'ERROR! You have entered a non number value.')
    updatehealthenemb = tkinter.Button(settingwindow, text="Set Health", command=updateEnem_health)
    updatehealthenemb.place(x=300, y=389)

    #### damage setting handler ####

    damageEnemylabel = tkinter.Label(settingwindow, text = "Enemy Damage:")
    damageEnemylabel.place(x=50, y= 430)
    damageEnemy_entry = tkinter.Entry(settingwindow)
    damageEnemy_entry.place(x=160, y= 430)
    damageEnemy_entry.insert(0, str(enemy.damage))
    
    def updatedEnemamage():
        try:
            newEnemy_damage = int(damageEnemy_entry.get())
            if newEnemy_damage <= 0 or newEnemy_damage > 10:
                tkinter.messagebox.showerror('Out of range', 'You inputted an out of range number! range: 1-10')
            else:
                enemy.damage = newEnemy_damage
                tkinter.messagebox.showinfo('Success!', 'Damage Changed Successfully!')
        except ValueError:
            tkinter.messagebox.showerror('Non number value!', 'ERROR! You have entered a non number value.')
    updatedamageb = tkinter.Button(settingwindow, text="Set Damage", command= updatedEnemamage)
    updatedamageb.place(x=300,y= 429)
 
 #### geeks4geeks ####
    
    def showEnem():
        selectedEnem_weapon = cbEnem.get()
        enemy.weapon = selectedEnem_weapon 
        lblEnem.config(text=f"Weapon set to: {selectedEnem_weapon}")  
        print(enemy.weapon)
    
    WeaponSelectEnemy = ["None", "Sword", "Gun"]


    cbEnem = ttk.Combobox(settingwindow, values=WeaponSelectEnemy)
    cbEnem.set(f"{enemy.weapon}")
    cbEnem.place(x=151, y=470)
    confirmEnemweap = tkinter.Button(settingwindow, text="Set Weapon", command=showEnem)
    confirmEnemweap.place(x=300, y=470)
    lblEnem = tkinter.Label(settingwindow, text="")
    lblEnem.place(x=151, y=495)
    weaponEnemlabl = tkinter.Label(settingwindow, text= "Enemy Weapon:")
    weaponEnemlabl.place(x=50, y = 470)
    
    #### geeks4geeks ####

    rngEnemylabel = tkinter.Label(settingwindow, text = "Enemy RNG:")
    rngEnemylabel.place(x=50, y= 520)
    rngEnemy_entry = tkinter.Entry(settingwindow)
    rngEnemy_entry.place(x=160, y=520)
    rngEnemy_entry.insert(0, str(enemy.rng))
    def rngEnem():
        try:
            newEnemy_rng = int(rngEnemy_entry.get())
            if newEnemy_rng <= 0 or newEnemy_rng > 100:
                tkinter.messagebox.showerror('Out of range', 'You inputted an out of range number! range: 1-100')
            else:
                enemy.rng = newEnemy_rng
                tkinter.messagebox.showinfo('Success!', 'RNG Changed Successfully!')
        except ValueError:
            tkinter.messagebox.showerror('Non number value!', 'ERROR! You have entered a non number value.')
    updatedrngb = tkinter.Button(settingwindow, text="Set RNG", command= rngEnem)
    updatedrngb.place(x=300,y= 519)
        
#### UI buttons handling ####




#### main menu UI ####
logo = tkinter.PhotoImage(file="Media/logo.png")  
logolabel = tkinter.Label(window, image=logo)
logolabel.place(x=0, y=0)  # initial creation, will be overidden later 
playbutton = tkinter.Button(window, text= "Play", background='grey', height= 2, width= 21, command=playpressed)
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

def savedata():
    data = {
        "Playerhealth" : player.health,
        "Playerdmg" : player.damage,
        "Playerweap" : player.weapon,
        "Enemhealth" : enemy.health,
        "Enemdmg" : enemy.damage,
        "Enemweap" : enemy.weapon,
        "Enemrng" : enemy.rng
    }
    with open(saveloc, "wb") as file:
        pickle.dump(data, file)







window.mainloop()
