from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk
from tkinter import Event as TkEvent
from typing import Optional

class MyPhoto(ImageTk.PhotoImage):
    def __init__(self, row: int, col: int, image:Image.Image, empty=False):
        super().__init__(image)
        self.curr_row = row
        self.curr_col = col
        self.expected_row = row
        self.expected_col = col

        self.image = image
        self.empty = empty
        


class MyLabel(tk.Label):
    def __init__(self, row: int, col: int, frame:tk.Frame, image_widget: MyPhoto, event: TkEvent):
        super().__init__(frame, image=image_widget, background="white")
        self.curr_row = row
        self.curr_col = col
        self.frame = frame
        self.image_widget = image_widget
        self.image_widget.curr_row = row
        self.image_widget.curr_col = col
        self.empty = image_widget.empty

        #self.label = tk.Label(self.frame, image=self.image_widget, background="white")
        #if self.curr_row == 0 and self.curr_col == 1:
        #    path = "dummy_images/image_1.png"
        #    image = Image.open(path)
        #    image = image.resize((200, 200))
        #    image = ImageTk.PhotoImage(image)
        #    self.label = tk.Label(self.frame, image=image)
        #else:
        #    self.label = tk.Label(self.frame, image=self.image_widget)
        self.grid(row=self.curr_row, column=self.curr_col)
        self.bind("<Button-1>", event)
        self.configure(height=200,width=200)
        self.propagate(0)

    def set_image_widget(
        self,
        image_widget: MyPhoto,
        background: Optional[str] = None
    ):
        """Change the image in the inner widget"""
        if background:
            self.config(background=background)
        
        self.config(image=image_widget)
        self.image_widget = image_widget
        self.empty = image_widget.empty
        image_widget.curr_row = self.curr_row
        image_widget.curr_col = self.curr_col
