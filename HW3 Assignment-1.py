from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as scrollText
from tkinter import ttk,messagebox,colorchooser
from tkinter.filedialog import asksaveasfilename,askopenfilename
import os

#fot dictionary font (color and size)
defaultColorAndSizeName=["fg","size"]
defaultColorAndSizeValue=["#000000","11"]
defaultFileExtension=[".txt",".edit"]

def New():
    # Refresh UI from .edit file 
    style=ttk.Style()
    style.configure("textcolor.TButton",foreground="#000000")
    scrollTextBox.configure(fg="#000000", font=("Arial",11))
    selectedFontSize.set(11)
    scrollTextBox.delete("1.0","end")
    
def Open():
    toOpenFilePath=askopenfilename(
        title="Open file!",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    
    if toOpenFilePath:
        openFileDir,openFileName=os.path.split(toOpenFilePath)
        openFileName=os.path.splitext(openFileName)[0]
        
        for exten in defaultFileExtension:
            fileOpen=os.path.join(openFileDir,f"{openFileName}{exten}")
            if exten==".txt":
                with open(fileOpen,"r") as file:
                    textContent=file.read()
                scrollTextBox.delete("1.0","end")
                scrollTextBox.insert("insert",textContent)
            else:
                try:
                    with open(fileOpen,"r") as file:
                        colorAndSize=file.read()
                        colorAndSizeValueList=eval(colorAndSize)
                        defaultColorAndSizeValue[:]=list(colorAndSizeValueList.values())
                        # Refresh UI from .edit file 
                        style=ttk.Style()
                        style.configure("textcolor.TButton",foreground=defaultColorAndSizeValue[0])
                        scrollTextBox.configure(
                        fg=defaultColorAndSizeValue[0], 
                        font=("Arial", defaultColorAndSizeValue[1]))
                        selectedFontSize.set(str(defaultColorAndSizeValue[1]))
                except Exception as e:
                    messagebox.showinfo(title="Error",message="Fontsize and color will setup with default.\n"+str(e))
                    # Refresh UI from .edit file 
                    style=ttk.Style()
                    style.configure("textcolor.TButton",foreground="#000000")
                    scrollTextBox.configure(
                    fg="#000000", 
                    font=("Arial",11))
                    selectedFontSize.set(11)
        

def Save():
    color_size_dict=dict(zip(defaultColorAndSizeName,defaultColorAndSizeValue))
    filePathToSave = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save file!"
    )
    
    if filePathToSave:
        fileDir,fileName=os.path.split(filePathToSave)
        fileName=os.path.splitext(fileName)[0]
        if filePathToSave.endswith(".edit"):
            messagebox.showerror(title="Error",message="The '.edit' cannot be used as a file extension.")
        else:    
            for ext in defaultFileExtension:
                filePath=os.path.join(fileDir,f"{fileName}{ext}")
                if ext!=".edit":
                    try:
                        with open(filePath, 'w') as file:
                            file.write(scrollTextBox.get("1.0",tk.END))
                    except Exception as e:
                        messagebox.showerror(title="Error",message=e)
                else:
                    try:
                        with open(filePath, 'w') as file:
                            file.write(str(color_size_dict))
                    except Exception as e:
                        messagebox.showerror(title="Error",message=e)
    else:
        print("Canceled to save.")

def FontColor():
    fontColor=colorchooser.askcolor()[1]
    if fontColor:
        defaultColorAndSizeValue[0]=format(fontColor)
        style=ttk.Style()
        style.configure("textcolor.TButton",foreground=fontColor)
        scrollTextBox.configure(fg=fontColor)
        scrollTextBox.tag_configure("default",foreground=fontColor)
        scrollTextBox.tag_add("default","1.0","end")

def About():
    messagebox.showinfo(title="about",message="This is hw3.")
    
def UpdateFontSize(*args):
    newFontSize=selectedFontSize.get()
    if newFontSize.isdigit():
        defaultColorAndSizeValue[1]=format(newFontSize)
        newSize=f"Arial {newFontSize}"
        scrollTextBox.configure(font=newSize)

root=Tk()
root.geometry("500x500")


#menubar
menubar=Menu(root)
menubar.configure(bg="white")

#filemenu
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=New)
filemenu.add_command(label="Open",command=Open)
filemenu.add_command(label="Save",command=Save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File",menu=filemenu)

#helpmenu
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=About)
menubar.add_cascade(label="Help",menu=helpmenu)

#toolbar
frame=ttk.Frame(root,padding="100 2 100 2")
frame.pack(side=TOP,fill=X)

#toolbar button
fontColorButton=ttk.Button(frame,text="Font Color",command=FontColor,style="textcolor.TButton")
fontColorButton.grid(column=0,row=0)
#toolbar label
fontSizeLabel=ttk.Label(frame,text="Font Size")
fontSizeLabel.grid(column=1,row=0)

#toolbar combobox
fontSizeList=list(range(11,32,2))
selectedFontSize=StringVar(value=str(defaultColorAndSizeValue[1]))
selectedFontSize.trace_add("write",UpdateFontSize)
fontSizeCombobox=ttk.Combobox(frame,values=fontSizeList,textvariable=selectedFontSize)
fontSizeCombobox.grid(column=3,row=0)

#scrolled text
scrollTextBox=scrollText.ScrolledText(root,width=500,height=500,font=("Arial",str(defaultColorAndSizeValue[1])))
scrollTextBox.tag_configure("default",foreground=str(defaultColorAndSizeValue[0]))
scrollTextBox.configure(fg=str(defaultColorAndSizeValue[0]))
scrollTextBox.pack()


root.configure(menu=menubar,bg="white")
root.mainloop()