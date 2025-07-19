from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont
import sqlite3

LARGEFONT = ("Verdana", 35)

font = ("Arial", 10)
title_font = ("Arial", 12)
background_colour = "#191c27"
button_colour = "#010127"
other_objects_colour = "#333344"
text_colour = "#ffffff"

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #if not work try to replace root with container or sometimes self

        # frame
        container = tk.Frame(self, bg=background_colour)
        container.pack(side="top", fill="both", expand=True)



        #logo
        def logo():
            image_label = tk.Label(container, bg=background_colour)
            image_label.pack(pady=20)

            try:
                # Load and display the logo
                img = Image.open("TotalTrader_logo.png")
                img = img.resize((150, 24))
                tk_image = ImageTk.PhotoImage(img)

                image_label.config(image=tk_image)
                image_label.image = tk_image  # Keep reference to prevent garbage collection

            except Exception:  # if logo is not loaded then display this
                image_label.config(text="Logo Not Found", image="", fg="white", bg=background_colour, font=font)

        # Nav bar
        def nav_bar():
            navbar = tk.Frame(container, bg=background_colour, height=50)
            navbar.pack(side="top", fill="x")
            buttons = ["Home", "Stocks", "Bonds", "Currencies", "Crypto", "Commodities"]
            pages = [Home, Stocks, Bonds, Currencies, Crypto, Commodities]

            for i, page in enumerate(pages):
                btn = tk.Button(
                    navbar,
                    text=buttons[i],
                    bg=button_colour,
                    fg=text_colour,
                    font=font,
                    command=lambda p=page: self.show_frame(p)
                )
                btn.pack(side="left", fill="both", expand=True, padx=5, pady=5)

            # Content area below nav bar
            self.content = tk.Frame(container, bg=background_colour)
            self.content.pack(side="top", fill="both", expand=False)

            self.frames = {}
            for F in pages:
                frame = F(self.content, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

        #money
        def show_balance():
            money=1
            balance_text = f"balance: ${money}"
            text_font = tkFont.Font(font=font)

            # Measure text width and height
            text_width = text_font.measure(balance_text)
            text_height = text_font.metrics("linespace")

            # Add padding around text
            padding_x = 10
            padding_y = 5

            canvas_width = text_width + padding_x * 2
            canvas_height = text_height + padding_y * 2

            canvas = tk.Canvas(container, width=canvas_width, height=canvas_height,
                               bg=container['bg'], highlightthickness=0)
            canvas.pack(anchor='w')

            # Draw rounded rectangle (tight fit around text)
            radius = canvas_height // 2  # half height for rounded corners

            # Four corner arcs
            canvas.create_arc(0, 0, radius * 2, radius * 2, start=90, extent=90,
                              fill=other_objects_colour, outline="")
            canvas.create_arc(canvas_width - radius * 2, 0, canvas_width, radius * 2,
                              start=0, extent=90, fill=other_objects_colour, outline="")
            canvas.create_arc(0, canvas_height - radius * 2, radius * 2, canvas_height,
                              start=180, extent=90, fill=other_objects_colour, outline="")
            canvas.create_arc(canvas_width - radius * 2, canvas_height - radius * 2,
                              canvas_width, canvas_height, start=270, extent=90,
                              fill=other_objects_colour, outline="")

            # Rectangles to connect arcs
            canvas.create_rectangle(radius, 0, canvas_width - radius, canvas_height,
                                    fill=other_objects_colour, outline="")
            canvas.create_rectangle(0, radius, canvas_width, canvas_height - radius,
                                    fill=other_objects_colour, outline="")

            # Draw text centered vertically and horizontally
            canvas.create_text(padding_x, padding_y,
                               text=balance_text, font=font,
                               fill=text_colour, anchor="nw")



        #assets
        def show_assets():
            assets_types = ["Stocks", "Bonds", "Currencies", "Cripto", "Commodities"]
            # adds the "Assets:" text

            label = tk.Label(container, text="Assets:", font=title_font, anchor="w", bg=background_colour, fg=text_colour,
                             width=20)
            label.pack(fill="x", pady=10, padx=10)  # Make label fill horizontally and add padding

        logo()
        nav_bar()
        show_balance()
        show_assets()

        self.show_frame(Home)






    # to displays the current frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#Home frame
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_colour)
        label = tk.Label(self, text="Home", font=LARGEFONT,bg=background_colour)
        label.grid(row=0, column=4, padx=10, pady=10)


#Stocks frame
class Stocks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Stocks", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
#Bonds frame
class Bonds(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Bonds", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

#Currencies frame
class Currencies(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Currencies", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

#Crypto frame
class Crypto(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Crypto", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

#Commodities frame
class Commodities(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Commodities", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)


# Driver Code
root = tkinterApp()
root.mainloop()