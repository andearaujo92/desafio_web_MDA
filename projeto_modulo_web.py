from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
import time
import random
from selenium.webdriver.common.keys import Keys

class ProjetoModulo3:

    def __init__ (self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe',options=chrome_options)
        self.driver.get('https://cursoautomacao.netlify.app/')
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[

                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )
    def Iniciar (self):

        def EscolherRadioButton():
            usuario_digita = input('Digite qual o sistema operacional')
            entrada_do_usuario = usuario_digita.capitalize()

            radio_button = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,f'//input[@id="{entrada_do_usuario}RadioButton"]')))
            self.driver.execute_script('arguments[0].click()',radio_button)


        def DeixarComentario():
            comentario_do_usuario = input('Digite o comentário que deseja deixar ná página')

            area_de_comentario = self.driver.find_element_by_xpath('//textarea [@placeholder="digite seu texto aqui"]')
            time.sleep(3)    
            self.driver.execute_script('arguments[0].click()',area_de_comentario)

            DigiteComoUmaPessoa(self, area_de_comentario, comentario_do_usuario)    

        def DigiteComoUmaPessoa(self, elemento, texto):
            for letra in texto:
                elemento.send_keys(letra)
                time.sleep(random.randint(1,5)/20)

        def NivelAcesso():
            try:  
                nivel = input('''Quais níveis deseja liberar? (digite-os separado por vírgula)''')
                niveis_desejados = nivel.split(',')

                for nivel_desejado in niveis_desejados:
                    checkbox = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,f'//input[@id="acessoNivel{nivel_desejado}Checkbox"]')))
                    self.driver.execute_script('arguments[0].click()',checkbox)
            except:
                print('Digite um nível de acesso válido')
                         

        EscolherRadioButton()
        DeixarComentario()
        NivelAcesso()            


projeto_web = ProjetoModulo3()
projeto_web.Iniciar()