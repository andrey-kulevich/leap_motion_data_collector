# coding=utf-8
from MainWindow import MainWindow
from Tkinter import *
from ttk import *

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()

# def record(current_letter, letters, images):
#     # Create a sample listener and controller
#     # listener = ActionListener(self.letters[self.current_letter])
#     # controller = Leap.Controller()
#
#     start.config(text="ИДЕТ ЗАПИСЬ...")
#     root.update()
#
#     # Have the sample listener receive events from the controller
#     # controller.add_listener(listener)
#     #
#     # # Keep this process running 4 seconds
#     # time.sleep(4)
#     #
#     # controller.remove_listener(listener)
#
#     start.config(text="НАЧАТЬ")
#     current_letter += 1
#     exp_letter.config(text=alphabet[current_letter])
#     img.config(image=images[letters[current_letter]])
#
#
# root = Tk()
#
# current_letter = 0
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
#            'H', 'I', 'J', 'K', 'L', 'M', 'N',
#            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#            'V', 'W', 'X', 'Y', 'Z']
# images = {}
#
# root.title("Сбор данных для распознавания азбуки жестов")
# root.minsize(width=300, height=300)
# root.iconbitmap('./img/hand.ico')
# root.configure(bg='white')
# bg_style = Style()
# bg_style.configure('bg.TLabel', background='white')
#
# images.fromkeys(letters)
# for i in range(len(letters)):
#     images[letters[i]] = PhotoImage(file='./img/' + letters[i] + '.gif')
#
# start = Button(root, text="НАЧАТЬ", command=record)
# exp_letter = Label(text=letters[current_letter], font=('Roboto', 64), style='bg.TLabel')
#
# img = Label(image=images[letters[current_letter]], style='bg.TLabel')
#
# header = Label(text="Попробуйте повторить этот жест. Затем нажмите кнопку \"Начать\" \n"
#                     "и удерживайте этот жест в течение 4 секунд. \n"
#                     "Держите руку перед контроллером, пока идет запись. \n",
#                font=('Roboto', 11), style='bg.TLabel')
# header.pack(padx=5, pady=5)
#
# img.pack(padx=5, pady=5)
# exp_letter.pack(pady=20)
# start.pack(side="bottom", fill=X, padx=5, pady=5)
#
#
#
#
#
# if __name__ == "__main__":
#     root.mainloop()
