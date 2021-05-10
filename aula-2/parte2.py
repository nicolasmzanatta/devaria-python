if __name__ == '__main__':

    try:
        print('Iniciando calculo')
        n = 6 / 2

        print (n)

    except Exception as e:
        print('Desculpe, ocorreu um erro, favor tentar novamente.')






    notasDosAlunos = [90, 71, 82, 93, 75, 82]
    mediaDasNotas = lambda notas : sum(notas) / len(notas)
    print(f'A média das notas é {mediaDasNotas(notasDosAlunos)}')
