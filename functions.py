import random, string

def SenhaNumerica(qtdSenha, tamanhoSenha):
    print("====SENHAS GERADAS====")
    for i in range(qtdSenha):
        print(''.join(random.sample(string.digits, k = tamanhoSenha)))

def SenhaLetras(qtdSenha, tamanhoSenha):
    print("====SENHAS GERADAS====")
    for i in range(qtdSenha):
        print(''.join(random.sample(string.ascii_letters, k = tamanhoSenha)))

def SenhaAlfanumerica(qtdSenha, tamanhoSenha):
    print("====SENHAS GERADAS====")
    for i in range(qtdSenha):
        print(''.join(random.sample(string.ascii_letters + string.digits, k = tamanhoSenha)))

def SenhaAlfanumericaEPontuacao(qtdSenha, tamanhoSenha):
    print("====SENHAS GERADAS====")
    for i in range(qtdSenha):
        print(''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, k = tamanhoSenha)))