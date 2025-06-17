import getpass
USUARIO_CORRETA = "Allany"

while True:
    Usuario = input("Digite a senha:")
    if Usuario == USUARIO_CORRETA:
        print("Login Bem-Sucedido! Bem-vindo(a)")
        break
    else:
        print("Senha incorreta. Tente novamente")

while True:
    print("\n Ola Kauan bem vindo Windows 11, vc pode fazer por vc??")
    print("1.Need for Speed Most Wansted")
    print("2.Visual Studio Code")
    print("3.Xbox")
    print("4.Spotify")
    print("5.Google")
    print("6.Desligar")
    escolha= input("Escolha uma opçao (1,2,3,4,5 ou 6):")

    if escolha == "1":
        print("Tou entrando no Jogo ")
    elif escolha == "2":
        print("Vc estar acessando o Visual Studio Code")
    elif escolha == "3":
        print("Vc estar entrando no Xbox")
    elif escolha == "4":
        print("Vc esta entrando no Spotify")
    elif escolha == "5":
        print("Vc esta entrando no Google")
    elif escolha == "6":
        print("Desligando o computador")
        break
    else:
        print("Opçao Invalida!!")
