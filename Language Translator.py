from tkinter import *
import translate

global TextVar
global OutputVar

# initializing window
Screen = Tk()
Screen.geometry("750x250")
Screen.title("Language Translator ")
Screen.configure(bg='#f8f4f4')

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

# Tuple for choosing languages
LanguageChoices = {'Hindi', 'English', 'French', 'German', 'Bengali'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = translate.Translator(from_lang=InputLanguageChoice.get(), to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


Label(Screen, text="WELCOME TO THE TRANSLATER").grid(row=0, column=1)

# Choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
Label(Screen, text="Enter a language").grid(row=2, column=1)
InputLanguageChoiceMenu.grid(row=3, column=1)

# Choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
Label(Screen, text="Translated Language").grid(row=2, column=2)
NewLanguageChoiceMenu.grid(row=3, column=2)

Label(Screen, text="Enter Text").grid(row=4, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar).grid(row=4, column=1)

Label(Screen, text="Output Text").grid(row=4, column=2)
OutputVar = StringVar()
TextBox = Entry(Screen, textvariable=OutputVar).grid(row=4, column=3)

Label(Screen, text="Tip: 1. Write input text in CAPITALS to get Output in ENGLISH").grid(row=6, column=1)
Label(Screen, text="   Tip: 2. Write input in SMALLS to get Output in DESIRED LANGUAGE").grid(row=7, column=1)
Label(Screen, text="\nCreated by Rohan, Rishikesh, Prathamesh, Amar ").grid(row=8, column=1)

# Button for calling function
B = Button(Screen, text="Translate", command=Translate, relief=GROOVE).grid(row=5, column=1, columnspan=3)
mainloop()
