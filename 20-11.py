import tkinter as tk
from PIL import Image, ImageTk
def message():
    label_text.config(text = "chuc mung ngay phu nu viet nam 20/10")
    img = Image.open("20-11.png")
    img = img.resize((180,180))
    photo = ImageTk.PhotoImage(img)
    label_img.config(image=photo)
    label_img.image = photo
root = tk.Tk()
root.title("20/10")
root.geometry("360x360")
root.configure(bg="#fff7e6")
button = tk.Button(root, text = "Nhan vao day",font = ("Arial",14),bg="#fff7e6",fg="white", command=message)
button.pack(pady=20)
label_text = tk.Label(root,text ="",font =("Arial,14"),bg="#fff7e6",fg="#e75480")
label_text.pack (pady=10)
label_img = tk.Label(root, bg = "#fff7e6")
label_img.pack(pady=10)
root.mainloop()