# python-ai
This is the instructions file for the Virtual Assistant Friday.
First you may have to install a few modules to get the program running.They are :-

pyttsx3: pip install pyttsx3
sppech recognition : pip install SpeechRecognition
beautifulsoup 4 : pip install beautifulsoup4
google : pip install google
wikipedia : pip install wikipedia
pandas :  pip install pandas
PyPDF2 : pip install PyPDF2
pyaudio : pip install PyAudio-0.2.11-cp37-cp37m-win32

List Of Commands : 
Note : (- : means anything can come there)
- wikpedia : will search and read first two lines of wikipedia for whatever in place of '-'.
open youtube : will open youtube in a new browser tab(mention correct path for chrome in 'chrome_path' for this to work.)
open google  : will open google.com in a new browser tab(mention correct path for chrome in 'chrome_path' for this to work.)
my mail : will open gmail.com in a new browser tab(mention correct path for chrome in 'chrome_path' for this to work.)
music : will play music randomly from your selected music directory
time : will tell current time
-.com : will open the website -.com 
send mail : will send email from your account.
            Make sure that you input coorect email address and its password in server.login and server.sendmail and also turn on less secure apps for that gmail. Also,             if you want to use preset emails add them in the 'edict' dictionary.
search - : will search google for whatever it is in place of - 
audiobook : will read any pdf file you input.(the pdf file should be in the same folder as this program.)
open notepad : will open any notepad file if it is in the same folder as the program.
check for birthdays : will check if there is anyone's birthday from your birthday table in mysql. (input correct username,passwd and database name in sqlr.connect                       clause).
add birthdays : will add rows in the birthday table for further use.
quit or stop : will end the program.
