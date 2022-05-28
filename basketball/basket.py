

from tkinter import *
from tkinter.ttk import Combobox, Style
from PIL import Image, ImageTk

root = Tk()
root.geometry('1920x1080')
root.title('GoBasketball')
root.configure(bg='#ecd8e0')


def coachCheck():
    coachValue = coachVar.get()
    if coachValue == 'NULL':
        pass
    else:
        courtCombo.configure(values=courtList)
    coachLabel.configure(text='Excellent Choice!')

    if coachValue == 'Romy Chandra':
        coachPreviewLabel.configure(image=romyFinal)
    elif coachValue == 'Aldi Subroto':
        coachPreviewLabel.configure(image=aldiFinal)
    elif coachValue == 'Rasya Dara':
        coachPreviewLabel.configure(image=rasyaFinal)
        


   
def courtCheck():
    courtValue = courtVar.get()
    if courtValue == 'YPK Wijaya':
        timeCombo.configure(values=timeListYPK)
        courtPreviewLabel.configure(image=ypkFinal)
    elif courtValue == 'GOR Bulungan':
        timeCombo.configure(values=timeListGORBul)
        courtPreviewLabel.configure(image=gorFinal)
    elif courtValue == 'Buls Bulungan':
        timeCombo.configure(values=timeListBulsB)
        courtPreviewLabel.configure(image=bulsFinal)
    elif courtValue == 'Bulungan Court':
        timeCombo.configure(values=timeListBulC)
        courtPreviewLabel.configure(image=bulcFinal)
    elif courtValue == 'STC Senayan':
        timeCombo.configure(values=timeListSTC)
        courtPreviewLabel.configure(image=stcFinal)
    courtLabel.configure(text='Great court pick!')
 


def timeCheck():
    timeValue = timeVar.get()
    timeLabel.configure(text='Be ready!')




def result():
    def again():
        coachLabel.configure(text='Pick your Coach!')
        courtLabel.configure(text='Pick the court!')
        timeLabel.configure(text='Hours available')
        nameEntry.delete(0, END)
        coachCombo.configure(values=coachList)
        courtCombo.configure(values=courtListError)
        courtCombo.current(0)
        timeCombo.configure(values=timeListError)
        timeCombo.current(0)
        resultLabel.configure(text="")
        resultLabel.grid(row=7,column=0)

    if coachVar.get() == 'Romy Chandra':
        coachPrice = romyPrice
    elif coachVar.get() == 'Aldi Subroto':
        coachPrice = aldiPrice
    elif coachVar.get() == 'Rasya Dara':
        coachPrice = rasyaPrice

    if courtVar.get() == 'YPK Wijaya':
        courtPrice = ypkPrice
    elif courtVar.get() == 'GOR Bulungan':
        courtPrice = gorPrice
    elif courtVar.get() == 'Buls Bulungan':
        courtPrice = bulsPrice
    elif courtVar.get() == 'Bulungan Court':
        courtPrice = bulCPrice
    elif courtVar.get() == 'STC Senayan':
        courtPrice = stcPrice

    
    nameResult = str(nameEntry.get())
    resultPrice = str(coachPrice + courtPrice)

    resultLabel = Label(root,bg='#ecd8e0',text='Congratulations! ' + nameResult +  '\nYou have booked for a private training with ' + coachVar.get() + ' on ' + courtVar.get() + ' at ' +timeVar.get() + '\n Your total price will be ' + resultPrice + '.00 Rp' + '\nYou can transfer to NIM : 21120121140155 Rajendra Aurelius Ritmanto \n' + "Don't forget to have fun!")
    resultLabel.grid(row=5,column=1)

    againButton = Button(root,command=again,text='Book Again')
    againButton.grid(row=6,column=1)
    #print(coachPrice)

coachList = [
    "Romy Chandra",
    "Aldi Subroto",
    "Rasya Dara"
]

romyPrice = 100000
aldiPrice = 250000
rasyaPrice = 300000

romyPhoto = Image.open('C:\\Users\\USER\\Desktop\\work\\basketball\\abdalla-m-y1TF3eH-S6M-unsplash.png')
resizeRomy = romyPhoto.resize((150,200),)
romyFinal = ImageTk.PhotoImage(resizeRomy)

aldiPhoto = Image.open('C:\\Users\\USER\\Desktop\\work\\basketball\\851fcde8-d7b2-499a-84db-4f36d7ff52e5.png')
resizeAldi = aldiPhoto.resize((150,200))
aldiFinal = ImageTk.PhotoImage(resizeAldi)

rasyaPhoto = Image.open(r'C:\Users\USER\Desktop\work\basketball\julia-rekamie-Z72YujnOrlY-unsplash.png')
resizeRasya = rasyaPhoto.resize((150,200))
rasyaFinal = ImageTk.PhotoImage(resizeRasya)

