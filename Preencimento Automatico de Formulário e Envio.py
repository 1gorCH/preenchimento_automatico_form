# https://selenium-python.readthedocs.io/index.html

from selenium import webdriver
import chromedriver_autoinstaller

from selenium.webdriver.common.by import By 
from time import sleep
from selenium.webdriver.common.keys import Keys

# Instalação automática do ChromeDriver (commicação entre cod e navegador)
chromedriver_autoinstaller.install()

# Inicializar o navegador Chrome
navegador = webdriver.Chrome()

# Exemplo: abrindo paginas Web
Link = "https://rpachallenge.com/"
navegador.get(Link)

sleep(5) # tempo de espera da pagina

# %%
empresa = navegador.find_element(by= By.ID,value="AsMLC").send_keys("Teste")

# %%
empresa = navegador.find_element(by= By.ID,value="AsMLC").clear()

# %%
papelcompania = navegador.find_element(by= By.XPATH,value='//*[@id="ff0iT"]')
papelcompania.send_keys("Industrial")



# %%
sobrenome = navegador.find_element(by= By.XPATH,value='//*[@id="g6aFX"]')
sobrenome.send_keys("Alves")


# %%
Enviar = navegador.find_element(by= By.XPATH,value='/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
Enviar.click()


# %%
sleep(5) # tempo de espera da pagina
navegador.quit()


