# Create project with: Tkiner, Pillow

from tkinter import Button, Label, Tk, messagebox, filedialog, simpledialog
from PIL import Image, ImageTk, ImageFilter

# Variables
root = Tk()

# Settings for the window
root.title("Photo App")
# Size of the window
root.geometry("500x500")
# Center the window
root.eval('tk::PlaceWindow . center')
# Disable resize
root.resizable(False, False)


def selectImage():
    
    global loadImage
    loadImage = filedialog.askopenfilename()
    image = Image.open(loadImage)

    # Open the image in label
    renderImage = ImageTk.PhotoImage(
        image.resize((300, 300), Image.Resampling.LANCZOS))

    labelImage.configure(image=renderImage)
    labelImage.image = renderImage


def setImage():
    
    try:
        image = Image.open(loadImage)
    except:
        messagebox.showerror("Error", "Please select an image first")
    return image


def convertBlackAndWhite():
    message = messagebox.showinfo("Info", "This will convert the image to black and white")
    
    imageBN = setImage().convert("L")

    # nameImage = simpledialog.askstring("Input", "Name to save the image", parent=root)
    imageBN.save("blackandwhite.jpg")
    imageBN.show()

def generateBlur():
    
    message = messagebox.showinfo("Info", "This will blur the image")

    imageBlur = setImage().filter(ImageFilter.GaussianBlur(25))
    imageBlur.save("blur.jpg")
    imageBlur.show()



def generateOutline():
    
    message = messagebox.showinfo("Info", "This will outline the image")

    imageOutline = setImage().filter(ImageFilter.FIND_EDGES)
    imageOutline.save("outline.jpg")
    imageOutline.show()


def generateHighLight():
    
    message = messagebox.showinfo("Info", "This will highlight the image")
    
    imageHighLight = setImage().filter(ImageFilter.EMBOSS)
    imageHighLight.save("highlight.jpg")
    imageHighLight.show()


labelImage = Label(root, text="Select an image")

buttonSelectImage = Button(root, text="Select Image", command=selectImage)

buttonConvertBlackWhite = Button(
    root, text="Convert to Black and White", command=convertBlackAndWhite)

buttonBlurImage = Button(root, text="Blur Image", command=generateBlur)

buttonOutline = Button(root, text="Outline", command=generateOutline)

buttonHighLight = Button(root, text="Highlight", command=generateHighLight)


# Order of the widgets
labelImage.pack()

buttonSelectImage.pack()

buttonConvertBlackWhite.pack()

buttonBlurImage.pack()

buttonOutline.pack()

buttonHighLight.pack()

# Window app
root.mainloop()
