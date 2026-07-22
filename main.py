import func

user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if func.verificar_senha(user, senha):
    print("Login bem-sucedido!\n")
else:
    criar_conta = input("Login ou senha incorretos.\nDeseja criar uma conta? (s/n): ")

if criar_conta.lower() == 's':
    func.criar_conta(user, senha)
    print("Conta criada com sucesso!")
