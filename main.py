# Import the required module for text
# to speech conversion
# This module is imported so that we can
# play the converted audio
import os

from gtts import gTTS

# The text that you want to convert
mytext = 'स्वागत हे आपका VENV में!'

# Language in which you want to convert
language = 'hi'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
# os.system("mpg321 welcome.mp3")
# ```
# The above code will convert the given text to speech and create a welcome.mp3 file in the same directory. Then it will play the audio file. It is important to note that the mpg321 command is used to play the audio file. You can install the mpg321 package using the following command.
# ```bash
# sudo apt-get install mpg321
# ```
# If you are using Windows, you can use the following command to play the audio file.
# ```bash
os.system("welcome.mp3")
# ```
# The gTTS module supports multiple languages. You can pass the language as an argument to the gTTS() class. For example, if you want to convert the text to Hindi, you can use the following code.
# ```python
# mytext = 'स्वागत हे आपका गीक्स फॉर गीक्स में!'
# language = 'hi'
# ```
# The gTTS module also provides a save() method to save the audio file. You can pass the name of
