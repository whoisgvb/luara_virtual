import speech_recognition as sr
from subprocess import call # Mac / Linux

import sys, requests
import webbrowser
argument = sys.argv

with open('luaravirtual-37b4ea7a626d.json') as credencialGoogle:
  credencialGoogle = credencialGoogle.read()


def audioMicrofone():
  hotword = 'luara'
  microfone = sr.Recognizer()
  with sr.Microphone() as source:
    while True:
      print('[ + ] Aguardando fala: ')
      audio = microfone.listen(source)

      try:
        trigger = microfone.recognize_google_cloud(audio, credentials_json=credencialGoogle, language='pt-BR')
        trigger = trigger.lower()

        if hotword in trigger:
          # print(trigger)
          pesquisa = trigger.lstrip(hotword)
          resposta('abrenavegador')
          url = 'https://www.google.com.tr/search?q='+ pesquisa
          webbrowser.open_new_tab(url)
          break

      except sr.UnknownValueError:
        print('Nao entendi o audio :(')
      except sr.RequestError as e:
        print('Erro com a api {0}'.format(e))
    
  return trigger
  
    

def resposta(arquivo):
  call(['afplay', 'audio/'+arquivo+'.mp3']) # Mac

def main():
  audioMicrofone()

main()


#jogar a funçao cria audio aqui
#transcrever o que eu falei pro mp3
