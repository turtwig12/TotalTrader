import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont

# Create the main window
root = tk.Tk()
root.title("Black Tkinter Window")



def make_ui():
    # background colour is #191c27
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    money = 10000

    font="Arial, 10"
    title_font = "Arial, 12"
    background_colour = "#191c27"
    button_colour = "#010127"
    other_objects_colour = "#333344"
    text_colour = "#ffffff"

    def make_basic_frame():
        root.configure(bg=background_colour)
        root.geometry(f"{int(screen_width / 2)}x{int(screen_height / 2)}")
    def add_logo():
        image_label = tk.Label(root, bg=background_colour)
        image_label.pack(pady=20)

        try:
            # Load and display the logo
            img = Image.open("TotalTrader_logo.png")
            img = img.resize((150, 24))
            tk_image = ImageTk.PhotoImage(img)

            image_label.config(image=tk_image)
            image_label.image = tk_image  # Keep reference to prevent garbage collection

        except Exception: #if logo is not loaded then display this
            image_label.config(text="Logo Not Found", image="", fg="white", bg=background_colour, font=font)
    def make_nav_bar():
        assets_types=["Stocks", "Bonds", "Currencies", "Cripto", "Commodities"]
        # Create a gray box (frame)
        gray_box = tk.Frame(root, bg=background_colour, width=screen_width, height=50)
        gray_box.pack_propagate(False)
        # Configure the columns of gray_box for equal spacing
        for i in range(5):
            gray_box.grid_columnconfigure(i, weight=1)

        # Create buttons with custom colours
        for i in range(5):
            button = tk.Button(
                gray_box,
                text=assets_types[i],
                bg=button_colour, #background colour
                fg=text_colour,  # Text colour
                font=font
            )
            button.grid(row=0, column=i, sticky="ew", padx=5)  # Sticky expands horizontally

        gray_box.pack(pady=5, fill="x")
    def show_balance():
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

        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height,
                           bg=root['bg'], highlightthickness=0)
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
    def show_assets():
        assets_types = ["Stocks", "Bonds", "Currencies", "Cripto", "Commodities"]
        #adds the "Assets:" text

        label = tk.Label(root, text="Assets:", font=title_font, anchor="w", bg=background_colour, fg=text_colour, width=20)
        label.pack(fill="x", pady=10, padx=10)  # Make label fill horizontally and add padding


    make_basic_frame()
    add_logo()
    make_nav_bar()
    show_balance()
    show_assets()




# Run the application
make_ui()
root.mainloop()
