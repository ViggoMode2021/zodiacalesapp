import pyttsx3
from tkinter import *
import random
from PIL import Image, ImageTk
root = Tk()
root.geometry('500x500')
root.title('zodiacal')
bg = PhotoImage(file='galaxy.png')
my_background = Label(root, image=bg)
my_background.place(x=0, y=0)
from pygame import mixer
clicked = StringVar()
clicked.set('Signos Zodiacales')

#sag photo label
global sag_image
sag_image = PhotoImage(file='sagitario.png')
global photo_label_sag
photo_label_sag = Label(root, image=sag_image)

#escorpio photo label
global escorpio_image
escorpio_image = PhotoImage(file='escorpio.png')
global photo_label_escorpio
photo_label_escorpio = Label(root, image=escorpio_image)

#escorpio photo label
global capricornio_image
capricornio_image = PhotoImage(file='capricornio.png')
global photo_label_capricornio
photo_label_capricornio = Label(root, image=capricornio_image)

global acuario_image
acuario_image = PhotoImage(file='acuario.png')
global photo_label_acuario
photo_label_acuario = Label(root, image=acuario_image)

global piscis_image
piscis_image = PhotoImage(file='piscis.png')
global photo_label_piscis
photo_label_piscis = Label(root, image=piscis_image)

global aries_image
aries_image = PhotoImage(file='aries.png')
global photo_label_aries
photo_label_aries = Label(root, image=aries_image)

global tauro_image
tauro_image = PhotoImage(file='tauro.png')
global photo_label_tauro
photo_label_tauro = Label(root, image=tauro_image)

global geminis_image
geminis_image = PhotoImage(file='geminis.png')
global photo_label_geminis
photo_label_geminis = Label(root, image=geminis_image)

global cancer_image
cancer_image = PhotoImage(file='cancer.png')
global photo_label_cancer
photo_label_cancer = Label(root, image=cancer_image)

global leo_image
leo_image = PhotoImage(file='leo.png')
global photo_label_leo
photo_label_leo = Label(root, image=leo_image)

global virgo_image
virgo_image = PhotoImage(file='virgo.png')
global photo_label_virgo
photo_label_virgo = Label(root, image=virgo_image)

global libra_image
libra_image = PhotoImage(file='libra.png')
global photo_label_libra
photo_label_libra = Label(root, image=libra_image)

def info(): #sag info
    global my_label
    if clicked.get() == 'Sagitario':
        my_label = Label(root, text='23 de noviembre - 22 de diciembre. T?? eres sincero, honesto, generoso, y optimista', font= ('calibri', 17), bg='white', fg='blue').pack()
        global engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('sagitario. 23 de noviembre - 22 de diciembre. T?? eres sincero, honesto, generoso, y optimista')
        photo_label_sag.place(x=8, y=8)
        engine.runAndWait()

    if clicked.get() == 'Escorpio':
        my_label = Label(root, text='24 de octubre - 22 de noviembre. T?? eres nervioso, decidido, extremista, y devoto', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('escorpio. 24 de octubre - 22 de noviembre. T?? eres nervioso, decidido, extremista, y devoto')
        photo_label_escorpio.place(x=8, y=180)
        engine.runAndWait()

    if clicked.get() == 'Capricornio':
        my_label = Label(root, text='23 de diciembre - 20 de enero. T?? eres reservado, organizado, y decidido', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('capricornio. 23 de diciembre - 20 de enero. T?? eres reservado, organizado, y decidido')
        photo_label_capricornio.place(x=8, y=360)
        engine.runAndWait()

    if clicked.get() == 'Acuario':
        my_label = Label(root, text='21 de enero - 19 de febrero. T?? eres original, din??mico, intuitivo, curioso, y espont??neo', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('acuario. 21 de enero - 19 de febrero. T?? eres original, din??mico, intuitivo, curioso, y espont??neo')
        photo_label_acuario.place(x=8, y=540)
        engine.runAndWait()

    if clicked.get() == 'Piscis':
        my_label = Label(root, text='20 de febrero - 20 de marzo. T?? eres generoso, idealista, modesto, pac??fico, y espont??neo', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('piscis. 20 de febrero - 20 de marzo. T?? eres generoso, idealista, modesto, pac??fico, y reservado')
        photo_label_piscis.place(x=180, y=8)
        engine.runAndWait()

    if clicked.get() == 'Aries':
        my_label = Label(root, text='21 de marzo - 20 de abril. T?? eres valiente, independiente, impaciente, y ambicioso', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('aries. 21 de marzo - 20 de abril. T?? eres valiente, independiente, impaciente, y ambicioso')
        photo_label_aries.place(x=180, y=180)
        engine.runAndWait()

    if clicked.get() == 'Tauro':
        my_label = Label(root, text='21 de abril - 21 de mayo. T?? eres tolerante, afortunado, y extravagante', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('tauro. 21 de abril - 21 de mayo. T?? eres tolerante, afortunado, y extravagante')
        photo_label_tauro.place(x=180, y=360)
        engine.runAndWait()

    if clicked.get() == 'G??minis':
        my_label = Label(root, text='22 de mayo - 21 de junio. T?? eres intelectual, flexible, intranquilo, y en??rgico', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('g??minis. 22 de mayo - 21 de junio. T?? eres intelectual, flexible, intranquilo, y en??rgico')
        photo_label_geminis.place(x=180, y=540)
        engine.runAndWait()

    if clicked.get() == 'C??ncer':
        my_label = Label(root, text='22 de mayo - 21 de junio. T?? eres t??mido, pr??ctico, introspectivo, idealista, y modesto', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('c??ncer. 22 de mayo - 21 de junio. T?? eres t??mido, pr??ctico, introspectivo, idealista, y modesto')
        photo_label_cancer.place(x=1200, y=8)
        engine.runAndWait()

    if clicked.get() == 'Leo':
        my_label = Label(root, text='24 de julio - 23 de agosto. T?? eres responsable, arrogante, dram??tico, generoso, y ambicioso', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('leo. 24 de julio - 23 de agosto. T?? eres responsable, arrogante, dram??tico, generoso, y ambicioso')
        photo_label_leo.place(x=1200, y=180)
        engine.runAndWait()

    if clicked.get() == 'Virgo':
        my_label = Label(root, text='24 de agosto - 23 de septiembre. T?? eres inteligente, l??gico, intolerante, y organizado', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('virgo. 24 de agosto - 23 de septiembre. T?? eres inteligente, l??gico, intolerante, y organizado')
        photo_label_virgo.place(x=1200, y=360)
        engine.runAndWait()

    if clicked.get() == 'Libra':
        my_label = Label(root, text='24 de septiembre - 23 de octubre. T?? eres justo, sincero, rom??ntico, y tolerante', font= ('calibri', 17), bg='white', fg='blue').pack()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say('libra. 24 de septiembre - 23 de octubre. T?? eres justo, sincero, rom??ntico, y tolerante')
        photo_label_libra.place(x=1200, y=540)
        engine.runAndWait()


drop = OptionMenu(root, clicked, 'Capricornio', 'Acuario', 'Piscis', 'Aries', 'Tauro', 'G??minis', 'C??ncer', 'Leo', 'Virgo', 'Libra', 'Escorpio', 'Sagitario')
drop.pack()

horoscopo_button_dos = Button(root, text='Escuchar y leer hor??scopo ', font= ('calibri', 15), command=info)
horoscopo_button_dos.pack()

root.mainloop()
