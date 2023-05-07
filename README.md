# InstaBot
O código é uma implementação de um bot para interagir com o Instagram usando a biblioteca Selenium em Python, realizando login, navegando por hashtags e realizando ações como curtir e comentar em fotos.

--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--

Esse é um código em Python que utiliza a biblioteca Selenium para automatizar interações com o Instagram. Ele cria uma classe BotInstagram que contém métodos para entrar em um link, fazer login, pegar links de fotos, dar like e comentar em fotos.

No método __init__, é inicializado um objeto da classe webdriver.Chrome que será utilizado para executar o navegador Google Chrome.

No método entrar_link, é utilizado o método get do objeto driver para navegar até o link especificado.

No método login, são encontrados os campos de username e senha da página de login do Instagram através do método find_element e preenchidos com as informações fornecidas pelo usuário. Em seguida, é clicado o botão de login.

No método pegar_link_das_fotos, são encontrados todos os links da página atual do Instagram através do método find_elements. Depois, é verificado se cada um desses links começa com a string "https://www.instagram.com/p/", que indica que é um link para uma foto. Os links que correspondem a fotos são adicionados em uma lista que é retornada pelo método.

No método dar_like, é clicado o botão de "curtir" da foto atual.

No método comentar, é clicado o botão de "comentar" da foto atual e depois encontrado o campo de texto onde o comentário será digitado. Em seguida, o campo é limpo e preenchido com o comentário fornecido pelo usuário. Por fim, é clicado o botão de "publicar" para enviar o comentário.

No programa principal, é solicitado ao usuário que informe o seu username, senha e o comentário que deseja fazer nas fotos. Depois, é criado um objeto BotInstagram e são realizadas as seguintes ações:

Navegar até a página inicial do Instagram e fazer login.
Navegar até a página de fotos que estão marcadas com a hashtag #python e pegar os links dessas fotos.
Para cada link de foto, navegar até a página da foto, dar like e fazer um comentário com o texto informado pelo usuário.
No final, o programa espera 30 segundos antes de encerrar a execução.
