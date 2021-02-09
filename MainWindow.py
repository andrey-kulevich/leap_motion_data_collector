# coding=utf-8
from Tkinter import *
from ttk import *
from ActionListener import ActionListener
import Leap
import time


class MainWindow(Tk):
    current_letter = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, master=Tk):
        Tk.__init__(self)
        self.title("Сбор данных для распознавания азбуки жестов")
        self.minsize(width=300, height=300)
        self.iconbitmap('./img/hand.ico')
        label_style = Style()
        label_style.configure('Label', font=('Roboto', 20))

        self.start = Button(self, text="НАЧАТЬ", command=self.record)
        self.exp_letter = Label(text=self.alphabet[self.current_letter], font=('Roboto', 64))

        self.master = master
        self.create_widgets()

    def create_widgets(self):
        header = Label(text="Найдите данную букву в азбуке жестов. Попробуйте повторить этот жест. \n"
                            "Затем нажмите кнопку \"Начать\" и удерживайте этот жест в течение 4 секунд. \n"
                            "Держите руку перед контроллером, пока идет запись. \n",
                       font=('Roboto', 11))
        header.pack(padx=5, pady=5)

        self.exp_letter.pack(pady=20)
        self.start.pack(side="bottom", fill=X, padx=5, pady=5)

    def record(self):
        # Create a sample listener and controller
        listener = ActionListener(self.alphabet[self.current_letter])
        controller = Leap.Controller()

        self.start.config(text="ИДЕТ ЗАПИСЬ...")
        self.update()

        # Have the sample listener receive events from the controller
        controller.add_listener(listener)

        # Keep this process running 4 seconds
        time.sleep(4)

        controller.remove_listener(listener)

        self.start.config(text="НАЧАТЬ")
        self.current_letter += 1
        self.exp_letter.config(text=self.alphabet[self.current_letter])
