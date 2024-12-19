from tkinter import *
from tkinter import ttk,scrolledtext
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox


openTextFile=""
contents=""
defaultFileExtension=[".txt",".hist"]
searchHistoryKeyWord=[]
searchHistoryKeyWordCount=[]
searchHistoryDict={}


def New():
    scrolledTextForLoadFile.delete("1.0","end")
    scrolledTextForSearchHistory.delete("1.0","end")
    bookTitle.config(text="Book Title")
    bookInfo.config(text="Book Info.")
    searchHistory.config(text="Search History")
    searchResults.config(text="Search Results")
    searchedWord.set("")
    
def Open():
    global openTextFile
    global contents
    global fileDir
    global fileName
    #to clear previous open file contents
    New()
    openTextFile=askopenfilename(
        title="Open file",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if openTextFile:
        fileDir,fileName=os.path.split(openTextFile)
        fileName=os.path.splitext(fileName)[0]
        
        for ext in defaultFileExtension:
            filePathToOpen=os.path.join(fileDir,f"{fileName}{ext}")
            if ext==".txt":
                try:
                    with open(str(filePathToOpen),"r") as file:
                        contents=file.read()
                        lengthOfText=len(contents)
                        countOfWord=len(contents.split())
                        scrolledTextForLoadFile.delete("1.0","end")
                        scrolledTextForLoadFile.insert("insert",contents)
                        bookTitle.config(text=fileName)
                        bookInfo.config(text=f"Length of the text: {lengthOfText}\n Count of words: {countOfWord}")
            
                except Exception as e:
                    messagebox.showerror(title="file opening warning",message=e)
            else:
                try:
                    with open(filePathToOpen,"r") as file:
                        historyText=file.read()
                        searchHistory.config(text=historyText)
                except Exception as e:
                    messagebox.showerror(title="file opening warning",message="Previous search history not found")
        
       
def Search(event=NONE):
    global openTextFile
    global contents
    global searchHistoryDict
    if openTextFile!="" and searchedWord.get()!="":
        word=searchedWord.get()
        sentenceCount=0
        scrolledTextForSearchHistory.delete("1.0","end")
        sentenceList=[]
        for sentence in contents.split('\n'):
            if word.lower() in sentence:
                sentenceCount+=1
                sentenceList.append(sentence +"\n")
        # print(f"Sentence Count =>{sentenceCount}")
        searchHistoryKeyWord.append(word)
        searchHistoryKeyWordCount.append(sentenceCount)
        searchHistoryDict=dict(zip(searchHistoryKeyWord,searchHistoryKeyWordCount))
        searchHistory.config(text=searchHistoryDict)
        
        if sentenceCount==0:
            messagebox.showerror(title="search error",message=f"No matching sentence is found for {word}")
        else:
            searchResults.config(text=f"{sentenceCount} sentences were found.")
            for content in sentenceList:
                scrolledTextForSearchHistory.insert("insert",content+"\n")
        
    else:
        messagebox.showerror(title="search error",message="no search keyword or no text to search")
    
def Save():
    if searchHistoryDict:
        pathToSave=os.path.join(fileDir,f"{fileName}{defaultFileExtension[1]}")
        try:
            # print(str(searchHistoryDict))
            # print(str(openTextFile))
            # print(str(pathToSave))
            with open(pathToSave,'w') as file:
                file.write(str(searchHistoryDict))
                messagebox.showinfo(title="save history",message=f"The search history has been successfully saved at {pathToSave}")
        except Exception as e:
            messagebox.showerror(title="Error",message=e)
    else:
        messagebox.showerror(title="history saving warning",message="No contents found.")

root=Tk()
root.geometry("1100x800")
root.minsize(600,500)
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)

#Menubar
menubar=Menu(root,background="white")
#file menu
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=New)
filemenu.add_command(label="Open",command=Open)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(menu=filemenu,label="File")

#history menu
historymenu=Menu(menubar,tearoff=0)
historymenu.add_command(label="Save",command=Save)
menubar.add_cascade(menu=historymenu,label="History")

#FrameOne 5row/2column
frameOne=ttk.Frame(root,padding=10)
frameOne.grid(row=0,column=0,sticky="news")
for i in range(5):
    frameOne.grid_rowconfigure(i, weight=1)
for j in range(2): 
    frameOne.grid_columnconfigure(j, weight=1)
    
    
bookTitle=ttk.Label(frameOne,text="Book Title")
bookTitle.grid(column=0,row=0,padx=50,pady=50)
bookInfo=ttk.Label(frameOne,text="Book Info.")
bookInfo.grid(column=0,row=1,padx=50,pady=50)
searchHistory=ttk.Label(frameOne,text="Search History")
searchHistory.grid(column=0, row=2,padx=50, pady=50)

searchedWord=StringVar()
searchBox=ttk.Entry(frameOne,width=20,textvariable=searchedWord)
searchBox.grid(column=0, row=3,sticky="news")
searchBox.bind("<Return>",Search)

searchButton=ttk.Button(frameOne,width=15,text="Search",command=Search)
searchButton.grid(column=1, row=3,sticky="news")  
searchResults=ttk.Label(frameOne,text="Search Results")
searchResults.grid(column=0,row=4,padx=50,pady=50)

#FrameTwo 2row/2column
frameTwo=ttk.Frame(root,padding=10)
frameTwo.grid(row=0,column=1,sticky="news")
frameTwo.grid_rowconfigure(1, weight=1) 
frameTwo.grid_rowconfigure(2, weight=1) 
frameTwo.grid_columnconfigure(1, weight=1)

#Two scrolledText
scrolledTextForLoadFile=scrolledtext.ScrolledText(frameTwo)
scrolledTextForLoadFile.grid(column=1,row=1,padx=5, pady=5,sticky="news")
scrolledTextForSearchHistory=scrolledtext.ScrolledText(frameTwo)
scrolledTextForSearchHistory.grid(column=1,row=2,padx=5, pady=5,sticky="news")




root.config(menu=menubar,bg="lightgray")
root.mainloop()