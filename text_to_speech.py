import gtts
from playsound import playsound

# make request to google to get synthesis
text_to_speech = gtts.gTTS("Tell me why I feel like there's no way out")
# save the audio file
text_to_speech.save("no_way_out.mp3")
# play it
playsound("no_way_out.mp3")

# BG Version
# import gtts
# from playsound import playsound

# make request to google to get synthesis
# text_to_speech = gtts.gTTS("Здравейте!", lang="bg")
# save the audio file
# text_to_speech.save("no_way_out.mp3")
# play it
# playsound("no_way_out.mp3")
