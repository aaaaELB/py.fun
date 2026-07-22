import hashlib
import json

def verificar_senha(user, senha):
    # Verifica a senha no banco de dados (simulado no arquivo json)
    with open('D:\\Codes\\py.fun\\usuarios.json', 'r') as f:
        usuarios = json.load(f)

    salt = "brawl"

    hash_senha = hashlib.sha256((senha + salt).encode('utf-8')).hexdigest()

    for usuario in usuarios["usuarios"]:
        if usuario['user'] == user and usuario['senha'] == hash_senha:
            return True
    return False

def criar_conta():

    while True:
        user = input("Digite o nome do novo usuário: ")
        with open('D:\\Codes\\py.fun\\usuarios.json', 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
        if any(usuario['user'] == user for usuario in usuarios["usuarios"]):
            print("Usuário já existe. Tente outro nome.")
        else:
           break

    while True:
       senha = input("Digite a senha do novo usuário: ")
       confirmar_senha = input("Confirme a senha: ")
       if senha == confirmar_senha:
           break
       else:
           print("As senhas não coincidem. Tente novamente.")

    salt = "brawl"
    hash_senha = hashlib.sha256((senha + salt).encode('utf-8')).hexdigest()

    usuarios["usuarios"].append({"user": user, "senha": hash_senha})

    with open('D:\\Codes\\py.fun\\usuarios.json', 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)

def apagar_login():
    user = input("Digite o nome do usuário a ser removido: ")
    with open('D:\\Codes\\py.fun\\usuarios.json', 'r', encoding='utf-8') as f:
        usuarios = json.load(f)

    for i in usuarios["usuarios"]:
        if i['user'] == user:
            senha = input("Digite a senha do usuário a ser removido: ")
            if hashlib.sha256((senha + "brawl").encode('utf-8')).hexdigest() == i['senha']:
                usuarios["usuarios"].remove(i)
                with open('D:\\Codes\\py.fun\\usuarios.json', 'w', encoding='utf-8') as f:
                    json.dump(usuarios, f, indent=4)
                print("Usuário removido com sucesso.")
                return
            else:
                print("Senha incorreta. Não foi possível remover o usuário.")
                return