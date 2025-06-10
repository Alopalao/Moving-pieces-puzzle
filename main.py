import tkinter as tk
from tkinter import Tk
from tkinter import Event as TkEvent
from PIL import Image, ImageTk
import random
from computer import Computer
from photos import MyPhoto, MyLabel

class Game:
    def __init__(self, screenSize, screenName, image_path:str=None, window:Tk=None):
        self.screenSize = screenSize
        self.screenName = screenName

        self.image_path = image_path
        self.window = Tk(className="screenName")
        self.window.geometry(screenSize)
        name_label = tk.Label(self.window, text=self.screenName, bg="salmon", font=("Arial", 21))
        name_label.pack(pady=5)

        self.image_label = None
        self.image = self.get_image_from_path(self.image_path)
        self.empty_image = self.get_image_from_path("white-space.png")
        self.image_complete = ImageTk.PhotoImage(self.image)

        self.image_frame = tk.Frame(self.window, width=624, height=624, bg="medium turquoise")
        self.image_frame.pack(pady=5)
        self.button_frame = tk.Frame(self.window, width=600, height=200, bg="black")
        self.button_frame.pack(pady=5)

        # Grid 3x3 variables
        self.imagesList: list[MyPhoto] = []
        self.labelList: list[MyLabel] = []

        # Click Event
        self.event = self.on_label_click
        self.selected_label: MyLabel = None

    def check_for_completion(self):
        for image in self.imagesList:
            if image.curr_col != image.expected_col or image.curr_row != image.expected_row:
                return False
        return True

    def on_label_click(self, event: TkEvent):
        """Click on a label"""
        clicked_label:MyLabel = event.widget

        if self.selected_label is None:
            clicked_label.config(background="black")
            self.selected_label = clicked_label

        elif self.selected_label == clicked_label:
            self.selected_label.config(background="white")
            self.selected_label = None

        else:
            if self.able_to_move(clicked_label):
                selected_image_wd = self.selected_label.image_widget
                self.selected_label.set_image_widget(clicked_label.image_widget, "white")
                clicked_label.set_image_widget(selected_image_wd)
                self.selected_label = None
            
                if self.check_for_completion():
                    print("GAME OVER")

            else:
                print("NOT MOVE")
                self.selected_label.config(background="white")
                self.selected_label = None

    def able_to_move(self, clicked_label: MyLabel) -> bool:
        """Determine if the images are going to be swap.
         In this puzzle, the images can only move if:
         - One of the label have to have an empty space
         - The image is next to the selected one.
         - Diagonal positions are not count as next to.
        """
        #return True
        clicked_row = clicked_label.curr_row
        clicked_col = clicked_label.curr_col

        selected_col = self.selected_label.curr_col
        selected_row = self.selected_label.curr_row

        if not clicked_label.empty and not self.selected_label.empty:
            return False

        if clicked_row == selected_row:
            if clicked_col in (selected_col+1, selected_col-1):
                return True
        elif clicked_col == selected_col:
            if clicked_row in (selected_row+1, selected_row-1):
                return True
        return False

    def get_image_from_path(self, image_path: str) -> Image.Image:
        "Returns resized image from path."
        image = Image.open(image_path)
        image = image.resize((600, 600))
        return image

    def idk(self):
        self.image_label_complete.config(background="red")

    def clean_screen(self):
        """Clean the frames on screen."""
        for widget in self.image_frame.winfo_children():
            widget.destroy()
        
        #for widget in self.button_frame.winfo_children():
        #    widget.destroy()

    def randomize_pictures(self):
        """Start by randomizing the position of the pictures."""
        self.selected_label = None
        possible_pos = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
        ]
        random.shuffle(possible_pos)
        random_number = random.randrange(0, 9)
        (empty_row, empty_col) = possible_pos[random_number]
        self.imagesList = []
        self.labelList = []

        rows = 3
        cols = 3
        size_img = 200
        for row in range(rows):
            for col in range(cols):
                left = col * size_img
                right = left + size_img
                top = row * size_img
                bottom = top + size_img
                if row == empty_row and col == empty_col:
                    cropped = self.empty_image.crop((left, top, right, bottom))
                    Aphoto = MyPhoto(row, col, cropped, empty=True)
                else:
                    cropped = self.image.crop((left, top, right, bottom))
                    Aphoto = MyPhoto(row, col, cropped)
                self.imagesList.append(Aphoto)

        self.clean_screen()
        for i, (row, col) in enumerate(possible_pos):
            Alabel = MyLabel(row, col, self.image_frame, self.imagesList[i], self.event)
            self.labelList.append(Alabel)

    def start(self):
        "Start game window."
        #self.image_frame.grid_rowconfigure(0, weight=1)
        #self.image_frame.grid_columnconfigure(0, weight=1)
        #self.image_frame.grid_propagate(0)
        self.clean_screen()
        self.image_label_complete = tk.Label(self.image_frame, image=self.image_complete, background="black", borderwidth=5)
        self.image_label_complete.grid(row=0, column=0)

        click_bt = tk.Button(self.button_frame, text="Click", background='lightcoral', command=self.idk)
        click_bt.pack(pady=5)

        click_bt = tk.Button(self.button_frame, text="Start game", background='cyan', command=self.randomize_pictures)
        click_bt.pack(pady=5)

        quit_bt = tk.Button(self.button_frame, text="Quit", command=self.window.destroy)
        quit_bt.pack(pady=5) 
        self.window.mainloop()


if __name__ == '__main__':
    screenSize = "800x800"
    screenName = "8-Puzzle Game"
    image_path = "burger-eating.png"
    game = Game(screenSize, screenName, image_path=image_path)
    game.start()
