from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

class whatsappBot:
    def __init__(self):
        self.mensagem = "Teste Bot"
        self.grupos = ["TESTE"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagem(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)

            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)

            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)


bot = whatsappBot()
bot.EnviarMensagem()