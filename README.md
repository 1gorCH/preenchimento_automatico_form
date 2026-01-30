# Automação Web com Selenium – Preenchimento de Formulário

Este script demonstra uma **automação de navegação web** utilizando Python e Selenium.  
O processo acessa um site, preenche campos de formulário, envia as informações e fecha o navegador automaticamente.

## 🚀 Funcionalidades
- Inicialização automática do ChromeDriver
- Acesso automatizado a página web
- Preenchimento e limpeza de campos de formulário
- Envio de dados via botão
- Encerramento automático do navegador

## 🛠️ Tecnologias Utilizadas
- Python
- Selenium
- ChromeDriver (auto-instalação)
- Google Chrome

## 🌐 Site Utilizado
- https://rpachallenge.com/

## ⚙️ Como funciona
1. Instala automaticamente o ChromeDriver compatível  
2. Abre o navegador Google Chrome  
3. Acessa o site definido  
4. Localiza elementos por **ID** e **XPath**  
5. Preenche, limpa e envia os dados do formulário  
6. Fecha o navegador ao final da execução  

## 🧩 Exemplo de Interação com Elementos
```python
navegador.find_element(By.ID, "AsMLC").send_keys("Teste")
navegador.find_element(By.ID, "AsMLC").clear()

sleep(5)
```
***Observações: O Chrome deve estar instalado na máquina; IDs e XPaths podem mudar conforme o site; Para projetos maiores, recomenda-se o uso de WebDriverWait***
