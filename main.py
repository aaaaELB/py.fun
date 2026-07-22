import func


print('Bem-vindo ao sistema!\n')
print('1 - Realizar login.')
print('2 - Cadastrar novo usuário.')
print('3 - Apagar login.')
print('4 - Alterar senha.')
print('5 - Sair do sistema.\n')
input_usuario = input()

if input_usuario == '1':
    user = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if func.verificar_senha(user, senha):
        print("\nLogin bem-sucedido!\n")
    else:
        print("\nLogin ou senha incorretos.\n")

elif input_usuario == '2':
        func.criar_conta()
        print("Conta criada com sucesso!")

elif input_usuario == '3':
    func.apagar_login()

elif input_usuario == '4':
    func.alterar_senha()

elif input_usuario == '5':
    print("Saindo do sistema...")
    exit()