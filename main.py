import func

user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if func.verificar_senha(user, senha):
    print("Login bem-sucedido!")
else:
    print("Login ou senha incorretos.")