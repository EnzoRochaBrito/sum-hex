import customtkinter as ctk
from tkinter import messagebox
import hextodec

#=========================================Functions==========================================

def responsible_labels(event): #Update the labels width and height at real time
    
    std_width      = round(win.winfo_width() * 0.266)
    std_height     = round(win.winfo_height() * 0.066)
    title_size     = round(win.winfo_height() * 0.05)
    entry_box_size = round(win.winfo_height() * 0.03)
    
    EntryHex1.configure(width=std_width, height=std_height)
    EntryHex2.configure(width=std_width, height=std_height)
    CalcHexButton.configure(width=std_width, height=std_height)
    
    title_font.configure(size=title_size)
    entry_box.configure(size=entry_box_size)

def mix_color(): #Update the colorrow labels and calcule the hexadecimal color
    
    color3 = []
    newhex = "#"
    
    hexcode1 = EntryHex1.get().removeprefix("#")
    hexcode2 = EntryHex2.get().removeprefix("#")
    
    if hexcode1:
        try:
            colorrow1.configure(fg_color=f"#{hexcode1}", text=f"#{hexcode1}")
        except:
            messagebox.showerror(title="Invalid HexCode", message="The HexCode in the \"Color 1\" entry is unvalid!")
            return -1
    
    if hexcode2:
        try:
            colorrow2.configure(fg_color=f"#{hexcode2}", text=f"#{hexcode1}")
        except:
            messagebox.showerror(title="Invalid HexCode", message="The HexCode in the \"Color 2\" entry is unvalid!")
            return -1
    
    if (hexcode1 and hexcode2):
        color1 = hextodec.rgb(hexcode1)
        color2 = hextodec.rgb(hexcode2)
        
        for i in range(3):
            color3.append((color1[i]//2)+(color2[i]//2)) #Sum the RGB of both Entry's and breaks it in half
        
        for rgb in color3: #Transforms the RGB into Hexadecimal Code again
            newhex += hex(rgb)[2:]
        
        colorrow3.configure(fg_color=newhex, text=newhex)
        
        if sum(color3) > 381:
            colorrow1.configure(text_color="black")
            colorrow2.configure(text_color="black")
            colorrow3.configure(text_color="black")
        else:
            colorrow1.configure(text_color="white")
            colorrow2.configure(text_color="white")
            colorrow3.configure(text_color="white")

#==========================================Settings==========================================
win = ctk.CTk('white')
win.title('Sum Hex')
ctk.set_appearance_mode('light')
win.iconbitmap('image\\SumHexIco.ico')
win.minsize(600, 500)

#---------- Grid  ----------
win.grid_rowconfigure(index=(0,1,2), weight=1)
win.grid_columnconfigure(index=0, weight=3)
win.grid_columnconfigure(index=1, weight=1)

win.bind("<Configure>", responsible_labels) #Responsive labes

#---------- Fonts ----------

std_font   = ctk.CTkFont('Verdana', size=26, weight='bold', slant='italic', underline=True)    
title_font = ctk.CTkFont('Verdana', weight='bold', slant='italic', underline=True)
entry_box  = ctk.CTkFont('Verdana', weight='bold')

#===========================================Labels===========================================

#---------- Colors Column ----------

colorrow1 = ctk.CTkLabel(win, fg_color="#000", text="#000", font=std_font, text_color='white')
colorrow2 = ctk.CTkLabel(win, fg_color="#000", text="#000", font=std_font, text_color='white')
colorrow3 = ctk.CTkLabel(win, fg_color="#000", text="#000", font=std_font, text_color='white')

colorrow1.grid(column=0, row=0, sticky='nsew')
colorrow2.grid(column=0, row=1, sticky='nsew')
colorrow3.grid(column=0, row=2, sticky='nsew')

#---------- Buttons and Texts ----------

Title         = ctk.CTkLabel(win, fg_color='white', text='Sum-Hex', font=title_font, text_color='darkblue')

EntryHex1     = ctk.CTkEntry(win, fg_color='#ffffff', placeholder_text="Hexadecimal Color 1", font=entry_box)
EntryHex2     = ctk.CTkEntry(win, fg_color='#ffffff', placeholder_text="Hexadecimal Color 2", font=entry_box)

CalcHexButton = ctk.CTkButton(win, fg_color='#707070', hover_color="#efefef" ,text='Mix Colors', font=std_font, text_color='darkblue', command=mix_color)

Title.grid(column=1, row=0, sticky='ns')
EntryHex1.grid(column=1, row=1, sticky='n')
EntryHex2.grid(column=1, row=1)
CalcHexButton.grid(column=1, row=1, sticky='s')

win.mainloop()