from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageDraw,ImageFont,ImageTk
import glob

image_path = 'C:\\Users\Jatin verma\PycharmProjects\ImageWatermarking\in\*.*'
watermark = 'JV_Enterprises'

def watermark_image(input_img_path,output_img_path,text):
    photo = Image.open(input_img_path)
    w,h=photo.size
    print(w,h)
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype('arial.ttf',50)
    text = text
    text_w, text_h = drawing.textsize(text,font)
    print(text_w,text_h)
    pos = w-text_w,(h-text_h)
    print(pos)
    c_text = Image.new('RGB',(text_w,text_h), color='#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0,0),text, fill = '#ffffff', font=font)
    c_text.putalpha(50)
    photo.paste(c_text,pos,c_text)
    photo.save(output_img_path)

def upload():
    list = glob.glob(image_path)

    for photo in list:
        noit = photo.split('\\')
        tex = noit[-2].replace('in', 'out')
        noit.pop(-2)
        noit.insert(-1, tex)
        out = '\\'.join(noit)
        watermark_image(photo, out, watermark)

def opn_fun():
    filename = filedialog.askopenfilename()
    return filename

def opn_img():
    x = opn_fun()
    img_name = x.split('/')[-1]
    # img = Image.open(x)
    # w,h = (img.width//2, img.height//2)
    # img = img.resize((w,h), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)
    # panel = Label(window, image=img)
    # panel.image = img
    out = f'out/{img_name}'
    # panel.pack()
    watermark_image(x,out, watermark)
    show_img(out)

def show_img(out):
    new_img = Image.open(out)
    w,h = (new_img.width//2, new_img.height//2)
    new_img = new_img.resize((w,h), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(new_img)
    panel = Label(window, image=new_img)
    panel.image = new_img
    panel.pack()


window=Tk()
window.title('Create watermark on Image')
window.config(padx=50,pady=50)

label = Label(text='Create watermark on Image', font=('Arial',24))
label.pack()

button = Button(text='UPLOAD FOLDER', command = upload)
button.pack()
button_image = Button(text='UPLOAD IMAGE', command =opn_img)
button_image.pack()

window.mainloop()

