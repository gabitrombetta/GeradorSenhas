import functions

print(f'''
    Qual será o tipo da senha?
    [ 1 ] Somente números
    [ 2 ] Somente letras
    [ 3 ] Letras e números
    [ 4 ] Letras, números e pontuação
    ''')
tipoSenha = int(input("Escolha uma opção: "))

while (tipoSenha < 1 or tipoSenha > 4):
    print("OPÇÃO INVÁLIDA")
    tipoSenha = int(input("Escolha uma opção: "))

qtdSenha = int(input("Informe quantas senhas você quer gerar: "))

tamanhoSenha = int(input("Informe quantos caracteres a senha terá: "))

if (tipoSenha == 1):
    functions.SenhaNumerica(qtdSenha, tamanhoSenha)
elif (tipoSenha == 2):
    functions.SenhaLetras(qtdSenha, tamanhoSenha)
elif (tipoSenha == 3):
    functions.SenhaAlfanumerica(qtdSenha, tamanhoSenha)
elif (tipoSenha == 4):
    functions.SenhaAlfanumericaEPontuacao(qtdSenha, tamanhoSenha)