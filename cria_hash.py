# praticar hash SHA-256
import hashlib

def hash_sha256(entrada, saida, salt):
# Recebe uma string e transforma em hash SHA-256, em bytes ou hexadecimal, dependendo do pedido do usuário.    
    if saida == 'bytes':
        return hashlib.sha256((entrada + salt).encode('utf-8')).digest()
    
    if saida == 'hex':
        return hashlib.sha256((entrada + salt).encode('utf-8')).hexdigest()

mensagem = input("Digite uma mensagem: ")
salt = input("Digite um salt (uma string aleatória para aumentar a segurança da senha): ")
while True:
    modo = input("Escolha o modo de saída (bytes ou hex): ")
    if modo != 'bytes' and modo != 'hex':
        print("Modo inválido.")
    else:
        break

hash = hash_sha256(mensagem, modo, salt)

print(f'Sua mensagem em SHA-256:\n  {hash}')