import customtkinter
from PIL import Image

app = customtkinter.CTk()
app.title("Cat App")
app.geometry("400x300")
app.maxsize(400, 300)
app.minsize(400, 300)
app.iconbitmap('kot.ico')

my_image = customtkinter.CTkImage(dark_image=Image.open("kot.png"), light_image=Image.open("kot.png"), size=(400, 300))

image_label = customtkinter.CTkLabel(app, image=my_image, text="")
image_label.pack()

app.mainloop()
