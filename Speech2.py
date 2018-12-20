"""
README:
Before Running this program, please ensure that you have installed the following modules that are required to run it:
-> If you are using a Macbook : 1:)pip install SpeechRecognition # For using a microphone for speech detection:
																2:)brew install portaudio
																3:)pip install PyAudio # For using the different speech-to-text engines: We are using a google cloud based free service.
																4:)pip install PocketSpinx #for a local speech-to-text engine.

"""



import speech_recognition as sr

# This piece of code finds out the Ratio of Similarity between two different strings:
import difflib 

# For GUI: I have assumed that you have downloaded the same:
from tkinter.ttk import Progressbar
from tkinter import *

# Global Variables:
r = sr.Recognizer()
s1 = 'I like sunny days'


# Main initializer class:
class SpeechRecognizerGUI:
	# This is where we detech the speech from the microphone. Once the microphone detects a sound, it sends it to google cloud where it is returned as Human understandable langauge.

	def clicked(self):
		
		# Sort of a progress bar: Doesnt work that great.
		self.bar['value']=0

		with sr.Microphone() as source:

			# This is where the code tells the system to listen to the sound. Please use a system that has a microphone enabled. I am using a laptop and there is no issue on my side.

			audio = r.listen(source)
			self.bar['value']=100
			try:
				# Here the audio is being passed to the Google Cloud Service for Speech to Text recognition
				s2 = r.recognize_google(audio)

			except sr.UnknownValueError:
				s2 = "Speech Recognition could not understand audio"
			except sr.RequestError as e:
				s2 = 'Could not request results from Speech Recognition service'

		# Display what you have heard from the user:
		self.label3.configure(text= "You said "+s2)

		# Find out the similarity of the two strings that we have got.
		ratio = difflib.SequenceMatcher(None,s1,s2).ratio()

		# Display the similarity of the two strings.
		self.label4.configure(text='You matched {0}% with {1}'.format(ratio*100,s1))

	def __init__(self,master):
		
		# In this class we are initializing all the GUI Elements of the TKinter window: Please ensure that you have installed that correctly
		
		self.master = master
		master.title("Welcome to EncycloJobs")
		master.geometry('400x200')

		self.label1 = Label(master, text="Please click the button and say the following sentence")
		self.label1.grid(column=0, row=0)

		self.label2 = Label(master,text=s1)
		self.label2.grid(column=0,row=1)

		self.label3 = Label(master,text='')
		self.label3.grid(column=0, row=4)

		self.label4 = Label(master,text='')
		self.label4.grid(column=0,row=5)

		self.bar = Progressbar(master, length=200)
		self.bar.grid(column=0,row=2)
		self.bar['value']=0

		btn = Button(master, text="Click Me", command=self.clicked)
		btn.grid(column=0, row=3)

root = Tk()
my_gui = SpeechRecognizerGUI(root)
root.mainloop()

