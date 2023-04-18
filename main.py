import tkinter as tk
import random
import os
from PIL import Image


def generate():
    global Top, Tishka, Pants, top_images, tishka_images, pants_images

    new_top_img = os.path.join(Top, random.choice(top_images))
    new_tishka_img = os.path.join(Tishka, random.choice(tishka_images))
    new_pants_img = os.path.join(Pants, random.choice(pants_images))
    return new_top_img, new_tishka_img, new_pants_img


def update_image():
    global path, top_images,\
        cnv_top, cnv_tishka, cnv_pants, \
        image_top_cfg, image_pants_cfg, image_tishka_cfg,\
        new_top_image, new_tishka_img, new_pants_img,\
        new_top, new_tishka, new_pants, btn_gen
    try:
        new_top_img, new_tishka_img, new_pants_img = generate()
    except Exception:
        btn_gen['text'] = 'DOWNLOAD PNG'
    else:
        btn_gen['text'] = 'Generate'
        new_top = tk.PhotoImage(
            file=new_top_img
        )
        cnv_top.itemconfig(image_top_cfg, image=new_top)

        new_tishka = tk.PhotoImage(
            file=new_tishka_img
        )
        cnv_tishka.itemconfig(image_tishka_cfg, image=new_tishka)

        new_pants = tk.PhotoImage(
            file=new_pants_img
        )
        cnv_pants.itemconfig(image_pants_cfg, image=new_pants)


def main():
    global path, top_images, tishka_images, pants_images,\
        cnv_top, cnv_tishka, cnv_pants, \
        image_top_cfg, image_pants_cfg, image_tishka_cfg,\
        new_top_image, new_tishka_img, new_pants_img,\
        new_top, new_tishka, new_pants, Top, Tishka, Pants, \
        btn_gen

    try:
        os.chdir("Clothes_Randomizer")
    except FileNotFoundError:
        pass

    if not os.path.isdir("Clothes"):
        os.mkdir("Clothes")
        os.chdir("Clothes")
        if not os.path.isdir("Top"):
            os.mkdir("Top")
        if not os.path.isdir("Tishka"):
            os.mkdir("Tishka")
        if not os.path.isdir("Pants"):
            os.mkdir("Pants")
    else:
        try:
            os.chdir("Clothes")
        except FileNotFoundError:
            pass

    path = os.getcwd()
    print(path)
    Top = os.path.join(path, "Top")
    Tishka = os.path.join(path, "Tishka")
    Pants = os.path.join(path, "Pants")

    window = tk.Tk()
    window.title("Clothes randomizer v1.0 by ihopes0")
    window.columnconfigure([0, 1], weight=1, minsize=400)
    window.rowconfigure(0, weight=1, minsize=300)
    frm_left = tk.Frame(window)
    frm_left.grid(row=0, column=0)
    frm_right = tk.Frame(window)
    frm_right.grid(row=0, column=1)

    btn_gen = tk.Button(
        master=frm_left,
        text='Generate',
        relief=tk.RAISED,
        borderwidth=5,
        width=30,
        bg='grey',
        command=update_image,
    )
    btn_gen.grid(
        row=0,
        column=0,
        padx=10
    )
    cnv_top = tk.Canvas(master=frm_right)
    cnv_top.pack(anchor=tk.CENTER, expand=1)
    cnv_tishka = tk.Canvas(master=frm_right)
    cnv_tishka.pack(anchor=tk.CENTER, expand=1)
    cnv_pants = tk.Canvas(master=frm_right)
    cnv_pants.pack(anchor=tk.CENTER, expand=1)

    image_top_cfg = cnv_top.create_image(
        0, 0, anchor='nw',
        )

    image_tishka_cfg = cnv_tishka.create_image(
        0, 0, anchor='nw',
        )
    image_pants_cfg = cnv_pants.create_image(
        0, 0, anchor='nw',
        )

    top_images = []
    for root, dirs, files in os.walk(Top):
        for f in files:
            if f[-4:] == '.png':
                top_f_path = os.path.join(Top, f)
                img_orig = Image.open(top_f_path)
                img_orig.thumbnail(size=(300, 300))
                img_orig.save(top_f_path)
                top_images.append(f)
    print(top_images)

    tishka_images = []
    for root, dirs, files in os.walk(Tishka):
        for f in files:
            if f[-4:] == '.png':
                tishka_f_path = os.path.join(Tishka, f)
                img_orig = Image.open(tishka_f_path)
                img_orig.thumbnail(size=(300, 300))
                img_orig.save(tishka_f_path)
                tishka_images.append(f)
    print(tishka_images)
    pants_images = []
    for root, dirs, files in os.walk(Pants):
        for f in files:
            if f[-4:] == '.png':
                pants_f_path = os.path.join(Pants, f)
                img_orig = Image.open(pants_f_path)
                img_orig.thumbnail(size=(300, 300))
                img_orig.save(pants_f_path)
                pants_images.append(f)
    print(pants_images)
    window.mainloop()


if __name__ == "__main__":
    main()
