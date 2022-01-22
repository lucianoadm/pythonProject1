def escolher():
    resposta = input('\nEscolha uma opção\n'
                     '<I> para Inserir um elemento\n'
                     '<R> para Resumir um elemento\n'
                     '<L> para Listar um elemento: ').upper()
    return resposta


def inserir(dicionario):
    dicionario[input('Digite o Serial: ').upper()] = [input('Digite o elemento: ').upper(),
                                                      int(input('Digite a quantidade: ')),
                                                      float(input('Digite o valor unitário: ')),
                                                      input('Digite a última data de entrada: '),
                                                      int(input('Digite a quantidade da última entrada: '))]
    salvar(dicionario)


def salvar(dicionario):  # função 'salvar', logo após a iserção dos dados ele será salvo automaticamente
    with open('bd.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ': ' + str(valor))


def resumir(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print(f'\nElemento.............: {lista[0]}')
        print(f'Quantidade inicial.....: {lista[1]}')
        print(f'Valor unitário.........: {lista[2]}')
        print(f'Qtd última entrada.....: {lista[4]}')
        quantidade_total = lista[1] + lista[4]
        print(f'Quantidade total.......: {round(quantidade_total,2)}')
        custo_total = (lista[1] + lista[4]) * lista[2]
        print(f'Custo Total............: {custo_total}')


def listar(dicionario):
    for chave, valor in dicionario.items():
        print('\nObjeto.....')
        print('Login.....', chave)
        print('Dados.....', valor, '\n')
