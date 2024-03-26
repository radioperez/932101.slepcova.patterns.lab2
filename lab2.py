import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from io import BytesIO
from functools import partial

class ImageController:
    #image - Pillow format
    #tkimage - TKinter compatibility layer
    #image_id - id on the canvas
    global canvas
    def display(self):
        path = tk.filedialog.askopenfilename(initialdir="~/Pictures", filetypes=[("Image","*.png *.jpg *.jpeg")])
        if path != "":
            self.image = Image.open(path)
            IMSIZE = (self.image.width, self.image.height)
            MAXSIZE = (int(canvas.winfo_width()), int(canvas.winfo_height()))
            DISPLAYSIZE = (min(IMSIZE[0],MAXSIZE[0]),min(IMSIZE[1], MAXSIZE[1]))
            self.image = self.image.resize(DISPLAYSIZE)
            self.tkimage = ImageTk.PhotoImage(self.image)
            self.image_id = canvas.create_image(0,0,image=self.tkimage, anchor="nw")
        
    def flip(self, direction):
        dir = Image.FLIP_LEFT_RIGHT if direction == 0 else Image.FLIP_TOP_BOTTOM
        if self.image_id != "":
            self.image = self.image.transpose(dir)
            self.tkimage = ImageTk.PhotoImage(self.image)
            canvas.itemconfig(self.image_id, image=self.tkimage)
    def decreaseQuality(self):
        if self.image_id != "":
            oldw, oldh = self.image.size
            tempsize = (oldw * 2, oldh * 2)
            self.image = self.image.resize(tempsize, Image.NEAREST)
            self.image = self.image.resize((oldw, oldh))
            self.tkimage = ImageTk.PhotoImage(self.image)
            canvas.itemconfig(self.image_id, image=self.tkimage)

class ImageControllerComplex(ImageController):
    #imgData - encoded bytes
    #image - PIL image format
    #tkimage - TKinter compatibility layer
    #image_id - id on the canvas 
    global canvas
    def display(self):
        path = tk.filedialog.askopenfilename(initialdir="~/Pictures", filetypes=[("Image","*.png *.jpg *.jpeg")])
        if path != "":
            file = open(path, mode="rb")
            self.imgData = file.read()
            self.image = Image.open(BytesIO(self.imgData))
            
            IMSIZE = (self.image.width, self.image.height)
            MAXSIZE = (int(canvas.winfo_width()), int(canvas.winfo_height()))
            DISPLAYSIZE = (min(IMSIZE[0],MAXSIZE[0]),min(IMSIZE[1], MAXSIZE[1]))
            self.image = self.image.resize(DISPLAYSIZE)
            self.tkimage = ImageTk.PhotoImage(self.image)
            self.image_id = canvas.create_image(0,0,image=self.tkimage, anchor="nw")
        
    def flip(self, direction):
        dir = Image.FLIP_LEFT_RIGHT if direction == 0 else Image.FLIP_TOP_BOTTOM
        if self.image_id != "":
            self.image = self.image.transpose(dir)
            self.tkimage = ImageTk.PhotoImage(self.image)
            canvas.itemconfig(self.image_id, image=self.tkimage)
    def decreaseQuality(self):
        if self.image_id != "":
            oldw, oldh = self.image.size
            tempsize = (oldw // 2, oldh // 2)
            self.image = self.image.resize(tempsize, Image.NEAREST)
            self.image = self.image.resize((oldw, oldh))
            self.tkimage = ImageTk.PhotoImage(self.image)
            canvas.itemconfig(self.image_id, image=self.tkimage)

def simple():
    global controller
    controller = ImageController
    controller.display(controller)
def notsimple():
    global controller
    controller = ImageControllerComplex
    controller.display(controller)

def flip(direction):
    global controller
    controller.flip(controller, direction)

def quality():
    global controller
    controller.decreaseQuality(controller)

root = tk.Tk()
root.geometry("1000x1000")
root.title("ImageEditor 9000")
tk.Label(root, text="Welcome to ImageEditor 9000").pack()
imgpane = tk.Frame(root)
imgpane.pack(fill="both", expand=True)
canvas = tk.Canvas(imgpane, bg="white", width=500, height=500)
canvas.pack(fill="both", expand=True)

control = tk.Frame(root)
control.pack()

tk.Button(control, text="Open Image (Simple)", command=simple).pack(side="left")
tk.Button(control, text="Open Image (Bytes)", command=notsimple).pack(side="left")
tk.Button(control, text="Flip horizontally", command=partial(flip, 0)).pack(side="left")
tk.Button(control, text="Flip vertically", command=partial(flip, 1)).pack(side="left")
tk.Button(control, text="Quality", command=quality).pack(side="left")

root.mainloop()

