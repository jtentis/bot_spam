from bs4 import BeautifulSoup
import requests 
import pyautogui
import time

# Bot de spam a partir de um site, puxando pelo html.
# Essa é a função de spam, que tem 2 parametros: url e tag.
def bot_spam(url, tag):
    time.sleep(5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag) #pegar no site tudo que tem a tag selecionada
    print(html)

    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press("enter")
        time.sleep(1)

bot_spam('https://www.mensagens10.com.br/mensagens-de-bom-dia', 'p')
    
