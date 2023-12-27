from gtts import gTTS 

text = 'Exemplo de texto gerado em Python'

gtts_object = gTTS(text, lang='pt', tld='com.br', slow=False)

gtts_object.save('audio.mp3')

