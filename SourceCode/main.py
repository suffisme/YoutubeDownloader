# importing tkinter as main file
import tkinter as tk

# importing tkinter fonts separately to change fonts family and size of text used in screens  
import tkinter.font as font

import time

# for taking data from clipboard (removed here)
'''
import win32clipboard
'''

# most important library used here, pytube which creates an API for connecting python to youtube server
from pytube import YouTube

#Starting Screen

def message_from_author():
	msg = '''
**************************
***** Welcome To My ******
********* Mini ***********
*** Youtube Downloader ***\t**************************
**************************\t**** Download Youtube ****
                          \t********* In HD **********
**************************\t**************************
******** CREATOR *********
*** Mohd Sufiyan Ansari***
**************************

'''
	print(msg)
	time.sleep(1)

#This functions is called upon when you hit the search button

def clip_board():
	# to get link entered in search box
	link = video_link.get()
	# checking if file can be downloaded
	try:
		# creating a global variable yt, so as to use in some other functions
		global yt
		yt = YouTube(link)
		# yt variable will contains the video info, working as an instancs
		# to youtube

		# yt.title gives main title you searched and yt_title will store it
		yt_title = tk.Label(window,text='Title :'+yt.title)

		# if video is found i.e. try case ran then download button is popped up clicking which will transfer to 'download_file' function 
		download_button = tk.Button(window,text='Download Now', command = download_file)

		# adding youtube video title and button on the screen on different rows
		# sticky = 'we' means text will be horizonatlly and centred aligned
		yt_title.grid(row=2,column=0,sticky='we')
		download_button.grid(row=3,column=0)
	# if file was not found or link was wrong then raise an error
	except Exception as e: 
	    # print this message on console
	    lbl_console_message['text'] = "Error"+e


# if above try case ran successfully and then download_file
# function will be called 
def download_file():
	# SAVE_PATH_DIR variable to hold path where videos will be downloaded
	SAVE_PATH_DIR = "./videos/"

	# message before downloading on console
	lbl_console_message['text'] = 'Downloading--- '+yt.title+' into location : '+SAVE_PATH_DIR

	'''
		NOW COMES THE BEST PART FORMAT AND  DOWNLOADING
		THERE ARE MANY ITAGS WHICH DENOTES THE FORMAT AND QUALITY
		FIND THE FILE itags.txt WHERE YOU WILL GET TO KNOW DIFFERENT
		ITAGS FOR DIFFERENT FORMATS

		Here itag is used as 135 which is for 480p mp4
		and 136 itag is for 720p mp4
	'''
	#creating an instance of streams and taking format through itag
	itag = 135
	stream = yt.streams.get_by_itag(itag)

	# downloading the file on the required path
	stream.download(SAVE_PATH_DIR)

	# after downloading, printing success message from console
	lbl_console_message['text'] = 'Download Successful'

	'''
	yt.streams.all() contains all the available format
	'''
	

# FIRST SCREEN FROM PYTHON
message_from_author()

# tkinter init
window = tk.Tk()

# Title for the tkinter window
window.title('Youtube Downloader - Created By Sufiyan')
# Configuring Window
window.rowconfigure([0,1,2,3,4,5],weight=1)
window.columnconfigure(0,weight=1,minsize=500)

# Creating Label for HEADING on the main window
label_head = tk.Label(window,text='YouTube Downloader',bg="#333",fg="#ff3333")
head_font = font.Font(family='Arial',size=30,weight='bold')
label_head['font'] = head_font
# Adding the label to the screen on top
label_head.grid(row=0,column=0,pady=10,padx=10,sticky='we')

# Creating multiple FRAMES (for different widgets) under window as master frame

# Main_frame will contain search box and search button
main_frame = tk.Frame(window)

# As name indicates this frame is for console message during process
console_frame = tk.Frame(window)

# Footer frame for containing my contact details
contact_frame = tk.Frame(window)

# Configuring main_frame containing search box in 1st column and search button in 2nd one
main_frame.rowconfigure(0,weight=1)
main_frame.columnconfigure(0,weight=1,minsize=400)
main_frame.columnconfigure(1,weight=1,minsize=20)

#Configuring Console_frame containing heading and message
console_frame.columnconfigure(0,weight=1,minsize=30)
console_frame.columnconfigure(1,weight=1,minsize=180)

# The default link that search box will contain
default_link = 'https://www.youtube.com/watch?v=668nUCeBHyY'

# Creating Search box in main_frame
video_link = tk.Entry(main_frame)
video_link.insert(0,default_link)

# Adding video_link to the frame
video_link.grid(row=0,column=0,ipadx=5,ipady=5,sticky='we',padx=5,pady=5)


# Creating and adding search button in main_frame
# Clicking this will trigger clip_board function
search_button = tk.Button(main_frame,text='Search',command=clip_board)
search_button.grid(row=0,column=1,ipadx=5,ipady=5,sticky='we',padx=5,pady=5)
# Adding main_frame to the window on the 2nd row
main_frame.grid(row=1,column=0)

# Creating console label and message to the console frame in required way
lbl_console = tk.Label(console_frame,text='Message From Server : ')
lbl_console.grid(row=0,column=0,sticky='e',ipadx=5)
lbl_console_message = tk.Label(console_frame,text='Welcome To My YT Downloader')
lbl_console_message.grid(row=0,column=1,sticky='w',ipadx=5)

# Adding console_frame to window
console_frame.grid(row=5,column=0,pady=10)

# Creating and adding label containing Contacts in contact frame
lbl_contact = tk.Label(contact_frame,text='Contact Information')
lbl_contact.grid(row=0,column=0,sticky='e',ipady=10)

# The github label
lbl_contact_github = tk.Label(contact_frame,text='Github : ')
lbl_contact_github.grid(row=1,column=0,sticky='e',ipadx=5)
lbl_contact_github_message = tk.Label(contact_frame,text='https://github.com/suffisme')
lbl_contact_github_message.grid(row=1,column=1,sticky='w',ipadx=5)

# Email information
lbl_contact_email = tk.Label(contact_frame,text='Email : ')
lbl_contact_email.grid(row=2,column=0,sticky='e',ipadx=5)
lbl_contact_email_message = tk.Label(contact_frame,text='ansari_841903@student.nitw.ac.in')
lbl_contact_email_message.grid(row=2,column=1,sticky='w',ipadx=5)

# Linkedin URL
lbl_contact_Linkedin = tk.Label(contact_frame,text='Linkedin : ')
lbl_contact_Linkedin.grid(row=3,column=0,sticky='e',ipadx=5)
lbl_contact_Linkedin_message = tk.Label(contact_frame,text='https://www.linkedin.com/in/sufiyan-ansari-1823b2192/')
lbl_contact_Linkedin_message.grid(row=3,column=1,sticky='w',ipadx=5)

# Adding contact frame to window
contact_frame.grid(row=6,column=0)

# The mainloop which will take care of dynamics of programs
# Basically to start event loop
window.mainloop()

'''

THANK YOU FOR VISITING 
DO CONTACT FOR ANY FURTHER EXPLANATION

'''