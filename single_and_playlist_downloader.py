import tkinter

import customtkinter
from pytube import Playlist, YouTube


def startDownload():
    try:
        ytLink=link.get()
        ytObject=YouTube(ytLink,on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title,text_color="white")
        finishedLabel.configure(text="")
        video.download('C:/Users/USER/Downloads')
        finishedLabel.configure(text="Downloaded!") 
    except:
        finishedLabel.configure(text="Download Error",text_color="red")


# download function for playlist
counter=0
totalVideo=0
def startPlaylistDownload(singleVideo):
    try:
        ytLink=f'{singleVideo}'
        ytObject=YouTube(ytLink,on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        count_title2.configure(text=f"Total:{totalVideo} and Complete:{counter}",text_color="white")
        title2.configure(text=ytObject.title,text_color="white")
        finishedLabel2.configure(text="")
        video.download('C:/Users/USER/Downloads')
        finishedLabel2.configure(text="Downloaded!") 
        counter+=1
    except:
        finishedLabel.configure(text="Download Error",text_color="red")



# progress bar 

def on_progress(stream,chunk,bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage_of_completion=bytes_downloaded/total_size*100
    per=str(int(percentage_of_completion))
    pPercentage.configure(text=per+'%')
    pPercentage.update()

    # update progress
    progressBar.set(float(percentage_of_completion)/100)



# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#Our app frame
app=customtkinter.CTk()
app.geometry("720X480")
app.title("Youtube Downloader")

# Adding ui elements
title=customtkinter.CTkLabel(app,text="Insert a single youtube link")
title.pack(padx=10,pady=10)



# link input
url_var=tkinter.StringVar()
link= customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack() 



# finished download
finishedLabel=customtkinter.CTkLabel(app,text="")
finishedLabel.pack()




# Download button
download=customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)



# progress percentage
pPercentage=customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar=customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

# """ ############################
#                                 #
# For playlist download          #
#                               #
#  """###########################

# Adding ui elements
title2=customtkinter.CTkLabel(app,text="Insert a youtube playlist link")
title2.pack(padx=10,pady=10)

# link input
url_var2=tkinter.StringVar()
link2= customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var2)
link2.pack() 



def playListDownload():
    playlist = Playlist(f'{link2.get()}')
    totalVideo=len(playlist.video_urls)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video_url in playlist.video_urls:
        # print(video_url)
        startPlaylistDownload(video_url)
        

# Download button
download2=customtkinter.CTkButton(app,text="Download",command=playListDownload)
download2.pack(padx=10,pady=10)


# Adding ui elements
# count_title2=customtkinter.CTkLabel(app,text=f"Total:{totalVideo} and Complete:{counter}")
# count_title2.pack(padx=10,pady=10)
count_title2=customtkinter.CTkLabel(app,text=f"Total:{totalVideo} and Complete:{counter}")
count_title2.pack(padx=10,pady=10)
# finished download
finishedLabel2=customtkinter.CTkLabel(app,text="")
finishedLabel2.pack()



#Run app
app.mainloop()







# playlist.download_all()