courtList = [ 
    "YPK Wijaya",
    "GOR Bulungan",
    "Buls Bulungan",
    "Bulungan Court",
    "STC Senayan"
]

ypkPrice = 300000
gorPrice = 275000
bulsPrice = 350000
bulCPrice = 200000
stcPrice = 400000


ypkPhoto = Image.open(r'C:\Users\USER\Desktop\work\basketball\Artwork YPK.png')
resizeYPK = ypkPhoto.resize((150,200))
ypkFinal = ImageTk.PhotoImage(resizeYPK)

gorPhoto = Image.open(r'C:\Users\USER\Desktop\work\basketball\gorbul.png')
resizeGor = gorPhoto.resize((150,200))
gorFinal = ImageTk.PhotoImage(resizeGor)

bulsPhoto = Image.open(r'C:\Users\USER\Desktop\work\basketball\buls.png')
resizeBuls = bulsPhoto.resize((150,200))
bulsFinal = ImageTk.PhotoImage(resizeBuls)

bulcPhoto = Image.open(r'C:\Users\USER\Desktop\work\basketball\bulungan.png')
resizeBulc = bulcPhoto.resize((150,200))
bulcFinal = ImageTk.PhotoImage(resizeBulc)

stcPhoto = Image.open(r'C:\Users\USER\Desktop\work\basketball\stc.png')
resizeSTC = stcPhoto.resize((150,200))
stcFinal = ImageTk.PhotoImage(resizeSTC)





timeListYPK = [ 
    "09:00",
    "12:00",
    '13:00',
    '15:00',
    '18:00'
]

timeListGORBul = [ 
    '12:00',
    '14:00',
    '17:00',
    '21:00'
]

timeListBulsB = [ 
    '08:00',
    '10:00',
    '11:00',
    '13:00'
]

timeListBulC = [ 
    '20:00',
    '22:00',
    '23:00'
]

timeListSTC = [ 
    '11:00',
    '15:00',
    '19:00',
    '23:30'
]

timeListError = [ 
    'Choose your court first!'
]

courtListError = ['Choose your coach first!']



#comboStyle = Style()
#comboStyle.theme_create('combostyle',settings={'TCombobox': {'configure': {'selectbackground : #ccc8c8'}}})
#comboStyle.theme_use('combostyle')

nameEntry = Entry(root,font=('bold', 12))
nameEntry.grid(row=0,column=1)

nameLabel = Label(root, text='Enter your name here!', font=('bold', 12,), pady=20,bg='#ecd8e0')
nameLabel.grid(row=0,column=0)

coachVar = StringVar()
coachCombo = Combobox(root, values=coachList, textvariable=coachVar,)
coachCombo.grid(row=2,column=0,padx=50)


coachLabel = Label(root, text='Pick your Coach!', font=('bold', 12), pady=20,bg='#ecd8e0')
coachLabel.grid(row=1,column=0)

coachButton = Button(root, text='Confirm', command=coachCheck,fg='#96796e',bg='#D7E2E8')
coachButton.grid(row=3,column=0,pady=20)

#coachErrorLabel = Label(root, text='.', font=('bold', 12), pady=20,bg='#ecd8e0')
#coachErrorLabel.grid(row=4,column=0)




courtLabel = Label(root, text='Pick the court!', font=('bold', 12), pady=20,bg='#ecd8e0')
courtLabel.grid(row=1,column=1)

courtVar = StringVar()
courtCombo = Combobox(root, values=courtListError, textvariable=courtVar,)
courtCombo.grid(row=2,column=1,padx=50)
courtCombo.current(0)

courtButton = Button(root, text='Confirm', command=courtCheck,fg='#96796e',bg='#D7E2E8')
courtButton.grid(row=3,column=1,pady=20)




timeLabel = Label(root, text="Hours available", font=('bold', 12), pady=20,bg='#ecd8e0')
timeLabel.grid(row=1,column=2)

timeVar = StringVar()
timeCombo = Combobox(root, value=timeListError, textvariable=timeVar)
timeCombo.grid(row=2,column=2,padx=50)
timeCombo.current(0)

timeButton = Button(root, text='Confirm', command=timeCheck,fg='#96796e',bg='#D7E2E8')
timeButton.grid(row=3,column=2,pady=20)


resultButton = Button(root, text='Book', command=result,bg='#D7E2E8',fg='green')
resultButton.grid(row=5,column=1,pady=20)


coachPreviewLabel = Label(root, image='',bg='#ecd8e0')
coachPreviewLabel.grid(row=7,column=0)

courtPreviewLabel = Label(root, image='',bg='#ecd8e0')
courtPreviewLabel.grid(row=7,column=1)

root.mainloop()