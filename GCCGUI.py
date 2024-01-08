# TKInter module
import tkinter as tk

def init_tk_object():
    root = tk.Tk()
    return root

def set_window_dimension(root, w_width, w_height):
    # Set the Windows dimension to be presented.
    root.geometry(str(w_width) + 'x' + str(w_height))


def set_window_title(root, title_string):
    root.title(title_string)


def add_label(root, label_text, label_font, label_font_size, paddingx, paddingy):
    o_label = tk.Label(root, text=label_text, font=(label_font, label_font_size))
    o_label.pack(padx=paddingx, pady=paddingy)


def add_textbox(root, textbox_width, textbox_height, textbox_font, textbox_font_size, paddingx, paddingy):
    o_textbox = tk.Text(root, width=textbox_width,
                        height=textbox_height,
                        font=(textbox_font, textbox_font_size))
    o_textbox.pack(padx=paddingx, pady=paddingy)


def add_button(root, button_text, button_font, button_font_size, paddingx, paddingy):
    o_button = tk.Button(root, text=button_text, font=(button_font, button_font_size))
    o_button.pack(paddingx, paddingy)


def execute_window (root):
    root.mainloop()