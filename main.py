if __name__ == '__main__':
    temperatura = 20
    print(type(temperatura))

    temperatura = "Filipe"
    print(type(temperatura))

    listaNomes = ['Filipe', 'Daniel', 'Rafa', 'Douglas']
    print(type(listaNomes))

    idade = 29
    print(type(idade))

    dicionarioPessoa = {
        'nome': 'Filipe',
        'idade': idade
    }

    print(dicionarioPessoa)
    print(type(dicionarioPessoa))

    numeroComplexo = 5 + 5j
    print(type(numeroComplexo))

    verificacao = False
    print(verificacao)

    # Comentario no python


    nota = int(input('Digite sua nota')) #tem q converter a string q o input retorna em int

    if nota <= 30:
        print("Voce foi reprovado!")
    elif nota <60:
        print("Voce ficou de prova final!")
    else:
        print("Voce está aprovado")








