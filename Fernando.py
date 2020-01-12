import gtts #gtts(google text to speech) will able use to read and
import speech_recognition as sr  #record our audio and execute commands attached to it
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gtts(text-audio, lang="en") #setting up gtts to be english
    tts.save("audio.mp3") #save our audio file in the same folder as your script is
    os.system("mpg123 audio.mp3") #this will play the audio.mp3 file with mpg123

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source: #this will use the speaker that is on your laptop by default
        print("I am ready for your next command")
        r.pause_threshold = 1 #this will give a small timer until our next command
        r.adjust_for_ambient_noise(source, duration = 1) #this is so that your speech recogniser will not pick up noise from your background
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command + "/n")

    #loop back if the speech is not recognisable

    except sr.UnknownValueError:
            assistant(myCommand())

    return command

    #if statements to execute our commands

def assistant(command):

        if "open github" in command:
            chromePath = "/Applications/Google Chrome" #This if statement will recognise when we say 'open github' and launch chrome with the url
            url = "https://github.com/login"
            webbrowser.get(chromePath).open(url)

        if "What\'s up" in command:             
            talkToMe("I am good thank you") #this willjust return a string back with "I am good thank you"


        if "Send email" in command:
            talkToMe("Who is the recipient?") #this statement will ask the user who is the recipient and take in who we say e.g. "Ryan"
            recipient = myCommand()

        if "Ryan" in recipient:
            talkToMe("What should I say?") #this statement will find the contact "Ryan" with the email below and ask what to right
            content = myCommand()

        if "Open youtube" in command:
            chromePath = "/Applications/Google Chrome"
            url = "https://www.youtube.com/?gl=GB&hl=en-GB" #this statement will open up chrome and load up the youtube url
            webbrowser.get(chromePath).open(url)

        if "What is your name" in command:
            talkToMe("My name is Fernando")

            #gmail SMTP
            mail = smtplib.SMTP("smtp.gmail.com, 587") #setting up the email transfer SMTP with gmail as that's what we will use

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #Login for gmail
            mail.login("sunnymaugin@gmail.com", "sunny12345")

            #send message
            mail.sendmail("Ryan", "ryanmauginn@gmail.com", content)

            #close connection
            mail.close()

            talkToMe("Email sent")

            talkToMe("I am ready for your next command")

while True:
    assistant(myCommand()) #this will loop so that it will ask for another command
