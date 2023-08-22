import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askinteger
import qrcode
from PIL import ImageTk, Image, ImageOps
from tkinter import filedialog


# generate .exec ==> pyinstaller --onefile app.py


class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zetro's QR Code Generator")
        self.root.geometry("600x600")  

        self.label = tk.Label(root, text="Enter data:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.fill_color_label = tk.Label(root, text="Fill Color:")
        self.fill_color_label.pack()

        self.fill_color_button = tk.Button(root, text="Pick Fill Color", command=self.pick_fill_color)
        self.fill_color_button.pack()

        self.back_color_label = tk.Label(root, text="Background Color:")
        self.back_color_label.pack()

        self.back_color_button = tk.Button(root, text="Pick Background Color", command=self.pick_back_color)
        self.back_color_button.pack()

        self.border_label = tk.Label(root, text="Border Size:")
        self.border_label.pack()

        self.border_entry = tk.Entry(root)
        self.border_entry.pack()

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.qr_code_label = tk.Label(root)
        self.qr_code_label.pack()

        self.fill_color = "#000000" 
        self.back_color = "#FFFFFF"  

        self.qr_code_data = None  

    def pick_fill_color(self):
        color = askcolor(color=self.fill_color)[1]
        if color:
            self.fill_color = color
            self.fill_color_button.config(bg=color)

    def pick_back_color(self):
        color = askcolor(color=self.back_color)[1]
        if color:
            self.back_color = color
            self.back_color_button.config(bg=color)

    def generate_qr_code(self):
        data = self.entry.get()

        border_size = int(self.border_entry.get() or 1) 

        box_size = 12  

        if data:
            self.qr_code_data = data 
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border_size,
            )
            qr.add_data(data)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
            self.qr_code_image = ImageTk.PhotoImage(qr_image)

            self.qr_code_label.config(image=self.qr_code_image)
            self.qr_code_label.image = self.qr_code_image

    def save_image(self):
        if self.qr_code_data:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                size = askinteger("Image Size", "Enter the size of the image", minvalue=1)
                if size:
                    border_size = int(self.border_entry.get() or 1)  

                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=size,
                        border=border_size,
                    )
                    qr.add_data(self.qr_code_data)
                    qr.make(fit=True)

                    qr_image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
                    qr_image = ImageOps.expand(qr_image, border=border_size, fill=self.back_color)
                    qr_image.save(save_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
