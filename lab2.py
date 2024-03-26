import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv

class ImageController:
    #image - Pillow format
    #tkimage - TKinter compatibility layer
    #image_id - id on the canvas
    global canvas
    def display(self):
        path = tk.filedialog.askopenfilename(initialdir="~/Pictures", filetypes=[("Image","*.png *.jpg *.jpeg")])
        if path != "":
            self.image = Image.open(path)
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
    def display(imgData, imgSize):
        pass
    def flip(direction, imgData, imSize, resData, resSize):
        pass
    def decreaseQuality(imgData, imSize, resData, resSize):
        pass



def open_image():
    global controller
    controller = ImageController
    controller.display(controller)
def test_q():
    global controller
    controller.decreaseQuality(controller)


root = tk.Tk()
root.geometry("1000x700")
root.title("ImageEditor 9000")
tk.Label(root, text="Welcome to ImageEditor 9000").pack()
imgpane = tk.Frame(root)
imgpane.pack(fill="both", expand=True)
canvas = tk.Canvas(imgpane, bg="white", width=500, height=500)
canvas.pack(fill="both", expand=False)

control = tk.Frame(root)
control.pack()
tk.Button(control, text="Open Image", command=open_image).pack(side="left")
tk.Button(control, text="Flip horizontally", command=test_q).pack(side="left")
tk.Button(control, text="Flip vertical").pack(side="left")
tk.Button(control, text="UH OH").pack(side="left")

root.mainloop()

