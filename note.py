from tkinter import *

FONT = ("Verdena",20,"normal")




window=Tk()
window.title("Secret Notes")
window.config(padx=30 , pady=30 )


#UI

photo=PhotoImage(file="yessss.png")
photo_label=Label(image=photo)
photo_label.pack()


#photo_button=Label(image=photo)
#photo_button.pack()

#canvas=Canvas(height=200,width=2000)
#canvas.create_image(100,100 ,image= photo)
#canvas.pack()




title_info_label = Label(text="Enter your title"    ,   font=FONT )
title_info_label.pack()



title_entry = Entry(width=30)
title_entry.pack()


input_info_label=Label(text="Enter your secret", font=FONT)
input_info_label.pack()

input_text=Text(width=50, height=25)
input_text.pack()


master_secret_secret_label=Label(text="Enter master key",font=FONT)
master_secret_secret_label.pack()



master_secret_input=Entry(width=30)
master_secret_input.pack()


save_button=Button(text="Save & Encrypt")
save_button.pack()

decrypt_button = Button(text="Decrypt")
decrypt_button.pack()


window.mainloop()
