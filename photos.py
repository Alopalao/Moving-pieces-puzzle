from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk
from tkinter import Event as TkEvent
from typing import Optional

class MyPhoto(ImageTk.PhotoImage):
    """Photos objects, its positioning is modifiable."""
    def __init__(self, row: int, col: int, image:Image.Image, is_empty=False):
        super().__init__(image)
        self.curr_row = row
        self.curr_col = col
        self.expected_row = row
        self.expected_col = col

        self.image = image
        self.is_empty = is_empty


class MyLabel(tk.Label):
    """Label objects containing images, its position is static."""
    def __init__(self, row: int, col: int, frame:tk.Frame, image_widget: MyPhoto, event: TkEvent):
        super().__init__(frame, image=image_widget, background="white")
        self.curr_row = row
        self.curr_col = col
        self.frame = frame
        self.image_widget = image_widget
        self.image_widget.curr_row = row
        self.image_widget.curr_col = col
        self.is_empty = image_widget.is_empty

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
        self.is_empty = image_widget.is_empty
        image_widget.curr_row = self.curr_row
        image_widget.curr_col = self.curr_col
