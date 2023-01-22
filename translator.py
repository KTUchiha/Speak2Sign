import streamlit as st
import whisper
from audiorecorder import audiorecorder
import whisper
from PIL import Image
import re
import pandas as pd
import os
from io import StringIO


#dict of letters and their photos for version 1
letters={'A':'A.png','B':'B.png','C':'C.png','D':'D.png','E':'E.png','F':'F.png','G':'G.png','H':'H.png','I':'I.png','J':'J.png','K':'K.png','L':'L.png','M':'M.png','N':'N.png','O':'O.png','P':'P.png','Q':'Q.png','R':'R.png','S':'S.png','T':'T.png','U':'U.png','V':'V.png','W':'W.png','X':'X.png','Y':'Y.png','Z':'Z.png'}
st.title("Speak2Sign")
#extra info
with st.expander('What is Speak2Sign?'):
	st.write("""Speak2Sign is a web app created to help those who use ASL. Speak2Sign can be used
	by those who are hard of hearing to translate audio into American Sign Language. It can also be used by a user that
	is communicating with someone who uses ASL. 
	""")
with st.expander('How do I use Speak2Sign?'):
	st.write(""" To use Speak2Sign, click on the record button and play your audio. To stop recording, click on the 
		button again. Watch as your audio is converted into an ASL video. Your audio is also spelt out in ASL below """)
banner=Image.open('banner.png')
st.image(banner)

#upload a file
#does not work yet, want to improve in the future
uploaded_file = st.file_uploader("Choose an audio file")
if uploaded_file is not None:
    model = whisper.load_model("base")
    result = model.transcribe(uploaded_file)
    x=result["text"].upper()
    words=re.sub('[^A-Z ]','',x)
    st.write(f'### {words}')


audio = audiorecorder("Click to translate", "Recording...")

#records audio
if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())
#whisper from Open AI
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
x=result["text"].upper()
words=re.sub('[^A-Z ]','',x)
st.write(f'### {words}')

words_for_video=words.lower()
df=pd.read_csv('small/new_words.txt')
df=df.set_index('word')
#this function gets the path of the video for each word
def get_video(word):
    try:
        path=df.loc[word]['id']
    except:
        path=df.loc['hello']['id']
    #path='small/'+ str(path) +'.mp4'
    return path
#takes a word and returns video name
def make_video(x):
    list_of_paths=[]
    w=x.split(' ')
    for word in w:
        list_of_paths.append(get_video(word))
    return combine_paths(list_of_paths)
        
#takes list of paths and concatanates the video 
# adds the concatenated video to files.txt
def combine_paths(paths):
    with open("files.txt","w") as f:
        for path in paths:
            f.write(f"file '{path}' \n" )
    os.system('ffmpeg -f concat -i files.txt -y -c copy output.mp4')
    return 'output.mp4'


#plays video
video_file = open(make_video(words_for_video), 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

### THIS IS THE FIRST ITERATION PART OF THE APP
lst_of_letters=[]
for i in words:
	lst_of_letters.append(i)
#for letter in lst:
	#image=Image.open(lst_of_letters[letter])
	#st.image(image,width=60)

counter=0
i=0
cols = st.columns(10)
#Creating columns and looping through them to add the ASL photos
while i < 10 and counter < len(lst_of_letters) :
	if lst_of_letters[counter]==' ':
		i=0
		counter=counter+1
		cols = st.columns(10)
		continue 

	image=Image.open(lst_of_letters[counter]+'.png')
	image=image.resize((70,90))
	cols[i].image(image)
	with cols[i]:
		st.write(lst_of_letters[counter])
	counter=counter+1
	i=i+1


