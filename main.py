def morse(text):
    morse_dict = {"A":"._",
                  "B":"_...",
                  "C":"_._.",
                  "D":"_..",
                  "E":".",
                  "F":".._.",
                  "G":"_ _.",
                  "H":"....",
                  "I":"..",
                  "J":"._ _ _",
                  "K":"_._",
                  "L":"._..",
                  "M":"._ _",
                  "N":"_.",
                  "O":"_ _ _",
                  "P":"._ _.",
                  "Q":"_ _._",
                  "R":"._.",
                  "S":"...",
                  "T":"_",
                  "U":".._",
                  "V":"..._",
                  "W":"._ _",
                  "X":"_.._",
                  "Y":"_._ _",
                  "Z":"_ _..",
                  "1":"._ _ _ _",
                  "2":".._ _ _",
                  "3":"..._ _",
                  "4":"...._",
                  "5":".....",
                  "6":"_....",
                  "7":"_ _...",
                  "8":"_ _ _..",
                  "9":"_ _ _ _.",
                  "0":"_ _ _ _ _",
                  "error":"invalid character"
    }
    morse_list = []
    for alph in text:
        if alph.upper() in morse_dict:
            morse_list.append(morse_dict[alph.upper()])
        else:
            return (f"invalid character {alph}")

    return ("|".join(morse_list))


from tkinter import *
class UI():
    def __init__(self,engine):
        self.engine = engine
        self.window = Tk()
        self.window.title("morse code converter")
        self.window.config(pady=50, padx=50)
        self.logo_label = Label(text="Morse Code converter")
        self.logo_label.grid(column=1,row=0)
        self.input_label = Label(text="Text")
        self.input_label.grid(column=0,row=1)
        self.input = Entry()
        self.input.grid(column=1,row=1, columnspan=2)
        self.button = Button(text="convert", command=self.morse_com)
        self.button.grid(column=1, row=3)
        self.window.mainloop()

    def morse_com(self):
        morse_code = self.engine(self.input.get())
        self.morse_input = Entry()
        self.morse_input.insert(END, f"{morse_code}")
        self.morse_input.grid(row=2, column=1)








ui=UI(morse)
