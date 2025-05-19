#Operadores condicional
Conta_dados = 0

if Conta_dados == 0:

    print("Nome")

elif Conta_dados == 2:
    print("Email")

elif Conta_dados == 3:
    print("CPF")


elif Conta_dados == 4:
    print("Senha")

else:
    print("Opçao Invalida!!")


#Entrando A minha conta do Overwatch
email_correto="KauanLopes293@gmail.com" 
senha_correto= "232424"

email = input("Digite o Email:")
senha = input("Digite a sua Senha:")

if email_correto == email and senha_correto == senha:

    print("Vc Acessou a sua conta do Jogo")

else:

    print ("Email e Senha esta invalida!")

