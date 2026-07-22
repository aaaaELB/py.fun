import hashlib

mensagem = input("Digite uma mensagem: ")

print(mensagem)
print(type(mensagem))

dados = mensagem.encode()

print(dados)
print(type(dados))

hash_obj = hashlib.sha256(dados)

print(hash_obj)
print(type(hash_obj))

hash_final = hash_obj.hexdigest()

print(hash_final)
print(type(hash_final))