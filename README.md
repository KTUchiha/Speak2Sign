# Speak2Sign
An Speech to ASL translating app!
## Inspiration
About 70 million people in the world use sign language as their first language. When I first heard this I was astonished! There are almost 70 million people who use sign language to communicate but most people do not know sign language. Most TV shows, podcasts, and announcements completely overlook this group of people. I was inspired to create to Speak2Sign because I wanted to make daily life easier for those who are hard of hearing.

## What it does
Speak2Sign takes an audio input and translates it into 2 types of sign language. First, it shows the user a video of someone signing the audio and then it also shows each specific letter signed out. The user can record announcements, conversations and even upload podcasts to translate.

## How I built it
To build Speak2 Sign I used OpenAI's Whisper text-to-speech model. Then I downloaded a dataset of about 1200 most common words and their respective ASL videos. Using python I located the ASL videos for each word. Then I used the ffmpeg software to concatenate the videos into one video. The first iteration of my app uses ASL pictures for each letter and displays them below.  For the UI I used python's streamlit package which was very wonderful and easy to use! Currently, Speak2Sign uses NO APIS and I have run everything on my computer!
## Challenges I ran into
Creating Speak2Sign was a journey full of many challenges! Gunn Hacks was my first Hackathon so it was a completely different experience. Firstly downloading the Whisper text-to-speech model on my laptop was a struggle. I had to download much other software to get the text-to-speech working. Then, I struggled with formatting all the ASL photos into neat columns. I spent many hours formatting them nicely. Lastly, the dataset of ASL videos that I used turned out to be corrupted and I had to spend a lot of time removing videos from the dataset.

## Accomplishments that I'm proud of
I am so proud to have Speak2Sign working! I'm so proud of concatenating all the videos properly and displaying the sign language photos neatly below.

## What I learned
I learned how to see a project from start to finish in only 24 hrs! I learned a lot of time management and perseverance. During the hackathon, I realized that I could not code for perfection but I had to make sacrifices. I also learned a lot about combining videos using ffmpeg and formating in Streamlit!

## What's next for Speak2Sign
Currently Speak2Sign uses a very limited dataset, in the future I would like to use a larger more complete dataset. Also, Speak2Sign does not account for the small grammar differences between English and ASL which makes it difficult to translate extremely large conversations.

## How to use
To use download the ASL Video dataset from Kaggle.
Also, download all the specific letter photos from Kaggle.
