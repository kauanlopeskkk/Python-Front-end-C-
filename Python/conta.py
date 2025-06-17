import getpass
USUARIO_CORRETO = "Allany"


while True:
    usuario = input("Senha: ")

    if usuario == USUARIO_CORRETO:
        print("Login bem-sucedido! Bem-vindo(a),")
        break
    else:
        print("senha incorreta. Tente novamente")


def login():
    nome_usuario = input("Digite seu nome:")
    senha = input("Digite sua senha:")

    with open("usuario.txt", "r") as arquivo:
        for linha in arquivo:
            user, passw = linha.strip().split(":")
            if user.strip() == nome_usuario and passw.strip() == senha:
                print(f"Login realizado com sucesso!")
                return True
    print("Nome de usuario ou senha incorreto")
    return False

def registrar():
    nome_usuario = input("Digite o seu nome de usuario:")
    senha = input("Digite a sua senha:")
    email = input("Digite o seu email:")
    
    with open ("usuario.txt", "a") as arquivo:
        arquivo.write(f"{nome_usuario}: {senha} \n")
def deletar():
    nome_usuario = input("Digite o seu nome:")
    senha = input("Digite sua senha:")
  
    linhas = []
    removido = False

    with open("usuario.txt", "r") as arquivo:
        for linha in arquivo:
            user, passw = linha.strip().split(":")
            if user == nome_usuario and passw.strip() == senha:
                removido = True
                continue  
            linhas.append(linha)

    # Reescreve o arquivo sem o usuário removido
    with open("usuario.txt", "w") as arquivo:
        arquivo.writelines(linhas)

    if removido:
        print(f"Usuário '{nome_usuario}' removido com sucesso!")
    else:
        print("Usuário ou senha incorretos. Nenhum usuário removido.")


while True:
    print("\nOla, O que vc gostaria de fazer?")
    print("1. Registrar")
    print("2. Login")
    print("3.Deletar")
    print("4. Sair")

    escolha = input("Escolha uma opçao (1,2,3 ou 4): ")

    if escolha == "1":
        registrar()
    elif escolha == "2":
        login()
    elif escolha == "3":
        deletar()
    elif escolha == "4":
        print("saindo do programa!!")
        break
    else:
        print("Opçao invalida.")


   

