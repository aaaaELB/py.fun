import func


print('Bem-vindo ao sistema!\n')
print('1 - Realizar login.')
print('2 - Cadastrar novo usuário.')
print('3 - Apagar login.')
print('4 - Sair do sistema.\n')
input_usuario = input()
print()
while True:
    if input_usuario == '1':
        user = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        if func.verificar_senha(user, senha):
            print("\nLogin bem-sucedido!\n")
            break
        else:
            print("\nLogin ou senha incorretos.\n")
            break

    elif input_usuario == '2':
            func.criar_conta()
            print("Conta criada com sucesso!")
            break

    elif input_usuario == '3':
        func.apagar_login()
        break

    elif input_usuario == '4':
        print("Saindo do sistema...")
        exit()