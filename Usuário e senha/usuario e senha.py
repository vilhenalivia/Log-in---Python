# Usuário e senha pré definidos
usuario = "Admin"
senha = 123456789

# Entrada do usuário
entrada_usuario = input("\nDigite o nome de usuário: ")
entrada_senha = int(input("Digite a senha: "))

# Condicionais de verificação
if entrada_usuario == usuario and entrada_senha == senha:
    print("\nAcesso aceito")
else:
    print("\nAcesso recusado. Tente novamente!")

