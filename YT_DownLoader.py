from tkinter import *
from tkinter import messagebox
from pytube import YouTube

path="C:/Users/Somdeep Sardar/Downloads"

root = Tk()
root.title ("!!YouTube downloader!!")
root.geometry ("500x150")

YtLink = StringVar()
label_A = Label(root, text="YTLink",width=20,font=("bold", 10)).place(x=0,y=30)

entry_A = Entry(root,textvar=YtLink, bg="green")
entry_A.place(x=120, y=30, width = 320)

def DownloadMenu():
    link = entry_A.get()
    yt = YouTube(link)
    window = Toplevel()
    window.geometry('500x350')
    window.title("Download Form")
    Label(window, text = "TTITLE", padx=5, bg="red").place(x = 230, y = 10)
    Label(window, text = yt.title, padx= 5, bg="orange").place(x = 50, y = 40)
    def VidorAud():
        if(OnlyVid.get() == 1):
            print("HIII")
            Label(window, text="Select the approrpiate resolution", bg= "blue", padx=5).place(x = 180, y = 180)
            ytRes = StringVar()
            def VidDwnld():
                stream = yt.streams.filter(progressive= True, res= ytRes)
                i = len(stream)
                stream[i-1].download(output_path= path)
                Label(window, text = "Downloaded!!").place(x = 240, y = 270)
            
            Entry(window,textvar=ytRes, bg="green").place(x=260, y=210, width=30)
            Button(window, text="Submit",width=30,bg='brown',fg='white', command=VidDwnld).place(x = 160, y =240 )
        else:
            stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4")
            i = len(stream)
            stream[i-1].download(output_path = path)
            Label(window, text = "Downloaded!!").place(x = 200, y = 180)

    Label_01 = Label(window, text = "Video or Audio only?")
    Label_01.place(x = 200, y = 70)
    OnlyVid = IntVar()
    button_01 = Radiobutton(window, text="Video",padx = 5, variable=OnlyVid, value=1).place(x=200,y=100)
    button_02 = Radiobutton(window, text="Only Audio",padx = 5, variable=OnlyVid, value=0).place(x=200,y=120)

    button_03 = Button(window, text="Submit",width=30,bg='brown',fg='white', command=VidorAud)
    button_03.place(x=160,y=150)

def on_button():
    if entry_A.get()[0] == "h":
        print(entry_A.get()[0])
        DownloadMenu()
    else  :
        messagebox.showerror("Alert!","Link denied!!")

Button(root, text="Submit",width=30,bg='brown',fg='white', command=on_button).place(x=150,y=90)
root.mainloop()