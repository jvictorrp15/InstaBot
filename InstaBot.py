from selenium import webdriver
import time

class BotInstagram():
    def __init__(self): # No método __init__, é inicializado um objeto da classe webdriver.Chrome que será utilizado para executar o navegador Google Chrome.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def entrar_link(self, link): # No método entrar_link, é utilizado o método get do objeto driver para navegar até o link especificado.
        self.driver.get(link)
    
    def login(self): # No método login, são encontrados os campos de username e senha da página de login do Instagram através do método find_element e preenchidos com as informações fornecidas pelo usuário. Em seguida, é clicado o botão de login.
        self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
        self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]/button/div').click()

    def pegar_link_das_fotos(self): # No método pegar_link_das_fotos, são encontrados todos os links da página atual do Instagram através do método find_elements. Depois, é verificado se cada um desses links começa com a string "https://www.instagram.com/p/", que indica que é um link para uma foto. Os links que correspondem a fotos são adicionados em uma lista que é retornada pelo método.
        os_links = self.driver.find_elements("tag name", 'a')
        
        todos_os_links = []
        for os_link in os_links:
            href = os_link.get_attribute("href")
            if(href.startswith("https://www.instagram.com/p/")):
                todos_os_links.append(href)
        
        return todos_os_links

    def dar_like(self): # No método dar_like, é clicado o botão de "curtir" da foto atual.
        self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/div[1]/div[1]/span[1]/button').click()

    def comentar(self, comentario): # No método comentar, é clicado o botão de "comentar" da foto atual e depois encontrado o campo de texto onde o comentário será digitado. Em seguida, o campo é limpo e preenchido com o comentário fornecido pelo usuário. Por fim, é clicado o botão de "publicar" para enviar o comentário.
        textarea = self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/div[1]/div[1]/span[2]/button')
        time.sleep(1)
        textarea.click()
        time.sleep(1)
        textarea = self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/section/div/form/div/textarea')
        time.sleep(1)
        textarea.clear()
        time.sleep(1)
        textarea.send_keys(comentario)
        time.sleep(2)
        self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/section/div/form/div/div[2]/div').click() 

username = input(print("Qual o seu login?"))
senha = input(print("Qual a sua senha?"))
comentario = input(print("Qual o comentario você quer fazer?"))

bot = BotInstagram() # Cria uma classe BotInstagram que contém métodos para entrar em um link, fazer login, pegar links de fotos, dar like e comentar em fotos.

bot.entrar_link("https://www.instagram.com/")
time.sleep(5)

bot.login()
time.sleep(10)

bot.entrar_link("https://www.instagram.com/explore/tags/python/") #
time.sleep(10)

links_fotos = bot.pegar_link_das_fotos()
print(links_fotos)

for link_foto in links_fotos:
    bot.entrar_link(link_foto)
    time.sleep(3)
    bot.dar_like()
    time.sleep(3)
    bot.comentar(comentario)
    time.sleep(3)

time.sleep(30)
