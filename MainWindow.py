# coding=utf-8
from Tkinter import *
from ttk import *
from ActionListener import ActionListener
import Leap
import time


class MainWindow(Tk):
    current_letter = 0
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    images = {}

    def __init__(self, master=Tk):
        Tk.__init__(self)
        self.title("Сбор данных для распознавания азбуки жестов")
        self.minsize(width=300, height=300)
        self.iconbitmap('./img/hand.ico')
        self.configure(bg='white')
        bg_style = Style()
        bg_style.configure('bg.TLabel', background='white')

        self.master = master
        self.load_images()

        self.start = Button(self, text="НАЧАТЬ", command=self.record)
        self.exp_letter = Label(text=self.letters[self.current_letter], font=('Roboto', 64), style='bg.TLabel')

        self.img = Label(image=self.images[self.letters[self.current_letter]], style='bg.TLabel')
        self.create_widgets()

    def create_widgets(self):
        header = Label(text="Попробуйте повторить этот жест. Затем нажмите кнопку \"Начать\" \n"
                            "и удерживайте этот жест в течение 4 секунд. \n"
                            "Держите руку перед контроллером, пока идет запись. \n",
                       font=('Roboto', 11), style='bg.TLabel')
        header.pack(padx=5, pady=5)

        self.img.pack(padx=5, pady=5)
        self.exp_letter.pack(pady=20)
        self.start.pack(side="bottom", fill=X, padx=5, pady=5)

    def load_images(self):
        self.images.fromkeys(self.letters)
        for i in range(len(self.letters)):
            self.images[self.letters[i]] = PhotoImage(file='./img/' + self.letters[i] + '.gif')

    def record(self):
        # Create a sample listener and controller
        # listener = ActionListener(self.letters[self.current_letter])
        # controller = Leap.Controller()

        self.start.config(text="ИДЕТ ЗАПИСЬ...")
        self.update()

        # Have the sample listener receive events from the controller
        # controller.add_listener(listener)
        #
        # # Keep this process running 4 seconds
        # time.sleep(4)
        #
        # controller.remove_listener(listener)

        self.start.config(text="НАЧАТЬ")
        self.current_letter += 1
        self.exp_letter.config(text=self.alphabet[self.current_letter])
        self.img.config(image=self.images[self.letters[self.current_letter]])
