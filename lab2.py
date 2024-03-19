import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv

class ImageControllerComplex: 
    def display(imgData, imgSize):
        pass
    def flip(direction, imgData, imSize, resData, resSize):
        pass
    def decreaseQuality(imgData, imSize, resData, resSize):
        pass

class ImageController(ImageControllerComplex):
    def display(img):
        pass
    def flip(direction, img):
        pass
    def decreaseQuality(img):
        pass

def open_image():
    global canvas, opened
    path = tk.filedialog.askopenfilename(initialdir="~/Pictures", filetypes=[("Image","*.png *.jpg *.jpeg")])
    if path != "":
        opened = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0,0,image=opened, anchor="nw")

root = tk.Tk()
root.geometry("1000x700")
root.title("ImageEditor 9000")
tk.Label(root, text="Welcome to ImageEditor 9000").pack()
imgpane = tk.Frame(root)
imgpane.pack(fill="both", expand=True)
canvas = tk.Canvas(imgpane, bg="white", width=500, height=500)
canvas.pack(fill="both", expand=True)

control = tk.Frame(root)
control.pack()
tk.Button(control, text="Open Image", command=open_image).pack(side="left")
tk.Button(control, text="Flip horizontally").pack(side="left")
tk.Button(control, text="Flip vertical").pack(side="left")
tk.Button(control, text="UH OH").pack(side="left")

root.mainloop()

