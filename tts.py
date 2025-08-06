from gtts import gTTS

text_to_say = input("Digite qual texto que quer que seja lido: ")

language = "en"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("gtts.wav")

