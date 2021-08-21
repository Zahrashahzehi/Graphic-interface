from tkinter import *  
from PIL import ImageTk, Image
window = Tk()
window.title("form information page")
window.geometry('600x500')
window.config(bg='red')
bg = ImageTk.PhotoImage(file="blood_red5.png")
canvas = Canvas(window, width=600, height=500)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=bg, anchor='nw')
# def resize_image(e):
#    global image, resized, image2
#    image = Image.open("blood_red.png")
#    resized = image.resize((e.width, e.height), Image.ANTIALIAS)
#    image2 = ImageTk.PhotoImage(resized)
#    canvas.create_image(0, 0, image=image2, anchor='nw')
# window.bind("<Configure>", resize_image)
def cheek():
          label_view.config(text="welcom to our upp"  , bg=_from_rgb((194, 147, 132)), fg=_from_rgb((28, 27, 27)))
def sign_in_bu():
     if Checkbutton_language_statue.get() == 1:
         if choose_gender.get() == "Fmale":
             print("welcom miss {} {} to our opp".format(entry_first_name.get() , entry_last_name.get()))
             print("languge if farsi . ")
         elif choose_gender.get() == "male":
             print("welcom mr {} {} to our opp".format(entry_first_name.get() , entry_last_name.get()))
             print("languge is farsi . ")  
     else:
         if choose_gender.get() == "Fmale":
             print("welcom miss {} {} to our opp".format(entry_first_name.get() , entry_last_name.get()))
             print("languge if english . ")
         elif choose_gender.get() == "male":
             print("welcom mr {} {} to our opp".format(entry_first_name.get() , entry_last_name.get()))
             print("languge is english . ") 
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb               
label_first_name = Label(window , text="first name : " , fg=_from_rgb((28, 27, 27)) , font=("Elephant" , 20) , border="7" , relief="raised", bg=_from_rgb((194, 147, 132)))

label_first_name.place(x=15 , y=10)
entry_first_name = Entry(window  , bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised" )
entry_first_name.place(x=15 , y=65)                    
label_last_name = Label(window , text="last name :  " , fg=_from_rgb((28, 27, 27)) , font=("Elephant" , 20) , border="7" , relief="raised", bg=_from_rgb((194, 147, 132)))
label_last_name.place(x=15 , y=100)
entry_last_name = Entry(window  , bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised")
entry_last_name.place(x=15 , y=155)
label_language = Label(window , text="Please choose languge : " ,  fg=_from_rgb((28, 27, 27)) , font=("Elephant" , 15) , border="7" , relief="raised", bg=_from_rgb((194, 147, 132)))
label_language.place(x=280 , y=10 )
Checkbutton_language_statue = IntVar()
Checkbutton_language = Checkbutton(window , text="language_farsi" , variable=Checkbutton_language_statue ,  bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised" , font=("Elephant" , 10) )
Checkbutton_language.place(x=280 , y=65)
label_Gender = Label(window , text="Gender : " , fg=_from_rgb((28, 27, 27)) , font=("Elephant" , 15) , border="7" , relief="raised", bg=_from_rgb((194, 147, 132)))
label_Gender.place(x=280 ,y=110)
choose_gender = StringVar()
Radiobutto_1 = Radiobutton(window , text="male" , variable=choose_gender , command=sign_in_bu , value="male" , bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised" , font=("Elephant" , 10))
Radiobutto_1.place(x=300 , y=165)
Radiobutto_2 = Radiobutton(window , text="Fmale" , variable=choose_gender , command=sign_in_bu , value="Fmale" , bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised" , font=("Elephant" , 10) )
Radiobutto_2.place(x=300 , y=200)
sign_in_bu = Button(window , text="sign_in" , command= cheek , borderwidth=10 , activebackground="red" , state=NORMAL , highlightbackground="green" , bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised" , font=("Elephant" , 15))
sign_in_bu.place(x=180 , y=300)
label_view=Label(window)
label_view.place(x=160 , y=360)
Checkbutton_bot_state = IntVar()
Checkbutton_bot = Checkbutton(window , text="i'm not robot :) " , variable=Checkbutton_bot_state  , bg=_from_rgb((204, 177, 177)) , border="4" , relief="raised" , font=("Elephant" , 10) )
Checkbutton_bot.place(x=180 , y=260)
window.mainloop()