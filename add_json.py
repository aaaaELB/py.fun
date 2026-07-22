import json
import hashlib

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