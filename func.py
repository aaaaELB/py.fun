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