import speech_recognition as sr
import playsound
from gtts import gTTS
import openai
from IPython.display import Audio
 
 
lang = 'en'
 
openai.api_key = "your_api"

 
tts = gTTS('hello lol!')
tts.save('hello.mp3')
 
guy = ""
while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            audio = r.listen(source)
            said = ""
 
            try:
                said = r.recognize_google(audio)
                print(said)
                global guy
                guy = said
               
 
                if "Eva" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    #print(new_string)
                    completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":said}])
                    text = completion.choices[0].message.content
                    print(completion.choices[0].message.content)
                    speech = gTTS(text = text, lang=lang, slow=False, tld="co.uk")
                    speech.save("sarasvoice.mp3")
                    playsound.playsound("sarasvoice.mp3")
                    print(text)
               
                   
            except Exception:
                print(":)")
 
 
        return said
 
    if "stop" in guy:
        break
 
 
    get_adio()
 
    
    

