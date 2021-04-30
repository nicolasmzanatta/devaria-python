if __name__ == '__main__':
    listaConvidados = ['Filipe', 'Douglas', 'Rafael']

    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))

    estaNaLista = nome in listaConvidados
    maiorIdade = idade >= 18

    if estaNaLista:

        if maiorIdade:
            print('Seja bem vindo a festa!')
        else:
            print('Desculpe, seu nome está na lista mas você não é maior de idade!')
    else:
        print('Desculpa, mas seu nome não está na lista')
